# Four-Layer Code Research Method

Use this method to move from surface familiarity to architecture-level judgment.
The layers are sequential, but do not treat them as a rigid checklist. Let the
repository's shape decide where to spend time.

## 1. Codebase Map

Goal: answer "what is here, and where should I start?"

Capture:

- Primary languages and package managers
- Build, test, and run entry points
- Public API or CLI entry points
- Major directories and ownership boundaries
- Dependency manifests and notable dependencies
- Documentation, examples, and design notes
- Generated, vendored, fixture, and low-signal areas to avoid over-reading

Good output is a reading map, not a directory dump. Explain which files matter
first and why.

## 2. Runtime Story

Goal: answer "what actually happens when the system does its main job?"

Choose one representative scenario:

- HTTP request through a web service
- CLI command from argument parsing to output
- Library API call from public method to core engine
- Background job from scheduling to side effects
- Compiler or parser pipeline from input text to output artifact

Trace the path with file and line evidence. Prefer a small number of meaningful
steps over exhaustive call-chain noise.

## 3. Design Inquiry

Goal: answer "why does this design exist?"

For each core abstraction or module, ask:

- What problem does it remove from callers?
- What boundary does it create?
- What state or data does it own?
- What becomes easier because it exists?
- What becomes harder because it exists?
- What simpler alternative could have been used?
- Why might the project have rejected that alternative?

The best analysis explains tradeoffs in the project's context. Avoid generic
praise such as "clean architecture" unless the report shows the specific design
pressure that makes it clean.

## 4. Maintainer Notes

Goal: answer "how should someone responsibly work on this next?"

Include:

- Stable extension points
- Risky coupling or unclear boundaries
- Missing tests or observability on important paths
- The next files a new maintainer should read
- The first experiments or tests to run before making changes
- Refactor suggestions only when the evidence supports them

This layer should feel practical. A maintainer should be able to decide where to
start tomorrow morning.

