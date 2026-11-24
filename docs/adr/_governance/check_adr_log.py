#!/usr/bin/env python3
"""Conformance checker for the RH-ZMB ADR decision log.

Validates the properties that make this log production-grade:
- every ADR has the mandatory sections
- provenance summary matches inline basis tags
- theorem-shaped ADRs are Proposed until an attestation exists
- non-theorem ADRs are Accepted
- index and README links resolve
- no accepted ADR was edited in place (content hash manifest check)

Usage: python3 adr/_governance/check_adr_log.py
Exit code 0 = conformant, 1 = violations found.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ADR_DIR = Path(__file__).resolve().parents[1]
MANIFEST = ADR_DIR / "_governance" / "accepted_hashes.json"

REQUIRED_SECTIONS = [
    "## Status",
    "## Provenance",
    "## Context and Problem Statement",
    "## Decision Drivers",
    "## Considered Alternatives",
    "## Decision",
    "## Consequences",
    "### Positive",
    "### Negative",
    "### Neutral",
    "## Verification",
    "## Promotion Criteria",
    "## Links",
    "## Supersedes / Superseded by",
]

BASES = ("MEASURED", "MODEL", "FRONTIER")


def field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}: (.+)$", text, re.M)
    return match.group(1).strip() if match else ""


def check() -> list[str]:
    errors: list[str] = []
    files = sorted(ADR_DIR.glob("ADR-*.md"))
    if not files:
        return ["no ADR files found in adr/"]

    accepted_hashes: dict[str, str] = {}
    if MANIFEST.exists():
        try:
            accepted_hashes = json.loads(MANIFEST.read_text())
        except Exception as e:
            errors.append(f"malformed accepted_hashes.json: {e}")

    for path in files:
        text = path.read_text()
        name = path.name

        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{name}: missing section {section}")

        body = "\n".join(l for l in text.splitlines() if "Basis summary:" not in l)
        actual = tuple(
            str(len(re.findall(rf"\[{basis}\]", body))) for basis in BASES
        )
        summary_match = re.search(
            r"Basis summary: `MEASURED: (\d+)`, `MODEL: (\d+)`, `FRONTIER: (\d+)`",
            text,
        )
        if not summary_match:
            errors.append(f"{name}: missing or malformed basis summary")
        elif summary_match.groups() != actual:
            errors.append(
                f"{name}: basis summary {summary_match.groups()} != inline {actual}"
            )

        status = field(text, "status")
        module = field(text, "lexlean_module")
        attestation = field(text, "attestation")
        theorem_shaped = module not in ("none", "")

        if theorem_shaped:
            number_match = re.match(r"ADR-(\d{4})-", path.stem)
            number = number_match.group(1) if number_match else ""
            expected_attestation = f"artifacts/adr/{number}/verify.json"
            if status == "Accepted" and attestation == "none":
                errors.append(
                    f"{name}: theorem-shaped ADR accepted without {expected_attestation}"
                )
            if status == "Accepted" and not (ROOT / expected_attestation).exists():
                errors.append(f"{name}: missing attestation file {expected_attestation}")
        elif status != "Accepted":
            errors.append(f"{name}: non-theorem ADR should be Accepted, got {status}")

        if status in ("Accepted", "Deprecated", "Superseded") and name in accepted_hashes:
            digest = hashlib.sha256(text.encode()).hexdigest()
            if accepted_hashes[name] != digest:
                errors.append(f"{name}: accepted ADR body changed since manifest lock")

    for doc in (ROOT / "README.md", ADR_DIR / "README.md"):
        if not doc.exists():
            continue
        for target in re.findall(r"\]\((?:<([^>]+)>|([^)]+\.md))\)", doc.read_text()):
            rel = target[0] or target[1]
            if rel.startswith(("http://", "https://", "#")):
                continue
            if rel.startswith("file://"):
                path_str = rel[7:].split("#")[0].replace("%20", " ")
                resolved = Path(path_str)
            else:
                resolved = (doc.parent / rel).resolve()
            if not resolved.exists():
                errors.append(f"{doc.name}: broken link {rel}")

    return errors


if __name__ == "__main__":
    violations = check()
    for violation in violations:
        print(f"FAIL: {violation}")
    if violations:
        raise SystemExit(1)
    print(f"OK: {len(list(ADR_DIR.glob('ADR-*.md')))} ADRs conformant")
