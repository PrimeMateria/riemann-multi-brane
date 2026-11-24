#!/usr/bin/env bash
set -euo pipefail

# Script to post the RH-ZMB formal specification RFC issue to UOR-Foundation/f1
REPO_TARGET="UOR-Foundation/f1"
ISSUE_FILE="$(dirname "$0")/../issues/ISSUE_F1_SURFACE_RH_ZMB_SPECIFICATION.md"
ISSUE_TITLE="[RFC / Formal Specification] Riemann Zero as Multi-Brane (RH-ZMB): Arithmetic Surface Geometry over F1, Hodge Index Theorem on H-perp, and Dual-Plane Verification"

echo "=== RH-ZMB GitHub Issue Submission Tool ==="
echo "Target Repository: https://github.com/${REPO_TARGET}"
echo "Issue Title: ${ISSUE_TITLE}"
echo "Source File: ${ISSUE_FILE}"
echo "==========================================="

if ! command -v gh >/dev/null 2>&1; then
    echo "ERROR: GitHub CLI ('gh') is not installed in the current environment."
    echo "You can manually copy the markdown content from: ${ISSUE_FILE}"
    echo "and create an issue at: https://github.com/${REPO_TARGET}/issues/new"
    exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
    echo "WARNING: gh CLI is not authenticated."
    echo ""
    echo "To submit this issue via CLI, please run:"
    echo "    export GH_TOKEN=<your-github-token>"
    echo "or:"
    echo "    gh auth login"
    echo ""
    echo "Then re-run this script: $0"
    echo ""
    echo "Alternatively, you can manually copy the contents of:"
    echo "    ${ISSUE_FILE}"
    echo "and paste it directly into:"
    echo "    https://github.com/${REPO_TARGET}/issues/new"
    exit 2
fi

echo "Submitting issue to ${REPO_TARGET}..."
gh issue create \
    --repo "${REPO_TARGET}" \
    --title "${ISSUE_TITLE}" \
    --body-file "${ISSUE_FILE}" \
    --label "rfc,formal-specification,mathematics,f1-geometry"

echo "Issue submitted successfully!"
