#!/usr/bin/env python3
"""Render a human-readable project map from scan_repo.py JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def wants_chinese(text: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in text)


def zh_reason(reason: str) -> str:
    translations = {
        "Codex skill entrypoint": "Codex skill 入口",
        "orientation and project intent": "理解项目定位和使用方式",
        "runtime, dependency, and command surface": "运行时、依赖和命令入口",
        "high-signal implementation area": "高信号实现区域",
        "large source file worth skimming for responsibility boundaries": "大文件，适合快速确认职责边界",
        "main entry path from public surface to core behavior": "从公开入口到核心行为的主路径",
        "command flow from arguments to output": "从参数到输出的命令流程",
        "request path through route, middleware, handler, and response": "经过路由、中间件、处理器和响应的请求路径",
        "public API handoff into core engine": "公开 API 进入核心引擎的交接路径",
        "configuration loading and precedence": "配置加载和优先级",
        "extension points and plugin lifecycle": "扩展点和插件生命周期",
        "ports, adapters, and external systems": "端口、adapter 和外部系统边界",
        "state ownership and persistence boundary": "状态归属和持久化边界",
        "job scheduling, execution, retry, and commit": "任务调度、执行、重试和提交",
        "pipeline from input to intermediate form to output": "从输入到中间结构再到输出的管道",
        "intent, planning, tool execution, observation, response": "意图、规划、工具执行、观察和响应",
        "UI state and data ownership": "UI 状态和数据归属",
        "events, logs, metrics, and tracing boundary": "事件、日志、指标和追踪边界",
        "read next": "下一步阅读",
        "entry candidate": "入口候选",
    }
    if reason in translations:
        return translations[reason]
    if reason.startswith("conventional ") and reason.endswith(" entry file"):
        name = reason.removeprefix("conventional ").removesuffix(" entry file")
        return f"约定式入口文件 {name}"
    if reason.startswith("script `"):
        return reason.replace("script", "脚本", 1)
    return reason


def render_en(scan: dict[str, Any]) -> str:
    languages = ", ".join(
        f"{item['language']} {item['lines']} lines" for item in scan.get("languages", [])[:5]
    ) or "unknown"
    out = [
        "# Codebase Map",
        "",
        f"Root: `{scan.get('root', '')}`",
        f"Size: {scan.get('total_files', 0)} files, {scan.get('total_lines', 0)} lines",
        f"Languages: {languages}",
        "",
        "## Likely Entry Points",
    ]
    entries = scan.get("entry_candidates", [])
    if entries:
        for item in entries[:8]:
            out.append(f"- `{item['path']}`: {item.get('reason', 'entry candidate')} (score {item.get('score')})")
    else:
        out.append("- No strong entry candidate found. Start from docs and manifests.")

    out.extend(["", "## Manifests and Command Surfaces"])
    manifests = scan.get("manifests", [])
    if manifests:
        for item in manifests[:10]:
            bits = [item.get("type", "manifest")]
            if item.get("name"):
                bits.append(f"name `{item['name']}`")
            if item.get("scripts"):
                bits.append("scripts " + ", ".join(f"`{s}`" for s in item["scripts"][:8]))
            out.append(f"- `{item['path']}`: " + "; ".join(bits))
    else:
        out.append("- No manifest recognized.")

    out.extend(["", "## High-Signal Directories"])
    for item in scan.get("core_directories", [])[:8]:
        if item.get("directory") == ".":
            continue
        languages = ", ".join(lang["language"] for lang in item.get("languages", [])[:3])
        signals = ", ".join(item.get("signals", [])) or "code"
        arch = ", ".join(item.get("architecture_signals", [])[:5])
        arch_suffix = f", architecture: {arch}" if arch else ""
        out.append(
            f"- `{item['directory']}`: {item.get('code_lines', 0)} code lines, "
            f"{languages or 'mixed'}, signals: {signals}{arch_suffix}"
        )

    out.extend(["", "## Architecture Signals"])
    arch_signals = scan.get("architecture_signals", [])
    if arch_signals:
        for item in arch_signals[:10]:
            sample = ", ".join(f"`{path}`" for path in item.get("sample", [])[:3])
            out.append(f"- {item['signal']}: {item['files']} files, {item['lines']} lines; sample {sample}")
    else:
        out.append("- No strong architecture signal recognized from paths.")

    out.extend(["", "## Diagram Suggestions"])
    suggestions = scan.get("diagram_suggestions", [])
    if suggestions:
        for item in suggestions[:6]:
            sample = ", ".join(f"`{path}`" for path in item.get("evidence_sample", [])[:3])
            out.append(f"- {item['kind']} for {item['focus']}: {item['why']}; evidence {sample}")
    else:
        out.append("- No diagram suggested by the scan. Add visuals only if source reading reveals a useful boundary.")

    out.extend(["", "## Documentation"])
    docs = scan.get("documentation", [])
    if docs:
        for item in docs[:10]:
            out.append(f"- `{item['path']}`: {item.get('kind', 'docs')}")
    else:
        out.append("- No documentation-like files recognized.")

    out.extend(["", "## Tests, Examples, Generated Code"])
    tests = scan.get("tests", {})
    examples = scan.get("examples", {})
    generated = scan.get("generated_code", {})
    out.append(f"- Tests: {tests.get('count', 0)} files")
    out.append(f"- Examples: {examples.get('count', 0)} files")
    out.append(f"- Generated code: {generated.get('count', 0)} files")

    out.extend(["", "## Suggested Reading Route"])
    route = scan.get("reading_route", [])
    if route:
        for idx, item in enumerate(route, start=1):
            out.append(f"{idx}. `{item['target']}`: {item.get('why', 'read next')}")
    else:
        out.append("1. Start from the README or top manifest, then inspect the largest source files.")

    out.extend(["", "## Reading Coverage Seed"])
    out.append("- Scanned: all files counted in this map, excluding skipped binary/vendor/build areas.")
    if route:
        out.append("- Skim next: " + ", ".join(f"`{item['target']}`" for item in route[:5]))
    if entries:
        out.append(f"- Trace candidate: `{entries[0]['path']}`")
    out.append("- Do not make strong design claims until the relevant files are skimmed, traced, or audited.")

    out.extend(["", "## Next Research Move"])
    if entries:
        out.append(f"Trace the path starting at `{entries[0]['path']}` and connect it to the main output or side effect.")
    else:
        out.append("Identify the public command, API, route, or documented quickstart before writing a runtime story.")
    return "\n".join(out) + "\n"


def render_zh(scan: dict[str, Any]) -> str:
    languages = "，".join(
        f"{item['language']} {item['lines']} 行" for item in scan.get("languages", [])[:5]
    ) or "未知"
    out = [
        "# 项目地图",
        "",
        f"根目录：`{scan.get('root', '')}`",
        f"规模：{scan.get('total_files', 0)} 个文件，{scan.get('total_lines', 0)} 行",
        f"语言：{languages}",
        "",
        "## 可能入口",
    ]
    entries = scan.get("entry_candidates", [])
    if entries:
        for item in entries[:8]:
            out.append(f"- `{item['path']}`：{zh_reason(item.get('reason', 'entry candidate'))}（score {item.get('score')}）")
    else:
        out.append("- 没有识别到强入口，先从文档和 manifest 读起。")

    out.extend(["", "## Manifest 与命令面"])
    manifests = scan.get("manifests", [])
    if manifests:
        for item in manifests[:10]:
            bits = [item.get("type", "manifest")]
            if item.get("name"):
                bits.append(f"名称 `{item['name']}`")
            if item.get("scripts"):
                bits.append("scripts " + "，".join(f"`{s}`" for s in item["scripts"][:8]))
            out.append(f"- `{item['path']}`：" + "；".join(bits))
    else:
        out.append("- 没有识别到 manifest。")

    out.extend(["", "## 高信号目录"])
    for item in scan.get("core_directories", [])[:8]:
        if item.get("directory") == ".":
            continue
        languages = "，".join(lang["language"] for lang in item.get("languages", [])[:3])
        signals = "，".join(item.get("signals", [])) or "code"
        arch = "，".join(item.get("architecture_signals", [])[:5])
        arch_suffix = f"，架构信号：{arch}" if arch else ""
        out.append(
            f"- `{item['directory']}`：{item.get('code_lines', 0)} 行代码，"
            f"{languages or '混合'}，信号：{signals}{arch_suffix}"
        )

    out.extend(["", "## 架构信号"])
    arch_signals = scan.get("architecture_signals", [])
    if arch_signals:
        for item in arch_signals[:10]:
            sample = "，".join(f"`{path}`" for path in item.get("sample", [])[:3])
            out.append(f"- {item['signal']}：{item['files']} 个文件，{item['lines']} 行；样例 {sample}")
    else:
        out.append("- 没有从路径中识别到强架构信号。")

    out.extend(["", "## 配图建议"])
    suggestions = scan.get("diagram_suggestions", [])
    if suggestions:
        for item in suggestions[:6]:
            sample = "，".join(f"`{path}`" for path in item.get("evidence_sample", [])[:3])
            out.append(f"- {item['kind']} / {item['focus']}：{zh_reason(item['why'])}；证据 {sample}")
    else:
        out.append("- 扫描阶段没有建议配图；只有源码阅读发现关键边界时再画。")

    out.extend(["", "## 文档"])
    docs = scan.get("documentation", [])
    if docs:
        for item in docs[:10]:
            out.append(f"- `{item['path']}`：{item.get('kind', 'docs')}")
    else:
        out.append("- 没有识别到文档类文件。")

    out.extend(["", "## 测试、示例、生成代码"])
    tests = scan.get("tests", {})
    examples = scan.get("examples", {})
    generated = scan.get("generated_code", {})
    out.append(f"- 测试：{tests.get('count', 0)} 个文件")
    out.append(f"- 示例：{examples.get('count', 0)} 个文件")
    out.append(f"- 生成代码：{generated.get('count', 0)} 个文件")

    out.extend(["", "## 建议阅读路线"])
    route = scan.get("reading_route", [])
    if route:
        for idx, item in enumerate(route, start=1):
            out.append(f"{idx}. `{item['target']}`：{zh_reason(item.get('why', 'read next'))}")
    else:
        out.append("1. 先读 README 或顶层 manifest，再看最大源文件。")

    out.extend(["", "## 阅读覆盖起点"])
    out.append("- Scanned：本地图已统计所有纳入扫描的文件，跳过了二进制、vendor、构建产物等低信号区域。")
    if route:
        out.append("- Skim next：" + "，".join(f"`{item['target']}`" for item in route[:5]))
    if entries:
        out.append(f"- Trace candidate：`{entries[0]['path']}`")
    out.append("- 相关文件进入 skimmed、traced 或 audited 之前，不要做强设计结论。")

    out.extend(["", "## 下一步研究动作"])
    if entries:
        out.append(f"从 `{entries[0]['path']}` 开始追一条运行路径，并连接到主要输出或副作用。")
    else:
        out.append("先确认公开命令、API、路由或 README quickstart，再写 Runtime Story。")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a scan_repo.py JSON result.")
    parser.add_argument("scan_json", help="Path to scan JSON")
    parser.add_argument("--lang", choices=["en", "zh"], help="Output language")
    parser.add_argument("--query", help="Original user request for language auto-detection")
    parser.add_argument("--out", help="Output markdown path. Defaults to stdout.")
    args = parser.parse_args()

    scan_path = Path(args.scan_json)
    if not scan_path.exists():
        parser.error(f"scan JSON does not exist: {scan_path}")
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    lang = args.lang or ("zh" if wants_chinese(args.query or "") else "en")
    rendered = render_zh(scan) if lang == "zh" else render_en(scan)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
