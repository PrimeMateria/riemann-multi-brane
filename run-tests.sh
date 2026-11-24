#!/usr/bin/env bash
# RH-ZMB Production Test & Verification Pipeline
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

MODE="${1:-all}"
if [[ "${MODE}" == "--hook" || "${MODE}" == "--unit" ]]; then
    MODE="unit"
fi

echo "========================================================================"
echo "RH-ZMB Production Multi-Plane Verification Pipeline"
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "Mode: ${MODE}"
echo "========================================================================"

echo ""
echo "▶ Plane 1: ADR Decision Log Governance Audit"
python3 docs/adr/_governance/check_adr_log.py

if [[ "${MODE}" == "all" || "${MODE}" == "formal" ]]; then
    echo ""
    echo "▶ Plane 2: Lean 4 Kernel Formal Attestation (LexLean)"
    lexlean verify --all

    echo ""
    echo "▶ Plane 3: PrismPM Platform Model Verification"
    prismpm check
fi

echo ""
echo "▶ Plane 4: Empirical Mathematical Invariant Test Suite"
python3 run_tests.py

if [[ "${MODE}" == "all" || "${MODE}" == "benchmarks" ]]; then
    echo ""
    echo "▶ Plane 5: High-Scale Numerical Stress Benchmark Suite (TRR Milestones)"
    python3 benchmark_rh_scaling.py
fi

echo ""
echo "========================================================================"
echo "Final Verdict: ALL CONFIGURED PLANES VERIFIED SUCCESSFULLY"
echo "========================================================================"
