# Deep Architecture Report

Use this reference for `/code-research-deep` or when the user explicitly asks for
a deep architecture report.

## Research Discipline

- Evidence first: important claims should point to source files and preferably
  line numbers.
- Explain design pressure before design choice.
- Prefer one well-traced runtime path over many shallow file summaries.
- Separate observed facts from informed interpretation.
- If web context is unavailable, say so and keep ecosystem claims conservative.
- Diagrams should clarify flow, ownership, or dependency direction. Do not add
  diagrams as decoration.

## Suggested Report Shape

Adapt headings to the project. Do not force every section when it adds little.

1. Executive Summary
   - What the project is
   - The central architecture idea
   - The most important strengths and risks

2. Problem and Product Frame
   - Who uses this project
   - What pain it addresses
   - What existing alternatives or simpler approaches compete with it

3. Codebase Map
   - Languages and runtime
   - Entry points
   - Major directories
   - Build/test/development surfaces

4. Architecture Overview
   - High-level components
   - Ownership boundaries
   - Main data/control flow

5. Runtime Story
   - Trace one representative scenario from input to output
   - Include Mermaid sequence or flow diagram when helpful

6. Core Module Studies
   - Role in the system
   - Key data structures or abstractions
   - Main collaborators
   - Design tradeoffs
   - Evidence references

7. Design Tradeoffs
   - What the project optimizes for
   - What it intentionally pays for that choice
   - Where the design could become strained

8. Engineering Maturity
   - Tests
   - Error handling
   - Configuration
   - Observability
   - Documentation and examples

9. Maintainer Notes
   - Safe extension points
   - Risky changes
   - Recommended reading order
   - Suggested next investigations

10. Evidence Index
   - Claim
   - Source file
   - Line or symbol
   - Confidence

## Writing Style

Write like a senior engineer explaining the system to a new maintainer. Be clear,
specific, and opinionated when the code supports an opinion. Avoid inflated
language and avoid turning the report into a list of files.

