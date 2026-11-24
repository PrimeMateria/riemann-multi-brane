---
adr: "0001"
title: "Adopt an append-only, verification-bound ADR practice for RH-ZMB"
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
tags: [governance, adr, rh-zmb]
---

# ADR-0001: Adopt an append-only, verification-bound ADR practice for RH-ZMB

## Status

`Accepted` (2026-11-23). Foundational governance decision. Non-theorem ADR.

## Provenance

- LexLean module: `none` (process governance).
- Attestation: `none`.
- Test suite: `adr/_governance/check_adr_log.py` [MEASURED].
- Basis summary: `MEASURED: 4`, `MODEL: 4`, `FRONTIER: 1`.

## Context and Problem Statement

The Riemann Zero as Multi-Brane (RH-ZMB) subsystem investigates non-trivial connections between spectral theory, $\mathbb{F}_1$ algebraic geometry, and combinatorial sieve bounds [MODEL]. In historical projects, theoretical physics investigations suffer from undocumented shifts in assumptions, unrecorded changes to definitions, and conflation of conjectures with proven facts [MEASURED].

A production-grade system requires an immutable, machine-checked decision log where every architectural and mathematical choice is recorded sequentially and permanently [MODEL].

## Decision Drivers

1. **Immutability of Accepted Decisions**: Prevent rewriting history or silently changing definitions [MODEL].
2. **Auditability and Conformance**: Enable automated continuous integration to verify that the decision log meets strict structural standards [MEASURED].
3. **Decoupling Open Conjectures from Proven Theorems**: Ensure speculative hypotheses remain explicitly tracked as open risks [FRONTIER].

## Considered Alternatives

### Option 1: Append-only, hash-locked ADR log with conformance enforcement
- Pros: Complete audit trail, cryptographic tamper resistance via SHA-256 manifests, strict provenance tracking.
- Cons: High ceremony; superseding an accepted decision requires authoring a new ADR.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Living design document (single wiki or README)
- Pros: Low friction, easy to edit in place.
- Cons: Destroys historical decision context; allows silent drift in definitions and unverified claims.
- Rejected because: violates production-grade reproducibility.
- Basis: [MEASURED]

## Decision

We adopt an append-only, sequentially numbered Architecture Decision Record (ADR) system for the RH-ZMB subsystem:
1. Every new architectural or mathematical commitment begins as `Proposed` in `adr/ADR-NNNN-<slug>.md`.
2. Once reviewed and backed by required tests or formal specs, it transitions to `Accepted`.
3. Accepted ADR bodies are cryptographically locked in `adr/_governance/accepted_hashes.json` and are never edited in place.
4. Any amendment must be implemented by authoring a new ADR that explicitly declares `supersedes: [ADR-XXXX]`.
5. Automated validation is enforced via `python3 adr/_governance/check_adr_log.py`.

## Consequences

### Positive
- Every mathematical formulation and empirical test parameter is permanently recorded with full rationale.
- Silent regression or unannounced shifts in analytical definitions are prevented.
- Clear onboarding for contributors and automated verification agents.

### Negative
- Minor refinements require authoring superseding ADRs rather than quick in-place edits.
- Requires maintenance of the hash manifest and governance validation scripts.

### Neutral
- Development files and test suites remain located within the repository structure.

## Verification
- Conformance validation via `python3 adr/_governance/check_adr_log.py`.
- Integrity verification against `adr/_governance/accepted_hashes.json`.

## Promotion Criteria
1. Initial ADR log initialized with standard templates and governance scripts.
2. `check_adr_log.py` executes with exit code 0.

## Links
- Source plan: `../ADR Plan Production Grade.md` (§3)
- Research source: `../Riemann-zero-as-multi-brane.txt`

## Supersedes / Superseded by
- Supersedes: none
- Superseded by: none
