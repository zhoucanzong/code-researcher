# Runtime Story / 运行故事

Use a runtime story to turn a repository from "many files" into "one working
system." The story should follow a real scenario from the outside boundary to a
visible result.

运行故事的目的不是列调用链，而是把“很多文件”变成“一条真实可理解的系统路径”。

## Pick One Scenario / 选择一条主路径

Choose the scenario that best represents the repository's main value:

- Web service: request enters a route, passes middleware or handlers, touches
  domain logic, returns a response or side effect.
- CLI tool: command arguments are parsed, configuration is loaded, work is
  executed, output is printed or files are changed.
- Library/framework: public API is called, options are normalized, core engine
  runs, result or extension hook is returned.
- Compiler/parser: input text enters lexer/parser/planner, internal structures
  are built, output artifact or diagnostics are produced.
- Background system: scheduler or trigger creates work, worker executes it,
  retries/errors are handled, state is committed.
- Agent/tooling project: user intent becomes planning, tool selection, execution,
  observation, and final response.

中文选择原则：

- Web 服务：请求从路由进入，到中间件、业务逻辑、响应或副作用。
- CLI 工具：参数解析、配置加载、执行任务、输出或改文件。
- 库/框架：公开 API、选项归一化、核心引擎、结果或扩展点。
- 编译器/解析器：输入文本、解析/规划、内部结构、产物或诊断。
- 后台系统：调度/触发、worker 执行、重试/错误、状态提交。
- Agent/工具链：用户意图、规划、工具选择、执行、观察、最终回答。

## Evidence Needed / 必要证据

Every runtime story should include evidence for:

- Entry: route, command, public API, scheduler, or event listener.
- Normalization: config, arguments, request context, or input shaping.
- Core handoff: the moment control moves into the main engine or domain module.
- State or external boundary: database, filesystem, network, process, cache,
  model call, queue, or plugin boundary.
- Output: response, printed text, generated file, returned value, emitted event,
  stored state, or error.

中文证据要求：

- 入口：路由、命令、公开 API、调度器或事件监听。
- 归一化：配置、参数、上下文或输入结构整理。
- 核心交接点：控制权进入核心引擎或领域模块的地方。
- 外部边界：数据库、文件系统、网络、进程、缓存、模型调用、队列、插件。
- 输出：响应、终端文本、生成文件、返回值、事件、状态写入或错误。

## Writing Shape / 写法

Prefer 5-9 meaningful steps. Each step should say:

- What happens
- Which file or symbol supports it
- What crosses the boundary
- Why this step matters to the architecture

Avoid exhaustive call-chain noise. If a helper function only formats a string or
passes through arguments, skip it unless it changes a contract.

中文写法：

- 用 5-9 个关键步骤讲清楚，不要穷举所有函数调用。
- 每一步说明发生了什么、证据在哪里、跨过了什么边界、为什么重要。
- 普通 helper 可以跳过，除非它改变了契约、状态或错误语义。

## When Unsure / 不确定时

If several scenarios seem plausible, choose the one closest to the user's stated
goal. If the user gave no goal, choose the path exposed by the most public entry
point: CLI command, exported API, HTTP route, package binary, or documented
quickstart.

如果有多条路径都合理，优先选用户问题指向的那条。用户没有指定时，选最公开、
最能代表项目价值的入口：命令、导出 API、HTTP 路由、package binary 或 README
quickstart。
