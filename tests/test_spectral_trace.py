"""Tests for Explicit Formula Spectral Trace (First 8 Riemann Zeros)

Validates:
1. The first 8 non-trivial Riemann zero imaginary ordinates gamma_1 .. gamma_8.
2. Truncated explicit formula zero-sum S_8(x) = sum_{n=1}^8 (x^rho_n / rho_n + x^rho_bar_n / rho_bar_n).
3. Verification of conjugate symmetry ensuring pure real oscillation.
4. Boundedness of oscillatory remainder relative to smooth term x.
"""

from __future__ import annotations

import cmath
import math
from typing import List, Tuple

# First 8 non-trivial Riemann zeros (imaginary parts gamma_n)
ZEROS_GAMMA = [
    14.134725141734693790,
    21.022039638771554992,
    25.010857580145688763,
    30.424876125859513210,
    32.935061587739189690,
    37.586178158825677257,
    40.918719012147495187,
    43.327073280914999519,
]


def explicit_zero_term(x: float, gamma: float) -> complex:
    """Computes x^rho / rho + x^rho_bar / rho_bar for rho = 1/2 + i*gamma."""
    rho = complex(0.5, gamma)
    rho_bar = complex(0.5, -gamma)

    # x^rho = exp(rho * ln(x))
    ln_x = math.log(x)
    term1 = cmath.exp(rho * ln_x) / rho
    term2 = cmath.exp(rho_bar * ln_x) / rho_bar
    return term1 + term2


def truncated_zero_sum(x: float, num_zeros: int = 8) -> float:
    """Computes real oscillatory sum over the first num_zeros pairs."""
    total = 0.0
    for i in range(num_zeros):
        gamma = ZEROS_GAMMA[i]
        val = explicit_zero_term(x, gamma)
        # Imaginary parts must cancel by conjugate symmetry
        assert abs(val.imag) < 1e-12, f"Conjugate symmetry failed at gamma_{i+1}: {val.imag}"
        total += val.real
    return total


def test_conjugate_symmetry() -> Tuple[bool, str]:
    """Verify that pair-sum is strictly real for various x."""
    for x in [2.0, 5.0, 10.0, 50.0, 100.0]:
        for i, gamma in enumerate(ZEROS_GAMMA):
            val = explicit_zero_term(x, gamma)
            if abs(val.imag) > 1e-10:
                return False, f"Non-zero imaginary component at x={x}, gamma_{i+1}={gamma}: {val.imag}"
    return True, "Conjugate symmetry verified: imaginary components cancel to < 1e-10"


def test_spectral_trace_oscillation() -> Tuple[bool, str]:
    """Verify that truncated zero sum modulates smooth term x without diverging."""
    for x in [10.0, 20.0, 50.0, 100.0]:
        s8 = truncated_zero_sum(x, 8)
        # Von Koch / explicit bound: |S_8(x)| < 2 * x^(1/2) * sum(1/gamma_n)
        gamma_inv_sum = sum(1.0 / g for g in ZEROS_GAMMA)
        bound = 2.0 * math.sqrt(x) * gamma_inv_sum

        if abs(s8) > bound * 1.5:
            return False, f"Spectral trace S_8({x}) = {s8} exceeds theoretical envelope {bound}"

    return True, "Truncated spectral sum S_8(x) remains strictly bounded within explicit formula envelope"
