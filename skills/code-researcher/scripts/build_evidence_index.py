#!/usr/bin/env python3
"""Extract lightweight evidence references from a markdown report."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REFERENCE_RE = re.compile(
    r"(?P<path>(?:[\w.-]+/)+[\w.@-]+(?:\.[A-Za-z0-9]+)?)(?::(?P<line>\d+))?"
)


def extract(markdown: str) -> list[dict]:
    evidence = []
    seen = set()
    for line_no, line in enumerate(markdown.splitlines(), start=1):
        for match in REFERENCE_RE.finditer(line):
            path = match.group("path")
            source_line = match.group("line")
            key = (path, source_line, line_no)
            if key in seen:
                continue
            seen.add(key)
            evidence.append(
                {
                    "report_line": line_no,
                    "source": path,
                    "source_line": int(source_line) if source_line else None,
                    "context": line.strip()[:240],
                }
            )
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an evidence index from a report.")
    parser.add_argument("report", help="Markdown report path")
    parser.add_argument("--out", help="Output JSON path. Defaults to stdout.")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        parser.error(f"report does not exist: {report_path}")

    evidence = extract(report_path.read_text(encoding="utf-8", errors="ignore"))
    payload = json.dumps({"report": report_path.as_posix(), "evidence": evidence}, ensure_ascii=False, indent=2)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

