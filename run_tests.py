#!/usr/bin/env python3
"""RH-ZMB Production Test Harness Runner

Executes mathematical and empirical tests for the Riemann Zero as Multi-Brane subsystem:
- Sieve and central binomial bounds (Stirling vs 4^n)
- F1-square Néron-Severi pairing and Hodge index on H^perp
- Dual-channel regularizers (R_err + R_bin in Z-MOD)
- Explicit formula spectral trace across first 8 Riemann zero ordinates

Generates:
- Human-readable console report
- `reports/latest_report.md`
- `reports/latest_results.json`
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "reports"

# Import test modules
from tests.test_combinatorial_bounds import (
    test_gradient_finite_differences,
    test_stirling_vs_trivial_ratio,
    test_tightness_and_asymptotics,
    test_upper_bound_property,
)
from tests.test_hodge_pairing import (
    test_ample_class_degree,
    test_neron_severi_matrix,
    test_orthogonal_complement_negative_definiteness,
    test_scaling_graph_multi_brane_pairing,
)
from tests.test_regularizers import (
    test_dual_channel_regularizer_monotonicity,
    test_gradient_smoothness,
)
from tests.test_spectral_trace import (
    test_conjugate_symmetry,
    test_spectral_trace_oscillation,
)


TEST_SUITES = [
    {
        "suite": "Combinatorial Sieve Bounds (ADR-0005)",
        "tests": [
            ("Upper Bound Property B_bin(n) >= C(2n, n)", test_upper_bound_property),
            ("Stirling Bound Tightness (<0.1% error for n>=10)", test_tightness_and_asymptotics),
            ("Stirling vs Trivial 4^n Envelope Ratio", test_stirling_vs_trivial_ratio),
            ("Analytic Gradient vs Finite Differences", test_gradient_finite_differences),
        ],
    },
    {
        "suite": "F1-Square Geometry & Hodge Pairing (ADR-0004)",
        "tests": [
            ("Néron-Severi Intersection Matrix Template Q", test_neron_severi_matrix),
            ("Ample Class Degree H^2 = 2 > 0", test_ample_class_degree),
            ("Hodge Negative-Definiteness on H^perp (Signature (1, 2))", test_orthogonal_complement_negative_definiteness),
            ("Extended Multi-Brane Scaling Brane Pairing Gamma_p", test_scaling_graph_multi_brane_pairing),
        ],
    },
    {
        "suite": "Dual-Channel Regularizers (Z-MOD Coupling)",
        "tests": [
            ("Dual-Channel Regularizer Monotonicity", test_dual_channel_regularizer_monotonicity),
            ("Coupled Loss Gradient Smoothness", test_gradient_smoothness),
        ],
    },
    {
        "suite": "Explicit Formula Spectral Trace",
        "tests": [
            ("Conjugate Symmetry of Zero Pair Terms", test_conjugate_symmetry),
            ("Spectral Trace Oscillation Boundedness S_8(x)", test_spectral_trace_oscillation),
        ],
    },
]


def run_all_tests() -> Dict[str, Any]:
    start_time = time.perf_counter()
    timestamp = datetime.now().isoformat()
    results = {
        "timestamp": timestamp,
        "total": 0,
        "passed": 0,
        "failed": 0,
        "suites": [],
        "verdict": "PASSED",
    }

    print("=" * 72)
    print("RH-ZMB Production Test Harness Runner")
    print(f"Timestamp: {timestamp}")
    print("=" * 72)

    for suite_def in TEST_SUITES:
        suite_name = suite_def["suite"]
        print(f"\n▶ Suite: {suite_name}")
        suite_record = {
            "name": suite_name,
            "tests": [],
            "passed": 0,
            "failed": 0,
        }

        for test_name, test_fn in suite_def["tests"]:
            results["total"] += 1
            t0 = time.perf_counter()
            try:
                ok, msg = test_fn()
            except Exception as e:
                ok, msg = False, f"Unhandled exception: {e}"
            elapsed = time.perf_counter() - t0

            status = "PASSED" if ok else "FAILED"
            if ok:
                results["passed"] += 1
                suite_record["passed"] += 1
                icon = "✔"
            else:
                results["failed"] += 1
                suite_record["failed"] += 1
                results["verdict"] = "FAILED"
                icon = "✖"

            suite_record["tests"].append({
                "name": test_name,
                "status": status,
                "duration_sec": elapsed,
                "message": msg,
            })

            print(f"  [{icon}] {test_name:<55} ({elapsed*1000:.1f}ms)")
            if not ok:
                print(f"      Details: {msg}")

        results["suites"].append(suite_record)

    total_duration = time.perf_counter() - start_time
    results["duration_sec"] = total_duration

    print("\n" + "=" * 72)
    print(f"Summary: {results['passed']}/{results['total']} tests passed in {total_duration:.3f}s")
    print(f"Final Verdict: {results['verdict']}")
    print("=" * 72)

    return results


def write_reports(results: Dict[str, Any]):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Machine-readable JSON
    json_path = REPORTS_DIR / "latest_results.json"
    json_path.write_text(json.dumps(results, indent=2))

    # Human-readable Markdown
    md_path = REPORTS_DIR / "latest_report.md"
    lines = [
        "# RH-ZMB Test Execution Report",
        "",
        f"- **Execution Timestamp**: `{results['timestamp']}`",
        f"- **Verdict**: **{results['verdict']}**",
        f"- **Summary**: {results['passed']} / {results['total']} tests passed ({results['duration_sec']:.3f} seconds)",
        "",
        "## Test Suite Breakdown",
        "",
    ]

    for suite in results["suites"]:
        lines.append(f"### {suite['name']}")
        lines.append(f"Result: {suite['passed']}/{len(suite['tests'])} passed\n")
        lines.append("| Status | Test Name | Duration | Diagnostic Message |")
        lines.append("|---|---|---|---|")
        for t in suite["tests"]:
            icon = "✅ PASSED" if t["status"] == "PASSED" else "❌ FAILED"
            lines.append(f"| {icon} | {t['name']} | {t['duration_sec']*1000:.1f}ms | {t['message']} |")
        lines.append("")

    md_path.write_text("\n".join(lines) + "\n")
    print(f"Generated test reports in: {REPORTS_DIR}")


def main():
    results = run_all_tests()
    write_reports(results)
    if results["verdict"] != "PASSED":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
