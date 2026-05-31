---
name: code-researcher
description: >
  Bilingual code research and architecture reporting for repositories. Use when
  the user asks to understand a codebase, map a project, study source code,
  trace execution, explain architecture, evaluate maintainability, compare
  repositories, or produce a deep architecture report. Trigger phrases include:
  code research, source study, repo map, architecture report, runtime trace,
  maintainer notes, understand this repo, study this library, compare projects,
  代码研究, 源码分析, 架构报告, 项目地图, 执行路径, 读代码, 学习项目,
  维护者视角, 对比项目.
---

# Code Researcher

Turn an unfamiliar repository into a clear, evidence-backed understanding of what
it contains, how its main path runs, why its abstractions exist, and how a
maintainer should work with it.

把陌生代码库转化为一份有证据、有执行路径、有设计判断、也能服务维护者的架构理解。

## Language Routing / 语言路由

- Match the user's language. If the user writes Chinese, answer in Chinese; if
  the user writes English, answer in English; if the request is mixed, use the
  language that carries the actual task.
- Read bilingual guidance as one policy, not two separate workflows. Prefer the
  wording and examples that match the user's language, but keep the same research
  bar in every language.
- Keep source identifiers, commands, file paths, symbols, API names, and package
  names in their original language.
- When repository docs use a different language from the user request, cite the
  source faithfully and explain it in the user's language.
- Do not translate code concepts mechanically. Choose the idiom an engineer in
  that language would naturally use.

## Commands / 命令

The skill should feel like a small product with clear actions:

- `/code-map <repo>`: fast project map, entry candidates, high-signal
  directories, and a reading route.
- `/code-trace <repo> [scenario]`: follow one concrete request, CLI command,
  job, or API from input to output.
- `/code-research <repo>`: default research report with map, runtime story,
  design reading, and maintainer notes.
- `/code-research-deep <repo>`: deeper architecture report for serious source
  study, including module investigations, tradeoffs, risks, diagrams when useful,
  and an evidence index.
- `/code-compare <repoA> <repoB>`: compare architecture, abstractions, maturity,
  risks, and fit for the user's decision.

中文语义：

- `/code-map <repo>`：项目地图、入口候选、核心目录、阅读路线。
- `/code-trace <repo> [场景]`：追踪一个真实请求、命令、任务或 API。
- `/code-research <repo>`：默认代码研究报告。
- `/code-research-deep <repo>`：深度架构报告。
- `/code-compare <repoA> <repoB>`：对比两个项目的架构取舍与适用性。

If the user does not use a command, infer the nearest action. Default to
`/code-research` for broad requests and `/code-map` for quick overview requests.

## Default Behavior / 默认行为

- Prefer action over interviews. Ask only when the repository cannot be located,
  the comparison targets are missing, or the requested runtime story is too
  ambiguous to choose responsibly.
- Use local code and repository documentation as primary evidence.
- The report must analyze architecture together with code evidence. Do not write
  a design-only essay detached from source files.
- Use web research only when the user asks for it, the repository is remote, or
  current ecosystem context materially affects the analysis.
- For conclusions about behavior or design, cite file paths and line numbers
  whenever practical.
- When depth is not specified, deliver a concise report first and name the best
  next deep-dive path.
- Treat generated code, vendored code, fixtures, and examples as secondary unless
  they explain the system's contract.
- Use the depth implied by the command:
  - `skim`: `/code-map`
  - `study`: `/code-research` and `/code-trace`
  - `deep`: `/code-research-deep` and large comparisons
- For large repositories, do not ask for mode selection unless the user's goal
  would materially change the work. Choose a reasonable depth and name the choice.

中文原则：

- 默认少问，能从代码和文档判断的事就直接判断。
- 以本地代码和仓库文档为第一证据。
- 报告必须结合代码一起分析，不能脱离源码空谈架构概念。
- 除非用户要求、仓库是远程目标，或生态背景会明显影响判断，否则不做网页调研。
- 行为和设计结论尽量标注文件路径和行号。
- 未指定深度时先交付可用的标准研究报告，再指出最值得继续深挖的方向。

## Research Method / 研究方法

Use the four-layer method in `references/research-method.md`:

1. Codebase Map: language, entry points, dependencies, directories, key files.
2. Runtime Story: trace one real request, command, job, or API through the code.
3. Design Inquiry: explain core abstractions, tradeoffs, and alternatives.
4. Maintainer Notes: highlight risks, extension points, and reading routes.

中文四层方法：

1. Codebase Map：项目地图，回答“这里有什么，先读哪里”。
2. Runtime Story：运行故事，回答“主流程真实怎么跑”。
3. Design Inquiry：设计追问，回答“为什么这样设计”。
4. Maintainer Notes：维护者笔记，回答“接下来怎么安全地改”。

## Workflow / 工作流

1. Locate or clone the repository. If the input is a local path, use it directly.
2. Run `scripts/scan_repo.py <repo> --out <work_dir>/repo-scan.json`.
3. Optionally run `scripts/summarize_scan.py <work_dir>/repo-scan.json --query
   "<user request>"` to turn the JSON scan into a first project-map draft in the
   user's language.
4. Review the scan's `reading_route`, `manifests`, `entry_candidates`,
   `core_directories`, `tests`, and `generated_code` before opening many files.
5. Read the project docs, dependency/command manifests, likely entry points, and
   the highest-signal implementation directories.
