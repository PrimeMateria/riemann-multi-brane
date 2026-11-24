# RH-ZMB Numerical Stress Benchmark Report (TRR Milestone)

- **Timestamp**: `2026-11-24T06:58:50.912362`
- **Final Verdict**: **PASSED**
- **Total Duration**: `157.42 ms`

## Benchmark Results Breakdown

| ID | Benchmark | Status | Latency | Key Metric |
|---|---|---|---|---|
| `BENCH-01` | Sieve Asymptotics & Stirling Precision Scaling (n <= 10,000) | ✅ PASSED | 0.4ms | Rel Error = 2.50e-05 at n=10000 |
| `BENCH-02` | Multi-Brane Hodge Intersection Eigenspectra (p_1000 = 7919) | ✅ PASSED | 120.2ms | Dim 1003x1003, Sig (1, 1002) |
| `BENCH-03` | Coupled Regularizer Gradient Stability Across Embedding Heights (t in [1, 500]) | ✅ PASSED | 0.2ms | t in [1, 500], Min Log-Grad = 0.26 |
| `BENCH-04` | Explicit Formula Spectral Trace Throughput (10,000 Riemann Zeros) | ✅ PASSED | 36.6ms | 21392296 evals/sec (10k zeros) |

## Diagnostic Telemetry Summary

### BENCH-01: Sieve Asymptotics & Stirling Precision Scaling (n <= 10,000)
- **Verdict**: `PASSED`
- **Latency**: `0.36 ms`
- **Diagnostic**: Evaluated n in [10, 10000]; strictly majorizes exact comb; rel error decays to 2.500e-05 at n=10000.

### BENCH-02: Multi-Brane Hodge Intersection Eigenspectra (p_1000 = 7919)
- **Verdict**: `PASSED`
- **Latency**: `120.22 ms`
- **Diagnostic**: Constructed 1003x1003 intersection matrix across 1000 primes. Strict Lorentzian signature (1, 1002); H^2 = 2.0; 0 violations on H^perp.

### BENCH-03: Coupled Regularizer Gradient Stability Across Embedding Heights (t in [1, 500])
- **Verdict**: `PASSED`
- **Latency**: `0.20 ms`
- **Diagnostic**: Swept t in [1.0, 500.0] across 50 heights. Zero overflow/underflow in log-coordinates; strictly positive monotonic gradients.

### BENCH-04: Explicit Formula Spectral Trace Throughput (10,000 Riemann Zeros)
- **Verdict**: `PASSED`
- **Latency**: `36.64 ms`
- **Diagnostic**: Evaluated 10,000 zeros up to gamma = 9878.70. Throughput = 21392296 evals/sec; conjugate imaginary error < 0.00e+00.
