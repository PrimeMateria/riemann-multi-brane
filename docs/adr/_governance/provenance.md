# Provenance Basis Taxonomy — RH-ZMB

Every factual or mathematical claim across decision records, documentation, and test outputs in the RH-ZMB subsystem carries one of three explicit provenance bases:

| Basis | Definition | Evidentiary Standard | Falsification / Retirement |
|---|---|---|---|
| `[MEASURED]` | Empirical computation, verified numerical result, or kernel-checked proof. | Machine output from `run_tests.py`, Lean 4 kernel attestation, or exact algebraic evaluation. | Fails reproducible numerical re-run or regression test. |
| `[MODEL]` | Derived from stated mathematical definitions, explicit formulas, or monoid algebra. | Analytical derivation from established definitions (e.g., explicit formula, Deitmar monoid relations). | Counterexample, algebraic inconsistency, or faulty deduction. |
| `[FRONTIER]` | Design hypothesis, open conjecture, or asymptotic scaling extrapolation. | Stated conjecture (e.g., global Hodge negative-definiteness on $H^\perp$ for all $N \to \infty$). | Formal proof/refutation or empirical divergence at finite cutoff. |

## Application Rules

1. **No Silent Upgrades**: A claim cannot be tagged `[MEASURED]` unless an automated test or Lean attestation directly checks it.
2. **Dual-Channel Distinction**:
   - Spectral claims derived from $\zeta(s)$ explicit formulas are `[MODEL]` until evaluated on discrete zeros (`[MEASURED]`).
   - Sieve claims derived from combinatorial bounds (e.g., Stirling vs $4^n$) are `[MODEL]` analytically and `[MEASURED]` numerically on prime truncations.
3. **Summary Invariance**: The summary header in each ADR's `## Provenance` section must exactly match the count of inline tags in the document body. Conformance is strictly checked by `adr/_governance/check_adr_log.py`.
