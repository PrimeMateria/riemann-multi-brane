---
adr: "0002"
title: "Adopt dual-plane architecture: formal specification and empirical test harness"
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
tags: [architecture, verification, test-harness]
---

# ADR-0002: Adopt dual-plane architecture: formal specification and empirical test harness

## Status

`Accepted` (2026-11-23). Foundational architectural decision. Non-theorem ADR.

## Provenance

- LexLean module: `none` (architectural framework).
- Attestation: `none`.
- Test suite: `run_tests.py` [MEASURED].
- Basis summary: `MEASURED: 4`, `MODEL: 5`, `FRONTIER: 1`.

## Context and Problem Statement

Mathematical physics projects exploring non-trivial geometric approaches to the Riemann Hypothesis risk two failure modes [MODEL]:
1. **The Pure Prose Failure**: High-level conceptual descriptions that omit explicit boundary conditions, intersection matrices, or remainder terms [MODEL].
2. **The Ungrounded Numerics Failure**: Numerical simulations that calculate approximations over finite cutoffs without formal algebraic invariants or error bounds [MEASURED].

To eliminate both failure modes, the development of RH-ZMB must separate and interlock two complementary planes: the **Formal Verification Plane** (symbolic and kernel-checked logic) and the **Empirical Test Plane** (executable simulation and numerical harness) [MODEL].

## Decision Drivers

1. **Zero Unfalsifiable Claims**: Every analytical proposition must either compile to a formal Lean proof or be tested by numerical computation [MODEL].
2. **Reproducibility**: Empirical tests must run automatically via standard shell scripts without external cloud dependencies [MEASURED].
3. **Multi-Scale Coverage**: From algebraic monoid intersections to finite prime truncations and spectral loss functions [FRONTIER].

## Considered Alternatives

### Option 1: Dual-plane architecture (Formal Specification + Empirical Test Harness)
- Pros: Complete separation of symbolic proof obligations and numerical validation; mutual cross-checking.
- Cons: Requires developing both Lean formal models and Python numerical test suites.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Python numerical simulation only
- Pros: Rapid prototyping of eigenvalue spectra and regularizer gradients.
- Cons: Cannot verify algebraic correctness of monoid intersections or prevent circular reasoning.
- Rejected because: leaves theoretical foundations uncertified.
- Basis: [MEASURED]

## Decision

We establish a dual-plane architecture for the RH-ZMB subsystem:
1. **Verification Plane**: Uses formal specification (Lean 4 / LexLean) to codify the algebraic structures of the $\mathbb{F}_1$-square, Néron-Severi pairings, and combinatorial lemmas.
2. **Empirical Test Plane**: Uses an in-repo Python test harness (`run_tests.py` and `tests/`) to verify numerical evaluations, calculate eigenspectra of the intersection matrix on $H^\perp$, evaluate the dual-channel loss ($R_{\text{err}} + R_{\text{bin}}$), and generate automated human-readable reports.
3. Both planes are invoked and checked via local project scripts kept inside the project folder.

## Consequences

### Positive
- Prevents theoretical errors by testing both symbolic proofs and finite-truncation approximations.
- Clear boundary between algebraic exactness and floating-point numerical tolerances.
- Automated generation of test and conformance reports for CI/CD integration.

### Negative
- Increased development scope requiring maintenance of both formal modules and test scripts.
- Numerical evaluations must account for floating-point precision limits when checking near-zero eigenvalues.

### Neutral
- Standard Python 3 test harness operates alongside Lean toolchains without conflicting dependencies.

## Verification
- Execution of `python3 run_tests.py` produces structured markdown and JSON test evidence.
- Verification of ADR conformance via `python3 adr/_governance/check_adr_log.py`.

## Promotion Criteria
1. Test harness runner `run_tests.py` and shell wrapper `run-tests.sh` operational.
2. Initial test suite verifying basic algebraic invariants passes.

## Links
- Source plan: `../ADR Plan Production Grade.md` (§2)
- Reference notes: `../Riemann-zero-as-multi-brane.txt`

## Supersedes / Superseded by
- Supersedes: none
- Superseded by: none
