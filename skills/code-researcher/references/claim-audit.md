# Claim Audit / 结论审计

A claim audit is a final pass over the report's strongest statements. It keeps
the report sharp without letting it drift away from code.

结论审计是在最终交付前检查最强判断，保证报告有观点，但不脱离源码。

## Claims to Audit / 需要审计的结论

Audit claims that use language like:

- "central", "core", "primary", "main"
- "guarantees", "ensures", "prevents"
- "scales", "safe", "stable", "reliable"
- "risk", "bottleneck", "coupling", "technical debt"
- "designed for", "optimizes for", "tradeoff"

中文需要审计的表达：

- “核心”“主要”“关键”
- “保证”“确保”“防止”
- “可扩展”“安全”“稳定”“可靠”
- “风险”“瓶颈”“耦合”“技术债”
- “为了……设计”“优化了……”“取舍”

## Audit Questions / 审计问题

- Is there a source path near the claim?
- Does the cited code actually support the claim?
- Is this fact, behavior, interpretation, risk, or recommendation?
- Should the wording be softened from conclusion to inference?
- Does the report name what was not inspected?

中文问题：

- 结论附近有没有源码路径？
- 引用的代码是否真的支撑这个结论？
- 这是事实、行为、解释、风险，还是建议？
- 是否应该从确定结论降级为推断？
- 报告有没有说明哪些地方没读？

## Fixes / 修正方式

- Add source evidence.
- Split observation from interpretation.
- Replace absolute wording with confidence-aware wording.
- Remove unsupported claims.
- Add a note about missing evidence.

中文修正：

- 补源码证据。
- 拆开代码事实和设计解释。
- 把绝对措辞改成有置信度的措辞。
- 删除无证据结论。
- 标注证据缺口。
