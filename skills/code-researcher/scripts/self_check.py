#!/usr/bin/env python3
"""Minimal self-check for the code-researcher skill."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def run_scan(root: Path, out: Path) -> None:
    script = root / "skills" / "code-researcher" / "scripts" / "scan_repo.py"
    target = root / "skills" / "code-researcher"
    subprocess.run([sys.executable, str(script), str(target), "--out", str(out)], check=True)


def run_summary(root: Path, scan: Path) -> str:
    script = root / "skills" / "code-researcher" / "scripts" / "summarize_scan.py"
    result = subprocess.run(
        [sys.executable, str(script), str(scan), "--lang", "en"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def run_claim_audit(root: Path, report: Path) -> dict:
    script = root / "skills" / "code-researcher" / "scripts" / "claim_audit.py"
    result = subprocess.run(
        [sys.executable, str(script), str(report), "--format", "json"],
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    root = repo_root()
    with tempfile.TemporaryDirectory() as tmpdir:
        scan_path = Path(tmpdir) / "scan.json"
        report_path = Path(tmpdir) / "report.md"
        run_scan(root, scan_path)
        scan = json.loads(scan_path.read_text(encoding="utf-8"))
        summary = run_summary(root, scan_path)
        report_path.write_text(
            "\n".join(
                [
                    "# Test Report",
                    "",
                    "The core boundary is implemented by `skills/code-researcher/SKILL.md`.",
                    "",
                    "",
                    "This is a critical risk without evidence nearby.",
                ]
            ),
            encoding="utf-8",
        )
        audit = run_claim_audit(root, report_path)

    manifests = {item["path"]: item for item in scan.get("manifests", [])}
    docs = {item["path"]: item for item in scan.get("documentation", [])}
    entries = {item["path"]: item for item in scan.get("entry_candidates", [])}
    core_dirs = {item["directory"]: item for item in scan.get("core_directories", [])}
    route = [item["target"] for item in scan.get("reading_route", [])]
    languages = {item["language"] for item in scan.get("languages", [])}
    diagrams = scan.get("diagram_suggestions", [])

    assert_true("SKILL.md" in manifests, "SKILL.md should be recognized as a manifest")
    assert_true(manifests["SKILL.md"]["type"] == "codex-skill", "SKILL.md should be codex-skill")
    assert_true("SKILL.md" in docs, "SKILL.md should be documentation")
    assert_true("SKILL.md" in entries, "SKILL.md should be an entry candidate")
    assert_true("scripts" in core_dirs, "scripts should be a core directory")
    assert_true("references/runtime-story.md" in docs, "runtime-story reference should be documentation")
    assert_true("references/evidence-quality.md" in docs, "evidence-quality reference should be documentation")
    assert_true("Python" in languages, "Python lines should be counted")
    assert_true("Markdown" in languages, "Markdown lines should be counted")
    assert_true(route and route[0] == "SKILL.md", "reading route should start from SKILL.md")
    assert_true(isinstance(scan.get("architecture_signals", []), list), "architecture_signals should exist")
    assert_true(diagrams, "diagram suggestions should exist")
    assert_true(diagrams[0]["focus"] == "entry-flow", "first diagram suggestion should be entry flow")
    assert_true("# Codebase Map" in summary, "summary should render an English codebase map")
    assert_true("Suggested Reading Route" in summary, "summary should include a reading route")
    assert_true("Diagram Suggestions" in summary, "summary should include diagram suggestions")
    assert_true(audit["total_high_impact_claims"] >= 2, "claim audit should find high-impact claims")
    assert_true(audit["unsupported_high_impact_claims"] >= 1, "claim audit should flag unsupported claims")

    print("self-check ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
