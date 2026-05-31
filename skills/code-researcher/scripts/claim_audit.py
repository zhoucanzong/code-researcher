#!/usr/bin/env python3
"""Flag high-impact report claims that may need stronger source evidence."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SOURCE_RE = re.compile(
    r"(?P<path>(?:[\w.@-]+/)+[\w.@-]+(?:\.[A-Za-z0-9]+)?|[\w.@-]+\.(?:py|js|ts|tsx|jsx|go|rs|java|md|toml|json|yaml|yml))(?::(?P<line>\d+))?"
)

HIGH_IMPACT_RE = re.compile(
    r"\b("
    r"core|central|primary|main|critical|guarantees|ensures|prevents|"
    r"scales|scalable|safe|stable|reliable|risk|bottleneck|coupling|"
    r"technical debt|designed for|optimizes for|tradeoff|abstraction|boundary"
    r")\b",
    re.IGNORECASE,
)

ZH_HIGH_IMPACT_RE = re.compile(
    r"(核心|主要|关键|中心|保证|确保|防止|可扩展|安全|稳定|可靠|风险|瓶颈|耦合|技术债|为了.+设计|优化|取舍|抽象|边界)"
)

CLAIM_HINT_RE = re.compile(r"^(\s*(?:[-*]|\d+\.)\s+|#{1,4}\s+)?(.{18,})$")


def classify(line: str) -> str:
    lowered = line.lower()
    if any(word in lowered for word in ("risk", "bottleneck", "technical debt", "coupling")) or any(
        word in line for word in ("风险", "瓶颈", "技术债", "耦合")
    ):
        return "risk"
    if any(word in lowered for word in ("should", "recommend", "next", "maintainer")) or any(
        word in line for word in ("建议", "应该", "维护者", "下一步")
    ):
        return "recommendation"
    if any(word in lowered for word in ("designed for", "optimizes", "tradeoff", "abstraction", "boundary")) or any(
        word in line for word in ("设计", "优化", "取舍", "抽象", "边界")
    ):
        return "design-reading"
    if any(word in lowered for word in ("calls", "returns", "loads", "writes", "reads", "routes")) or any(
        word in line for word in ("调用", "返回", "加载", "写入", "读取", "路由")
    ):
        return "behavior"
    return "fact-or-summary"


def has_source_near(lines: list[str], index: int, radius: int = 1) -> bool:
    start = max(0, index - radius)
    end = min(len(lines), index + radius + 1)
    return any(SOURCE_RE.search(lines[i]) for i in range(start, end))


def extract_sources(lines: list[str], index: int, radius: int = 1) -> list[dict[str, Any]]:
    start = max(0, index - radius)
    end = min(len(lines), index + radius + 1)
    sources = []
    seen = set()
    for i in range(start, end):
        for match in SOURCE_RE.finditer(lines[i]):
            path = match.group("path")
            line = int(match.group("line")) if match.group("line") else None
            key = (path, line)
            if key in seen:
                continue
            seen.add(key)
            sources.append({"path": path, "line": line})
    return sources


def audit(markdown: str) -> dict[str, Any]:
    lines = markdown.splitlines()
    claims = []
    unsupported = []
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        if not CLAIM_HINT_RE.match(line):
            continue
        high_impact = bool(HIGH_IMPACT_RE.search(line) or ZH_HIGH_IMPACT_RE.search(line))
        if not high_impact:
            continue
        has_evidence = has_source_near(lines, index)
        item = {
            "report_line": index + 1,
            "type": classify(line),
            "has_nearby_source": has_evidence,
            "sources": extract_sources(lines, index),
            "claim": stripped[:280],
        }
        claims.append(item)
        if not has_evidence:
            unsupported.append(item)
    return {
        "total_high_impact_claims": len(claims),
        "unsupported_high_impact_claims": len(unsupported),
        "claims": claims,
        "unsupported": unsupported,
    }


def render_text(result: dict[str, Any], lang: str) -> str:
    if lang == "zh":
        lines = [
            "# 结论审计",
            "",
            f"- 高影响结论：{result['total_high_impact_claims']}",
            f"- 缺少邻近源码证据：{result['unsupported_high_impact_claims']}",
        ]
        if result["unsupported"]:
            lines.extend(["", "## 需要补证据的结论"])
            for item in result["unsupported"][:30]:
                lines.append(f"- L{item['report_line']} [{item['type']}] {item['claim']}")
        else:
            lines.extend(["", "没有发现缺少邻近源码证据的高影响结论。"])
        return "\n".join(lines) + "\n"

    lines = [
        "# Claim Audit",
        "",
        f"- High-impact claims: {result['total_high_impact_claims']}",
        f"- Missing nearby source evidence: {result['unsupported_high_impact_claims']}",
    ]
    if result["unsupported"]:
        lines.extend(["", "## Claims Needing Evidence"])
        for item in result["unsupported"][:30]:
            lines.append(f"- L{item['report_line']} [{item['type']}] {item['claim']}")
    else:
        lines.extend(["", "No high-impact claims without nearby source evidence were found."])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a markdown report for source-backed claims.")
    parser.add_argument("report", help="Markdown report path")
    parser.add_argument("--out", help="Output path. Defaults to stdout.")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    parser.add_argument("--lang", choices=["en", "zh"], default="en")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        parser.error(f"report does not exist: {report_path}")
    result = audit(report_path.read_text(encoding="utf-8", errors="ignore"))
    rendered = (
        json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.format == "json"
        else render_text(result, args.lang)
    )
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
