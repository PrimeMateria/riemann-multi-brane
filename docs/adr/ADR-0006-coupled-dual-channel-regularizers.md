---
adr: "0006"
title: "Couple spectral error-term and sieve regularizers into a unified reliability loss"
status: Accepted
date: 2026-11-23
deciders: [Mathematical Physics Board, Formal Verification, Empirical Testing]
consulted: [Analytic Number Theory Group, Sieve Geometry Group]
workstream: B
gate: CDR
lexlean_module: spec/adr/0006/DualChannel.lex.tex
attestation: artifacts/adr/0006/verify.json
supersedes: []
superseded_by: []
source_plan: "ADR Plan Production Grade.md"
tags: [regularizer, dual-channel, spectral, sieve, z-mod]
---

# ADR-0006: Couple spectral error-term and sieve regularizers into a unified reliability loss

## Status

`Accepted` (2026-11-23). Theorem-shaped. Promoted on `lexlean verify` attestation `316f8ca7be8b01d39da39008404a6fea23233d76346a01b4a727e4f636094407`, produced under `leanprover/lean4:v4.32.2`. Verified theorems `coupled_loss_monotonic`, `spectral_error_bounded`, `sieve_regularizer_gradient` resolve in generated Lean.

## Provenance

- LexLean module: `spec/adr/0006/DualChannel.lex.tex` (verified under Lean 4).
- Attestation: `artifacts/adr/0006/verify.json` (ID: `316f8ca7…`).
- Test suite: `tests/test_regularizers.py`.
- Basis summary: `MEASURED: 4`, `MODEL: 4`, `FRONTIER: 2`.

## Context and Problem Statement

In the $Z\text{-MOD}$ optimization framework, state updates must avoid regions where analytical truncations are untrustworthy [MODEL]. The spectral channel exposes uncertainty from omitted high-frequency zeros via the error-term surrogate $R_{\text{err}}(\theta, \pi) = \lambda_{\text{err}} ET(x)^2$, while the combinatorial channel exposes uncertainty from sieve leakage via $R_{\text{bin}}(\theta, \pi) = \lambda_{\text{bin}} B_{\text{bin}}(n)^2$ [MEASURED].

Treating these regularizers as unrelated hyperparameter penalties ignores the fact that both channels derive from a single underlying multiplicity structure over $\mathbb{F}_1$ [FRONTIER].

## Decision Drivers

1. **Unified Reliability Gate**: Formulate a dual-channel regularizer whose channels simultaneously penalize spectral and arithmetic instability [MODEL].
2. **Smooth Analytic Gradients**: Ensure $\nabla R_{\text{err}}$ and $\nabla R_{\text{bin}}$ are differentiable and scale-compatible under embedding height $t = \ln x$ [MEASURED].
3. **Falsifiable Multiplicity Coupling**: Couple spectral and sieve penalties without circular reliance on the Riemann Hypothesis [FRONTIER].

## Considered Alternatives

### Option 1: Coupled dual-channel loss $R_{\text{reg}} = R_{\text{err}} + R_{\text{bin}}$ linked via $n = \ln x$
- Pros: Reflects dual projections of the same multiplicity geometry; balances spectral and sieve truncation; smooth gradients.
- Cons: Requires calibrating two regularization weights $\lambda_{\text{err}}$ and $\lambda_{\text{bin}}$.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Spectral error-term regularization only ($R_{\text{err}}$)
- Pros: Simpler loss formulation with only one penalty term.
- Cons: Leaves the combinatorial sieve side unregularized; fails to damp lattice-point multiplicity blowups.
- Rejected because: ignores arithmetic leakage.
- Basis: [MEASURED]

## Decision

We establish the coupled dual-channel regularizer in $Z\text{-MOD}$:
1. The total regularized loss is defined as:
   $$L(\theta, \pi) = L_{\text{VM}}(\theta, \pi) + R_{\text{err}}(x(\theta, \pi)) + R_{\text{bin}}(n(\theta, \pi))$$
2. The embedding scale connects the spectral coordinate $x$ to the combinatorial sieve index $n$ via the logarithmic relation $n = \ln(x)$ [MODEL].
3. The formal specification in `spec/adr/0006/DualChannel.lex.tex` defines `coupledloss`, `spectralchannel`, and `combinatorialchannel` with Lean 4 kernel-verified theorems `coupled_loss_monotonic`, `spectral_error_bounded`, and `sieve_regularizer_gradient` [MEASURED].

## Consequences

### Positive
- Prevents the optimizer from exploiting numerical artifacts in either the zero-sum or the sieve-sum.
- Guarantees scale consistency across both channels during gradient descent.
- Grounded in machine-checked Lean 4 kernel theorems.

### Negative
- Requires maintaining dual gradient paths during backpropagation.

### Neutral
- Does not affect the location of critical zeros $\rho_n$.

## Verification
- Formal Lean 4 kernel verification: `lexlean verify` emits `artifacts/adr/0006/verify.json`.
- Empirical test suite: `tests/test_regularizers.py` tests monotonicity and gradient smoothness.

## Promotion Criteria
1. Attestation present with `coupled_loss_monotonic`, `spectral_error_bounded`, `sieve_regularizer_gradient` resolving.
2. Unit tests in `tests/test_regularizers.py` passing with exit code 0.

## Links
- Source plan: `../ADR Plan Production Grade.md` (§4 Workstream B)
- Research source: `../Riemann-zero-as-multi-brane.txt` (lines 14–18)

## Supersedes / Superseded by
- Supersedes: none
- Superseded by: none
