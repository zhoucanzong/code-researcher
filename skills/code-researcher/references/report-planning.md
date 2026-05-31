# Report Planning / 报告规划

Plan the report before writing a deep analysis. The plan should be short, but it
must explain why this report is organized this way.

深度分析前先做报告规划。规划不需要长，但要解释为什么这样组织报告。

## Planning Questions / 规划问题

- What is the user's real decision or learning goal?
- What is the repository's main job?
- Which runtime story best reveals that job?
- Which responsibilities are core, and which are supporting?
- What visual would reduce the most confusion?
- Which claims will need careful evidence?

中文问题：

- 用户真正想学习或判断什么？
- 这个仓库最核心的工作是什么？
- 哪条运行路径最能展示这件事？
- 哪些责任是核心，哪些只是支撑？
- 哪张图最能减少理解成本？
- 哪些结论需要特别严谨的证据？

## Original Report Spine / 原创报告骨架

Use this as a thinking aid, not a fixed template:

1. Why this repository exists
2. Where to read first
3. The main runtime story
4. Responsibilities that make the story work
5. Design pressures and tradeoffs
6. Code-backed risks and maintainer moves

中文骨架：

1. 项目为什么存在
2. 先读哪里
3. 主运行路径
4. 支撑这条路径的责任模块
5. 设计压力和取舍
6. 有源码依据的风险与维护建议

## Module Narrative / 模块叙事

Do not arrange modules by directory order unless directory order is the
architecture. Arrange them by reader understanding:

- Input boundary -> normalization -> core engine -> external boundary -> output
- User-facing API -> orchestration -> domain state -> adapters
- Problem -> first constraint -> second constraint -> design consequence

中文规则：

- 不按目录机械排列模块，除非目录本身就是架构。
- 优先按读者理解路径组织：入口、归一化、核心引擎、外部边界、输出。
- 每个模块都说明它接过了什么问题，又把什么问题交给下一部分。

## Stop Conditions / 停止条件

Stop expanding the report when another paragraph would only repeat a file list,
function summary, or generic praise. Add depth only when it clarifies behavior,
design pressure, risk, or maintainability.

如果新增段落只是在重复文件列表、函数摘要或泛泛称赞，就停止扩写。深度必须服务
行为、设计压力、风险或可维护性。
