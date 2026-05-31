# Evidence Quality / 证据质量

The report should feel opinionated, but opinions must be earned by reading the
code. Use this guide before making strong claims.

报告可以有判断，但判断要从代码里长出来。

## Source-Coupled Reporting / 源码绑定报告

Architecture analysis must stay coupled to source code. Every major section
should answer two questions together:

- What does the architecture mean?
- Which code makes that architecture real?

中文要求：

- 架构分析必须和源码绑定。
- 每个主要章节都要同时回答“这个架构含义是什么”和“哪些代码让它真实存在”。
- 如果某段分析找不到源码证据，它只能作为假设或待验证问题，不能作为结论。

## Claim Types / 结论类型

- Fact: directly visible in code or docs.
- Behavior: what happens when a scenario runs.
- Design reading: why a boundary, abstraction, or flow likely exists.
- Risk: what could make maintenance, extension, debugging, or operation harder.
- Recommendation: what a maintainer should read, test, or change next.

中文分类：

- 事实：代码或文档直接可见。
- 行为：某个场景运行时会发生什么。
- 设计解读：某个边界、抽象或流程为什么可能存在。
- 风险：什么会让维护、扩展、调试或运行变难。
- 建议：维护者接下来该读、测或改什么。

## Minimum Evidence / 最小证据

- Fact: cite file path; use line numbers when practical.
- Behavior: cite entry, handoff, and output or side effect.
- Design reading: cite the code shape, then mark the interpretation.
- Risk: cite the coupling, missing guard, weak test signal, or unstable boundary.
- Recommendation: connect it to a concrete file, test, module, or runtime path.

中文标准：

- 事实：至少给文件路径，重要处给行号。
- 行为：至少给入口、核心交接点、输出或副作用。
- 设计解读：先给代码形态，再给解释。
- 风险：指出耦合、缺少保护、测试薄弱或边界不稳的证据。
- 建议：落到具体文件、测试、模块或运行路径。

## Useful Wording / 推荐措辞

English:

- "The code shows..."
- "This suggests..."
- "A likely design pressure is..."
- "I would treat this as a risk because..."
- "I did not find evidence that..."

中文：

- “代码直接显示……”
- “这暗示……”
- “一个可能的设计压力是……”
- “我会把这里视为风险，因为……”
- “我没有找到……的证据。”

## Red Lines / 红线

- Do not infer intent from naming alone.
- Do not call something "clean", "scalable", or "well-designed" without naming
  the concrete pressure it handles.
- Do not use ecosystem comparisons unless the comparison target is genuinely
  similar or the user asked for that context.
- Do not hide uncertainty. Uncertainty is useful information.

中文红线：

- 不只靠命名推断设计意图。
- 不用“优雅”“可扩展”“设计很好”这种无证据评价。
- 不随便拉业界对比，除非确实同类或用户需要。
- 不掩盖不确定性；不确定本身就是有价值的信息。
