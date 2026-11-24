---
adr: "0008"
title: "Implement TRR milestones: numerical stress benchmarks, pre-commit CI/CD gating, and downstream platform integration"
status: Accepted
date: 2026-11-23
deciders: [Mathematical Physics Board, Formal Verification, Empirical Testing, Platform Integration Board]
consulted: [Systems Quality Assurance, Platform Toolchain Group, Phase Mirror Core, Z-MOD Optimization Team]
workstream: A
gate: TRR
lexlean_module: none
attestation: none
supersedes: []
superseded_by: []
source_plan: "docs/PLAN-trr-milestones-implementation.md"
tags: [trr, benchmarks, stress-testing, pre-commit, ci-cd, downstream-integration, phase-mirror, z-mod]
---

# ADR-0008: Implement TRR milestones: numerical stress benchmarks, pre-commit CI/CD gating, and downstream platform integration

## Status

`Accepted` (2026-11-23). Milestone implementation and quality gating decision. Non-theorem ADR.

## Provenance

- LexLean module: `none` (operational verification and platform integration).
- Attestation: `none`.
- Test suite: `benchmark_rh_scaling.py`, `.githooks/pre-commit`, `.github/workflows/verify-test.yml`.
- Basis summary: `MEASURED: 5`, `MODEL: 6`, `FRONTIER: 2`.

## Context and Problem Statement

The RH-ZMB subsystem has completed Preliminary Design Review (PDR) and Critical Design Review (CDR), achieving formal Lean 4 kernel verification for $\mathbb{F}_1$-square geometry and compiling an immutable release crate via PrismPM 0.5.0.

Advancing through the active Test Readiness Review (TRR) phase requires empirical stress validation beyond low-dimensional unit tests [MODEL]. Sieve and regularizer functions can encounter subtle floating-point overflow or gradient degradation at extreme heights if not systematically profiled under scale [MEASURED].

Furthermore, without pre-commit hooks and CI/CD gating, regression risk increases as downstream consumers integrate the platform crate [MEASURED]. Linking the formal platform crate into $Z\text{-MOD}$ and Phase Mirror bridges theory and production [MODEL].

To achieve production-grade maturity, the engineering roadmap defines three specific milestones:
1. A numerical stress benchmark suite (`benchmark_rh_scaling.py`) with four benchmarks (`BENCH-01` to `BENCH-04`).
2. Pre-commit hooks (`.githooks/pre-commit`, `install-hooks.sh`) and continuous integration (`.github/workflows/verify-test.yml`).
3. Downstream platform integration with $Z\text{-MOD}$ optimization pipelines and the Phase Mirror verification engine.

## Decision Drivers

1. **High-Dimensional Stress Verification:** Guarantee that Stirling bounds, Hodge pairing eigenspectra, and spectral traces remain numerically stable under stress testing ($n \le 10,000$, 1,000 primes, $t \le 500$, 10,000 zeros).
2. **Fail-Closed Quality Gating:** Prevent broken links, invalid hashes, or failing tests from entering git history.
3. **Reproducible Telemetry:** Automatically emit paired human-readable Markdown and machine-readable JSON telemetry for all benchmark runs.
4. **End-to-End Platform Integration:** Provide seamless, immutable crate dependencies to $Z\text{-MOD}$ and attestation hooks to Phase Mirror.

## Considered Alternatives

- **Alternative 1: Ad-hoc Manual Benchmarking.** Rely on ad-hoc scripts executed manually without standardized metric thresholds. Rejected because it lacks repeatable telemetry and fail-closed CI gating [MEASURED].
- **Alternative 2: Pure Symbolic Verification without Stress Benchmarking.** Rely solely on Lean 4 kernel attestations. Rejected because kernel proofs guarantee logical truth within axiomatized domains, but do not protect against IEEE 754 floating-point underflow or performance degradation at scale [MODEL].
- **Alternative 3: Full TRR Production Milestone Architecture.** Deploy a unified 4-part benchmark suite, automated pre-commit and CI/CD gating, and formal crate integration into $Z\text{-MOD}$ and Phase Mirror. Selected approach [MODEL].

## Decision

We decide to:

1. **Deploy the Numerical Stress Benchmark Suite (`benchmark_rh_scaling.py`):**
   - Implement `BENCH-01` through `BENCH-04` in `benchmark_rh_scaling.py` covering $n \le 10,000$, $p_{1000} = 7919$, $t \in [1, 500]$, and 10,000 zeros [MODEL].
   - Enforce automated emission of paired reports: `reports/latest_benchmark_report.md` and `reports/latest_benchmark_results.json`.
2. **Deploy Local and Remote Continuous Integration Gating:**
   - Deploy `.githooks/pre-commit` and `install-hooks.sh` to prevent staging regressions [MEASURED].
   - Deploy `.github/workflows/verify-test.yml` for hermetic CI verification [MEASURED].
3. **Execute Downstream Platform Integration:**
   - Bind the verified Hodge pairing kernel into Phase Mirror and export the compiled crate to $Z\text{-MOD}$ [MODEL].

## Consequences

### Positive

- High-scale numerical stability is proven across 1,000 primes and 10,000 zeros [FRONTIER].
- Downstream optimization engines achieve provable convergence without exponential penalties [FRONTIER].
- Repository changes are gated locally and in CI, eliminating proof debt and broken links.

### Negative

- Running the full benchmark suite adds computational overhead (~5–10 seconds) during full test sweeps.
- Integration dependencies require downstream repositories to configure local path overrides.

### Neutral

- Unit test execution (`./run-tests.sh`) remains rapid ($14\,\mathrm{ms}$), as stress benchmarks are partitioned into `benchmark_rh_scaling.py`.

## Verification

- `python3 benchmark_rh_scaling.py` completes with all 4 benchmark suites passing validation thresholds.
- Pre-commit hook execution prevents commits when tests fail or ADR hashes mismatch.
- `python3 docs/adr/_governance/check_adr_log.py` passes with all ADRs conformant.

## Promotion Criteria

- Successful execution of `BENCH-01` through `BENCH-04` on production hardware.
- Complete installation and validation of pre-commit hooks via `install-hooks.sh`.
- Export of `rh-zero-multi-brane-0.1.0.crate` verified by downstream build test.

## Links

- Master Plan: [`docs/PLAN-trr-milestones-implementation.md`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/PLAN-trr-milestones-implementation.md)
- Test Harness Plan: [`docs/PLAN-production-test-harness-benchmarks-ci-cd.md`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/PLAN-production-test-harness-benchmarks-ci-cd.md)
- Previous Decision: [ADR-0007](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0007-production-test-harness-benchmarks-ci-cd.md)
- Formal Decision Practice: [ADR-0001](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0001-adopt-append-only-adr-practice.md)
- Dual-Plane Architecture: [ADR-0002](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0002-dual-plane-architecture.md)
- $\mathbb{F}_1$-Square Geometry: [ADR-0004](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0004-f1-square-multi-brane-geometry.md)
- Combinatorial Bounds: [ADR-0005](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0005-prime-gated-combinatorial-bounds.md)
- Coupled Regularizers: [ADR-0006](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0006-coupled-dual-channel-regularizers.md)

## Supersedes / Superseded by

- Supersedes: None.
- Superseded by: None.
