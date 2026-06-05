<div align="center">

# 🗺️ Code Researcher

**代码库研究与架构报告 | Codebase Research & Architecture Reporting**

输入代码库路径，输出带证据的架构理解。支持项目地图、执行路径追踪、深度架构报告和项目对比。

*Input a repository path, get an evidence-backed architecture understanding. Supports project mapping, execution tracing, deep architecture reports, and project comparison.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

> **这是一个 Agent Skill，不是 Python 程序。**
>
> 打开你正在用的 agent（Claude Code、Codex、Cursor、OpenClaw、Hermes、CodeBuddy、Workbuddy、Gemini CLI、OpenCode 等），告诉它：
>
> ```
> 帮我安装这个 skill：git@github.com:zhoucanzong/code-researcher.git
> ```
>
> 它会自己帮你 clone 并配置好，不需要 `pip install`。

---

## 目录 | Table of Contents

- [功能特性 | Features](#功能特性--features)
- [项目结构 | Project Structure](#项目结构--project-structure)
- [使用方式 | Usage](#使用方式--usage)
- [贡献指南 | Contributing](#贡献指南--contributing)
- [许可证 | License](#许可证--license)

---

## 功能特性 | Features

### 研究模式 | Research Modes

- **`/code-map <repo>`**：快速项目地图，识别入口候选、高信号目录与建议阅读路线。
- **`/code-trace <repo> [scenario]`**：追踪一个真实请求、命令或 API 从输入到输出的完整执行路径。
- **`/code-research <repo>`**：默认代码研究报告，包含项目地图、运行故事、设计追问和维护者笔记。
- **`/code-research-deep <repo>`**：深度架构报告，包含模块调研、设计取舍、风险评估、可视化图表和证据索引。
- **`/code-compare <repoA> <repoB>`**：对比两个项目的架构、抽象成熟度、风险与适用性。

### 核心功能 | Core Capabilities

| 功能 | 说明 |
|------|------|
| 🔍 仓库扫描 | 自动识别语言、入口点、依赖、目录结构和架构信号 |
| 📍 入口发现 | 基于约定式文件名和 manifest 识别项目入口候选 |
| 🛤️ 执行路径追踪 | 从公开接口追踪到核心行为的真实运行路径 |
| 🏗️ 架构信号识别 | 从路径和代码中识别 CLI、HTTP、插件、存储等架构模式 |
| 📊 图表建议 | 智能推荐 Mermaid 图表类型，辅助理解运行时与模块边界 |
| 🔎 证据审计 | 自动标记报告中缺少源码证据支撑的高影响结论 |
| 📑 证据索引 | 从报告中提取所有源码引用，建立轻量级证据索引 |
| 🌐 双语输出 | 中英文自动路由，按用户语言输出报告 |
| 🌐 HTML 展示 | 将 Markdown 报告转换为精美的 HTML 文件，自适应深色/浅色模式 |

| Feature | Description |
|---------|-------------|
| 🔍 Repo Scan | Auto-detect languages, entry points, dependencies, and directory structure |
| 📍 Entry Discovery | Identify project entry candidates from conventional filenames and manifests |
| 🛤️ Execution Tracing | Trace a real request or command from public surface to core behavior |
| 🏗️ Architecture Signals | Detect CLI, HTTP, plugin, storage, and other architectural patterns |
| 📊 Diagram Suggestions | Smart Mermaid diagram recommendations for runtime and module boundaries |
| 🔎 Evidence Audit | Flag high-impact claims that lack nearby source evidence |
| 📑 Evidence Index | Extract all source references from a report into a lightweight index |
| 🌐 Bilingual Output | Auto-route between Chinese and English based on user language |
| 🌐 HTML Export | Convert Markdown reports to polished HTML with dark/light mode |

---

## 项目结构 | Project Structure

```
code-researcher/
├── LICENSE                              # MIT License
├── README.md                            # 本文件 | This file
├── .gitignore                           # Git ignore rules
└── skills/
    └── code-researcher/                 # Skill content
        ├── SKILL.md                     # Skill definition & commands
        ├── assets/                      # (reserved for templates and configs)
        ├── references/                  # Methodology references
        │   ├── claim-audit.md
        │   ├── deep-architecture-report.md
        │   ├── evidence-quality.md
        │   ├── module-investigation.md
        │   ├── non-plagiarism.md
        │   ├── reading-coverage.md
        │   ├── report-planning.md
        │   ├── report-style.md
        │   ├── research-method.md
        │   ├── runtime-story.md
        │   └── visual-reporting.md
        └── scripts/                     # CLI tools (agent auto-calls)
            ├── build_evidence_index.py
            ├── claim_audit.py
            ├── scan_repo.py
            ├── self_check.py
            └── summarize_scan.py
```

---

## 使用方式 | Usage

安装后，直接在 agent 中使用以下命令：

```
/code-map <repo>                 # 快速项目地图
/code-trace <repo> [scenario]    # 追踪执行路径
/code-research <repo>            # 默认架构报告
/code-research-deep <repo>       # 深度架构报告
/code-compare <repoA> <repoB>    # 项目对比
```

或者直接用自然语言告诉 agent：

```
帮我分析这个代码库的架构
追踪一下 /api/login 的执行路径
对比这两个项目的设计有什么不同
```

Agent 会自己调用 `scripts/` 下的工具完成扫描 → 分析 → 报告流程。

HTML 导出：报告生成后，agent 会询问是否需要 HTML 版本，确认后自动输出精美的 HTML 文件（自适应深色/浅色模式）。

---

<details>
<summary>高级：手动脚本 / Advanced: Manual Script Usage</summary>

脚本仅使用 Python 3.10+ 标准库，无外部依赖。

```bash
# 1. 扫描仓库
python skills/code-researcher/scripts/scan_repo.py ./my-project --out ./scan.json

# 2. 生成项目地图
python skills/code-researcher/scripts/summarize_scan.py ./scan.json --lang en

# 3. 结论审计
python skills/code-researcher/scripts/claim_audit.py report.md --lang zh --out audit.md

# 4. 证据索引
python skills/code-researcher/scripts/build_evidence_index.py report.md --out evidence.json

# 5. 自检
python skills/code-researcher/scripts/self_check.py
```

</details>

---

## 贡献指南 | Contributing

欢迎 Issue 和 PR！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

Issues and PRs are welcome!

---

## 许可证 | License

本项目采用 [MIT License](LICENSE) 开源授权。

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ for code explorers.

</div>
