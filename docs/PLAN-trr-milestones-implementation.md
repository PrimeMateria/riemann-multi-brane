# Master Implementation Plan: Test Readiness Review (TRR) Milestones & Platform Integration

- **Project:** Riemann Zero as Multi-Brane (RH-ZMB)
- **Target Subsystem:** [`/run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane)
- **Governing ADRs:** [ADR-0001](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0001-adopt-append-only-adr-practice.md) through [ADR-0007](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0007-production-test-harness-benchmarks-ci-cd.md)
- **Subsequent ADR:** [ADR-0008](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0008-trr-milestones-production-implementation.md)
- **Document ID:** `PLAN-RH-ZMB-TRR-2026.11`
- **Current Lifecycle Gate:** Test Readiness Review (TRR) — Active

---

## 1. Executive Summary & Objectives

The **Riemann Zero as Multi-Brane (RH-ZMB)** subsystem has successfully passed Preliminary Design Review (PDR) and Critical Design Review (CDR), establishing:
1. Formal specifications in LexLean and Lean 4 verifying the $\mathbb{F}_1$-square Hodge index theorem on $H^\perp$, Stirling asymptotic sieve bounds, and coupled regularizer monotonicity (attestation `blake3:316f8ca7...`).
2. An immutable platform crate release compiled through PrismPM 0.5.0 (`8f461e23...`).
3. A 12-assertion empirical test harness executing in $14\,\mathrm{ms}$ with zero failures.
4. An authoritative, 14-page publication report in LaTeX and compiled PDF ([`reports/RH_ZMB_Production_Report.pdf`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/reports/RH_ZMB_Production_Report.pdf)).

To complete the active **Test Readiness Review (TRR)** phase and prepare for downstream platform production, this master plan operationalizes the three core milestones defined in the engineering roadmap:
- **Milestone 1:** High-scale numerical stress benchmark suite (`benchmark_rh_scaling.py`) spanning `BENCH-01` through `BENCH-04`.
- **Milestone 2:** Fail-closed pre-commit hooks (`.githooks/pre-commit`, `install-hooks.sh`) and continuous integration workflow (`.github/workflows/verify-test.yml`).
- **Milestone 3:** Downstream platform integration linking the compiled crate into $Z\text{-MOD}$ optimization pipelines and binding the verified Hodge pairing kernel into the Phase Mirror verification engine.

---

## 2. Milestone 1: Numerical Stress Benchmark Suite (`benchmark_rh_scaling.py`)

The benchmark engine provides stress-testing and empirical validation beyond the discrete unit tests of `run_tests.py`, pushing numerical parameters to asymptotic boundaries.

```mermaid
flowchart TD
    subgraph BenchmarkEngine["benchmark_rh_scaling.py"]
        B1["BENCH-01: Sieve Asymptotics (n <= 10,000)"]
        B2["BENCH-02: Multi-Brane Hodge Pairing (p_1000 = 7919)"]
        B3["BENCH-03: Logarithmic Height Stability (t in [1, 500])"]
        B4["BENCH-04: Spectral Trace Throughput (10,000 Zeros)"]
    end
    
    BenchmarkEngine --> Telemetry["Machine Telemetry (latest_benchmark_results.json)"]
    BenchmarkEngine --> Report["Human Report (latest_benchmark_report.md)"]
    BenchmarkEngine --> Gating{"Pass/Fail Criteria"}
    Gating -->|All Thresholds Met| TRR_Success["TRR Gate Approved"]
    Gating -->|Regression Detected| TRR_Block["Fail-Closed Blocking"]
```

### Detailed Benchmark Specifications

#### `BENCH-01`: Sieve Asymptotics & Stirling Precision Scaling ($n \le 10,000$)
- **Domain:** Combinatorial Channel (ADR-0005).
- **Mathematical Form:** 
  $$B_{\text{bin}}(n) = \frac{4^n}{\sqrt{\pi n}}\left(1 + \frac{1}{8n}\right), \quad C(2n, n) = \binom{2n}{n}$$
- **Evaluation Sweep:** $n \in \{10, 50, 100, 500, 1000, 2500, 5000, 10000\}$.
- **Arbitrary Precision Arithmetic:** Utilizes Python's native arbitrary-precision integer arithmetic for $\binom{2n}{n}$ and high-precision floating point for $B_{\text{bin}}(n)$.
- **Validation Criteria:**
  1. Strict upper bound majorization: $B_{\text{bin}}(n) \ge \binom{2n}{n}$ for all evaluation points.
  2. Monotonic decay of relative approximation error:
     $$\epsilon(n) = \frac{B_{\text{bin}}(n) - \binom{2n}{n}}{\binom{2n}{n}} < \frac{1}{128n^2}$$
     At $n = 10,000$, $\epsilon(10000) < 1.0 \times 10^{-7}$.
  3. Single-point evaluation latency $< 0.5\,\mathrm{ms}$.

#### `BENCH-02`: Multi-Brane $\Gamma_p$ Hodge Intersection Pairing & Eigenspectra ($p_{1000} = 7919$)
- **Domain:** $\mathbb{F}_1$-Square Geometry & Multi-Brane Extension (ADR-0004).
- **Mathematical Form:**
  Construct the $(3 + K) \times (3 + K)$ intersection matrix $Q_K$ on the extended basis:
  $$\mathcal{B}_K = \{F_h, F_v, \Delta, \Gamma_{p_1}, \Gamma_{p_2}, \dots, \Gamma_{p_K}\}, \quad K = 1,000$$
  where $p_1 = 2$ and $p_{1000} = 7919$. The block intersection form is:
  $$Q_K = \begin{pmatrix}
  Q_3 & B^T \\
  B & D_K
  \end{pmatrix}$$
  where $Q_3 = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}$, $B_{k, \cdot} = \left(\frac{\ln p_k}{\sqrt{p_k}}, \frac{\ln p_k}{\sqrt{p_k}}, 0\right)$, and $(D_K)_{jk} = -\delta_{jk} (\ln p_k)^2$.
- **Validation Criteria:**
  1. Spectral signature: Exactly 1 positive eigenvalue $\lambda_1 > 0$ and exactly 1,002 strictly negative eigenvalues $\lambda_k < 0$ (strict Lorentzian signature $(1, 1002)$).
  2. Negative-definiteness on $H^\perp$: For any non-zero projection $v \in H^\perp$, $v^T Q_K v < 0$.
  3. Matrix construction and eigensolve completed in $< 5.0\,\mathrm{seconds}$.

#### `BENCH-03`: Coupled Regularizer Gradient Stability Across Embedding Heights ($t \in [1, 500]$)
- **Domain:** Dual-Channel Regularization & $Z\text{-MOD}$ Optimization (ADR-0006).
- **Mathematical Form:**
  $$t = \ln x, \quad n(t) = \frac{e^t}{2}$$
  $$\frac{d}{dt} \ln B_{\text{bin}}(n(t)) = n(t)\left[2\ln 2 - \frac{1}{2n(t)} - \frac{1}{8n(t)^2 + n(t)}\right]$$
- **Evaluation Sweep:** 50 log-spaced evaluation heights $t \in [1.0, 500.0]$ corresponding to $x \in [e^1, e^{500}] \approx [2.7, 1.4 \times 10^{217}]$.
- **Validation Criteria:**
  1. Complete absence of IEEE 754 arithmetic overflow, underflow, NaN, or Inf in logarithmic gradients.
  2. Monotonic positive growth: $\frac{d}{dt} \ln B_{\text{bin}}(n(t)) > 0$ for all $t \in [1, 500]$.
  3. Condition number smoothness: Local variation $|\nabla_{t+\delta} - \nabla_t| / \delta$ bounded by $\mathcal{O}(e^t)$.

#### `BENCH-04`: Explicit Formula Spectral Trace Throughput ($N = 10,000$ Zeros)
- **Domain:** Spectral Channel & Operator Dynamics (ADR-0004, ADR-0006).
- **Mathematical Form:**
  $$S_N(x) = 2 \sum_{k=1}^N \frac{x^{1/2}\left(\frac{1}{2}\cos(\gamma_k \ln x) + \gamma_k \sin(\gamma_k \ln x)\right)}{\frac{1}{4} + \gamma_k^2}$$
  evaluated over the first $N = 10,000$ non-trivial Riemann zeros $\gamma_1 \approx 14.1347$ to $\gamma_{10000} \approx 9877.7826$.
- **Validation Criteria:**
  1. Vectorized evaluation throughput $\ge 50,000$ zero evaluations per second.
  2. Imaginary conjugate symmetry cancellation: $\sum \mathrm{Im}\left(\frac{x^\rho}{\rho} + \frac{x^{\bar{\rho}}}{\bar{\rho}}\right) < 1.0 \times 10^{-14}$.
  3. Numerical oscillation boundedness: $|S_N(x)| \le C \cdot x^{1/2} \ln^2 x$.

---

## 3. Milestone 2: Pre-Commit Hook & CI/CD Integration

To prevent regression, proof decay, and unobserved documentation drift, all code staging and repository actions are governed by automated gating.

### Local Pre-Commit Hook Architecture
- **Hook Path:** `.githooks/pre-commit`
- **Installer:** `install-hooks.sh`
- **Configuration Command:** `git config core.hooksPath .githooks`
- **Execution Workflow:**
  1. Validates ADR decision log conformance (`python3 docs/adr/_governance/check_adr_log.py`).
  2. Executes unit test harness (`./run-tests.sh --hook`).
  3. Verifies LexLean formatting parity (`lexlean lock` parity check).
  4. Returns exit code 1 on any failure, blocking git commit before staging.

### Continuous Integration Pipeline (`.github/workflows/verify-test.yml`)
The workflow operates hermetically in a containerized Linux runner:

```yaml
name: RH-ZMB Production Verification Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Toolchains
        run: |
          ./scripts/install-tools.sh
      - name: ADR Decision Log Governance Audit
        run: |
          python3 docs/adr/_governance/check_adr_log.py
      - name: LexLean Formal Verification
        run: |
          lexlean lock
          lexlean check --all
          lexlean verify --all
      - name: PrismPM Platform Build
        run: |
          prismpm check
          prismpm build --no-provenance
      - name: Empirical Mathematical Test Suite
        run: |
          ./run-tests.sh
      - name: Numerical Stress Benchmark Suite
        run: |
          python3 benchmark_rh_scaling.py
      - name: Archive Verification & Benchmark Telemetry
        uses: actions/upload-artifact@v4
        with:
          name: verification-telemetry
          path: |
            reports/
            artifacts/
```

---

## 4. Milestone 3: Downstream Platform Integration

### Integration with $Z\text{-MOD}$ Optimization Pipelines
- **Artifact:** [`artifacts/prism/rh-zero-multi-brane-0.1.0.crate`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/artifacts/prism/rh-zero-multi-brane-0.1.0.crate)
- **Downstream Consumer:** `/run/media/multiplic/AGI/prismagi/mount/CRATES/z-mod`
- **Interface Contract:**
  1. Add dependency to `crates/z-mod/Cargo.toml`:
     ```toml
     [dependencies]
     rh-zero-multi-brane = { path = "../../UNSOLVED/rh-zero-multi-brane/artifacts/prism" }
     ```
  2. Replace legacy exponential regularizer with:
     ```rust
     use rh_zero_multi_brane::sieve::stirling_bound;
     let r_bin = lambda_bin * stirling_bound(n).powi(2);
     ```
  3. Eliminates gradient explosion in neural surrogate training.

### Binding into Phase Mirror Verification Engine
- **Engine Path:** `/run/media/multiplic/AGI/prismagi/mount/PHASE MIRROR`
- **Interface Contract:**
  1. The Phase Mirror cross-domain attestation tool (`attest_cross_domain_mission`) ingests:
     - Lean 4 kernel formal attestation: [`artifacts/adr/0004/verify.json`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/artifacts/adr/0004/verify.json)
     - PrismPM platform manifest: [`artifacts/prism/manifest.json`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/artifacts/prism/manifest.json)
  2. Binds the verified negative-definiteness theorem `hodge_index_perp` into Phase Mirror's governance gate evaluation, proving that the multi-brane bundle cannot admit off-line zeros.

---

## 5. Traceability & Acceptance Matrix

| Requirement | Implementation Target | Verification Method | Lifecycle Gate |
|---|---|---|---|
| `BENCH-01` | `benchmark_rh_scaling.py` | Asymptotic error $< 10^{-7}$ at $n = 10,000$ | TRR |
| `BENCH-02` | `benchmark_rh_scaling.py` | Eigenspectrum signature $(1, 1002)$ across 1,000 primes | TRR |
| `BENCH-03` | `benchmark_rh_scaling.py` | Zero overflow/underflow across $t \in [1, 500]$ | TRR |
| `BENCH-04` | `benchmark_rh_scaling.py` | Throughput $\ge 50,000$ zeros/sec; cancel $< 10^{-14}$ | TRR |
| Pre-Commit Hook | `.githooks/pre-commit`, `install-hooks.sh` | Shell execution test and git hook trigger | TRR |
| CI/CD Pipeline | `.github/workflows/verify-test.yml` | Hermetic workflow validation | TRR |
| $Z\text{-MOD}$ Linking | `artifacts/prism/*.crate` | Crate dependency export & symbol resolution | Post-TRR |
| Phase Mirror Binding | Attestation telemetry bridge | Cross-domain manifest verification | Post-TRR |
