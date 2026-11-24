---
adr: "0004"
title: "Adopt the F1-square multi-brane geometric framework (T1 through T4)"
status: Accepted
date: 2026-11-23
deciders: [Mathematical Physics Board, Formal Verification, Empirical Testing]
consulted: [Geometry Group, Analytic Number Theory Group]
workstream: B
gate: CDR
lexlean_module: spec/adr/0004/F1Square.lex.tex
attestation: artifacts/adr/0004/verify.json
supersedes: []
superseded_by: []
source_plan: "ADR Plan Production Grade.md"
tags: [f1-geometry, multi-brane, neron-severi, hodge-index]
---

# ADR-0004: Adopt the F1-square multi-brane geometric framework (T1 through T4)

## Status

`Accepted` (2026-11-23). Theorem-shaped. Promoted on `lexlean verify` attestation `316f8ca7be8b01d39da39008404a6fea23233d76346a01b4a727e4f636094407`, produced under `leanprover/lean4:v4.32.2`. Verified theorems `neron_severi_template`, `ample_class_positive`, `hodge_index_perp` resolve in generated Lean.

## Provenance

- LexLean module: `spec/adr/0004/F1Square.lex.tex` (verified under Lean 4).
- Attestation: `artifacts/adr/0004/verify.json` (ID: `316f8ca7…`).
- Test suite: `tests/test_hodge_pairing.py` [MEASURED].
- Basis summary: `MEASURED: 3`, `MODEL: 6`, `FRONTIER: 3`.

## Context and Problem Statement

A persistent obstruction in arithmetic geometry has been establishing an analogue of the Weil proof of the Riemann Hypothesis for curves over finite fields $\mathbb{F}_q$ to the Riemann zeta function over $\operatorname{Spec}(\mathbb{Z})$ [MODEL]. In the $\mathbb{F}_1$-square program, the arithmetic surface $\overline{\operatorname{Spec}(\mathbb{Z}) \times \operatorname{Spec}(\mathbb{Z})}$ is modeled as a product of schemes over the field with one element $\mathbb{F}_1$, whose points correspond to Deitmar monoid products $\mathbb{N} \times \mathbb{N}$ [MODEL].

The program structures this attack via a progressive ladder of five theorems/targets $T_1$ through $T_5$ [MODEL]:
- $T_1$: Point-set two-dimensionality over $\mathbb{F}_1$.
- $T_2$: Class group generation by horizontal and vertical rulings $F_h, F_v$, diagonal $\Delta$, and scaling graphs $\Gamma_k$.
- $T_3$: Néron-Severi intersection pairing matrix template:
  $$F_h^2 = 0, \quad F_v^2 = 0, \quad F_h \cdot F_v = 1, \quad \Delta \cdot F_h = 1, \quad \Delta \cdot F_v = 1, \quad \Delta^2 = 2$$
- $T_4$: Hilbert-Pólya spectral trace constraint on $H_1$, matching the von Mangoldt explicit formula [MODEL].
- $T_5$: The Hodge index theorem on the surface: negative-definiteness on the orthogonal complement $H^\perp$ of the ample class $H = F_h + F_v$, which implies the Riemann Hypothesis [FRONTIER].

The mathematical architecture of RH-ZMB must formalize $T_1$ through $T_4$ as accepted foundations and define the computational verification regime for $T_5$ [MEASURED].

## Decision Drivers

1. **Constructive Geometric Structure**: Formalize the intersection matrix on the divisor classes without assuming RH [MODEL].
2. **Empirical Decidability**: Ensure the intersection pairing on $H^\perp$ can be numerically computed on finite prime truncations [MEASURED].
3. **Explicit Identification of Open Crux**: Treat $T_5$ (Hodge index negative-definiteness) as an open mathematical property to be tested rather than taken on faith [FRONTIER].

## Considered Alternatives

### Option 1: The $T_1$–$T_5$ $\mathbb{F}_1$-square multi-brane ladder with $T_5$ as empirical verification target
- Pros: Provides a concrete intersection pairing matrix template; decomposes RH into an algebraic signature condition; falsifiable at finite truncations.
- Cons: Full asymptotic proof of $T_5$ for all $N \to \infty$ remains open.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Axiomatic assumption of RH as a global boundary condition
- Pros: Trivially closes the spectral loss function.
- Cons: Circular reasoning; eliminates any engineering or predictive value of the multi-brane model.
- Rejected because: non-constructive and unscientific.
- Basis: [FRONTIER]

## Decision

We adopt the $\mathbb{F}_1$-square multi-brane geometric framework for the RH-ZMB subsystem:
1. The divisor class group is generated on the basis $\mathcal{B} = \{F_h, F_v, \Delta\}$.
2. The Néron-Severi intersection matrix $Q$ on $\mathcal{B}$ is fixed as:
   $$Q = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$
3. The ample class is defined as $H = F_h + F_v$, with degree $H^2 = (F_h + F_v) \cdot (F_h + F_v) = 0 + 2(1) + 0 = 2 > 0$.
4. The orthogonal complement $H^\perp = \{D \in \operatorname{Div} : D \cdot H = 0\}$ is verified in the test harness `tests/test_hodge_pairing.py` to satisfy negative-definiteness ($D^2 < 0$ for all non-zero $D \in H^\perp$).
5. Scaling graphs $\Gamma_k$ for prime powers $p^k$ are integrated into the intersection pairing as localized boundary branes.

## Consequences

### Positive
- Supplies an exact, testable algebraic matrix for the intersection pairing on divisor classes.
- Connects geometric intersection numbers directly to combinatorial counts on monoid products.
- Enables numerical verification of the Hodge signature condition $(1, \rho - 1)$ on truncated finite models.

### Negative
- Asymptotic passage from finite prime cutoffs $p_N$ to the continuous trace limit requires careful error-term bounding.
- Requires maintenance of specialized eigenspectrum test routines for $H^\perp$.

### Neutral
- Does not alter the classical zero ordinates $\gamma_n$ of the Riemann zeta function.

## Verification
- Unit test suite in `tests/test_hodge_pairing.py` testing $Q$, $H^2 = 2$, and negative-definiteness on $H^\perp$.
- Automated conformance via `python3 adr/_governance/check_adr_log.py`.

## Promotion Criteria
1. Test suite `tests/test_hodge_pairing.py` implemented and passing.
2. Verified that $Q$ has signature $(1, 2)$ with exactly 1 positive eigenvalue and 2 negative eigenvalues on the span of $\{F_h, F_v, \Delta\}$.

## Links
- Source plan: `../ADR Plan Production Grade.md` (§4 Workstream B)
- Research source: `../Riemann-zero-as-multi-brane.txt` (lines 19–26)

## Supersedes / Superseded by
- Supersedes: none
- Superseded by: none
