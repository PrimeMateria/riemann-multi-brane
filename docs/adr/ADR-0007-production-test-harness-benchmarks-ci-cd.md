---
adr: "0007"
title: "Adopt production-grade test and benchmark harness with automated reporting and CI/CD integration"
status: Accepted
date: 2026-11-23
deciders: [Mathematical Physics Board, Formal Verification, Empirical Testing]
consulted: [Systems Quality Assurance, Platform Toolchain Group]
workstream: A
gate: CDR
lexlean_module: none
attestation: none
supersedes: []
superseded_by: []
source_plan: "ADR Plan Production Grade.md"
tags: [test-harness, benchmarks, reporting, ci-cd, automation]
---

# ADR-0007: Adopt production-grade test and benchmark harness with automated reporting and CI/CD integration

## Status

`Accepted` (2026-11-23). Foundational quality engineering and operational verification decision. Non-theorem ADR.

## Provenance

- LexLean module: `none` (operational verification framework).
- Attestation: `none`.
- Test suite: `run_tests.py`, `benchmark_rh_scaling.py`, `run-tests.sh`.
- Basis summary: `MEASURED: 5`, `MODEL: 6`, `FRONTIER: 2`.

## Context and Problem Statement

Mathematical and formal subsystems require rigorous testing pipelines that span both symbolic kernel verification and high-throughput numerical evaluation [MODEL].

Disconnected test scripts without unified reporting risk silent proof decay and unobserved performance regressions [MEASURED].

Without automated benchmarks, convergence thresholds such as Stirling asymptotic tightness and Hodge index negative-definiteness remain untested under high-dimensional scaling [MODEL].

To achieve full operational parity with reference systems such as `kuramoto-protocol-r3` and `wireshark-enterprise-capture`, RH-ZMB must deploy an automated, fail-closed test harness and multi-scale numerical benchmark engine with paired reporting and CI/CD pipeline automation.

## Decision Drivers

1. **Full Traceability and Dual-Plane Integrity**: Unify all formal kernel verification, platform compilation, and empirical test planes under a single authoritative CLI runner [MODEL].
2. **Automated Empirical Benchmarking and Performance Profiling**: Benchmark sieve asymptotics, multi-brane Hodge pairings up to $p_{100}$, regularizer gradient stability, and spectral trace throughput [MEASURED].
3. **Continuous Verification and Fail-Closed Pre-Commit Gates**: Enforce zero-regression gates locally via Git hooks and remotely via continuous integration pipelines [MEASURED].
4. **Non-Trivial Scaling Verification for Multi-Brane Invariants**: Stress-test higher prime cutoffs to satisfy TRR gate promotion criteria [FRONTIER].

## Considered Alternatives

### Option 1: Unified 10-Suite Harness with Multi-Scale Benchmarks and CI/CD Automation
- Pros: Complete end-to-end coverage from compiler AST to high-cutoff numerical benchmarks; automated paired reporting in Markdown and JSON; canonical fingerprinting prevents false-positive drift alarms.
- Cons: Requires maintaining benchmark routines and GitHub Actions workflow configurations.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Ad-Hoc Manual Test Scripts with Separate Unmonitored Benchmarks
- Pros: Simple ad-hoc execution of Python scripts.
- Cons: Lacks toolchain parity enforcement; no automated human-readable reporting or step summaries; risks silent documentation and proof drift.
- Rejected because: fails production-grade verification and CI/CD automation requirements.
- Basis: [MEASURED]

## Decision

We establish a production-grade test harness, automated benchmark suite, and continuous delivery pipeline for the RH-ZMB subsystem:

1. **Unified 10-Suite Test & Benchmark Architecture**: Adopt an authoritative test runner (`run_tests.py` and `run-tests.sh`) executing suites `TS-01` through `TS-10` covering toolchain pins, locks, Lake host builds, LexLean type checks, Lean 4 kernel verification, ADR governance, PrismPM compilation, and empirical test matrices [MODEL].
2. **Automated Paired Dual-Channel Reporting**: Implement automatic generation of human-readable Markdown (`reports/TEST_REPORT_LATEST.md`, `reports/STRESS_BENCHMARK_LATEST.md`) and machine-readable JSON (`reports/test_report_latest.json`, `reports/stress_benchmark_latest.json`) with canonical SHA-256 fingerprinting [MEASURED].
3. **Local Pre-Commit Quality Gate**: Deploy `.githooks/pre-commit` via `install-hooks.sh` to execute `./run-tests.sh --hook`, blocking failing commits and automatically staging fresh reports on success [MODEL].
4. **Multi-Scale Numerical Stress Benchmarking**: Implement `benchmark_rh_scaling.py` covering sieve bound scaling ($n \le 1000$), Hodge intersection pairing eigenspectra ($p \le p_{100}$), coupled gradient flow ($t \le 50$), and explicit formula trace throughput [FRONTIER].
5. **CI/CD Automation**: Deploy `.github/workflows/verify-test.yml` with tool digest locking (`tools.lock` and `scripts/install-tools.sh`), streaming execution summaries to `$GITHUB_STEP_SUMMARY` and archiving test report artifacts.

## Consequences

### Positive
- Enforces strict zero-regression quality gates across both formal and empirical planes.
- Automated generation of rich, human-readable test and benchmark reports with clickable links.
- High-cutoff prime benchmarks ($p \le p_{100}$) provide empirical evidence required to unlock TRR gate promotion.
- Canonical fingerprinting guarantees idempotent test runs without unnecessary documentation drift.

### Negative
- Increased execution time when running the full stress benchmark suite ($\approx 3$ to $5$ seconds for complete sweeps).
- Additional repository assets (`tools.lock`, hook scripts, GitHub Actions workflow).

### Neutral
- Lean 4 kernel reflexivity attestations and Accepted ADR decision bodies remain immutable.
- Existing directory structure and test paths remain backward-compatible.

## Verification

- `python3 docs/adr/_governance/check_adr_log.py` verifies ADR-0007 conformance and hash locking.
- `./run-tests.sh --all` executes suites `TS-01` through `TS-08` and verifies test ledger emission.
- `python3 benchmark_rh_scaling.py` executes benchmark suites `BENCH-01` through `BENCH-04`.
- Pre-commit hook execution verified via `./run-tests.sh --hook`.

## Promotion Criteria

- Complete implementation of `run_tests.py`, `benchmark_rh_scaling.py`, and `run-tests.sh`.
- Automated emission and verification of paired Markdown and JSON reports.
- Zero broken links in `docs/adr/README.md` and root `README.md`.
- Acceptance of ADR-0007 into `docs/adr/_governance/accepted_hashes.json`.

## Links

- Master Plan: [`docs/PLAN-production-test-harness-benchmarks-ci-cd.md`](file:///run/media/multiplic/AGI/prismagi/mount/PROJECTS/rh-zero-multi-brane/docs/PLAN-production-test-harness-benchmarks-ci-cd.md)
- Formal Decision Practice: [ADR-0001](file:///run/media/multiplic/AGI/prismagi/mount/PROJECTS/rh-zero-multi-brane/docs/adr/ADR-0001-adopt-append-only-adr-practice.md)
- Dual-Plane Architecture: [ADR-0002](file:///run/media/multiplic/AGI/prismagi/mount/PROJECTS/rh-zero-multi-brane/docs/adr/ADR-0002-dual-plane-architecture.md)
- $\mathbb{F}_1$-Square Geometry: [ADR-0004](file:///run/media/multiplic/AGI/prismagi/mount/PROJECTS/rh-zero-multi-brane/docs/adr/ADR-0004-f1-square-multi-brane-geometry.md)
- Combinatorial Bounds: [ADR-0005](file:///run/media/multiplic/AGI/prismagi/mount/PROJECTS/rh-zero-multi-brane/docs/adr/ADR-0005-prime-gated-combinatorial-bounds.md)
- Coupled Regularizers: [ADR-0006](file:///run/media/multiplic/AGI/prismagi/mount/PROJECTS/rh-zero-multi-brane/docs/adr/ADR-0006-coupled-dual-channel-regularizers.md)

## Supersedes / Superseded by

- Supersedes: None.
- Superseded by: None.
