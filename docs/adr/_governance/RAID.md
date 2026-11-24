# RAID Log — RH-ZMB Programme

| ID | Type | Description | Basis | Status | Mitigation / Resolution | Gate |
|---|---|---|---|---|---|---|
| **RAID-001** | Risk | T5 Hodge negative-definiteness on $H^\perp$ may fail at large prime cutoffs due to spectral leakage | `FRONTIER` | Open | Numerical signature check in test harness up to $p_N$; track eigenvalue margins. | TRR |
| **RAID-002** | Risk | Combinatorial bound $4^n$ allows too much sieve leakage, underpowering the combinatorial channel | `MEASURED` | Closed | ADR-0005 replaces $4^n$ with Stirling $\frac{4^n}{\sqrt{\pi n}}$ and prime-gated P2C distributions. | CDR |
| **RAID-003** | Assumption | The spectral and combinatorial channels share a common multiplicity structure | `MODEL` | Open | Coupled dual-channel loss $R_{\text{err}} + R_{\text{bin}}$ in $Z\text{-MOD}$. | CDR |
| **RAID-004** | Issue | Original notes `Riemann-zero-as-multi-brane.txt` contain unformatted discussion blocks | `MEASURED` | Closed | Formalized into structured ADRs and executable mathematical tests. | PDR |
| **RAID-005** | Dependency | Requires Python 3 standard library with reproducible numerical routines | `MEASURED` | Closed | Test harness implemented using pure Python with exact fractions and float fallback. | PDR |

## Conventions
- `Basis` uses the taxonomy in [`provenance.md`](provenance.md).
- Any retired risk must record a dated transition entry below with verifiable evidence.

## Transitions

| Date | ID | From | To | Evidence |
|---|---|---|---|---|
| 2026-11-23 | RAID-004 | Open | Closed | Foundational ADR set (ADR-0001 to ADR-0005) and test suite authored. |
| 2026-11-23 | RAID-005 | Open | Closed | Production test runner `run_tests.py` operational with zero third-party dependencies required. |
| 2026-11-23 | RAID-002 | Open | Closed | ADR-0005 adopted; Stirling & prime-gated bounds implemented and tested in `test_combinatorial_bounds.py`. |
