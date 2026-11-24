# ADR-9999: Foundry Surface RH‑ZMB

## Summary
This ADR documents the creation of a **Foundry‑owned surface** `foundry_surface_rh_zmb` that implements the arithmetic‑surface intersection matrix `Q` and the Hodge‑index negative‑definiteness predicate `is_negative_definite_on_h_perp`.

## Public Contract
- **Intersection matrix Q** (3 × 3) =
  ```
  0 1 1
  1 0 1
  1 1 0
  ```
- **Ample divisor** `H = (1,1,0)`.
- **Predicate** `is_negative_definite_on_h_perp(d)` returns `true` iff `d·H = 0` and `d·d < 0`.

## Ownership & Stratification
- The surface lives in the **Foundry** repository (`rh-zero-multi-brane`) and is exposed to downstream `UOR‑Foundation/f1` via a sealed PR.
- No direct mutation of the external `f1` repo; integration is performed by downstream maintainers after the artefacts are sealed.

## Open Debts / Future Work
- **Full lattice theory** (extension to `k` prime branes).
- **PrismPM sealed receipt** generation and inclusion in CI.
- **Hermetic CI workflow** to enforce dual‑gate verification.
- **Optional gateway‑mediated FFI** bridge for Lean callers.

## Governance
- Once the sealed receipt and CI pass, the entry will be added to `model/ids.toml` and the contract becomes part of the L0 claim table.

*Prepared by Antigravity – 2026‑11‑24*