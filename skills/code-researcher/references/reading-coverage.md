# Reading Coverage / 阅读覆盖

Reading coverage is not a vanity metric. It is a confidence tool: it tells the
reader which code was actually inspected and where the report is intentionally
conservative.

阅读覆盖不是为了凑数字，而是为了说明报告的可信范围：哪些代码读过，哪些只是扫过，
哪些地方不能下强结论。

## Coverage Levels / 覆盖层级

- Scanned: discovered by `scan_repo.py`, counted, classified, but not read in
  detail.
- Skimmed: opened enough to understand broad responsibility and public surface.
- Traced: followed as part of a runtime story or module path.
- Audited: revisited to verify an important claim.

中文层级：

- Scanned：扫描发现、统计和分类，但没有细读。
- Skimmed：读到足够理解职责和公开边界。
- Traced：作为运行路径或模块路径的一部分追过。
- Audited：为了验证关键结论回到源码复查过。

## What to Record / 记录什么

For non-trivial reports, keep a short coverage note:

- File or directory
- Coverage level
- Why it was read
- What claim it supports
- What remains unread or uncertain

中文记录：

- 文件或目录
- 覆盖层级
- 为什么读它
- 支撑什么结论
- 还有什么没读或不确定

## Report Use / 报告中如何使用

Do not dump a giant coverage table into the final report by default. Instead:

- Mention coverage briefly in the evidence or methodology note.
- Use it to limit overconfident claims.
- Include details only for deep reports, audits, or user-requested rigor.

中文规则：

- 默认不要把大覆盖表塞进最终报告。
- 用覆盖记录约束结论强度。
- 只有深度报告、审计场景或用户要求严谨时，才展示更完整的覆盖细节。

## Confidence Language / 置信表达

- "Traced through..." means the path was followed from entry to output.
- "Skimmed..." means responsibility is understood, but internal behavior may
  still need inspection.
- "I did not inspect..." means no strong claim should depend on that file.

中文表达：

- “已追踪……”表示从入口到输出走过路径。
- “已快速阅读……”表示理解职责，但内部细节还可能需要继续看。
- “未检查……”表示不能把强结论建立在这个文件上。
