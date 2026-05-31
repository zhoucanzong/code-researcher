<div align="center">

# 🗺️ Code Researcher

**代码库研究与架构报告助手 | Codebase Research & Architecture Reporting Assistant**

输入代码库路径，输出带证据的架构理解。支持项目地图、执行路径追踪、深度架构报告和项目对比。

*Input a repository path, get an evidence-backed architecture understanding. Supports project mapping, execution tracing, deep architecture reports, and project comparison.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

</div>

---

## 目录 | Table of Contents

- [功能特性 | Features](#功能特性--features)
- [项目结构 | Project Structure](#项目结构--project-structure)
- [快速开始 | Quick Start](#快速开始--quick-start)
- [使用说明 | Usage](#使用说明--usage)
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
        │   ├── claim-audit.md           # Claim audit methodology
        │   ├── deep-architecture-report.md
        │   ├── evidence-quality.md
        │   ├── module-investigation.md
        │   ├── non-plagiarism.md
        │   ├── reading-coverage.md
        │   ├── report-planning.md
        │   ├── report-style.md
        │   ├── research-method.md       # Four-layer research method
        │   ├── runtime-story.md
        │   └── visual-reporting.md
        └── scripts/                     # CLI tools
            ├── build_evidence_index.py  # Extract evidence references
            ├── claim_audit.py           # Audit source-backed claims
            ├── scan_repo.py             # Scan repository to JSON map
            ├── self_check.py            # Minimal self-check suite
            └── summarize_scan.py        # Render human-readable project map
```

---

## 快速开始 | Quick Start

### 环境要求 | Requirements

- Python 3.10+
- 标准库（无需额外依赖）

### 安装 | Installation

```bash
# 克隆仓库 | Clone the repo
git clone <repo-url>
cd code-researcher

# 无需安装依赖 | No dependencies to install
# 所有脚本仅使用 Python 标准库
```

### 第一步：扫描代码库 | Step 1: Scan a Repository

```bash
python skills/code-researcher/scripts/scan_repo.py ./my-project \
  --out ./my-project-scan.json
```

### 第二步：生成项目地图 | Step 2: Generate Project Map

```bash
python skills/code-researcher/scripts/summarize_scan.py \
  ./my-project-scan.json \
  --query "分析这个项目" \
  --out ./my-project-map.md
```

---

## 使用说明 | Usage

### 1. 仓库扫描 | Repository Scan

扫描代码库并输出紧凑的 JSON 地图：

```bash
python skills/code-researcher/scripts/scan_repo.py <repo-path> [--out <json-path>]
```

输出包含：语言统计、入口候选、核心目录、架构信号、图表建议、阅读路线等。

### 2. 项目地图渲染 | Project Map Rendering

将扫描结果渲染为人类可读的项目地图：

```bash
# 英文输出
python skills/code-researcher/scripts/summarize_scan.py scan.json --lang en

# 中文输出（自动检测）
python skills/code-researcher/scripts/summarize_scan.py scan.json --query "分析这个项目"
```

### 3. 结论审计 | Claim Audit

审计 Markdown 报告中的高影响结论是否具备邻近源码证据：

```bash
python skills/code-researcher/scripts/claim_audit.py report.md \
  --lang zh --out audit.md
```

### 4. 证据索引 | Evidence Index

从报告中提取所有源码引用，建立轻量级证据索引：

```bash
python skills/code-researcher/scripts/build_evidence_index.py report.md \
  --out evidence.json
```

### 5. 自检 | Self-Check

运行最小自检，确认技能的核心功能正常：

```bash
python skills/code-researcher/scripts/self_check.py
```

---

## 贡献指南 | Contributing

欢迎 Issue 和 PR！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

Issues and PRs are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 许可证 | License

本项目采用 [MIT License](LICENSE) 开源授权。

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ for code explorers.

</div>
