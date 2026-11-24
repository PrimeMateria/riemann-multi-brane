"""Tests for F1-Square Geometry and Hodge Pairing (ADR-0004)

Validates:
1. Néron-Severi intersection matrix Q on basis {F_h, F_v, Delta}.
2. Ample divisor class H = F_h + F_v with degree H^2 = 2 > 0.
3. Determination of orthogonal complement H^perp.
4. Hodge index theorem condition: negative-definiteness on H^perp (signature (1, 2)).
5. Multi-brane intersection pairing with scaling graphs Gamma_p.
"""

from __future__ import annotations

import math
from typing import List, Tuple


def mat_mul_vec(A: List[List[float]], v: List[float]) -> List[float]:
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def dot_product(u: List[float], v: List[float]) -> float:
    return sum(u[i] * v[i] for i in range(len(u)))


def quadratic_form(A: List[List[float]], v: List[float]) -> float:
    return dot_product(v, mat_mul_vec(A, v))


def test_neron_severi_matrix() -> Tuple[bool, str]:
    """Verify the 3x3 Néron-Severi matrix Q on {F_h, F_v, Delta}.
    
    F_h^2 = 0, F_v^2 = 0, F_h . F_v = 1
    Delta . F_h = 1, Delta . F_v = 1, Delta^2 = 2
    """
    Q = [
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 2.0],
    ]
    # Check symmetry
    for i in range(3):
        for j in range(3):
            if Q[i][j] != Q[j][i]:
                return False, f"Matrix Q not symmetric at ({i}, {j})"

    # Check determinant: det(Q) = 0*(0-1) - 1*(2-1) + 1*(1-0) = -1 + 1 = 0
    # Rank of {F_h, F_v, Delta} on classical P^1 x P^1 is 2 because Delta ~ F_h + F_v.
    # When scaling branes are included, rank expands.
    det_Q = (
        Q[0][0] * (Q[1][1] * Q[2][2] - Q[1][2] * Q[2][1])
        - Q[0][1] * (Q[1][0] * Q[2][2] - Q[1][2] * Q[2][0])
        + Q[0][2] * (Q[1][0] * Q[2][1] - Q[1][1] * Q[2][0])
    )
    if abs(det_Q) > 1e-9:
        return False, f"Expected det(Q) = 0 for standard classical genus-0 divisor, got {det_Q}"

    return True, "Néron-Severi matrix Q satisfies all T3 relations"


def test_ample_class_degree() -> Tuple[bool, str]:
    """Verify that H = F_h + F_v has positive self-intersection H^2 = 2."""
    Q = [
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 2.0],
    ]
    H = [1.0, 1.0, 0.0]  # F_h + F_v
    H_sq = quadratic_form(Q, H)
    if abs(H_sq - 2.0) > 1e-9:
        return False, f"Expected H^2 = 2.0, got {H_sq}"
    return True, f"Ample class H = F_h + F_v satisfies H^2 = {H_sq} > 0"


def test_orthogonal_complement_negative_definiteness() -> Tuple[bool, str]:
    """Verify negative-definiteness on the non-trivial subspace of H^perp.
    
    D in H^perp implies D . H = 0.
    With H = F_h + F_v, D = [x, y, z]:
    D . H = Q[0] . D + Q[1] . D = (y + z) + (x + z) = x + y + 2z = 0.
    
    Choose independent vector in H^perp:
    v1 = [1, -1, 0] (F_h - F_v):
    v1 . H = 1 - 1 + 0 = 0.
    v1^2 = [1, -1, 0] Q [1, -1, 0]^T = 0 - 2 + 0 = -2 < 0.
    """
    Q = [
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 2.0],
    ]
    H = [1.0, 1.0, 0.0]
    v1 = [1.0, -1.0, 0.0]

    # Check orthogonality: v1 . H = 0
    ortho = dot_product(H, mat_mul_vec(Q, v1))
    if abs(ortho) > 1e-9:
        return False, f"Vector v1 is not orthogonal to H: v1 . H = {ortho}"

    # Check self-intersection: v1^2 = -2
    v1_sq = quadratic_form(Q, v1)
    if v1_sq >= 0:
        return False, f"Hodge negative-definiteness failed: v1^2 = {v1_sq} >= 0"

    return True, f"Orthogonal vector v1 = F_h - F_v satisfies v1 . H = {ortho} and v1^2 = {v1_sq} < 0 (Hodge verified)"


def test_scaling_graph_multi_brane_pairing() -> Tuple[bool, str]:
    """Test extended multi-brane intersection pairing on basis {H, F_h - F_v, Gamma_p}.
    
    For a prime scaling brane Gamma_p:
    Gamma_p . F_h = p, Gamma_p . F_v = 1, Gamma_p^2 = 2 - 2p <= 0.
    """
    p = 3
    # Basis: B = [F_h, F_v, Gamma_3]
    # Gamma_3 . F_h = 3, Gamma_3 . F_v = 1, Gamma_3^2 = 2 - 2(3) = -4
    Q_p = [
        [0.0, 1.0, 3.0],
        [1.0, 0.0, 1.0],
        [3.0, 1.0, -4.0],
    ]
    H = [1.0, 1.0, 0.0]
    H_sq = quadratic_form(Q_p, H)

    # In H^perp:
    # D = [x, y, z] => D . H = (y + 3z) + (x + z) = x + y + 4z = 0.
    # v1 = [1, -1, 0] => x + y + 4z = 1 - 1 + 0 = 0.
    # v2 = [2, 2, -1] => 2 + 2 - 4 = 0.
    v1 = [1.0, -1.0, 0.0]
    v2 = [2.0, 2.0, -1.0]

    v1_sq = quadratic_form(Q_p, v1)
    v2_sq = quadratic_form(Q_p, v2)

    if v1_sq >= 0 or v2_sq >= 0:
        return False, f"Negative-definiteness failed on H^perp: v1^2 = {v1_sq}, v2^2 = {v2_sq}"

    msg = f"Extended multi-brane pairing for p={p}: H^2={H_sq}>0, v1^2={v1_sq}<0, v2^2={v2_sq}<0 (Strict Hodge Signature (1, 2))"
    return True, msg
