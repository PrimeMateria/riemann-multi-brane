pub const Q: [[i32; 3]; 3] = [[0, 1, 1], [1, 0, 1], [1, 1, 0]];

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct DivisorClass {
    pub x: i32,
    pub y: i32,
    pub z: i32,
}

impl DivisorClass {
    pub fn inner(self, other: DivisorClass) -> i32 {
        // Intersection pairing defined by Q matrix
        self.x * other.y + self.y * other.x +
        self.x * other.z + self.z * other.x +
        self.y * other.z + self.z * other.y
    }
}

pub const AMPLE_H: DivisorClass = DivisorClass { x: 1, y: 1, z: 0 };

/// Returns true iff the divisor `d` is orthogonal to `AMPLE_H` and
/// its self‑intersection is strictly negative.
pub fn is_negative_definite_on_h_perp(d: DivisorClass) -> bool {
    // Orthogonality condition: d·H = 0
    if d.inner(AMPLE_H) != 0 {
        return false;
    }
    // Strict negativity: d·d < 0
    d.inner(d) < 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_q_constant() {
        assert_eq!(Q, [[0, 1, 1], [1, 0, 1], [1, 1, 0]]);
    }

    #[test]
    fn test_ample_h_self_intersection() {
        assert_eq!(AMPLE_H.inner(AMPLE_H), 2);
    }

    #[test]
    fn test_negative_definite_example() {
        // D = F_h - F_v corresponds to (1, -1, 0)
        let d = DivisorClass { x: 1, y: -1, z: 0 };
        assert!(is_negative_definite_on_h_perp(d));
    }

    #[test]
    fn test_non_orthogonal_fails() {
        let d = DivisorClass { x: 1, y: 0, z: 0 };
        assert!(!is_negative_definite_on_h_perp(d));
    }
}
