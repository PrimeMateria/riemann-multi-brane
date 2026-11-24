# AGENTS — Riemann Zero as Multi-Brane (RH-ZMB) Production System

Standing instructions, operating invariants, and mechanical execution protocol for any agent, CLI tool, or automated pipeline operating in the **RH-ZMB** subsystem (`mount/UNSOLVED/rh-zero-multi-brane`).

---

## 1. Operating Rules & Stratification Discipline

All formalizations, proofs, platform crates, and decision records in RH-ZMB adhere to the three-tier stratification discipline (**LexLean → PIRTM → Sedona**):

| Tier | Plane | Mandatory Rule | Enforced By |
|---|---|---|---|
| **Tier 1** | **LexLean** (Compiler Grammar) | Closed lexicon filter. Strictly no raw prose, natural language paragraphs, or ungrounded floating-point estimators inside `.lex.tex` files (SPEC §4.2, §25). All mathematical structures and theorems are verified by the Lean 4 kernel (`v4.32.2`). | `lexlean check --all`, `lexlean verify --all` |
| **Tier 2** | **PIRTM** (Conservation & Duality) | Conservation Law: $\forall t \;\exists \bar{t} : t \equiv \pi(t) \oplus \bar{t}$ with $\langle\pi(t), \bar{t}\rangle = 0$. Zero silent omission. Every informal conjecture or non-formalized claim must carry an explicit, content-addressed rejection witness certificate $\bar{t}$. | `manifests/rejection_witness_matrix.json`, `tools/generate_rejection_matrix.py` |
| **Tier 3** | **Sedona Spine** (Evidentiary Non-Spoliation) | Proof of Non-Spoliation under Sedona Conference Principles 1 & 6. Cryptographically locked ADR hashes in `accepted_hashes.json`. Coverage Theorem verified with zero unmapped leakage across mathematical claims and test suites. | `docs/adr/_governance/check_adr_log.py`, `run-tests.sh` |

---

## 2. Standard Mechanical Execution Checklist for LexLean Re-Expression

Any agent, tool, or automated pipeline performing a LexLean formalization alongside an existing package or corpus must follow this standard mechanical 11-step pipeline without deviation:

- [ ] **Create LexLean project directory alongside original**  
  Mirror the target structure alongside the source package (e.g., `<package>-lexlean/` beside `<package>/`).
- [ ] **Initialize LexLean project (lexlean.toml, lockfile)**  
  Establish `lexlean.toml`, pin `lean-toolchain` (e.g., `v4.32.2`), generate `lakefile.toml`, and lock lexicon closures into `lexlean.lock`.
- [ ] **Write Object.lex.tex - Closed, Held, NonFactoring (discrete Nat version)**  
  Define closed primitive object types, non-factoring guarantees, and core structures using discrete `Nat` arithmetic.
- [ ] **Write Tier.lex.tex - tier bundle structure with certificate**  
  Construct tier bundle types, capability witnesses, and formal certificates.
- [ ] **Write Tiers.lex.tex - stacking composition (closed_comp)**  
  Formulate vertical tier stacking, inductive compositions, and proof of `closed_comp`.
- [ ] **Write Budget.lex.tex - horizon budget (Nat-based, K≤1 linear)**  
  Formulate finite horizon budget constraints (Nat-based, linear $K \le 1$ boundaries).
- [ ] **Write Mixing.lex.tex - deterministic vs stochastic defect**  
  Model deterministic vs. stochastic defects and empirical bounds.
- [ ] **Write Main.lex.tex - entrypoint importing all modules**  
  Canonical entrypoint module importing and re-exporting all verified modules.
- [ ] **Run lexlean lock, check, build to verify**  
  Execute `lexlean lock && lexlean check --all && lexlean verify --all` to obtain a content-addressed Lean 4 kernel attestation (`artifacts/verify.json`).
- [ ] **Generate PIRTM Rejection Witness Matrix**  
  Extract all verbatim section bodies from `corpus/`, compute SHA-256 digests, map formal projections $\pi(s)$, and issue classified residual certificates $\bar{s}$.
- [ ] **Verify Coverage Theorem & Lock Integrity**  
  Assert $\forall s \in \text{Sections}, \mathsf{Status}(s) \in \{\mathsf{Verified}(\pi(s)), \mathsf{WitnessedResidual}(\bar{s})\}$ with 0 unmapped leakage.

---

## 3. Dual-Plane System Architecture

The RH-ZMB repository operates strictly under the **Dual-Plane Architecture** codified in [ADR-0002](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/docs/adr/ADR-0002-dual-plane-architecture.md):

1. **The Formal Specification Plane (`spec/adr/`)**:
   - Written in LexLean and checked against the official Lean 4 kernel (`v4.32.2`).
   - Hosts `RhZmb.F1Square` (Néron-Severi lattice and Hodge index theorem $T_5$), `RhZmb.CombinatorialBounds` (Stirling bound $B_{\text{bin}}(n)$ majorization), and `RhZmb.DualChannel` (coupled regularizer monotonicity).
   - Certified attestation: `blake3:316f8ca735e58129849206d289069d5110a2f1abffbc207038a8ba9a7647dc74`.

2. **The Empirical Test & Benchmark Plane (`run_tests.py`, `benchmark_rh_scaling.py`)**:
   - Implemented in Python 3.10+ and compiled native crates via PrismPM 0.5.0.
   - Executes 12 mathematical test assertions and 4 stress benchmark suites (`BENCH-01` through `BENCH-04`).
   - Automatically generates paired reports:
     - Human-readable: `reports/latest_report.md` & `reports/latest_benchmark_report.md`.
     - Machine-readable JSON: `reports/latest_results.json` & `reports/latest_benchmark_results.json`.

---

## 4. Verification & Validation Commands

All verification must be run from `/run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane`:

```bash
# 1. Run the entire 5-plane production test suite (ADR, tests, benchmarks, build, report):
./run-tests.sh

# 2. Validate Architectural Decision Records (ADRs) governance and hash lockfile:
python3 docs/adr/_governance/check_adr_log.py

# 3. Execute the 12-assertion empirical test harness:
python3 run_tests.py

# 4. Execute the 4-stage numerical stress benchmark suite:
python3 benchmark_rh_scaling.py

# 5. Check LexLean formal closed-lexicon syntax:
lexlean check --all

# 6. Verify Lean 4 kernel cryptographic attestations:
lexlean verify --all

# 7. Check PrismPM platform package:
prismpm check
```

---

## 5. Downstream & Inter-Repository Links

- **GitHub Issue RFC**: [`issues/ISSUE_F1_SURFACE_RH_ZMB_SPECIFICATION.md`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/issues/ISSUE_F1_SURFACE_RH_ZMB_SPECIFICATION.md) for [`UOR-Foundation/f1`](https://github.com/UOR-Foundation/f1).
- **Formal Publication Report**: [`reports/RH_ZMB_Production_Report.pdf`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/reports/RH_ZMB_Production_Report.pdf) compiled from [`reports/RH_ZMB_Production_Report.tex`](file:///run/media/multiplic/AGI/prismagi/mount/UNSOLVED/rh-zero-multi-brane/reports/RH_ZMB_Production_Report.tex).
- **PrismPM Platform Crate**: `.prism/build/8f461e23.../rh-zero-multi-brane-0.1.0.crate`.
