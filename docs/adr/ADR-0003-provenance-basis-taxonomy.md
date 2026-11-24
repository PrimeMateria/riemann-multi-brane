---
adr: "0003"
title: "Adopt provenance basis taxonomy for spectral and arithmetic claims"
status: Accepted
date: 2026-11-23
deciders: [Mathematical Physics Board, Formal Verification, Empirical Testing]
consulted: [Geometry Group, Analytic Number Theory Group]
workstream: A
gate: PDR
lexlean_module: none
attestation: none
supersedes: []
superseded_by: []
source_plan: "ADR Plan Production Grade.md"
tags: [governance, provenance, taxonomy]
---

# ADR-0003: Adopt provenance basis taxonomy for spectral and arithmetic claims

## Status

`Accepted` (2026-11-23). Foundational governance decision. Non-theorem ADR.

## Provenance

- LexLean module: `none` (taxonomy specification).
- Attestation: `none`.
- Test suite: `adr/_governance/check_adr_log.py` [MEASURED].
- Basis summary: `MEASURED: 5`, `MODEL: 5`, `FRONTIER: 2`.

## Context and Problem Statement

Research touching the Riemann Hypothesis often blurs the line between proven mathematical facts, conditional derivations (assuming RH), numerical observations, and speculative conjectures [MODEL]. In `Riemann-zero-as-multi-brane.txt`, this is illustrated by the error term $r(x) = O(x^{1/2+\epsilon})$, which classical texts cite as an RH-conditional estimate, but which optimizer loss functions must treat as a regularizer without circular assumptions [MEASURED].

Without a strict provenance taxonomy, conditional statements can easily be mistaken for unconditional warrants [MODEL].

## Decision Drivers

1. **Epistemic Honesty**: Distinguish empirically verified facts, deductive derivations, and open conjectures [MODEL].
2. **Machine-Checkable Conformance**: Basis counts must be checked by automated tooling to prevent unverified drift [MEASURED].
3. **Explicit Handling of the Riemann Hypothesis**: RH itself must remain tagged as `FRONTIER` and never introduced as an unconditional premise [FRONTIER].

## Considered Alternatives

### Option 1: Three-basis taxonomy (`MEASURED`, `MODEL`, `FRONTIER`)
- Pros: Simple, precise, directly distinguishes empirical/proof-backed facts, deductive consequences, and conjectures.
- Cons: Requires manual tagging of every substantive statement in ADRs.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Binary division (Proven vs Unproven)
- Pros: Minimal overhead.
- Cons: Fails to separate rigorous deductive consequences under specific hypotheses from ungrounded heuristic guesses.
- Rejected because: insufficiently granular for mathematical physics.
- Basis: [MEASURED]

## Decision

We adopt a three-basis provenance taxonomy for all documentation, ADR claims, and test assertions in the RH-ZMB subsystem:
1. `[MEASURED]`: Empirical computations, numerical test harness outputs, and machine-checked kernel proofs.
2. `[MODEL]`: Deductions derived from explicit formulas, Deitmar monoid relations, or formal definitions under stated conditions.
3. `[FRONTIER]`: Unsettled conjectures (including RH, global Hodge negative-definiteness on $H^\perp$ for all $N$, and uncalibrated loss weights).
4. Every ADR must summarize its basis counts in the `## Provenance` section, and `adr/_governance/check_adr_log.py` enforces exact agreement with inline tags.

## Consequences

### Positive
- Absolute transparency regarding what has been mathematically proven versus empirically tested versus conjectured.
- Prevents circular reasoning in regularizer loss functions and geometric pairings.
- Automated validation blocks commits where basis counts diverge from inline tags.

### Negative
- Requires authors to tag every substantive claim and keep summary headers synchronized.

### Neutral
- Taxonomies match existing conventions across the parent project mount.

## Verification
- Automated validation via `python3 adr/_governance/check_adr_log.py`.

## Promotion Criteria
1. Governance documentation in `adr/_governance/provenance.md` completed.
2. `check_adr_log.py` validates tag counts across all active ADRs.

## Links
- Source plan: `../ADR Plan Production Grade.md` (§3.2)
- Taxonomy details: `_governance/provenance.md`

## Supersedes / Superseded by
- Supersedes: none
- Superseded by: none
