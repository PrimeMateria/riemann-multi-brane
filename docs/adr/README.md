# RH-ZMB ADR Index — Decision Log & Status Dashboard

This directory is the authoritative, append-only decision log for the **Riemann Zero as Multi-Brane (RH-ZMB)** subsystem.
All decisions are grounded in the architectural roadmap in [`../ADR Plan Production Grade.md`](<../ADR Plan Production Grade.md>) and the research notes in [`../Riemann-zero-as-multi-brane.txt`](<../Riemann-zero-as-multi-brane.txt>).

## Status summary

| Status | Count |
|---|---|
| Accepted | 8 |
| Proposed | 0 |
| Deprecated / Superseded | 0 |

## Decision log

| ADR | Title | Workstream | Gate | Status | LexLean Module | Attestation | Test Suite |
|---|---|---|---|---|---|---|---|
| [0001](ADR-0001-adopt-append-only-adr-practice.md) | Adopt an append-only, verification-bound ADR practice for RH-ZMB | A | PDR | Accepted | `none` | `none` | `check_adr_log.py` |
| [0002](ADR-0002-dual-plane-architecture.md) | Adopt dual-plane architecture: formal specification and empirical test harness | A | PDR | Accepted | `none` | `none` | `run_tests.py` |
| [0003](ADR-0003-provenance-basis-taxonomy.md) | Adopt provenance basis taxonomy for spectral and arithmetic claims | A | PDR | Accepted | `none` | `none` | `check_adr_log.py` |
| [0004](ADR-0004-f1-square-multi-brane-geometry.md) | Adopt the F1-square multi-brane geometric framework (T1 through T4) | B | CDR | Accepted | `spec/adr/0004/F1Square.lex.tex` | `316f8ca7…` | `test_hodge_pairing.py` |
| [0005](ADR-0005-prime-gated-combinatorial-bounds.md) | Replace trivial 4^n combinatorial bound with Stirling and prime-gated P2C asymptotics | B | CDR | Accepted | `spec/adr/0005/CombinatorialBounds.lex.tex` | `316f8ca7…` | `test_combinatorial_bounds.py` |
| [0006](ADR-0006-coupled-dual-channel-regularizers.md) | Couple spectral error-term and sieve regularizers into a unified reliability loss | B | CDR | Accepted | `spec/adr/0006/DualChannel.lex.tex` | `316f8ca7…` | `test_regularizers.py` |
| [0007](ADR-0007-production-test-harness-benchmarks-ci-cd.md) | Adopt production-grade test and benchmark harness with automated reporting and CI/CD integration | A | CDR | Accepted | `none` | `none` | `benchmark_rh_scaling.py` |
| [0008](ADR-0008-trr-milestones-production-implementation.md) | Implement TRR milestones: numerical stress benchmarks, pre-commit CI/CD gating, and downstream platform integration | A | TRR | Accepted | `none` | `none` | `benchmark_rh_scaling.py` |

## Workstream critical path

```text
Workstream A (Foundational Governance & Architecture: 0001-0003) ──► PDR (Closed)
      │
      ▼
Workstream B (Combinatorial Bounds & F1-Square Geometry: 0004-0006) ──► CDR (Closed)
      │
      ▼
Workstream C (Spectral Trace & Hodge Index T5 on H-perp: 0010-0012) ──► TRR (Open)
      │
      ▼
Workstream D (Empirical Test Harness & Production Release: 0020-0021) ──► SOW (Open)
```

## Governance references

- Provenance taxonomy: [`_governance/provenance.md`](_governance/provenance.md)
- Phase-gate criteria: [`_governance/gates.md`](_governance/gates.md)
- Risk and dependency register: [`_governance/RAID.md`](_governance/RAID.md)
- Template for new decisions: [`TEMPLATE.md`](TEMPLATE.md)
- Automated conformance validator: [`_governance/check_adr_log.py`](_governance/check_adr_log.py)
