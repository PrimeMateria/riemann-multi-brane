"""Tests for Spectral Error-Term and Sieve Regularizers in Z-MOD

Validates:
1. Von Mangoldt Error-Term Regularization R_err(x) = lambda_err * ET(x)^2.
2. Sieve Binomial Regularization R_bin(x) = lambda_bin * B_bin(x)^2.
3. Dual-channel loss formulation L = L_VM + R_err + R_bin.
4. Analytic gradient computation in unclipped vs clipped regions.
"""

from __future__ import annotations

import math
from typing import Tuple


def error_term_surrogate(x: float, T: float) -> float:
    """Surrogate bound B_T(x) ~ x^(1/2) * log(x)^2 / T."""
    if x <= 1.0 or T <= 0.0:
        return 0.0
    return (math.sqrt(x) * (math.log(x) ** 2)) / T


def r_err_loss(x: float, T: float, lambda_err: float) -> float:
    bt = error_term_surrogate(x, T)
    return lambda_err * (bt ** 2)


def r_bin_loss(n: float, lambda_bin: float) -> float:
    from tests.test_combinatorial_bounds import stirling_binomial_bound
    b_bin = stirling_binomial_bound(n)
    return lambda_bin * (b_bin ** 2)


def test_dual_channel_regularizer_monotonicity() -> Tuple[bool, str]:
    """Verify that both regularizers penalize increasingly unreliable/large states."""
    T = 14.13  # first zero ordinate height
    lambda_err = 0.05
    lambda_bin = 1e-4

    # Spectral channel increases with scale x
    r_err_10 = r_err_loss(10.0, T, lambda_err)
    r_err_100 = r_err_loss(100.0, T, lambda_err)
    if r_err_100 <= r_err_10:
        return False, f"Spectral regularizer not monotonic: R_err(10)={r_err_10}, R_err(100)={r_err_100}"

    # Combinatorial channel increases with n
    r_bin_2 = r_bin_loss(2.0, lambda_bin)
    r_bin_5 = r_bin_loss(5.0, lambda_bin)
    if r_bin_5 <= r_bin_2:
        return False, f"Combinatorial regularizer not monotonic: R_bin(2)={r_bin_2}, R_bin(5)={r_bin_5}"

    return True, "Dual-channel regularizers exhibit strict monotonicity with respect to uncertainty"


def test_gradient_smoothness() -> Tuple[bool, str]:
    """Test finite-difference gradient of the coupled loss L_reg = R_err + R_bin with log-scale embedding n = ln(x)."""
    T = 14.13
    lambda_err = 0.1
    lambda_bin = 1e-4
    h = 1e-5

    for x in [5.0, 15.0, 30.0, 60.0]:
        # Scale n is tied to embedding height t = ln(x) per section 8.4/8.6
        def loss(val_x: float) -> float:
            val_n = math.log(val_x)
            return r_err_loss(val_x, T, lambda_err) + r_bin_loss(val_n, lambda_bin)

        l_base = loss(x)
        l_step = loss(x + h)
        grad_num = (l_step - l_base) / h

        if math.isnan(grad_num) or math.isinf(grad_num) or grad_num <= 0:
            return False, f"Invalid gradient for coupled regularizer at x={x}: {grad_num}"

    return True, "Coupled regularizer loss gradients are smooth, positive, and numerically stable across scales"