6. Pick one runtime story using `references/runtime-story.md`. If the user did
   not specify one, choose the scenario that best represents the repo's main
   purpose.
7. Identify 2-5 responsibilities or modules worth explaining. Choose by runtime
   importance and ownership, not by directory names alone.
8. Use `references/visual-reporting.md` and the scan's `diagram_suggestions` to
   decide whether the report needs Mermaid diagrams.
9. For deep mode, sketch the report shape with `references/report-planning.md`
   and record reading confidence with `references/reading-coverage.md`.
10. For deep mode, follow `references/deep-architecture-report.md` and
    `references/module-investigation.md`.
11. Apply `references/evidence-quality.md` before making high-impact claims.
12. Build an evidence index with `scripts/build_evidence_index.py` when the
    report is long or contains many source-backed claims.
13. Audit strong claims with `references/claim-audit.md` and
    `scripts/claim_audit.py <report>` before final delivery when writing a long
    or deep report.
14. Deliver the requested report. Keep temporary notes in a `code-research/`
    work directory near the target repository unless the user requests otherwise.

## Command Playbooks / 命令交付口径

`/code-map` should be quick and concrete:

- What this repo appears to be
- Languages, package managers, and command surfaces
- Likely entry points and why they matter
- High-signal directories versus low-signal/generated areas
- Suggested reading route

`/code-trace` should be narrow:

- Scenario chosen or requested
- Entry point
- Step-by-step execution path with source references
- Data/control handoffs
- Where errors, configuration, or external effects enter

`/code-research` should answer the practical architecture question:

- Codebase Map
- Runtime Story
- Design Inquiry
- Maintainer Notes

`/code-research-deep` should add depth only where it buys understanding:

- Problem and architecture framing
- Core responsibility studies
- Design tradeoffs and rejected simpler shapes
- Engineering maturity: tests, configuration, errors, observability, docs
- Evidence index for major claims
- Visuals that explain architecture, runtime, or boundaries
- Reading coverage and claim audit notes when they improve trust

中文交付口径：

- `/code-map`：短、准、能指导下一步阅读。
- `/code-trace`：只追一条主路径，把入口、交接点、输出或副作用讲清楚。
- `/code-research`：用四层方法形成完整但不过度膨胀的研究报告。
- `/code-research-deep`：只在能增加理解的地方加深，避免堆章节。

## Evidence Bar / 证据标准

- A behavior claim needs a source path and, when practical, a line number.
- Every major architecture section must cite the code files it is interpreting.
- A runtime story needs evidence for entry, core handoff, and output or side
  effect.
- A design claim should separate observation from interpretation.
- A risk claim should state the likely maintenance impact.
- If the code does not prove the claim, mark it as an inference.
- For long or deep reports, run `scripts/claim_audit.py` and fix unsupported
  high-impact claims before delivery.

中文口径：

- 行为结论要有文件路径，重要结论尽量到行号。
- 每个主要架构章节都必须标出正在解读的源码文件。
- 执行路径至少覆盖入口、核心交接点、输出或副作用。
- 设计判断要区分“代码事实”和“研究推断”。
- 风险判断要说明对维护或演进的影响。
- 证据不足时要明说“不确定”，不要补剧情。
- 长报告或深度报告交付前运行 `scripts/claim_audit.py`，修正缺少证据的强结论。

## Output Standards / 输出标准

- `/code-map`: concise map, likely entry points, important directories, and an
  ordered reading route.
- `/code-trace`: sourced execution path for one scenario, with boundaries and
  side effects called out.
- `/code-research`: narrative report with code map, runtime story, important
  modules, design observations, and maintainer notes.
- `/code-research-deep`: deep architecture report with diagrams, module analysis,
  design tradeoffs, risks, and evidence index.
- `/code-compare`: side-by-side comparison of problem framing, architecture,
  abstractions, maturity, risks, and recommendation.

## Visuals / 配图

- Use Mermaid as the default visual format.
- Draw a diagram only when it clarifies runtime flow, module ownership, state,
  dependency direction, plugin/adapter boundaries, or external effects.
- For `/code-research-deep`, include at least one useful architecture or runtime
  diagram unless the repository is too small or the diagram would repeat prose.
- Keep diagrams evidence-backed: each important node or edge should be justified
  by nearby source references.
- Follow `references/visual-reporting.md`.

中文规则：

- 默认用 Mermaid。
- 图只服务理解：运行路径、模块归属、状态流转、依赖方向、插件/adapter 边界、外部副作用。
- 深度报告默认至少包含一张有用的架构图或运行图，除非项目太小或图会重复文字。
- 图也要有证据，关键节点和边要能对应源码或文档。

## Minimal Self-Check / 最小自检

Before publishing changes to this skill, run:

```bash
python3 skills/code-researcher/scripts/scan_repo.py skills/code-researcher --out /tmp/code-researcher-scan.json
python3 skills/code-researcher/scripts/summarize_scan.py /tmp/code-researcher-scan.json --query "请分析这个 skill"
python3 skills/code-researcher/scripts/self_check.py
```

Confirm that the output identifies `SKILL.md`, the reference files, script files,
documentation-like markdown, Python language lines, and a sensible reading route.

## Originality / 原创性

This skill may learn from common engineering analysis practices, but it must not
copy section titles, prose, examples, prompt templates, or report structures from
other skills. Follow `references/non-plagiarism.md`.

可以吸收通用工程分析原则，但不能复制其他 skill 的措辞、阶段名、模板、示例或报告结构。
