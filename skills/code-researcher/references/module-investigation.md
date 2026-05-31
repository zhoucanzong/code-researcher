# Module Investigation

Use this guide when a repository has clear core modules or when producing a deep
architecture report.

## Choosing Modules

Choose modules by responsibility, not by directory name alone. A module can span
several files, and one file can participate in several responsibilities.

Signals that a module is core:

- It sits on the primary runtime path
- Many other files depend on its types or services
- It owns important state
- It defines extension points or public API
- It contains unusual or project-specific abstractions
- Bugs in it would affect the main user experience

Treat test helpers, generated code, fixture data, and one-off scripts as
secondary unless they reveal something important about architecture.

## Investigation Questions

For each core module, answer:

- Why does this module exist?
- What input does it accept and what output does it produce?
- What state does it own or mutate?
- Which modules call it, and which modules does it call?
- What contract does it expose?
- What invariants does it protect?
- What error cases does it handle locally versus delegate?
- What would break if this module disappeared?
- What alternative design would be simpler, and what would that lose?

## Evidence Expectations

Each module study should include evidence for:

- Entry point or public interface
- Key type, object, function, route, command, or handler
- Main flow through the module
- Important boundary with another module
- One representative test, if tests exist

Use file paths and line numbers where practical. If exact line numbers are not
available, cite symbols and files.

## Output Shape

For each module:

```text
Module: <name>
Role: <why it exists in the system>
Evidence: <important files and symbols>
Flow: <short narrative or diagram>
Design reading: <tradeoff and rationale>
Maintainer note: <risk, extension point, or next read>
```

Keep the module section connected to the larger runtime story. Avoid isolated
mini-reports that do not explain how the whole system fits together.

