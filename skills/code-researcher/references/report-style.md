# Report Style

## Voice

- Clear, practical, and evidence-backed.
- Chinese by default for Chinese requests.
- Explain enough domain context for a capable engineer to follow.
- Use direct judgments when the source supports them.
- Mark uncertainty instead of pretending to know.

## Evidence

Use evidence references like:

- `src/server/router.ts:42`
- `packages/core/src/index.ts`
- `Parser.parse` in `src/parser.rs`

For high-impact claims, include at least one specific source reference. For
interpretive claims, separate the observation from the interpretation:

```text
Observation: `src/runtime/scheduler.ts` owns retry state and timeout handling.
Interpretation: this makes the scheduler the reliability boundary for jobs.
```

## Diagrams

Use Mermaid only when it clarifies:

- Request or command flow
- Module ownership
- Dependency direction
- State transitions
- Pipeline stages

Prefer small diagrams. A diagram with ten vague boxes is usually less useful
than a five-step runtime story with source references.

## Anti-patterns

Avoid:

- Directory-by-directory summaries
- Generic praise without evidence
- Large pasted code blocks
- Explaining every function name
- Treating tests, generated files, or examples as equally important to core code
- Overfitting the report to a fixed template when the project has a different
  shape

