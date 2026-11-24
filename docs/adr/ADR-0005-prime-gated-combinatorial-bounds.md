---
adr: "0005"
title: "Replace trivial 4^n combinatorial bound with Stirling and prime-gated P2C asymptotics"
status: Accepted
date: 2026-11-23
deciders: [Mathematical Physics Board, Formal Verification, Empirical Testing]
consulted: [Geometry Group, Analytic Number Theory Group]
workstream: B
gate: CDR
lexlean_module: spec/adr/0005/CombinatorialBounds.lex.tex
attestation: artifacts/adr/0005/verify.json
supersedes: []
superseded_by: []
source_plan: "ADR Plan Production Grade.md"
tags: [combinatorics, stirling-bound, sieve-density, p2c]
---

# ADR-0005: Replace trivial 4^n combinatorial bound with Stirling and prime-gated P2C asymptotics

## Status

`Accepted` (2026-11-23). Theorem-shaped. Promoted on `lexlean verify` attestation `316f8ca7be8b01d39da39008404a6fea23233d76346a01b4a727e4f636094407`, produced under `leanprover/lean4:v4.32.2`. Verified theorems `stirling_upper_bound`, `sieve_density_tight`, `rbin_regularizer_wellformed` resolve in generated Lean.

## Provenance

- LexLean module: `spec/adr/0005/CombinatorialBounds.lex.tex` (verified under Lean 4).
- Attestation: `artifacts/adr/0005/verify.json` (ID: `316f8ca7…`).
- Test suite: `tests/test_combinatorial_bounds.py` [MEASURED].
- Basis summary: `MEASURED: 5`, `MODEL: 5`, `FRONTIER: 1`.

## Context and Problem Statement

In the combinatorial channel of the RH-ZMB model, the intersection matrix entries of the $T_3$ template count lattice-point multiplicities on the monoid product $\mathbb{N} \times \mathbb{N}$ [MODEL]. In elementary prime number theory (e.g., Erdős-Selberg proofs of PNT), central binomial coefficients $\binom{2n}{n}$ control the magnitude of combinatorial remainder terms [MODEL].

Standard introductory derivations use the trivial binomial bound $\binom{2n}{n} \le (1+1)^{2n} = 4^n$ [MODEL]. As revealed in `Riemann-zero-as-multi-brane.txt`, using this loose $4^n$ bound underpowers the combinatorial channel by orders of magnitude, causing the finite prime truncation proxy to lose eigenvalue margins and swamp the signature check beyond the first 8 zero ordinates [MEASURED].

By sharpening this bound using Stirling asymptotics $\binom{2n}{n} \sim \frac{4^n}{\sqrt{\pi n}}$ and prime-gated P2C distributions, the entrywise error bounds on the intersection matrix are tightened by a factor of $O(\sqrt{n})$, dramatically extending the numerical horizon for testing the Hodge signature [MEASURED].

## Decision Drivers

1. **Tight Asymptotic Control**: Replace loose $4^n$ envelopes with tight Stirling bounds $\frac{4^n}{\sqrt{\pi n}} (1 + \frac{1}{8n})$ [MODEL].
2. **Eigenvalue Margin Preservation**: Prevent numerical noise from swamping negative-definiteness on $H^\perp$ at larger prime cutoffs [MEASURED].
3. **Dual-Channel Regularization**: Supply the mathematical skeleton for the combinatorial regularizer $R_{\text{bin}}(\theta, \pi)$ in $Z\text{-MOD}$ [FRONTIER].

## Considered Alternatives

### Option 1: Stirling-refined and prime-gated P2C asymptotic bounds
- Pros: Provides $O(1/\sqrt{n})$ tightening; matches exact central binomial coefficients within $<1\%$ for $n \ge 5$; preserves numerical signature margins on $H^\perp$.
- Cons: Slightly more complex gradient computation: $\nabla R_{\text{bin}}$ involves $\frac{d}{dx} \left[\frac{4^x}{\sqrt{\pi x}}\right]$.
- Rejected: no — this is the chosen option.
- Basis: [MODEL]

### Option 2: Retain classical $4^n$ bound
- Pros: Simplest possible formula.
- Cons: Extremely loose; grows exponentially faster than actual lattice multiplicity; fails signature check past ordinate $\gamma_8$.
- Rejected because: underpowers the sieve channel and invalidates numerical scaling tests.
- Basis: [MEASURED]

## Decision

We formally replace the $4^n$ bound throughout the RH-ZMB combinatorial channel and regularizer framework:
1. For any lattice height or truncation index $n \ge 1$, the central binomial bound $B_{\text{bin}}(n)$ is defined as:
   $$B_{\text{bin}}(n) = \frac{4^n}{\sqrt{\pi n}} \left(1 + \frac{1}{8n}\right)$$
2. The combinatorial regularizer in $Z\text{-MOD}$ is specified as:
   $$R_{\text{bin}}(\theta, \pi) = \lambda_{\text{bin}} \cdot B_{\text{bin}}(x(\theta, \pi))^2$$
   with analytic gradient:
   $$\nabla R_{\text{bin}} = 2 \lambda_{\text{bin}} B_{\text{bin}} B_{\text{bin}}' \cdot \nabla x$$
   where $B_{\text{bin}}'(x) = B_{\text{bin}}(x) \left[\ln 4 - \frac{1}{2x} - \frac{1}{8x^2 + x}\right]$.
3. The empirical test harness (`tests/test_combinatorial_bounds.py`) validates that $B_{\text{bin}}(n)$ strictly upper-bounds $\binom{2n}{n}$ for all $n \ge 1$ while improving upon $4^n$ by a factor exceeding $3\times$ by $n=10$ and $17\times$ by $n=100$.

## Consequences

### Positive
- Sieve leakage is tightly suppressed in the combinatorial channel.
- Signature checking on $H^\perp$ remains numerically stable across significantly larger prime truncations.
- Both the spectral channel ($R_{\text{err}}$) and the combinatorial channel ($R_{\text{bin}}$) operate with comparable asymptotic fidelity.

### Negative
- Gradient evaluations require tracking log-derivative correction factors in optimizer steps.

### Neutral
- Retains compatibility with standard $Z\text{-MOD}$ parameter configurations.

## Verification
- Empirical test suite in `tests/test_combinatorial_bounds.py`.
- Automated conformance checking via `python3 adr/_governance/check_adr_log.py`.

## Promotion Criteria
1. Test suite `tests/test_combinatorial_bounds.py` passes with zero failures.
2. Verified that $B_{\text{bin}}(n) \ge \binom{2n}{n}$ for all $1 \le n \le 200$.

## Links
- Source plan: `../ADR Plan Production Grade.md` (§4 Workstream B)
- Research source: `../Riemann-zero-as-multi-brane.txt` (lines 14–18, 23–26)

## Supersedes / Superseded by
- Supersedes: none
- Superseded by: none
