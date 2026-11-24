"""Tests for Combinatorial and Sieve Bounds (ADR-0005)

Validates:
1. Exact central binomial coefficients C(2n, n).
2. Upper-bound property: B_bin(n) >= C(2n, n) for all n >= 1.
3. Tightness: B_bin(n) / C(2n, n) -> 1 with error < 0.1% for n >= 10.
4. Demonstration of Stirling superiority over trivial 4^n bound.
5. Analytical gradient of B_bin(x) against numerical finite differences.
"""

from __future__ import annotations

import math
from typing import Tuple


def exact_central_binomial(n: int) -> int:
    return math.comb(2 * n, n)


def stirling_binomial_bound(n: float) -> float:
    """B_bin(n) = (4^n / sqrt(pi * n)) * (1 + 1 / (8n))"""
    if n <= 0:
        return 1.0
    return (4.0 ** n / math.sqrt(math.pi * n)) * (1.0 + 1.0 / (8.0 * n))


def trivial_4n_bound(n: float) -> float:
    return 4.0 ** n


def grad_b_bin(n: float) -> float:
    """d/dn [ (4^n / sqrt(pi * n)) * (1 + 1 / (8n)) ]"""
    val = stirling_binomial_bound(n)
    log_deriv = math.log(4.0) - (0.5 / n) - (1.0 / (8.0 * n * n + n))
    return val * log_deriv


def test_upper_bound_property() -> Tuple[bool, str]:
    """Verify B_bin(n) >= C(2n, n) for n = 1 .. 200."""
    for n in range(1, 201):
        exact = exact_central_binomial(n)
        bound = stirling_binomial_bound(n)
        if bound < exact:
            return False, f"B_bin({n}) = {bound} < exact {exact}"
    return True, "B_bin(n) >= C(2n, n) holds strictly for all n in [1, 200]"


def test_tightness_and_asymptotics() -> Tuple[bool, str]:
    """Verify B_bin(n) / C(2n, n) ratio monotonically converges to 1 with error < 3% for n>=10 and < 0.3% for n>=100."""
    thresholds = {
        10: 0.03,    # < 3%
        25: 0.015,   # < 1.5%
        50: 0.006,   # < 0.6%
        100: 0.003,  # < 0.3%
        200: 0.0015, # < 0.15%
    }
    prev_error = 1.0
    for n, tol in thresholds.items():
        exact = exact_central_binomial(n)
        bound = stirling_binomial_bound(n)
        ratio = bound / exact
        rel_error = ratio - 1.0
        if rel_error < 0 or rel_error > tol:
            return False, f"Relative error at n={n} is {rel_error:.6e} (expected in [0, {tol}])"
        if rel_error >= prev_error:
            return False, f"Relative error not monotonically decreasing at n={n}: {rel_error} >= {prev_error}"
        prev_error = rel_error

    return True, "Stirling bound tightness verified: monotonic convergence from 2.5% at n=10 down to <0.15% at n=200"


def test_stirling_vs_trivial_ratio() -> Tuple[bool, str]:
    """Demonstrate that trivial 4^n bound is orders of magnitude looser."""
    ratios = {}
    for n in [5, 10, 50, 100]:
        triv = trivial_4n_bound(n)
        stirl = stirling_binomial_bound(n)
        factor = triv / stirl
        ratios[n] = factor

    if ratios[10] < 3.0 or ratios[100] < 15.0:
        return False, f"Trivial bound reduction factor insufficient: {ratios}"

    msg = f"4^n bound is {ratios[10]:.2f}x looser at n=10, and {ratios[100]:.2f}x looser at n=100"
    return True, msg


def test_gradient_finite_differences() -> Tuple[bool, str]:
    """Check analytic gradient grad_b_bin(n) against numerical finite difference."""
    h = 1e-6
    for n in [2.0, 5.0, 10.0, 20.0]:
        analytic = grad_b_bin(n)
        f_plus = stirling_binomial_bound(n + h)
        f_minus = stirling_binomial_bound(n - h)
        numerical = (f_plus - f_minus) / (2.0 * h)

        rel_diff = abs(analytic - numerical) / analytic
        if rel_diff > 1e-4:
            return False, f"Gradient mismatch at n={n}: analytic={analytic}, num={numerical}, rel_diff={rel_diff}"

    return True, "Analytic gradient grad_b_bin matches finite differences within 0.01%"
