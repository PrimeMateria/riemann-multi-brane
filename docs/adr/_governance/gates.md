# Phase-Gate Criteria — RH-ZMB Programme

The development of the Riemann Zero as Multi-Brane subsystem proceeds through four formal gates:

| Gate | Focus | Mathematical Criteria | Software / Evidence Criteria |
|---|---|---|---|
| **PDR** | Foundational Architecture | ADR-0001 through ADR-0003 accepted. Scope, taxonomy, and mathematical problem defined. | Conformance script `check_adr_log.py` passes; test runner structure initialized. |
| **CDR** | Geometric & Sieve Model | ADR-0004 ($T_1$–$T_4$ geometry) and ADR-0005 (Stirling & P2C bounds) accepted. | Numerical test suite validates combinatorial bounds and $R_{\text{err}} + R_{\text{bin}}$ regularizers. |
| **TRR** | Hodge Index & Spectral Test | ADR-0010 through ADR-0012 accepted. $T_5$ Hodge signature check formulated on $H^\perp$. | Numerical verification of signature $(1, \rho - 1)$ on intersection matrix for prime cutoffs up to $p_{100}$. |
| **SOW** | Production Release | ADR-0020 and ADR-0021 accepted. Full system closure. | Complete test suite green (100% pass rate); release report generated. |

## Non-Negotiable Promotion Rules

1. An ADR cannot be promoted to `Accepted` if its basis summary does not match inline tags.
2. An accepted ADR is strictly immutable: modifying its body without superseding fails CI via `accepted_hashes.json`.
3. Mathematical claims must have corresponding executable assertions in `tests/`.
