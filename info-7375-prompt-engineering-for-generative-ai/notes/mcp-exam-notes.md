# MCP exam notes (INFO 7375 Prompt Engineering for Generative AI)

Running notes for the midterm. MCP is on the exam. Bear gives the prompts; entries are in order. Claude's answers are labeled as Claude's and are not signed off until Bear says so.

## 1. What is MCP?

**Claude's answer (not yet signed off).**

MCP, the Model Context Protocol, is an open standard for connecting an AI application to outside tools and data. It fixes the message format and the order of the conversation. It does not decide which tools to trust.

- **Parties.** A *host* is the AI application, for example Claude Code or Claude desktop. Inside it, a *client* holds one connection to one *server*. A *server* offers capabilities and describes them. Claude proposes using a tool; people and policy define authority.
- **Wire format.** JSON-RPC 2.0 messages: requests (with an `id`), responses (the same `id`), and notifications (no `id`, no reply).
- **Transports.** Standard input/output for local servers; HTTP-based for remote ones.
- **What a server can offer.** Tools (actions the model may call), resources (data the host can read in), and prompts (reusable templates).
- **Lifecycle.** The client sends `initialize`, the server answers with a protocol version and its capabilities, the client sends the `initialized` notification, and only then do ordinary requests such as `tools/list` and `tools/call` work. A request made too early is rejected.
- **Why it exists.** Without a standard, every app needs a custom integration for every tool (M apps times N tools). With one protocol, each side implements it once.

**The course's point (chapter 8).** MCP answers *interoperability*: can the parties exchange messages they understand? It does not answer *authorization*: should this server, this data and this action be used for this task? A server's tool description is its own claim, not a verified fact. A well-formed handshake says nothing about whether a tool is safe. The decision to connect a server belongs to a person.

**Exam traps to remember.**

- A valid handshake is not a trust signal.
- A JSON-RPC error (the protocol failed) is different from a tool result with `isError: true` (the call ran and the tool reported a failure).
- Initialization and readiness are two separate steps (`initialize`, then the `initialized` notification).
- The tool description is text the model reads; misleading text can steer tool choice.

**Sources in the repo.** `chapters/08-mcp-from-scratch.md` (four parties and one decision); the existing question pool is in `multiple-answer/ch08-mcp-from-scratch.md` (MA-ch08.1 to .64) and `essay/ch08-mcp-from-scratch.md` (60 essays).

## 2. Godot vs Unreal Engine vs Unity: why Godot does not need an MCP, and why Unity and Unreal do

**Bear's prompt:** "Use the example of Godot versus Unreal Engine versus Unity. Why Godot does not need an MCP? And why Unity and Unreal must have an MCP?"

**Claude's answer (not yet signed off).**

The test: *can the agent reach and change the project's state with files and a shell alone?* If yes, MCP adds little. If the state lives inside a running application or in binary formats, an MCP server is the way to give the model hands on it.

- **Godot: files and a shell are enough.** Scenes (`.tscn`), scripts (`.gd`), resources (`.tres`) and project settings are plain text. An agent can read, edit and diff them directly, and can run the engine from the command line (headless mode, a script, an export). The state is in the files; the shell is the interface.
- **Unreal: the state is in the editor and in binary.** Maps and assets (`.umap`, `.uasset`) and Blueprints (visual graphs) are binary. An agent cannot edit them as text. Changing them means asking the running editor to do it through its own API, so a server must wrap those editor operations as tools.
- **Unity: text on disk, but the truth is in the Editor.** Scenes and prefabs can be serialized as text, but they are tangled with GUIDs and `.meta` files, so hand edits break references. The Editor also holds state the files do not: import settings, play mode, the console, domain reloads after a compile. A server exposes those as tools.

**Caveats to state on the exam.**

- "Must" is too strong. Nothing forces an engine to have an MCP server; it is a design choice that pays off when the model cannot reach the state otherwise.
- Godot can have one too (editor state such as a screenshot of the running scene or the debugger output). The claim is that Godot does not *need* one to be useful, not that none exists.
- MCP only supplies the connection. The course point still holds: the server's tool list is its own claim, and a person decides whether this server, this project and this action belong together. An editor tool that can delete assets or run arbitrary code is an authorization question, not an interoperability one.

**Unchecked:** the engine details above are from Claude's general knowledge, not from the course or from a test run in this session.

## 3. Godot with an MCP vs without one; MCP vs an API; why not just call functions?

**Bear's prompt (dictation read as "Godot" and "versus not having one"):** "So let's take the Godot example. What were the advantages of Godot having one versus not having one? Also, make clear the distinctions between MCP and an API. Why can't we just use an API, call make function calls? What is the difference?"

**Claude's answer (not yet signed off).**

**Godot with an MCP vs without.** Without one, Claude Code can still edit the text files and run the engine headless from the shell. What an MCP server adds is mostly feedback and narrower control, not the ability to edit.

- *Live state.* Run the scene, read the debugger output and errors, see a screenshot of the running game, inspect the scene tree and node properties while it runs. Without a server the agent is blind to all of that unless it builds ad hoc scripts.
- *Editor-made changes.* Creating nodes or reimporting assets through the editor keeps its own bookkeeping (resource ids, import files) consistent, where a raw text edit can miss it.
- *One tool for any host.* The same server works from Claude Code, Claude desktop or any other MCP client, with no per-app glue.
- *Narrower permission.* "Run scene" and "read errors" can be allowed as named tools. The shell alternative is a broad "run any command" permission.
- *Costs.* More software to trust and keep running, and its tool descriptions take space in the model's context. For pure file edits the shell is simpler.

**MCP vs an API.**

- An **API** is the interface of one service: its own endpoints, authentication and data formats. A developer reads the documentation and writes code against it ahead of time.
- **MCP** is a standard protocol for exposing capabilities (tools, resources, prompts) so any host can find and call them the same way. The server tells the client what it offers at run time (`tools/list`, with names, descriptions and input schemas) after a standard handshake.
- They are not rivals. An MCP server often calls an API underneath. MCP wraps the API in a shape a model-using application can discover and use without custom code.
- Why a standard matters: without one, every app needs custom glue for every service (M apps times N services). With one, each side implements the protocol once.
- Sessions: MCP has a lifecycle (initialize, initialized, then requests) and capability negotiation. A typical web API call is a single independent request.
- Descriptions: an MCP tool's description is written to be read by the model.

**Why not just use function calls?** They sit at a different layer.

- *Function (tool) calling* is a model feature: the model emits a structured request such as "call `read_errors` with these arguments".
- Something still has to run it. The host can run a hard-coded function, call an API directly, or forward the request to an MCP server.
- So you can skip MCP, and many apps do. The price is writing and maintaining that glue yourself for each tool in each app. MCP standardizes how the host finds and runs the tools; function calling is how the model asks for one.

**Exam traps.**

- "MCP replaces APIs": false; servers usually wrap them.
- "MCP is the same as function calling": false; the model proposes, the host executes, and MCP is one way to execute.
- "MCP makes a tool safe": false. API keys settle who may call a service; they do not settle whether this task should use it. An MCP description is still the server's own claim, and the decision to connect remains a person's.

**Unchecked:** the Godot specifics (what an editor server can show) and the layering of function calling vs MCP are from Claude's general knowledge, not from the course or a test in this session.

## 4. Pros and cons of the protocol; alternatives to MCP; or everybody writes homegrown interfaces

**Bear's prompt (dictation; "percentages" read as "pros and cons"):** "percentages of the protocol, alternatives to MCP, or just have everybody write their own homegrown interfaces to their software."

**Claude's answer (not yet signed off).** No numbers are claimed; no adoption percentages were looked up.

**Pros of MCP.**

- One implementation per side instead of one per pair: M apps plus N services, not M times N.
- Discovery at run time: the host asks the server what tools it has, with schemas, instead of a developer hard-coding them.
- A shared lifecycle and error shapes, so hosts behave predictably across servers.
- Reuse: a server written once works in any compliant host.
- Permissions can be set per named tool instead of "run anything".

**Cons of MCP.**

- It is only a connection. It does not give trust, authorization or correctness; descriptions are the server's own claims.
- Every connected server is more code to trust, run and update; a malicious or sloppy one can mislead the model through its descriptions or return untrusted text.
- Tool lists and descriptions take space in the model's context, and many servers make tool choice harder.
- A standard is lowest-common-denominator: it cannot express everything a rich product does.
- A young standard changes (the course's server reports protocol version 2025-11-25), so servers and hosts must keep up.
- Where files and a shell already reach the state (Godot), it adds little.

**Alternatives.**

- *Hand-written function calling:* the app defines its own tools and runs them itself. Simple and fully controlled; no reuse across apps.
- *The shell / command line:* give the agent a CLI and let it run commands. Very general; the permission is broad.
- *Direct REST calls from an OpenAPI description:* tools generated from an API spec. Reuses existing APIs; no run-time handshake or session.
- *Plugin or SDK systems from one vendor:* work only inside that vendor's host.
- *Agent-to-agent protocols:* aimed at agents talking to other agents rather than a model reaching a tool; related, not a replacement.
- *Screen control (computer use):* drive the application's interface like a person. Works with software that has no interface for programs; slow and brittle.

**Homegrown interfaces for everyone.**

- Pros: total control, can be tuned to the one product, no outside dependency, nothing to trust beyond your own code.
- Cons: the M times N problem returns; every app re-implements discovery, errors, versioning and permission handling; no reuse; each integration is a one-off to maintain and audit.

**Judgment to state on the exam.** Choose by what must be reached and by whom. One app and one tool: hand-written function calling is fine. Many apps or many tools, owned by different parties: a standard pays for itself. State reachable by files and a shell: you may need neither. In every case a person still decides what is connected, and the connection check (handshake, listing) does not replace that decision.

**Unchecked:** the alternatives list and the tradeoffs are from Claude's general knowledge, not from the course or from a source looked up in this session.

## 5. Context: what else MCP provides beyond a common interface to an API

**Bear's prompt:** "And what about context? Besides just having a common interface to an API through an MCP, can it also provide other kinds of context, which are specifically useful for agentic programming?"

**Claude's answer (not yet signed off).** Yes. Tools are only one of the things a server can offer.

**What a server can supply.**

- *Tools:* actions the model may call. Controlled by the model (the host can still gate them).
- *Resources:* data the host can read into context, each addressed by a URI. Examples: a file, a database schema, an API's documentation, a log, the current scene tree. Controlled by the application: the host decides which resources to attach.
- *Prompts:* reusable templates and workflows the server provides, such as "review this diff" or "set up a new level". Controlled by the user, who picks one to run.
- *Server instructions:* text the server supplies about how to use its tools well. A host may place it in the model's context. (This very session's system prompt carries such instructions for connected servers.)
- *Change notifications:* a server can tell the client that its tool list or a resource changed, so context can stay current during a long task.
- *Tool metadata:* schemas for inputs, and hints such as whether a tool is read-only, which a host can use for permission decisions.
- *Client-side features in newer versions of the spec (check the version before relying on them):* roots (which directories or areas the server is meant to work in), sampling (the server asks the host's model for a completion), and elicitation (the server asks the user a question).

**Why this matters for agentic work.** An agent loops: observe, decide, act, check. Resources and live notifications feed the *observe* and *check* steps (current project state, schemas, errors). Prompts carry known-good workflows so the agent need not rediscover them. Server instructions carry conventions a tool's author knows and the model does not. Tools do the *act* step.

**Costs and the course's point.**

- Context is not free: every attached resource and description uses space in the model's window, and too much dilutes what matters.
- Everything a server supplies is text written by that server. It is a claim, and it can contain instructions aimed at the model (injection). It is data to weigh, not a command.
- The question to carry (chapter 7): *who decided what reaches Claude, and where is that written down?* With MCP the host decides what enters context, and a person decides which servers are connected.

**Exam traps.**

- "MCP only exposes functions": false; resources, prompts and instructions also exist.
- "Resources are model-controlled": false; the application attaches them. Tools are model-controlled; prompts are user-selected.
- "Context from a server is trustworthy because the connection is valid": false.

**Unchecked:** the control model (tools / resources / prompts), roots, sampling and elicitation are from Claude's general knowledge of the spec, not from the course or a spec read in this session. The course's server implements only initialization, tool listing and one read-only lookup.

## 6. What MCP buys you, what it costs; Bear's commentary

**Bear pasted an article (source not named) listing what MCP buys and costs, then commented.** The article's points, in short: runtime discovery; distribution across hosts; separation of labor; primitives with control semantics (tools model-controlled, resources application-controlled, prompts user-controlled, elicitation); a local stdio transport; standardized OAuth for remote servers; consent hooks and tool annotations (`readOnlyHint`, `destructiveHint`, which are hints and must be treated as untrusted unless the server is trusted); errors designed for a model (`isError` result, not a protocol error). Costs: the context tax (tool names, descriptions and schemas loaded into the window), a large security surface (injection through results and descriptions, local servers run with the user's permissions, community servers of unknown provenance), a moving spec, state becoming the tool designer's problem, a standardized plug but not standardized quality (a one-to-one wrapper of 90 REST endpoints is worse than a few task-level tools), and lowest-common-denominator host support for anything beyond tools.

**Bear's words, closely paraphrased (dictation errors fixed):**

- *Runtime discovery is the foundation.* Once an agent is connected it can ask the server "what can I do with you?" and get a list (create vertices, do this, do that). That matters because the list can change: what a server offers this week may differ from last week because functionality was added. A language model only knows what existed up to its training cutoff. If a model came out two months ago, anything added since is invisible to it except by looking it up or asking. If Unreal adds two functions to its server yesterday, a model released before that cannot know them, so it asks the server what it offers now. The answer changes the plan: "you now have a function that makes this easier, so I will use it instead."
- *Distribution.* An agreement among the big players on a standard, like the web standards. One server works with every host, instead of a different server for each model or coding agent. If someone builds a new coding agent tomorrow, it had better speak MCP; the burden is on the agent to speak the protocol and on the app owner to offer a server.
- *Project idea.* Build an MCP server for something as a final project; it makes a good portfolio piece when job hunting. Example: for the jobs site (jobs.humanitarians.ai), an agent would work with the site through an MCP server, so Claude can interact with it more naturally.
- *Students should know what REST is and why it matters* (see entry 7).
- Bear's message began "disagree with us, so let's take a look at this" (dictation unclear); his comments on the pasted points agree with runtime discovery and distribution. His remarks on the cost list were not given in this message.

**Claude's check (not yet signed off).**

- *The cutoff argument is sound and is the right way to state it.* A model's knowledge is frozen at training; a tool list obtained at run time is current. Note the link to the cost side: that list goes into context, so discovery is also where the context tax comes from.
- *Analogy.* HTML is a document format; the closer parallel to MCP is a protocol such as HTTP (or a USB-C-style port).
- *Verified by web search this session:* MCP was donated to the Agentic AI Foundation, a directed fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI, announced December 9, 2025 (Anthropic and MCP project blog posts).
- *Verified by web search, with a caveat:* a **2026-07-28** spec revision removes the `initialize` / `notifications/initialized` handshake and the `Mcp-Session-Id` header; protocol version and client capabilities ride in each request's `_meta`; a `server/discover` method returns capabilities on demand; results gain a required `resultType`; roots, sampling and logging are deprecated. Sources disagree on whether it was final or still a release candidate when written (one dated July 23 calls it an RC); check the official changelog.
- *Not verified:* the Perplexity "72% of the context window" claim, the VS Code 128-tool cap, and "supported by Claude, ChatGPT, Cursor, VS Code" as stated.

**Correction to earlier entries.** Entries 1 and 5 describe the lifecycle (`initialize`, then `initialized`) and list roots and sampling as client features. That is the model the course teaches (chapter 8's server reports protocol version 2025-11-25, and its tests check that a request before initialization is rejected). The 2026-07-28 revision replaces it with stateless requests and deprecates roots and sampling. **For the exam, answer in the course's version unless told otherwise, and name the version.** Discovery itself survives the change: a client can still ask what tools exist.

**Exam traps.**

- "Discovery means the model already knows the tools": false; it is learned at run time, which is the point.
- "Distribution means one server works in every host with every feature": false; support beyond plain tools is uneven.
- "The annotations guarantee a tool is read-only": false; they are hints.
- "A standard guarantees a good interface": false; it standardizes the plug, not the design of the tools.

## 7. What is REST, and why is it important?

**Bear's prompt:** "add rest, what is rest and why is rest important? People should know what rest is."

**Claude's answer (not yet signed off).**

**What it is.** REST (Representational State Transfer) is an architectural style for web APIs, described by Roy Fielding in his 2000 doctoral dissertation. In practice, "a REST API" means a service you reach over HTTP, built around these ideas:

- *Resources identified by URLs.* A thing is named by an address, for example `/jobs/42`.
- *A small set of standard verbs:* GET (read), POST (create), PUT or PATCH (update), DELETE (remove). The verb says what to do; the URL says to what.
- *Stateless requests.* Each request carries everything the server needs; the server keeps no memory of the conversation between requests. That is what lets requests be spread across many servers.
- *Representations.* What comes back is a representation of the resource, most often JSON.
- *Standard status codes:* 200 success, 404 not found, 401/403 not allowed, 500 server error.
- *Cacheable and layered:* ordinary web infrastructure (caches, load balancers, gateways) works with it.

Example: `GET /api/jobs?industry=pharma` returns a list of jobs as JSON. Many APIs called "REST" follow only part of Fielding's style (JSON over HTTP with these verbs); say so if asked.

**Why it matters.**

- It is the dominant way services expose functionality; almost every web service offers one.
- It is simple and language-independent: any language with an HTTP library can call it.
- It reuses web infrastructure, and statelessness makes it scale.
- Anything an MCP server wraps is most often a REST API, so knowing REST is knowing what MCP sits on top of.

**REST vs MCP (ties to entry 3).**

- REST has no run-time discovery of its own: the description (for example an OpenAPI file) is a separate document a developer reads. An MCP server lists its tools to the client on request.
- REST has no notion of who decides to invoke an endpoint; MCP names tools as model-controlled, resources as application-controlled, prompts as user-controlled.
- REST is stateless. Before the 2026-07-28 revision MCP was stateful (a handshake and a session); that revision makes MCP stateless too, which moves the two closer.
- REST endpoints are written for developers; MCP tool descriptions and errors are written for a model.

**Exam traps.**

- "REST and MCP are alternatives": mostly false; MCP servers usually wrap REST APIs.
- "REST keeps session state on the server": false; statelessness is a defining property.
- "A URL names an action": false in REST; it names a resource, and the verb is the action.

**Unchecked:** the REST description is from Claude's general knowledge, not the course.

## 8. REST vs API vs MCP, JSON, and HTTP (taught from a real call)

**Bear's prompt:** gave `https://boards-api.greenhouse.io/v1/boards/figma/jobs` and said: "We didn't know what REST is, how REST differs from an API, even though APIs can be built on REST. And how APIs differ from MCP. Why JSON is so common, and sort of what HTTP is."

**The live call (run 2026-11-02, Figma's public Greenhouse board).** Request: `GET /v1/boards/figma/jobs` on host `boards-api.greenhouse.io`, header `Accept: application/json`. Response: `HTTP/2 200`, `content-type: application/json`, about 89 KB, `meta.total` = 140 jobs. First job: id 5426468004, title "Account Executive, Enterprise", location "San Francisco, CA • New York, NY • United States", `updated_at` 2026-10-27, `company_name` "Figma", plus an `absolute_url` for the human page.

**Claude's answer (not yet signed off).**

**HTTP.** HyperText Transfer Protocol: the agreed way a client asks a server for something and the server answers. A request has a *method* (the verb: GET, POST, PUT/PATCH, DELETE), a *URL* (what), *headers* (extra information such as what format the client accepts), and sometimes a *body*. A response has a *status code* (200 OK, 404 not found, 401/403 not allowed, 500 server error), headers, and a body. It is stateless: each request stands alone. It is the same protocol your browser uses for every web page.

**API.** Application Programming Interface: *any* agreed way for one program to use another's functionality. "API" is the general category and says nothing about how. A function library, an operating system call, a command line and a web service can all be APIs.

**REST.** One *style* of building a web API: resources named by URLs, the HTTP verbs as the actions, stateless requests, representations (usually JSON) in the body, standard status codes. So: **every REST API is an API; not every API is REST.** Other web styles exist (SOAP, GraphQL, RPC-style calls), and many APIs are not web services at all. Relationship in one line: *API = the idea, REST = one way to build it, HTTP = the transport REST uses.* Many "REST" APIs follow only part of Fielding's original style; the common meaning is JSON over HTTP with these verbs.

**JSON.** JavaScript Object Notation: text made of key/value pairs, lists, strings, numbers, true/false and null, such as `{"title": "Account Executive", "id": 5426468004}`. Why it is everywhere: human-readable; every major language parses it with a built-in or standard library; it maps directly onto the dictionaries and lists programs already use; it is lighter than XML, which it displaced. Its weakness: it has no built-in schema or comments, so a separate description (such as a JSON Schema) is needed to say what is valid. MCP uses JSON too: its messages are JSON-RPC 2.0, and tool inputs are described by JSON Schema.

**API vs MCP.** An API (here a REST one) is how *a developer's code* uses one service: the developer reads the documentation and writes code ahead of time against fixed endpoints. MCP is a protocol that lets *any host and its model* discover and use a service's tools at run time, in one standard format, with tool descriptions and errors written for a model, and named control rules (tools model-controlled, resources application-controlled, prompts user-controlled). Typically an MCP server wraps an API: a `search_jobs` tool whose code does `GET /v1/boards/figma/jobs`. MCP does not replace the API; it makes it usable by agents without custom glue for each pairing.

**The same call at three levels.**

1. Browser: open the URL; the browser sends the HTTP GET and shows the JSON text.
2. Program: code makes the same GET and reads the JSON into a list of jobs. This is the REST API used directly.
3. Agent: a host connects to an MCP server that exposes `search_jobs`; the model finds the tool at run time, proposes a call, the host runs it (which makes the GET), and the result comes back to the model.

**Exam traps.**

- "REST is a protocol": false. HTTP is the protocol; REST is a style built on it.
- "API means web API": false; web APIs are one kind.
- "JSON is part of REST": no; REST usually returns JSON but does not require it (XML or plain text also work).
- "HTTP keeps a session between requests": false by design; each request stands alone (cookies and tokens are added on top).
- "MCP replaces REST": false; MCP servers usually call REST APIs.

**Unchecked:** the definitions are from Claude's general knowledge, not the course. The live call output above was run in this session.

## 9. RAG and APIs: is there a difference?

**Bear's prompt:** "explain RAG and APIs, the difference between if there is one between RAG and an API?"

**Claude's answer (not yet signed off).**

**Short answer.** Yes, they are different kinds of thing, so they are not rivals. An **API** is an *interface*: a way for one program to use another. **RAG** is a *pattern*: before the model answers, the system looks up relevant material and puts it in the prompt. A RAG system often *uses* an API to do the lookup.

**RAG (retrieval-augmented generation).** Steps: (1) take the user's question; (2) *retrieve* the most relevant passages from a collection of documents, usually by similarity search over text turned into vectors, sometimes by keyword search; (3) put those passages into the model's context; (4) the model *generates* an answer from the question plus the passages. It exists because a model's knowledge is frozen at training and is not your private data; retrieval supplies current or private text at question time without retraining. The retrieval step makes decisions (how to cut documents into pieces, how to score similarity, how many results to keep) that decide what the model ever sees; that is chapter 7's subject (the course calls it retrieval; its own chapters do not use the word "RAG").

**API.** Any agreed way for one program to use another's functionality (see entry 8). A REST API is one kind.

**How they differ.**

- *Category:* API = interface (how you call something). RAG = pattern (what you do before generating).
- *What comes back:* an API returns whatever its function returns (a job list, a price, a status). RAG returns passages chosen for relevance to a question, and the model then writes prose from them.
- *Selection:* an API call is exact: you name the resource or give parameters. Retrieval is approximate: it ranks by similarity and can miss or mis-rank.
- *Who decides the call:* in RAG the system retrieves on every question (or by a rule). With tools the model chooses whether to call.

**How they connect.**

- A retriever is often reached through an API (a vector database or a search service).
- An API can be a source for RAG: fetch from it, then place the result in context.
- Tool use through MCP can *do* retrieval: a `search_docs` tool returns passages, or an MCP resource supplies a document. That makes retrieval agent-driven: the model decides when to look.
- Example: "What is Figma's open job in New York?" Via API: `GET /v1/boards/figma/jobs`, filter, answer. Via RAG: the job descriptions were indexed ahead of time; the question retrieves the closest passages and the model writes the answer. API answers from exact structured data now; RAG answers from indexed text by relevance. Many systems combine both.

**Why this matters for checking (the course's stance).** Retrieval can return something plausible but incomplete, and a fluent answer can hide that. A person checks which sources reached the model and which did not.

**Exam traps.**

- "RAG is an alternative to an API": false; different categories, and RAG often uses one.
- "RAG retrains the model": false; the model is unchanged, only its input changes.
- "RAG guarantees correct answers": false; wrong or missing retrieval yields confident wrong answers.
- "An API call and a retrieval are both exact lookups": false; retrieval ranks by similarity and is approximate.

**Unchecked:** the definitions are from Claude's general knowledge; the course's chapter 7 covers the retrieval mechanics (tokenizing, term counts, vector similarity, top-k selection) but not the term "RAG".

## 10. Questions added: facts from retrieval vs letting the model plan

**Bear's prompt:** "or the exam come up with some questions around when should we be using actual facts from RAG? And when can we use a language models to plan the plans?"

Added to the pool (checker 0 problems; JSON rebuilt; pool now 985 MA / 941 ES; not committed):

- `MA-ch07.64`: private or post-training facts need retrieved sources; stable general knowledge may come from the model; quote and date for traceability.
- `MA-ch07.65`: exact changing values come from the system of record, similarity retrieval suits free-text passages, never present remembered text as sourced.
- `ES-ch07.60`: four tasks (current policy, checklist order, ledger balance, email draft): which need facts, which the model can do; the rule; what a person checks.
- `MA-ch10.64`: the model can propose steps and order, but facts about the real system must be observed; a plan is reviewed before action.
- `MA-ch10.65`: retrieve first, then plan; claims trace to sources; sources authorized by a person.
- `ES-ch10.61`: what a model can plan alone, what must be checked, what review happens.

True-statement counts in the four MA: 2, 3, 3, 4. Questions stand alone (no "the chapter says").

## 11. Need to know: a heuristic for what information an agent gets

**Bear's words (closely paraphrased):** He watched a video that made a good point about information, and it should be on the exam. The military uses "need to know" as a simple system for what information is given at what level. It is a good heuristic for agents too: if an agent does not need this information, it should not get it.

**Claude's answer (not yet signed off).**

- *The rule.* Give an agent only the information its task requires. The test is "does the task need this?", not "might it be useful?"
- *Why it helps.* Less to leak; an injected instruction cannot make an agent reveal what it never had; less irrelevant text in the context window; smaller damage when the agent is wrong.
- *It covers reach, not just the prompt.* An agent that can query every database effectively knows everything, so tool and data permissions follow the same rule. This is the information-side twin of least privilege (chapter 5), which limits what an agent can *do*.
- *Link to MCP.* Connect only the servers and resources a task needs: it keeps the context tax down and the security surface small, since each connected server adds descriptions the model reads and tools it can call.
- *Link to multiple agents.* An orchestrator should hand each worker only the part its subtask needs.
- *Limits.* It is a heuristic, not a guarantee. Starve an agent too far and it fails or guesses; so a person decides what the task needs and what to do when the agent says it cannot finish without more, and grants are deliberate. Check what actually reached the agent.

**Questions added (checker 0 problems, JSON rebuilt, uncommitted):** `MA-ch05.62`, `MA-ch12.61`, `ES-ch05.62`.

**Exam traps.**

- "More context always improves answers": false.
- "A trusted agent doesn't need limits": false.
- "Limiting the prompt is enough": false; tool and data access count too.
- "Need-to-know is decided by the agent": false; a person decides.

**Unchecked:** the military framing is Bear's; the rest is Claude's general knowledge, not a source read in this session.

## 12. Framing MCP as primarily a process of discovery: feedback

**Bear's prompt:** "Thoughts of framing MCP as primarily a process of discovery? Feedback?"

**Claude's feedback (not yet signed off).**

**Where the framing works.**

- Runtime discovery is what REST lacks: the client asks the server what it offers and gets names, descriptions and input schemas in one standard form. It answers the training-cutoff problem: a model cannot know a capability added after training, but it can ask.
- It survives the spec changes. The 2026-07-28 revision removes the handshake and sessions but adds a discovery method, so discovery is more durable than the handshake.

**Where it is incomplete.**

- Discovery is half of the loop. The other half is invocation under control: the model proposes, the host decides and runs, the result returns. The fuller phrase: *a standard for discovering and invoking capabilities*.
- Discovery is not unique to MCP. OpenAPI files, `--help` and tool registries also describe capabilities. What is distinctive is that it is standard, machine-readable, in-band at run time, uniform across servers, and written for a model.
- Resources and prompts are context supply as much as discovery, though they are listed the same way.
- Discovery shows only what exists, not when or how well to use it. Thin descriptions give the model little to go on.

**The sharp edge (links to entries 5, 6 and 11).**

- What is discovered is the server's *claim*. Discovery is also the attack surface: descriptions sit in the model's context before any call.
- Discovery fills the window (the context tax). Need-to-know says to expose only what the task needs, so the host should filter what is discovered, not show everything.

**Suggested exam framing.** *Discover, decide, invoke.* MCP standardizes the first and third steps; the middle step, whether this server belongs in this task, stays with a person. That keeps the course's split between interoperability and authorization.

**Exam framing (Bear's correction, 2026-11-02).** The exam does not turn on words like "only", "always" or "unique", and a statement is not false just because it sounds absolute. The point is what MCP is *used for*: it is used for discovery, and also for invocation and for supplying context. Discovery is not a guarantee that tools are safe or accurate, and it is not unique to MCP; those are background facts, not the lesson. State the use, then the limit: MCP is used to discover and invoke capabilities, and the decision to trust a server is made by a person. **Discover, decide, invoke** is the frame.

**Question-writing note.** Do not make a false statement detectable by its absolute word. A false statement should be a plausible claim a student could believe, such as "if the server lists a tool, the tool is accurately described", not "discovery guarantees..." or "only...". (Several false statements in the questions added on 2026-11-02 use such words and should be rewritten.)

## 13. Discover, decide, invoke: where is the human and where is the agent?

**Bear's words (closely paraphrased):** If we frame MCP as discover, decide, invoke, who does the discovering? There is human discovery and agentic discovery. The human decides which MCP server to use; then the agent asks the server what it can do. In the decide step the human can have gates and feedback, and the agent can make some decisions too. Invoke is mostly the agent doing the thing: calling the API and getting back whatever comes. So the frame should say where the human is and where the agent is.

**Claude's answer (not yet signed off).**

**Two kinds of discovery.**

- *Human discovery:* finding out that a server exists and choosing to connect it (reading about it, checking where it came from, adding it to the host's configuration). This is a person's act and it is where the first gate sits.
- *Run-time discovery:* once connected, the host's client asks the server what it offers (tool list, resources, prompts) and the model sees the result in its context. Colloquially "the agent asks"; strictly the host does the asking and the model reads the answer.

**Decide has layers, and the human and agent split it.**

- *Human decides (authority):* which servers to connect; which of their tools to allow or hide (need to know); which actions need approval; whether to grant more when the agent cannot finish. Gates and feedback live here, set in advance (configuration, allow lists) and at the moment (approval prompts on risky calls, tool hints such as read-only or destructive used by the host to decide when to ask).
- *Agent decides (tactics):* which tool to call, with what arguments, in what order, and whether the result is good enough to continue.
- *Host enforces:* it applies the human's policy; the model cannot waive it.

**Invoke is mostly automatic.** The model proposes a call; the host sends it to the server; the server runs its code (often calling an API); the result returns. The human is mostly absent during a call, except where a gate pauses it (an approval, or a server asking the user for missing input).

**It is a loop, not a line.** After a result comes back the agent observes, decides again, and may invoke again; the human returns afterward to check results and logs. Feedback runs through errors written for the model (a tool result marked as an error lets the agent retry with better arguments) and through the human's review.

| Step | Human | Agent / host |
|---|---|---|
| Discover | Finds and chooses which server to connect | Host asks the server what it offers; the model reads the list |
| Decide | Sets authority: allowed servers and tools, approvals, grants | Chooses tool, arguments and order; host enforces the human's policy |
| Invoke | Gates on risky calls; reviews afterward | Proposes and runs the call; the server may call an API; result returns |

**Link to the course.** The four parties (server, host, Claude, people and policy): the server describes, the host exposes selected tools and decides what enters context, Claude proposes, and people and policy define authority. This is "conduct, check, drive": the human conducts (chooses and scopes), checks (reviews results), and drives (decides what is allowed and when to stop).

**Exam traps (written as plausible claims).**

- "Once a server is connected, the model decides which of its tools exist for the task": the human or the host's policy decides which are exposed.
- "The model discovers servers on its own and connects them": a person (or a policy a person wrote) decides which servers are connected.
- "Approval prompts happen on every call": which calls are gated is a human decision set by policy and hints, and many calls run without a prompt.

**Unchecked:** the layering is Claude's synthesis of Bear's frame and the course's four-parties passage, not a source read in this session.

## 14. How A2A fits with MCP; is A2A widely accepted?

**Bear's prompt:** "how does A2A fit in all of this? Is A2A widely accepted at the moment?"

**Claude's answer (not yet signed off).**

**What A2A is.** The Agent2Agent protocol, an open standard that lets one agent find, talk to and hand work to another agent, including agents built by different vendors on different frameworks. Google introduced it in April 2025 and it moved to the Linux Foundation later that year (general knowledge; sources give mid-2025).

**How it fits with MCP.**

- *MCP connects an agent to tools, data and context* (agent to server). *A2A connects an agent to another agent* (agent to agent). One way to say it: MCP is the agent's hands and reading material; A2A is how agents talk to colleagues.
- They are layered, not rivals. An agent can use MCP to reach its own tools and A2A to delegate a task to another agent, which then uses its own MCP servers.
- Discover, decide, invoke applies to both. In A2A, discovery is an *Agent Card*, a description of what an agent can do and how to reach it. The decision to delegate to that agent, and what to share with it, belongs to a person or the policy a person wrote; invocation sends the task and returns results.
- A2A treats the other agent as *opaque*: it does not expose its internals, tools or memory, only its task interface. That matches need to know: share what the task needs and nothing more.
- Both ride on web standards (HTTP and JSON-based messages); the v1.0 spec adds signed Agent Cards so an agent's identity can be verified.

**Is it widely accepted?** Partly, and less than MCP. Evidence found by web search, mostly from secondary and vendor-adjacent sources:

- Reported: a stable v1.0 in early 2026 (one source says March 2026), 150+ supporting organizations and 22,000+ GitHub stars at the one-year mark (April 2026), and support in major cloud agent platforms. These figures come from an anniversary announcement and were not independently verified.
- MCP has the larger ecosystem: a February 2026 comparison put A2A's GitHub stars at about 40% of MCP's.
- Governance reports conflict (one says A2A is a separate Linux Foundation project; one German source dated August 2026 says it joined the Agentic AI Foundation). Unverified.
- Fair summary for the exam: accepted by major vendors and standardized, but MCP is the more mature and more widely used of the two. Check current status before relying on any number.

**Exam traps (as plausible claims).**

- "A2A replaces MCP for connecting an agent to its tools": it does not; MCP covers tools and context, A2A covers agent-to-agent work.
- "In A2A, the delegating agent can see the other agent's internal tools and memory": the other agent is opaque.
- "Adding A2A removes the need for a person to decide which agents may receive a task": the decision still belongs to a person or their policy.

**Unchecked:** adoption figures and governance (see above); the architecture description is Claude's general knowledge plus the search summaries, not a primary source.

## 15. A2A is thinly used; the real idea is handoff design (do it myself or delegate, and what comes back)

**Bear's words (closely paraphrased):** A2A seems thinly used now; he does not know many people who use it, and the evidence found fits that. Some of these ideas get conflated because many people write one agent that does everything inside its own loop. The idea is to write an agent so it can decide whether it needs to do a task itself or hand it to something else, and if it hands it off, what it can expect to get back.

**Claude's answer (not yet signed off).**

- *The idea does not need the protocol.* Delegation with a contract exists inside one framework (an orchestrator sending work to sub-agents or worker agents) without A2A. A2A is a standardized wire format for doing the same across vendor or organization boundaries. So "thinly used" (the standard) and "the idea matters" (delegation design) are both true.
- *The design question has two halves.*
  1. **Do it or delegate it?** Reasons to delegate: the task needs a capability this agent lacks; the work would flood this agent's context; it can run in parallel; it should be isolated; or only a narrow slice of information should be shared (need to know). Reasons to keep it in the loop: it is small, it needs the full context, the handoff cost (describing the task, waiting, checking) is larger than the work, or the information must not leave.
  2. **What comes back?** Decide before handing off: the output shape, a status (done, failed, needs more input), what evidence accompanies the claim, and how the result will be checked. A returned result is a claim from another agent, not a verified fact.
- *The handoff is a contract.* Task description and the information it carries (only what is needed), the expected output, a stop or time limit, and who approves anything with side effects. This is the same gate-and-sign-off logic as the rest of the course.
- *Where the human is.* The person (or their policy) decides which agents may receive work and what they may see; the agent decides, within that policy, whether to delegate a given task; the receiving agent does the work; the delegating agent or a person checks the result before it is used.
- *Link to the course.* Chapter 12's multiple-agents lesson: Claude coordinates and humans deliberate; combining workers' outputs is integration, not just sequencing, so conflicts between returned results need resolving by someone.
- *Link to the protocol.* A2A's task model (a task with a state such as working, needing input, completed or failed, returning outputs called artifacts) is one standard way to write that contract down. (General knowledge; check the spec for the exact state names.)

**Exam traps (as plausible claims).**

- "If an agent can do a task, it should do it itself in its own loop": not always; context cost, isolation and need to know can favor delegating.
- "A result from a delegated agent can be used as is because that agent is specialized": it is still a claim to check.
- "Delegation requires A2A": any orchestrator-worker design delegates; A2A only standardizes it across boundaries.

**Unchecked:** the delegation criteria are Claude's judgment; the A2A task-state detail is general knowledge.

## 16. Trust in agent-to-agent handoff: confidence that the work was done right

**Bear's words (closely paraphrased):** If A2A becomes widely adopted, trust will be a big deal. If an agent hands a subtask to another agent, how confident can it be that it will get it back with evidence that it was done right?

**Claude's answer (not yet signed off).**

**Three questions that get run together.** They are separate and a protocol answers at most one of them.

1. *Who is this agent?* Identity. Signed Agent Cards (A2A v1.0) help here: they show the card came from the claimed party.
2. *May it receive this task and this information?* Authorization. A person or their policy decides; need to know and least privilege apply.
3. *Did it do the work correctly?* Correctness. Neither identity nor authorization answers this. Only evidence and checking do.

This is the course's split between interoperability and authorization, with correctness as the third question, the one the computational-skepticism books are about.

**What makes a returned result trustworthy.**

- *Evidence comes with the claim, in a form the delegating side can check:* sources quoted with locations, tests that ran and their output, the inputs the work used, a log of the steps. "Done" with no evidence is only a claim.
- *Independent check.* The check must not share the producer's blind spots: a different method, a different source, or a person. Asking the same kind of agent to confirm its own work gives correlated errors.
- *Verification cost decides what to delegate.* Where a result is cheap to verify (code with tests, a calculation, a lookup with a quoted source), delegating is low risk. Where verifying is as hard as doing (judgment, open-ended analysis), the saving disappears or a person must still review.
- *Scoped authority limits the damage.* Give the other agent only the information the task needs, and only the actions it needs. Side effects (sending, deleting, paying) get an approval gate.
- *Track record* (how often this agent's results held up) is evidence about future work, not proof for this result.
- *Accountability.* The agent that delegated and the person behind it still answer for the outcome. Handing work to another agent does not hand off responsibility.

**Risks that grow with chains and openness.** Delegation chains (A to B to C) dilute confidence at each link; instructions hidden in returned text can steer the delegating agent (injection across agents); an agent can be tricked into using its own authority on another's behalf; and a vendor's agent is opaque by design, so you see outputs, not how they were made.

**Where the human is.** Sets which agents may receive work and what they see, decides how much evidence a result needs before it is used (the more consequential the task, the more), and signs off on high-stakes results. The delegating agent collects and checks evidence within those rules.

**Exam traps (as plausible claims).**

- "If the receiving agent's identity is verified, its result can be trusted": identity does not show the work is correct.
- "Asking a second copy of the same model to confirm the result gives an independent check": its errors can be correlated with the first.
- "Once a task is delegated, responsibility for the outcome moves to the receiving agent": the delegating side and its person remain accountable.
- "Higher-stakes tasks need the same evidence as routine ones": evidence required should scale with consequence.

**Unchecked:** this is Claude's synthesis with the course's themes, not a source read in this session.

## 17. Evidence must be independently checkable (the receipt test)

**Bear's words (closely paraphrased):** Evidence that the work is done is literally evidence, not an assertion. "Here you go" is not evidence. Just as with a hallucination, if I cannot independently check what comes back in some form, it is a problem. Example: I get a receipt. I (or another agent) can go somewhere and check that the receipt is a real receipt. Without verifiable evidence there is a big trust issue.

**Claude's answer (not yet signed off).**

**The test.** Can the receiving side confirm the evidence *without going through the agent that produced it*? If the only way to check is to ask the producer, it is testimony, not evidence.

**A ladder, weakest to strongest.**

1. *A claim:* "Done, payment made." Nothing to check.
2. *An attached artifact the producer made:* a receipt image or text, a pasted log, a printed test result. The producer controls it, so it can be wrong or fabricated as easily as the claim. It looks like evidence but only shows what the producer says it did. (A fabricated receipt, like a fabricated citation, can look entirely right.)
3. *A verifiable reference to something the producer does not control:* a transaction or confirmation id, an order number, a document location, a commit hash. The checker takes the reference to the system of record (the merchant, the payment processor, the source document, the repository) and looks it up. This is the receipt example.
4. *Evidence signed or issued by a third party:* a signature or record from the party that actually holds the fact, which the checker can validate.
5. *Re-doing or re-running the work independently:* re-run the tests, re-fetch and compare the source, repeat the lookup with another method.

**Correction to entry 16.** It listed "a log of the steps" and "tests that ran and their output" as evidence. Those are only as good as the checker's ability to confirm them: a log or test output the producer reports is testimony unless the tests are re-run or the log is tied to a system the checker can inspect. Evidence the producer merely describes belongs on rung 2.

**Where each type of task stands.**

- *Cheaply checkable:* a payment (confirmation id at the processor), a quoted passage (look up the source text and compare), code (run the tests yourself), a file written (inspect it).
- *Hard to check:* a judgment, a summary, a recommendation. Here the check is a person reading the original material, and the delegating agent should not treat the result as verified.

**Design rule for the handoff contract.** Say in advance what verifiable evidence must come back (the reference id, the source location, the artifact in a form that can be re-run). If the task cannot produce evidence of that kind, reconsider delegating it, or treat the result as an unverified claim: do not act on it for anything consequential until a person checks it.

**Link to the course.** Same logic as the hallucination material: fluent, plausible output is not evidence, and the check must be independent of the producer (use the AI to help check, but keep the check independent). It also parallels retrieval: a passage that quotes a source is checkable because the source exists and can be compared.

**Exam traps (as plausible claims).**

- "A receipt returned by the agent is proof the payment happened": it is an artifact the producer controls until it is verified at the payment system.
- "A detailed log from the receiving agent verifies the work": it is testimony unless the checker can confirm it against something the producer does not control.
- "If an agent returns many pieces of supporting material, the claim is well supported": volume is not verifiability; each piece has to be checkable.
- "A signed Agent Card shows the work was done correctly": it shows who the agent is, not that the result is right.

**Unchecked:** the ladder is Claude's synthesis of Bear's receipt example and the course's themes, not a source read in this session.

## 18. Could MCP be extended to verify things, not just do them?

**Bear's words (closely paraphrased):** If this becomes a widely adopted protocol, MCP itself might be extended, he does not know how much it is now, to support not just doing things but verifying things.

**Claude's answer (not yet signed off).**

**Where MCP is today (as found by web search; the official changelog was not read).** MCP standardizes discovery and invocation. A result can carry content, a structured output, and an error flag; tool annotations (read-only, destructive) are hints. No search result showed an official MCP feature that makes a tool result *verifiable* by the receiving side (a built-in evidence or proof field). Proposals exist outside the core spec:

- An individual (not working-group) IETF draft, "MCPS", dated March 2026: signed messages, agent identity ("passports"), tool-definition integrity, replay protection, wrapped around the existing messages. It signs where a message came from; it says it does not judge whether a tool is safe.
- A May 2026 academic paper on "attested tool-server admission": a server publishes a signed clearance, with a deny-by-default tool allowlist and an audit trail. This is about admitting servers, not checking each result.
- A July 2026 Agentic AI Foundation post on "verifiable evidence at the MCP boundary": hardware attestation of a policy gateway so each tool call becomes a signed record; extending it to the tool server itself is described as later work.
- Vendor identity products (marketing; claims not verified).

So "verification" is being worked on mostly at the *identity, integrity and audit* level, not yet as a standard way to prove a result is correct.

**What can be done today without changing the protocol.**

- *Verification as just another tool.* A server for the system of record can expose a read-only lookup (for example, confirm a payment by its id). The delegating agent checks the receipt by calling a *different* server than the one that produced it. Independence comes from using a separate party, which is the receipt example from entry 17.
- *Return verifiable references.* A tool's structured output can include transaction ids, source locations and hashes by convention, so a checker can look them up.
- *Host-side logs and gates* record what was called and with what arguments, which a person can audit.

**What an extension might add.** Standard fields for evidence (reference ids, source pointers, the inputs used); signed results from the party that holds the fact; a standard "verify" call shape; and audit records that can be checked later. Sources describe the 2026-07-28 revision as built to be extensible, but the extension details were not verified.

**Limits to state.**

- A signature shows *who sent* a result and that it was not altered. It does not show the result is *correct*. A signed wrong answer is still wrong.
- Verification through the same server that produced the result is not independent.
- A person still decides what evidence is enough for a given task.

**Link to the frame.** Discover, decide, invoke gains a fourth step, *verify*, and it is where the human's sign-off lives.

**Exam traps (as plausible claims).**

- "A digital signature on a tool result shows the result is correct": it shows origin and integrity.
- "Asking the same server to confirm its own result is a verification": it is not independent.
- "Verification needs a new protocol feature": a read-only lookup tool on a separate server already does it; extensions would standardize and strengthen it.

**Unchecked:** the proposals come from search summaries (draft, paper, foundation post, vendor page); none was read in full; the MCP changelog was not read.

## 19. What a model is trained on, how to give it today's information, and whether newspapers have an MCP

**Bear's words (closely paraphrased, dictation fixed), 2026-11-04.** He showed a screenshot of that morning's New York Times front page and asked what Sonnet 5.5's release date was and how Claude would learn what happened today. Then: "This could be a question." Students need to understand that what a model is trained on is its training data, which for frontier models is pretty much the entire internet, and that the size of the data set is what makes it a frontier model. Is that not true? Then: how do we give it data? A built-in web search goes to some set of places for election results. If he trusts other sources more than the Times he can tell Claude to look there. He can give a screenshot or a web page to analyze. And now there is MCP: if he does this a lot, does the New York Times have an MCP? Can Claude talk to the Times? Do newspapers have an MCP?

**Claude's answer (not yet signed off).**

**1. Training data: "pretty much the entire internet" is the right order of magnitude but too strong.**

- A frontier model is trained on a very large, *filtered* collection: a large share of the public web, plus licensed third-party data and synthetic data, and the model is then tuned after pretraining. Anthropic's stated approach, as quoted from its system cards by secondary sources, is to crawl public web pages while following the site's robots.txt, to skip pages behind a login or a CAPTCHA, to license some data, and to generate some synthetic data.
- Publishers can and do block crawlers, and duplicates and low-quality text are removed, so large parts of the internet are not in the data.
- *Observed in this session:* the search tool Claude uses refused the domains nytimes.com, reuters.com, reutersagency.com, ap.org and apnews.com with the message that they are "not accessible to our user agent". A site that blocks the crawler cannot be read by that tool.
- Data size is central to why frontier models are capable, but it is not the whole reason: parameters, computation and post-training matter too. Training ends at a cutoff, so later events are not in the weights, and a fluent answer can be stale.

**2. Ways to give a model today's information.** Every one of them puts text in the model's input; none changes the weights.

- *Paste or attach it:* article text, a web page's text or a screenshot. You choose the material; the model reads it for this conversation.
- *A built-in web search:* the system's search tool picks pages. Its options can include allowed or excluded sites, so naming the sources you trust is a real instruction; sites that block the tool cannot be read.
- *Fetch a page you name:* the same limits apply (blocked or paywalled pages).
- *Retrieval from your own collection* (chapter 7).
- *A connected tool, an MCP server or an API:* structured access to a source, if someone has built it and you have connected it.
- A screenshot is a claim: it does not prove the page is genuine or current. Confirm anything that matters in a second source.
- A person decides which sources are used and trusted. The model's answer, even with a citation, is a claim to check against the source (entries 16 and 17).

**3. Does the New York Times have an MCP? Do newspapers?** Found by web search this session; secondary sources only, none read in full.

- *New York Times:* no official MCP server found. The Times has developer APIs (article search, top stories, archive, bestsellers, per a community project's description) that need an API key. A community server (GitHub user jeffmm, "nytimes-mcp", MIT licence, version 0.1.0, listed on lobehub.com) wraps those APIs as MCP tools. Its maintenance and quality were not checked, and it is not the Times's own. The Times's site was not readable by the search tool.
- *Reuters and AP:* an aggregator headline says Reuters launched an MCP server, and a G2 marketplace page lists an AP MCP server with 26 tools. Neither was confirmed on the organization's own pages (both sites are blocked to the search tool). Thomson Reuters, the parent company, has documented MCP products for legal and tax (HighQ MCP, a CoCounsel Legal MCP connector with Claude), which are professional products, not a newsroom feed. One of its help pages is reported to restrict using its content with another professional AI tool, including through MCP.
- *Rights:* the Times sued OpenAI and Microsoft over training use (filed December 2023, in discovery as of early 2026; later status not found) and licensed content to Amazon (May 2025). Access through an API or an MCP server is still governed by the publisher's terms.
- *What carries into the exam:* an MCP server exists only where someone built it, official or community; a source with an API does not automatically have one; a community wrapper is not the publisher's; and the person decides whether to connect it. Which newspapers have one changes quickly and is not exam material.

**Questions added (checker 0 problems, JSON rebuilt, pool 989 MA / 943 ES, uncommitted, not blind-audited):** `MA-2.3` (what training data is and is not, cutoff, how post-cutoff information reaches a model; 3 true), `MA-2.4` (ways to supply today's news: pasted text, retraining myth, citation is not verification, naming sources and blocked crawlers, API versus MCP; 2 true), `ES-2.2` (analyst needs reliable daily answers: why training cannot supply it, three routes, weights unchanged, who decides, what to check).

**Exam traps (as plausible claims).**

- "A frontier model is trained on a complete copy of the internet": it is a filtered subset plus licensed and synthetic data.
- "Once you show the model today's article it knows it from then on": it is context for that conversation; the weights are unchanged.
- "An answer with a citation has been verified": it shows a source, not correctness.
- "A news site that offers a developer API also provides an MCP server": someone has to build one, and it may be unofficial.
- "A model can tell which of its answers depend on events after its cutoff": it cannot reliably.

**Unchecked:** the training-data description is from secondary summaries of Anthropic's system cards, not the cards themselves; the Reuters, AP and NYT items are from search summaries; the NYT developer portal was not read (blocked); the status of the NYT lawsuit after early 2026 was not found. Sources: [community NYT MCP listing](https://lobehub.com/es/mcp/jeffmm-nytimes-mcp) (lobehub), [Stanford transparency report on Anthropic](https://crfm.stanford.edu/fmti/December-2025/company-reports/Anthropic_FinalReport_FMTI2025.html), [TechCrunch on the NYT-Amazon deal](https://techcrunch.com/2025/05/29/the-new-york-times-and-amazon-ink-ai-licensing-deal), [Thomson Reuters HighQ MCP help](https://www.thomsonreuters.com/en-gb/help/highq/highq-mcp/overview), [AP MCP listing on G2](https://ai.g2.com/marketplace/tools/ap-mcp-server).

## 20. Fine-tuning: what it means and how it generally works

**Bear's words (closely paraphrased), 2026-11-04.** Students will not have to fine-tune models unless they do the optional assignment (an optional assignment to train a model, which can make up for a missed class; details not yet given), but they have to know what fine-tuning means and how it generally works.

**Claude's answer (not yet signed off).** Fine-tuning is taking a model that is already trained and training it some more, on a small, targeted set of examples, so its weights shift a little in a chosen direction.

1. Start from the pretrained weights (pretraining taught general language and world knowledge by next-token prediction on huge text).
2. Collect examples of the wanted behavior: prompt and ideal-response pairs (supervised fine-tuning), or pairs of a better and a worse response (preference tuning, the idea behind human-feedback training).
3. Choose an objective, a loss that measures how far the output is from the examples.
4. Run the chapter 9 loop: predict, measure the loss, compute the gradient, nudge the weights, repeat, with a small learning rate and few passes so the model keeps what it knew. The only difference from the chapter 9 toy is scale: billions of parameters starting from learned values, not two starting at zero.
5. Check on held-out examples; keep the result as a new artifact (often a small add-on to the weights, such as LoRA).

*Good for:* style, tone, output format, consistent behavior on a narrow task, shorter prompts, a smaller model doing one job. *Not good for:* adding lots of fresh or changing facts; learning from a chat (a prompt never changes weights); guaranteeing correct answers. *Risks:* overfitting, forgetting other abilities, flawed or biased examples baked in, harder to inspect and reverse than a prompt. *Chapter 9 link:* it is the weights row, the only one of the five objects with an optimizer; "we trained Claude on our policies" is almost always the context row. *Verbs:* "lowered the objective on the training pairs" is accurate; "generalizes" needs a held-out check; "causes" needs assumptions the data cannot supply.

**Exam traps (as plausible claims).** "Sending many prompts fine-tunes the model": prompts do not change weights. "Fine-tuning gives the model new abilities from nothing": it adjusts a model that was already pretrained. "A lower training loss shows the fine-tune works": it shows the objective fell on the examples shown.

**Unchecked:** general knowledge, not a source read in this session.

## 21. Fine-tuning versus retrieval

**Bear's choice, 2026-11-04:** "Fine-tune vs retrieval."

**Claude's answer (not yet signed off).** Fine-tuning changes the model; retrieval changes what the model sees this turn and leaves the model unchanged.

- *Best for:* fine-tuning for behavior (style, format, a consistent way of doing a task); retrieval for facts (private, changing or large collections).
- *Updating:* fine-tuning needs another training run; retrieval means editing the collection, effective at once.
- *Removing something:* hard in weights; easy in a collection (delete the document).
- *Checking a claim:* a fine-tuned model cannot point to where it learned something; retrieval can show which passages entered the input and cite them.
- *Failure:* fine-tuning overfits, forgets, bakes in errors and recalls facts blurrily; retrieval ranks by similarity and can miss or mis-rank, and retrieved text can carry injected instructions.
- *Cost:* fine-tuning is large up front, then shorter prompts; retrieval is cheap to set up, with longer prompts and a search step per question.
- *Rule of thumb:* behavior goes in the weights, knowledge goes in the context. Try the cheap, reversible things first: prompt, then context or retrieval, then tools, then fine-tuning last (chapter 9's order by reversibility and inspectability). They combine: tune for format and skill, retrieve for facts.
- *Example:* yesterday's election results are the wrong thing to fine-tune on: they keep changing, training takes longer than the news does, and nobody could check where a number came from. Use search, an API or an MCP server.

**Exam traps (as plausible claims).** "Fine-tuning on our policy documents keeps the model current with our policy": it is frozen at training time. "A fine-tuned model can cite its sources": it cannot. "Retrieval changes the model": it does not. "Retrieval guarantees correct answers": it does not. "Fine-tuning is the best way to add new facts": a weak one.

**Unchecked:** general knowledge; the claim that fine-tuning is a poor way to add facts is not backed by a source read in this session.

## 22. Hugging Face as a reference for what models can do

**Bear's words (closely paraphrased), 2026-11-04.** With a screenshot of Hugging Face's Models page (3,213,171 models; task filters; trending list): students should be able to describe what these fine-tuned models do. Hugging Face is the reference for what models can do.

**Claude's answer (not yet signed off).** Facts below were read from each model's public page and API on 2026-11-04; the download and like counts matched the screenshot. No model was run.

**How to describe a model from its listing and card (a checklist).**

1. *Task tag* = input to output. The tags read "X-to-Y": Text Generation (text in, text out), Image-Text-to-Text (image and text in, text out), Image-to-Text (captioning, reading text in images), Any-to-Any (several kinds in and out), Image-to-Image (editing), Text-to-Image and Text-to-Video (generate from a prompt), Text-to-Speech (text to audio), Automatic Speech Recognition (audio to text); the page lists 44 more.
2. *Size:* parameter count (and, for a mixture-of-experts name such as "A4B", how many are active per token, about 4 billion here, out of about 34 billion in total).
3. *Lineage:* the `base_model` field and the model's own page say what it was built from.
4. *How it was adapted:* pretraining, then post-training steps such as supervised fine-tuning and reinforcement learning.
5. *Limits and licence:* what the maker says it is not for.
6. *Claims:* benchmark tables on a card are the maker's own; popularity counts and "updated 6 days ago" show attention and last edit, not quality or training date.

**The three trending models in the screenshot.**

- **LiquidAI/LFM3-1.7B (Text Generation, 1.73B parameters).** A small text model for local agents, tool calling and structured outputs; about 1 GB at 4-bit, so it fits on a phone or laptop; 256K-token context. Lineage: post-trained from LFM3-1.7B-Base (pretrained on 22 trillion tokens); post-training is supervised fine-tuning on 1.75 trillion tokens (chat, reasoning, tool calling, agent traces) plus mixed reinforcement learning (math, code, SQL, structured output). Its card says it is meant to be fine-tuned further on one GPU, to use retrieval or search for knowledge-heavy tasks, and that it is not recommended for agentic coding or complex multi-step reasoning. That is the fine-tuning versus retrieval point from the maker's own mouth.
- **nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B (Automatic Speech Recognition, about 34B in total, about 4.3B active).** Takes recordings plus a text instruction and returns text: transcription in 40 languages, up to an hour of audio, speech translation, speaker-attributed transcription, timestamps, language identification and questions about audio. Lineage: a Nemotron-3.5 Lightning 30B language model with an audio encoder and a speaker encoder attached, so a language model adapted to take audio in. The training section was not read in full.
- **deepseek-ai/DeepSeek-V4.1-Flash-1017 (Image-Text-to-Text, about 763B parameters).** Takes images and text and returns text: reasoning, coding, agent tasks and visual questions; 1 million-token context; MIT licence; weights stored in 8-bit. Its card calls it a minor update to DeepSeek-V4.1-Flash with better reasoning, coding, agent and visual scores and shorter outputs. The base-model field is empty, so it is listed as a standalone release, and the card does not describe its training method. Its benchmark table (including rival models) is the maker's own.

**Exam traps (as plausible claims).**

- "A model with more downloads is the more accurate one": downloads show attention.
- "A benchmark table on a model card is an independent evaluation": it is the maker's claim.
- "Image-Text-to-Text means the model produces images": text and images go in, text comes out.
- "A model with a 'base model' listed was trained from scratch": it was adapted from that base.
- "Updated 6 days ago means it was trained 6 days ago": it is the last edit to the page.

**Unchecked:** the task descriptions beyond the three cards are general knowledge of Hugging Face's task names; the model-tree view on each page was not opened; benchmark figures were not checked against independent sources.

## 23. An image-text-to-text model reading a screenshot, and small models for narrow tasks

**Bear's words (closely paraphrased), 2026-11-04.** Use the example of a specific trained model being an image-text-to-text model. Talk about the issues with extracting the text of the New York Times image I gave you. Also talk about efficiency: if we are making something better at a very specific task, we do not necessarily need a model with a bajillion parameters; we can use a mini model.

**Claude's answer (not yet signed off).**

**The task.** Reading a screenshot is an image-text-to-text task: the input is an image plus an instruction ("list the Senate and House totals"), the output is text. A model with that tag, such as the Image-Text-to-Text model in entry 22, does it by perceiving the image and generating text, not by copying characters.

**Issues with extracting text from the New York Times screenshot.**

- *Perception errors.* The big numbers (54, 44, 237, 139) are easy; the small captions ("7 Flips", "34 seats not up for election", "31 seats not up", the 50 and 218 markers) are where a misread digit is likely. Images are also resized before a model sees them, which loses small text.
- *Layout.* Which number belongs to which party depends on position and colour (Democrats on the left in blue, Republicans on the right in red), not on the words alone.
- *The map.* State outcomes are conveyed by colour and hatching, the legend is out of frame, and the states are unlabeled. Reading them means guessing from shapes and shades.
- *Missing data.* A screenshot holds only what is visible at that moment: no per-district results, no vote counts, nothing below the fold, nothing in tooltips. It is stale the moment it is taken.
- *Fluent guessing.* A model fills gaps with plausible text and does not reliably flag what it could not read. Plausible is not verified.
- *Provenance.* A screenshot cannot show that it is genuine or current. A feed from the source (an API or an MCP server) carries exact values and a source.
- *Cross-checks catch misreads.* The numbers must add up. Senate: 54 minus 34 not up for election is 20 Democratic wins; 44 minus 31 is 13 Republican wins; 33 called of the 35 contests (35 on the Wikipedia page, counted in this session) leaves 2 uncalled, and 54 plus 44 is 98, which agrees. House: 237 plus 139 is 376 called, so 59 of 435 are uncalled. A reading that fails such a check is wrong somewhere.
- *Best fix:* do not read the picture at all when structured data exists. Where you must, read it two ways (a text-recognition tool and a model), compare, and confirm anything that matters at the source.

**Efficiency: a mini model for a narrow task.**

- *Cost scales with size.* The memory for the weights is roughly the number of parameters times the bytes per parameter. A 763-billion-parameter model stored in 8-bit is about 763 GB for the weights alone (a multi-GPU server); a 1.73-billion-parameter model in 4-bit is about 0.9 GB (the card says about 1 GB), so it runs on a laptop or phone. These are Claude's arithmetic from the cards.
- *Mixture of experts.* A model with about 4 billion active parameters out of about 34 billion saves computing per token but still has to hold all of the parameters in memory.
- *Narrow beats general when the task is narrow.* A small model fine-tuned (or trained to imitate a larger one, called distillation) on many examples of one task, such as reading results-page screenshots, can often match a much larger general model on that task, at lower cost, faster, privately on your own machine, and with weights you can version and audit. Often, not always: it has to be shown on held-out examples.
- *The trade-offs.* A narrow model is brittle outside its task (a redesigned page can break it), is weaker at open-ended reasoning, and needs training data and an evaluation up front. A large general model needs no training and handles surprises, but costs more per use, is slower, and sends data off your machine if it is hosted.
- *A sensible design.* Use plain code or an API when the data is structured; a small specialized reader for the repeated, narrow case; a large model only for the hard or ambiguous case; ordinary code to check the output (the sums above); a person for anything consequential. This is "let the model generate, let ordinary code check" again.
- *Link to the course.* This is the case for fine-tuning in entry 20 (behavior and a narrow skill, not a store of facts) and the reason the optional train-a-model assignment is feasible on a single GPU.

**Exam traps (as plausible claims).**

- "For a narrow task you need the biggest model available": a small tuned model can do it, if shown on held-out data.
- "Reading text from an image is exact copying": it is perception plus generation and can misread.
- "If the extracted numbers look plausible they are right": check them against each other or the source.
- "A screenshot of a results page contains the results": only what was visible at that moment.
- "A mixture-of-experts model with 4 billion active parameters needs memory for only 4 billion": all experts are loaded.

**Unchecked:** the memory figures are arithmetic, not measurements; the claim that small tuned models often match large ones on narrow tasks is general knowledge, not a source read in this session; the NYT legend and the map were not decoded.

## 24. Why fine-tuning matters: customization (a voice, a drawing hand, a writing style)

**Bear's words (closely paraphrased), 2026-11-04.** Promote the importance of fine-tuning in terms of customization: making a voice model that sounds like you, a drawing model that draws like you, and so on.

**Claude's answer (not yet signed off).**

- *The core idea.* A prompt tells a model what to do; fine-tuning teaches it how you do it. Some things can only be shown, not described: a voice, a drawing hand, a writing style, a house way of grading or coding. The examples go into the weights.
- *Examples by Hugging Face task tag.* Text-to-speech: a voice that sounds like you. Text-to-image: an add-on trained on your own drawings that draws new pictures in your hand. Text generation: your register and your field's terms. Speech recognition: your accent and your jargon. Image-text-to-text: your handwriting or one page layout (the screenshot-reading case in entry 23).
- *Why it matters.* The style is there every time, without a long prompt. A small tuned model can do the job cheaply (entry 23). It can run on your own machine, so your data stays yours and so do the weights. It is the difference between using a tool and making one.
- *Honest limits.* Not everything needs fine-tuning. A reference clip, examples in the prompt or retrieval may be enough, and they are cheaper and reversible (the ladder in entry 21). Fine-tuning pays off when you need a stable style, repeated many times. Whether it "sounds like you" or "draws like you" is a human check; a score cannot say. A model can also memorize its training clips instead of generalizing, and it needs enough clean data of your own.
- *Responsibility.* A voice or likeness model can be used to impersonate and defraud. Train only on your own voice and work, or with written consent; say when a voice or image is synthetic; guard the weights like a password; do not train a drawing model on other artists' work without permission.

**Exam traps (as plausible claims).**

- "To make a model write or draw in your style you must fine-tune it": a reference or examples may be enough; fine-tuning is for a stable, repeated style.
- "A voice model trained on a person's recordings can be used freely": consent and disclosure still apply.
- "If the output sounds like me, the fine-tune worked": that is a human check, and it does not show the model generalizes beyond its training clips.
- "Fine-tuning on your writing teaches the model facts about you": it teaches manner, not reliable facts (entry 21).

**Unchecked:** general knowledge, not a source read in this session; no amount of data or training time is claimed.

## 25. System prompts and fine-tuning: why the video's training has none

**Bear's words (closely paraphrased), 2026-11-04.** Watching the Hugging Face fine-tuning video, he sees an input and an output on a small model, and no system prompt.

**Claude's answer (not yet signed off).** He is right, and the reason is worth teaching.

- *What the video trains.* T5-small is an encoder-decoder text-to-text model. Each training example is a pair: input text (the dialogue, with the prefix "summarize: " in front) and target text (the human summary). There are no roles, no chat template and no system prompt. The prefix is part of the input: a tiny instruction T5 already knew from its multi-task pretraining.
- *What a system prompt is.* In a chat model it is text at the start of the conversation, marked with a "system" role, which the model learned during post-training to treat as standing instructions. It is not a separate protected channel: it is text in the context window, which is why injected text can compete with it.
- *Fine-tuning a chat model.* The examples are written as role-tagged messages (with a system prompt or without), run through the model's chat template. The loss is usually computed on the assistant's reply only, not on the prompt (the same idea as the video's -100 masking of padding, for a different reason). Train with the system prompt you will use at run time, or deliberately without one; a mismatch between training and use is a common cause of surprises.
- *Two customization routes compared.* A system prompt changes the prompt object: instant, visible, reversible, but it costs context on every call. Fine-tuning changes the weights: the behavior is built in, so the standing instruction can be shorter or dropped, but it is harder to inspect and undo. In the video the behavior (summarize dialogues) is taught by examples, so no instruction is needed.
- *A comparison for students.* A base chat model with a system prompt that says what to do, against a tuned model with no system prompt, on the same held-out inputs. If the prompt does as well, fine-tuning was not needed (the ladder in entry 21).

**Exam traps (as plausible claims).**

- "Every fine-tuned model is trained with a system prompt": only chat-style models use roles; T5 has none.
- "A system prompt is a separate, protected channel": it is text in the context that the model learned to weigh.
- "Fine-tuning removes the need to test a prompt first": compare the cheap route first.
- "The summarize: prefix in T5 is a system prompt": it is part of the input, learned from T5's multi-task training.

**Unchecked:** general knowledge; the video's code was not seen; the loss-masking practice is stated in general terms.

## 26. The Hugging Face CLI, a coding agent, and Hugging Face's MCP server

**Bear's words (closely paraphrased), 2026-11-04.** Hugging Face has a CLI: how is that different, and why use it instead of just Claude Code or Codex? Does Hugging Face have an MCP?

**Claude's answer (not yet signed off).** Facts read from Hugging Face's documentation and repository on 2026-11-04.

**CLI versus agent: different layers.**

- The `hf` command is a deterministic program from Hugging Face. It does fixed jobs on the Hub: log in, download and upload models and datasets, create and manage repositories and Spaces, set Space secrets, manage the local cache, and run jobs on Hugging Face's infrastructure. It does exactly what you type and cannot write training code.
- Claude Code and Codex are agents: they decide which steps to take, write the training script, run commands and explain the result. An agent can run the CLI. The CLI is the hands; the agent is the one deciding.
- *Why use the CLI instead of only the agent.* (1) It is the official client: resumable downloads, caching and checks, instead of improvised web code. (2) Tokens: `hf auth login` logs in through your browser, so the secret never passes through the agent's chat; its docs even describe an agent mode where the agent relays a code for you to approve in the browser. (3) Narrow permission: you can let the agent run `hf download` and `hf upload` rather than arbitrary scripts. (4) The cluster: download where there is internet, run offline later, push from where you are logged in. (5) Cost: a fixed command needs no reasoning.
- Hugging Face publishes an agent skill (`hf skills add`) so agents such as Claude Code and Codex know how to drive the CLI.

**Does Hugging Face have an MCP server? Yes, an official one.**

- Documented in the Hub docs ("Hugging Face MCP Server"); the code is in the `huggingface/hf-mcp-server` repository (MIT licence, last push 2026-11-04). You open the MCP settings page while logged in and copy the configuration it generates for your client.
- *What it can do:* search models, datasets, Spaces and papers; search Hugging Face's documentation in natural language; and, as optional tools you switch on, create repositories and write files, use sandboxes, and run and schedule jobs on Hugging Face infrastructure. It can also expose community Spaces that publish a Gradio MCP tool.
- The docs list Codex, Cursor, VS Code extensions, Zed, ChatGPT and Claude Desktop as clients. Claude Code was not tested here.
- *Cautions.* Tools that create repositories, run jobs or use sandboxes need your login and can change things. Community Spaces are third-party services, and tool descriptions are the server's own claims. What the generated configuration contains was not checked: if it includes a token, it is a secret.

**CLI or MCP for this course.** They overlap. The CLI and the plain Hub API need no extra trust and work in a shell, which suits the laptop and the cluster; the MCP server adds search and documentation lookup inside the agent, at the cost of tool descriptions in the context and one more connection to trust. The starter-model prompt used the plain search API and could be run through the MCP server instead.

**Exam traps (as plausible claims).**

- "The Hugging Face CLI and Claude Code do the same job": the CLI is a fixed tool; the agent decides and writes code.
- "An agent needs your token pasted in to use the Hub": the browser login keeps it out of the chat.
- "A source with an MCP server is trustworthy": the connection is a person's decision; the tool list is the server's claim.
- "Only newspapers lack MCP servers": platforms such as Hugging Face have an official one; check each source.

**Unchecked:** the MCP tool names; Claude Code as a client; the contents of the generated configuration; costs of Jobs.

## 27. Epochs and training curves: when has training ended, and did it ever start?

**Bear's words (closely paraphrased, dictation fixed), 2026-11-04.** We are going to talk about epochs and training curves. How do we know when training has ended? How do we know whether training never even really started? Once the video is open, we will go back to that. (Dictation wrote "trending"; read as "training".)

**Claude's answer (not yet signed off).**

- *Words.* A step is one update on one batch. An epoch is one full pass through the training data, so steps per epoch is the number of training examples divided by the batch size. Fine-tuning usually runs one to three epochs, because the model already knows a lot.
- *The curves.* Training loss against steps (noisy, so smooth it) and validation loss measured at each epoch on examples never used to update the weights. Two curves, not one.
- *Shapes.* **Healthy:** training loss falls steeply, then slowly, and validation loss falls with it. **Ended:** both flatten. **Overfitting:** training loss keeps falling while validation loss flattens, then rises; stop at the validation minimum and keep that checkpoint. **Never started:** the loss sits at its starting value from step zero. **Diverged:** the loss rises or becomes not-a-number (often a learning rate too high). **Loss fell but the outputs are bad:** the loss is not the goal (chapter 9: a lower loss supports one claim of three).
- *When has it ended?* Decide in the gate, before training: a fixed budget (so many epochs) or early stopping (stop when validation loss has not improved for a stated number of checks, keep the best checkpoint). A flat training loss alone does not say "done". Never use the test examples to decide when to stop, and log any change to the rule.
- *Did it ever start?* Check: (1) the loss at step zero against the loss after a few tens of steps; (2) whether any weight actually changed; (3) whether the model can overfit one small batch, which any working setup can do; (4) the gradients are not zero and the learning-rate schedule is not stuck at zero; (5) the labels are not all masked; (6) the outputs on one fixed example differ before and after. Common causes of a run that never started: a learning rate of zero or a warmup that never ends, frozen weights, an optimizer not given the parameters, a missing update step, all labels masked, inputs not paired with their targets.
- *Chapter 9 link.* The toy starts at zero parameters, where every probability is one-half and the loss is minus the log of one-half, 0.6931. If after 200 steps the loss is still 0.693 and the weight is still zero, training never started. The reference history holds only two numbers, the first and the last, which is not a learning curve.
- *The video.* Its progress bar counts steps, but it shows no validation loss and no curve, so it cannot tell you whether training ended or ever started. Its only evidence is the base and tuned outputs on one example.

**Exam traps (as plausible claims).**

- "If the loss stopped falling, training ended successfully": a plateau can mean a bug or a learning rate that is too small; check validation and outputs.
- "More epochs always improve the model": past a point the model memorizes the training set.
- "A falling training loss shows the model generalizes": it is measured on the training examples.
- "A flat loss from the first step means the model already knew the task": it may never have started.
- "Training and validation loss should be equal": validation is usually higher; the gap is what to watch.

**Unchecked:** general knowledge; "one to three epochs" is a common practice, not a source read; the starting loss of T5-small on this task has not been measured (the dry run will record it).

## 28. Hyperparameters: the important ones, and how we optimize them

**Bear's words (closely paraphrased), 2026-11-04.** Talk about hyperparameters, the important ones in training these kinds of models, and how we optimize them. "These are just notes for you now. We're going to talk about..." (the message was cut off; ask what comes next).

**Claude's answer (not yet signed off).**

**What a hyperparameter is.** The weights are *parameters*: training learns them by gradient descent. A *hyperparameter* is a setting you choose that controls how training runs, and the gradient does not update it. Chapter 9's deck says it directly: the learning rate and the step budget are settings of the experiment, not learned parameters. Keep these apart from the run-time generation settings (temperature, beam count, maximum length), which also matter when you evaluate and must be held fixed across conditions.

**The important ones for fine-tuning a model like T5-small or a chat model.**

1. **Learning rate**, the most important. The size of each update. Too high: the loss jumps or turns into not-a-number, or the model forgets what it knew. Too low: it crawls or looks as if it never started. Fine-tuning uses small values. Usually paired with a **schedule**: a short warmup, then a decay.
2. **Batch size** (and gradient accumulation, which fakes a bigger batch). It sets how noisy each update is, how much memory you need and how fast you run, and it interacts with the learning rate.
3. **Epochs or steps**, the budget, plus an **early-stopping** rule (how many checks without improvement before stopping).
4. **Optimizer settings**: which optimizer (AdamW is common), weight decay, and gradient clipping, which caps how big one update can be.
5. **Regularization**: dropout and weight decay, which guard against memorizing.
6. **Sequence lengths and truncation**: how much of each input and target the model sees. This changes both quality and cost.
7. **Numeric precision** (full, half or bfloat16): memory and stability.
8. **The random seed.** Not a quality dial, but results vary between seeds.
9. **For lightweight adapters such as LoRA**: the rank, the scaling factor and which layers are trained.
10. **Data choices that act like hyperparameters**: how much data, the prompt or prefix format, how the validation split is drawn.

A handful of these (learning rate, epochs, batch size, and the adapter rank if you use one) usually matter most, and the learning rate first.

**How we optimize them.**

- *The rule.* Tune on **development** data (the validation split), never on the held-out test set. Every time a choice is made by looking at a set, that set becomes development data (chapter 9, slide 18). Report the test result once, after every choice is fixed.
- *By hand, one dial at a time.* Start from the model card's or the library's defaults, then change one setting and hold the rest fixed. That is the one-object test applied to settings.
- *Grid search.* Try every combination from a short list. Simple, and the cost grows fast with the number of dials.
- *Random search.* Sample settings at random within ranges. For the same number of trials it often finds good settings with fewer wasted runs than a grid, because only a few dials matter.
- *Smarter search.* Bayesian optimization, and tools that run sweeps (names such as Optuna, Ray Tune and Weights & Biases sweeps, not checked here). Methods that **stop bad trials early** by watching the training curve save most of the compute.
- *A learning-rate range test.* Run a short job while raising the learning rate, and pick the range where the loss falls fastest, just below where it blows up.
- *Tune small, then scale.* Search on a small model or a subset, then carry the settings to the big run, and check they still hold.
- *Respect noise.* If two settings differ by less than the difference between two seeds of the same setting, the difference means nothing. Run each promising setting more than once if you can afford it.
- *Keep every trial.* Chapter 9 (slide 15): hold the data and initial parameters fixed, keep every result including the bad ones, and fix the evaluation criterion before looking for the most attractive run. Otherwise a comparison becomes a search, and a lucky run gets reported as a finding.
- *Agents can run sweeps.* Give a coding agent a budget (number of trials, time), a log file and the rule above; a sweep that peeks at the test set is an overclaim.

**The video.** It uses the defaults and changes only the number of epochs ("nothing special besides that epoch adjustment"), and says that is where you start tweaking as you go deeper. It shows no sweep and no validation score, so it cannot say that its settings are good.

**Exam traps (as plausible claims).**

- "Hyperparameters are learned from the data by gradient descent": they are chosen; the gradient updates the parameters.
- "Pick the settings with the best test score": choose on validation and use the test set once.
- "A higher learning rate just trains faster": it can destabilize training or erase what the model knew.
- "More epochs always improve the model": past a point the model memorizes.
- "Grid search is the most reliable way to tune": random search often does as well with fewer trials.
- "A setting that scores 0.3 points higher is better": that may be less than the seed-to-seed noise.
- "Batch size changes only the speed": it also changes the noise of each update and interacts with the learning rate.

**Unchecked:** general knowledge, not a source read in this session; no numeric ranges are given because none was checked; the tool names are examples only. The dry run uses fixed settings from its gate and does no search.

## 29. Checkpoints, and visualizing results so we know early whether training is working

**Bear's words (closely paraphrased), 2026-11-04.** In the video there are no checkpoints. He is not training for very long, which may be why. We still need to discuss checkpoints. We also need to discuss visualizing the results so we know early on whether training is working or not working: at each checkpoint, is there an improvement?

**Claude's answer (not yet signed off).**

**What a checkpoint is.** A saved snapshot of a training run. A *weights-only* checkpoint is enough to use the model. A *full* checkpoint also holds what is needed to resume the run: the optimizer's state, the learning-rate schedule's position, the step count and the random-number state. Resuming from weights alone is not the same as resuming the run. As arithmetic (not measured): an optimizer such as Adam keeps two extra numbers per weight, so a full checkpoint can take about three times the space of the weights alone.

**Why take them.**

1. *Recovery.* A crash, a power cut, or a cluster job that hits its time limit loses the whole run without one. This matters for the cluster plan: jobs have a wall-clock limit, so long runs must save and resume.
2. *Keeping the best.* The best model by validation score is often not the last one (overfitting, entry 27). Keep the best checkpoint and the last few, not every one.
3. *Analysis.* Comparing checkpoints shows when the model started to improve, plateau or overfit.
4. *Branching.* You can try different settings from a checkpoint instead of starting over (entry 28).

**How often.** At the end of each epoch, or every fixed number of steps. More often costs disk and time; fewer risks losing work. Set how many to keep.

**The video.** It saves no checkpoints and pushes only the final model. Because the run is a few minutes long, restarting is cheap, so that is acceptable. It also has no validation, so it could not pick a best checkpoint anyway. Any run longer than a coffee break, or on the cluster, needs them.

**Visualizing, so you know early whether it is working.**

1. *Loss curves.* Training loss against steps and validation loss at each checkpoint: the early warning for never started, diverged and overfitting (entry 27).
2. *A fixed panel at every checkpoint.* The same small validation sample and the same three to five fixed examples, run with the same generation settings each time. Record the score on the sample, and put the example outputs side by side across checkpoints so you can read the model getting better or worse.
3. *Cheap symptom checks on the outputs.* Average output length, how often the output is empty, repeats itself or just copies the input. A model can lower its loss and still produce worse text.
4. *A checkpoint table.* Checkpoint, step, training loss, validation loss, score, flag the best. "Improvement" should be defined in the gate before the run: for example, validation loss falls and the score on the fixed sample rises.
5. *Tools.* A spreadsheet or a plain log file and a small plot are enough. Experiment trackers (TensorBoard, Weights & Biases, Hugging Face's Trackio) draw the curves live; those are examples only.
6. *Voice and image models.* The only real check is to listen or look at the same fixed prompts, with fixed random seeds, at each checkpoint (entry 24).

**Rules of thumb.** Look early: by a fifth or so of the run the loss should be moving, and if the first checkpoint looks identical to the start, stop and debug instead of waiting. A difference smaller than the seed-to-seed noise is not an improvement, and a small sample is noisy. Loss and the score can disagree; read the text. Do not use the test examples for this.

**How many checkpoints do we take, and how many do we keep?** (Bear's follow-up was cut off after "how many checkpoints do we"; read as take and keep. Ask if he meant something else.) Separate three numbers: how often you *evaluate*, how often you *save*, and how many you *keep*. Decide them from five things.

1. *The cost of lost work.* Saving costs time and disk; not saving risks redoing the run. Choose the interval so a failure loses an amount of work you can accept, say a few percent of the run. High-performance computing has a classic rule for the best interval, which grows with the time to write a checkpoint and the expected time between failures (the Young and Daly estimates; general knowledge, not checked here). A cluster job also has a time limit, so at least one checkpoint must land before it.
2. *Run length.* A run of a few minutes needs at most the final model. A run of an hour or more needs checkpoints; on the cluster, every 30 to 60 minutes or every fixed number of steps is common.
3. *What you want to see.* To draw a curve and spot a plateau or overfitting you need roughly ten or more evaluation points across the run. Evaluating is cheap on a small fixed sample, so evaluate more often than you save. Look more often early on, to catch a run that never started.
4. *Disk.* Size times count. As arithmetic (not measured): at about 12 bytes per weight for a full checkpoint (4 for the weight, 8 for Adam's two extra numbers), T5-small is about 0.7 GB, so ten checkpoints are about 7 GB; a 1.7-billion-parameter model is about 20 GB each, so ten would fill a shared project quota. Keep the last two or three and the best by validation, and delete the rest.
5. *The risk of picking a lucky one.* The more checkpoints you compare on the same validation set, the more likely you pick one that is high by noise. Do not choose among checkpoints whose scores differ by less than the noise; prefer the start of the plateau, or average the last few; report the test set once.

*A starting recipe.* Evaluate every epoch (or every tenth of the run) on a fixed small sample; save at the same points; keep the last two plus the best; write the interval and the keep-count in the gate before you run; after the first run, adjust: save more often if runs are long or fail, keep fewer if disk is tight, save inside an epoch if one epoch takes hours. For the assignment's T5-small run of one to three epochs: a checkpoint before training and one per epoch, and keep them all because they are small.

**Chapter 9 link.** The reference run's history holds two numbers, which is not a curve; the stop rule is a design decision; keep every result; a lower loss supports one claim of three.

**Exam traps (as plausible claims).**

- "A checkpoint is the final trained model": it is a snapshot at any point, and a full one includes the optimizer and schedule state.
- "Always keep the last checkpoint": the best by validation may be an earlier one.
- "Training loss is lower at checkpoint 3 than checkpoint 2, so the model improved": that is measured on training examples; check validation and the outputs.
- "Plots are for presentations": they are an early-warning tool.
- "A short run needs no curves": it may not need checkpoints, but it still needs a curve.
- "Resuming from saved weights continues the run exactly": the optimizer and schedule state matter.
- "More checkpoints are always safer": they cost time and disk, and comparing many on one validation set invites picking a lucky one.
- "Choose the number of checkpoints by how many fit on disk": choose by the cost of lost work and by what you need to see; disk limits how many you keep.
- "You only evaluate when you save": evaluation can be more frequent than saving, and is cheaper.

**Unchecked:** general knowledge; the space figure is arithmetic; tool names are examples; the names of the save-related settings in Hugging Face's trainer were not checked. The dry run may add real checkpoint evidence.

## 30. A progress bar is not progress: epochs measure completion, not whether the task is working

**Bear's words (closely paraphrased), 2026-11-04.** Fundamental disagreement with what the video calls a progress bar. His "progress" is basically epochs. What we care about is the model getting better. If we are training for 30,000 epochs, we want to know within 200, 300, at most 1,000 whether our setup is doing a good job. Make a note: epochs are progress only in the sense of how far through the task you are, not whether the task is working. We do not want to run 100,000 epochs and then find we made a mistake in the setup. That is why checkpoints and visualizing them are critical. Understand how we are making real progress, meaning it is getting more accurate or the loss is falling, and why we would choose accuracy versus loss over "it's still running." The analogy: a taskbar that just rolls around and sits there, and you do not know what it is ending; that is what the video calls progress. Progress is not being X of the way through the job; progress is the job working.

**Claude's answer (not yet signed off).**

**Two different things.**

- *The bar* (step 10 of 1,300, epoch 2 of 3) measures **completion**: how much of the planned work has been done, and from that how long is left. It answers "how far along is the schedule?" It would read exactly the same on a run that is learning nothing.
- *Progress* is evidence that **the job is working**: the validation loss falls, the score on held-out examples rises, the outputs get better. It answers "is this run heading where we want?"
- *The analogies.* A spinner that rolls around says only "still running". A counter with a number is a spinner with a number on it. An odometer tells you how far you have driven, not whether you are on the right road. A kitchen timer says how long the soup has cooked; only tasting says whether it is working.

**Why the distinction matters: cost.** A setup mistake (wrong labels, a masked target, a learning rate that is too low or too high, the wrong split, frozen weights) costs the entire run if nobody looks until the end. If a check at 1% of the run exposes it, 99% of the cost is saved. So plan **an early go or no-go check** inside the first few hundred to few thousand epochs of a long run (or the first few percent, whichever comes first), and write it in the gate before the run: *by step N the validation loss must be below X, and the first checkpoint's outputs must differ from the start in the intended direction; otherwise stop and look for the setup mistake.* The unit can be epochs or steps; the principle is the same. The early check catches gross failures (never started, diverged, wrong data). Subtle problems such as overfitting show only later, so keep watching after it passes.

**What to look at in that early window.** (1) The loss at step zero is sensible, and then it moves (entry 27). (2) The model can overfit one small batch; run that check before the big run. (3) The validation loss and a task score on a fixed sample, compared with a **baseline** (the untrained model, a majority-class guess, or the base model with its prompt). A score is only progress relative to something. (4) The same few example outputs at each checkpoint, read by a person (entry 29).

**Loss versus accuracy (or another task score): why choose one, and why look at both.**

| | Loss | Accuracy or task score |
|---|---|---|
| What it measures | The objective the optimizer is lowering | What you actually want the model to do |
| Answers | "Is the optimizer working? Is the setup mechanically sound?" | "Is the task being done well enough to be useful?" |
| Strengths | Smooth, cheap, available every step, moves early and reveals trouble fast | Meaningful to people; the thing you will be judged on |
| Weaknesses | Not the task: it can fall while behavior stays wrong; its scale means little across tasks; confident mistakes dominate it | Coarse and jumpy; can sit at its starting value while the loss improves; slower to compute (generating text); a poor choice can mislead (a model that always says "no" is 99% accurate when 99% of cases are "no") |
| Best use | The early warning and the stability check | The test of whether the run succeeded |

So watch the loss for a fast, cheap signal that the setup is sound, and watch the task score and the outputs to learn whether the job is working. Choose the task score in the gate to fit the task (accuracy, a better-suited measure for lopsided data, an overlap score for summaries, a person reading examples for voice or images). Both must be measured on **validation** data, never only on the examples being trained on. "Still running" is neither.

**Chapter 9 link.** The deck's reference run records only the first and the last loss, which is not a learning curve; the stop rule is a design decision; lower loss supports one claim out of three; and a lower loss can sit beside the wrong behavior.

**The video.** Its attention is on the progress bar ("what we really care about is down here where we see this progress bar"). The bar shows how many steps remain, not whether the model is improving, and the run has no validation score, so it gives no evidence that the setup works.

**Exam traps (as plausible claims).**

- "The progress bar shows how well training is going": it shows how much of the schedule is done.
- "If the run is at epoch 90% the model must be nearly trained": the loss may not have moved.
- "Wait for the run to finish, then evaluate": a setup mistake can be found at 1% instead.
- "Falling training loss means the task is working": loss is the objective, measured on training data; check a held-out score and the outputs.
- "Accuracy is always the better thing to watch": it is coarse, late and can mislead on lopsided data; use it with the loss.
- "A task score of 90% is good progress": only compared with a baseline.

**Unchecked:** general knowledge; the 1% rule and the 200 to 1,000 epoch window are Bear's illustration of the principle, not measurements; real fine-tuning runs are usually a few epochs, so count steps there. The dry run gives real early-window numbers for one small case.

## 31. Three ways to work with Hugging Face: the Python library, the CLI and the MCP server (and why each)

**Bear's words (closely paraphrased), 2026-11-04.** He pasted a long write-up on talking to Hugging Face from Claude Code and Codex (the `hf` CLI and its agent skill, the official MCP server, and the Python library). We need a video on these options: why would you use a CLI, and why would we use the MCP? He assumes we can install Hugging Face as a Python library, locally or on the cluster, for training, and asks to be corrected if wrong. And the MCP would only be needed if we wanted to train on Hugging Face: is that true?

**Claude's answer (not yet signed off).**

**His assumption about the library is right.** "Hugging Face" means three different things: (1) the **Hub**, the website that hosts models and datasets; (2) the **libraries** (`transformers`, `datasets`, `accelerate`, `huggingface_hub`, and `peft` or `trl` for adapters and chat models), which are ordinary Python packages; (3) hosted **services** (Jobs, Spaces, Inference Endpoints). Training is done by the libraries, on whatever machine runs your Python: a laptop or the cluster. The dry run did exactly this, with no CLI, no MCP and no login; the Hub was only used to download the base model and the dataset.

**The second assumption is not quite right.** The MCP server is not about training. It is how an *agent* talks to the Hub: search models, datasets, Spaces and papers; search the documentation; and, as optional tools, create repositories and write files, use sandboxes, and run jobs on Hugging Face's machines. Training on Hugging Face's own machines does not need the MCP either: the CLI (`hf jobs run`) and the Python library can launch jobs too. The MCP's "run jobs" tool is one convenience among several.

| Door | What it is | Why use it | Why not |
|---|---|---|---|
| **Python libraries** | Code that runs inside your project | Do the actual work (training, evaluation) on a laptop or cluster; pinned versions; reproducible | They are the work, not an interface for an agent |
| **`hf` CLI (+ agent skill)** | A fixed command-line tool for Hub chores | Log in (browser flow, token stays out of the chat), download, upload, cache, jobs; exact, cheap, easy to give narrow permission; fits download-first-then-offline on a cluster | It cannot search by meaning or call Spaces as tools |
| **MCP server** | A hosted tool server the agent connects to | Clients with no shell (claude.ai, Claude Desktop); semantic search of papers, Spaces and docs; Spaces as tools | Tool descriptions cost context; community Spaces are third-party code feeding the model (prompt-injection surface); a token in the config is stored in plain text |

*For Claude Code or Codex*, which have a shell: start with the library for the work and the CLI for Hub chores, and add the MCP only for what the CLI does badly (meaning-based search, Spaces as tools). All three call the same Hub underneath.

**Checked against Hugging Face's own pages today:** the `hf` CLI is current (the old `huggingface-cli` name is the old one); the standalone installer adds the CLI's agent skill, and `hf skills add --global` adds it by hand after a pip or Homebrew install; the skill is generated from the installed CLI version, so it goes stale; the MCP server is at `huggingface.co/mcp`; its README gives `claude mcp add hf-mcp-server -t http https://huggingface.co/mcp?login` (browser login) and a token-header alternative; built-in tool groups include search, documentation search, repositories, sandboxes and jobs. **Not checked here:** the installer's web address and the Homebrew name in the write-up, the Codex commands and the Codex sandbox network setting, and `hf update`.

**Two places the write-up differs from our course advice.** It tells you to paste a token at `hf auth login`; the documentation says the login uses the browser by default, which is what the course teaches. It suggests allowing `Bash(hf:*)` in Claude Code, which allows every `hf` command including deletes and writes; allow narrow ones instead (such as `hf download`). Its warning that a header token is written into the config in plain text supports the course's token rules.

**For the film (Bear: "we need a video on these options").** Beats: (1) three meanings of "Hugging Face": the Hub, the libraries, the hosted services; (2) training runs on libraries, on your own laptop or cluster, no login needed (the dry run); (3) the CLI: why a fixed tool beats an agent improvising, and how the browser login keeps the token out of the chat; (4) the MCP: what it adds (search by meaning, Spaces as tools, clients without a shell) and what it costs (context, third-party tools, tokens in config); (5) the choice by situation, with the token-safety rules; (6) the starter-model prompt as the worked example of finding a model. Whether this is the same film that carries the starter-model prompt is to be confirmed.

**Exam traps (as plausible claims).**

- "The MCP server is how you train a model on Hugging Face": training is done by the libraries or a job; the MCP is an agent's interface to the Hub.
- "You must log in to Hugging Face to train a model": downloading public models and datasets and training need no login; publishing does.
- "The CLI and the MCP server do different jobs on different systems": they call the same Hub; they differ in who uses them and how.
- "An MCP server is always better than a command-line tool": for an agent with a shell, the CLI is simpler and needs no extra trust.
- "Allowing every command of a tool is fine if the tool is official": a write or delete command can still do damage; allow narrowly.
- "The `hf` command trains the model": it does Hub chores (login, download, upload, repositories, cache) and can launch a paid Job, but the training itself is your own script using PyTorch and the libraries.

**Follow-up (Bear, 2026-11-04): Spaces with the MCP for a limited GPU, buying compute, the cluster, and uploading.** Bear's understanding: Spaces with the MCP are good if you use Hugging Face's limited GPU; you can buy compute there (he thinks that is their business model); on the cluster he can install the CLI and run with Python, PyTorch and the other dependencies Hugging Face probably brings; and he would use the MCP to upload a trained model once he felt it was worth uploading. Claude's answer (not yet signed off), checked against Hugging Face's documentation and the dry-run environment:

- *Spaces and the MCP: right, for calling, not for training.* Any Gradio Space can be exposed as an MCP tool, and the docs list "Spaces as MCP servers" and "Spaces as agent tools". ZeroGPU gives Spaces shared GPUs, allocated and released dynamically, as a free option. That suits an agent calling a model (transcribe this audio, make this image). Spaces host apps and demos; they are not where you run a long training. ZeroGPU's limits were not checked.
- *Buying compute: yes.* Hugging Face Jobs run a command in a Docker image on a chosen hardware flavor (CPU, GPU or TPU). They are pay-as-you-go by the second and need a positive credit balance, and you launch them with `hf jobs run` or the Python library; the MCP is optional. A Space can also be upgraded to a GPU in its settings, and the docs list Inference Endpoints and subscription and enterprise plans. Prices are on the Jobs pricing page and change; check it. Which product earns most is not known here.
- *The cluster: yes you can train there, but the CLI is not what trains, and PyTorch is not a Hugging Face dependency.* You run your Python script with PyTorch and the libraries; the `hf` command is installed with the `huggingface_hub` package and is optional there (login, download, upload). In the dry-run environment, `huggingface_hub`, `transformers`, `datasets`, `tokenizers` and `sentencepiece` do not require PyTorch; `accelerate` does (and, as I understand it, `peft` and `trl` pull it in through `accelerate`). Install a PyTorch build that matches the cluster's GPUs, separately and pinned. (My notes call the cluster Explorer; if Discovery is its older name, the same applies.)
- *Uploading: the decision is right, the mechanism is not the MCP.* Whether the model is worth publishing is a human decision at the sign-off (chapter 9). To move the weights, use `hf upload` or the library's `push_to_hub`, which handle large files and resume. The MCP's optional write tool creates repositories and writes files, which suits a model card; I did not check how it handles large binary files, and a hosted MCP server cannot see files that sit on the cluster unless the agent reads them and passes them along. Uploading needs a write token, so log in by browser only at this step (the course token rules).
- *Add to the film:* a beat on buying compute (Jobs and Space upgrades) and when you would not need it.

**Exam traps (as plausible claims), addendum.**

- "PyTorch comes with the Hugging Face libraries": mostly not; install it separately.
- "The MCP server is the way to upload model weights": use the CLI or the library.
- "ZeroGPU Spaces are for long training runs": they are for apps and demos.
- "Training on Hugging Face's machines requires the MCP server": a Job launched from the CLI or library does it.
- "Hugging Face's services are all free": compute, upgrades and endpoints are paid.

**Unchecked:** as listed above; the pasted write-up's source is unknown; ZeroGPU's quotas and time limits; the MCP write tool's file-size limits; current prices; whether `peft` and `trl` require PyTorch (general knowledge).

**Second check of the write-up (Bear pasted it again, with no message, on 2026-11-04), against Hugging Face's own docs and the MCP server's README.**

- *Confirmed:* the standalone installer adds the CLI's agent skill and an install by pip or Homebrew does not; `hf skills add --global` (all projects) or `hf skills add` (this project) adds it by hand, and works for Claude Code, Codex, Cursor and others that read `~/.agents/skills`; the skill is generated from the installed CLI version and goes stale; `hf update` and `hf skills update -g` refresh it; the "Dynamic Spaces" option exists in the MCP settings and lets the assistant discover and use MCP Spaces at runtime; the Claude Code command for the MCP server (`claude mcp add ... -t http https://huggingface.co/mcp?login`) is in the server's README.
- *A discrepancy:* the write-up gives the Claude Code plugin as `hf-cli@huggingface/skills`; Hugging Face's page says `hf-cli@huggingface-skills` (a hyphen, not a slash).
- *Still not confirmed:* the installer's web address (the docs I read name the installer but give no address, so do not pipe an address from a pasted document into a shell without reading the script first), the Codex commands, the Codex sandbox network setting, and the bearer-token environment variable for Codex.
- *Risks in the write-up to keep in mind:* piping a downloaded script into a shell; allowing every `hf` command (`Bash(hf:*)`), which includes writes and deletes; turning on network access in the Codex sandbox, which weakens it; and the header-token form of the MCP command, which stores the token in plain text.

## 32. Why build this at all: the portfolio

**Bear's words (closely paraphrased), 2026-11-04.** This is mainly for the portfolio, which is something people should do.

**Claude's answer (not yet signed off).** A fine-tuned model on your own Hugging Face page is a portfolio piece that a reader can open and judge. What makes it a good one is the evidence, not the score: the gate written before the run, the loss curves, the held-out table against a baseline, three example outputs (including one that failed), an honest list of limits, the licences, and a model card that puts that on the front page. Claims should be the ones the evidence earns ("lowered the objective", "learned", not "works" or "generalizes" unless shown). A static Space (free, per Hugging Face's documentation) can hold a one-page write-up; a demo that runs the model needs hardware that a free account may not get. Keep tokens, personal data and the dataset itself out of anything public, and respect the dataset's non-commercial licence. Public is what a portfolio needs; private still shows a grader the work. This ties to entry 6, where Bear suggested building something as a final project because it makes a good portfolio piece when job hunting.

**Exam traps (as plausible claims).**

- "A portfolio piece is judged by its score": it is judged by whether the claims match the evidence.
- "A private model page counts as a portfolio": nobody else can see it.
- "Publishing a model is safe because I wrote the training code": the dataset's licence, personal data and secrets still apply.

**Unchecked:** the static Space claim is from Hugging Face's documentation read today; no portfolio was built or reviewed.

## 33. Before a serious cluster job: LoRA, QLoRA and quantization

**Bear's words (closely paraphrased), 2026-11-04.** He pasted the transcript of a video on LoRA and QLoRA (by Mark Hennings of Entry Point AI). Before running a big job, a serious job on the cluster, we want to talk a little about LoRA, QLoRA and quantization.

**Claude's answer (not yet signed off).** The abstracts of the two papers (LoRA, 2021; QLoRA, 2023) were read on arXiv today; the rest is general knowledge, and the arithmetic is mine.

**The problem.** Full fine-tuning updates every weight, so the memory has to hold the weights, their gradients and the optimizer's extra numbers. As arithmetic (not measured), a common setup needs roughly 12 to 16 bytes per weight, so a 7-billion-parameter model needs on the order of 84 to 112 GB: more than a single 80 GB GPU. That is why big models are not fine-tuned fully on small hardware. (The video places fine-tuning after pretraining: instruction tuning, safety tuning, then domain or task tuning; entry 20.)

**LoRA (low-rank adaptation).** Freeze the pretrained weights. For chosen layers, learn the *change* as the product of two small matrices of rank r, and compute with the original weight plus a scaled copy of that product. Only the two small matrices get gradients and optimizer state. The paper says this cuts the trainable parameters by 10,000 times and the GPU memory by 3 times for GPT-3 175B against fine-tuning with Adam, matches or beats fine-tuning on the models it tested, and adds no inference latency (the product can be merged into the weight). Toy arithmetic from the video: a 5 by 5 weight has 25 numbers; two rank-1 factors have 5 + 5 = 10. For a 4,096 by 4,096 layer at rank 8, about 65 thousand numbers against about 16.8 million (under 0.4%). The base model still has to be loaded, so LoRA saves the gradient and optimizer memory, not the weights themselves. The result is a small adapter file kept apart from the base model; you can keep one adapter per task.

**Quantization.** Storing each number with fewer bits: 16, 8 or 4. Memory is about the number of parameters times the bits divided by eight: a 7-billion-parameter model is about 14 GB at 16 bits, 7 GB at 8 bits and 3.5 GB at 4 bits (arithmetic). It is lossy: the rounding error stays. It is used to run big models on small hardware, and, in QLoRA, to hold the frozen base model.

**QLoRA.** LoRA on top of a 4-bit base model. The paper's abstract: gradients flow through a frozen 4-bit quantized model into the LoRA adapters, using a 4-bit data type suited to bell-curve-shaped weights (NormalFloat, NF4), double quantization (quantizing the quantization constants) and paged optimizers for memory spikes. It reports fine-tuning a 65-billion-parameter model on a single 48 GB GPU while preserving 16-bit fine-tuning task performance. The adapters stay in higher precision; the 4-bit weights are converted for each computation.

**The hyperparameters in the video** (the speaker's reading of the QLoRA paper, not checked in the paper itself).

- *Which layers.* Adapters on all the linear layers of the transformer blocks were needed to match full fine-tuning.
- *Rank r.* Seemed not to matter between 8 and 256 once all layers are adapted (QLoRA used 64); the speaker notes that complex behavior, or behavior that contradicts the base model's training, may need a higher rank.
- *Alpha.* A scale on the update, applied as alpha divided by r. QLoRA used alpha 16 with r 64, so a factor of one quarter. It overlaps with the learning rate, which the paper's authors suggest leaving fixed.
- *Dropout.* 0.1 for the 7B and 13B models and 0.05 for the larger ones, to guard against overfitting.
- *Learning rate, batch size* as in entry 28. The speaker's own advice: there are no hard rules; start from what others got good results with under similar conditions, and adjust to your data (tune on validation).

**Where the video is loose or wrong.**

1. "You are always still training all of the model's parameters": not so. LoRA freezes the original weights and trains only the small added matrices; the change it can learn is restricted to low rank.
2. "You recover the original precision": quantization is lossy. The QLoRA claim is that task performance matches 16-bit fine-tuning in its tests, not that the original numbers come back.
3. "Rank barely matters": one paper's experiments, within the range tested and on its benchmarks; not a law.
4. The percentages of trainable parameters assume one giant matrix; the speaker says so.

**Which to use.**

| Method | Base model | Trains | Use when |
|---|---|---|---|
| Full fine-tuning | 16-bit (or higher) | Every weight | The model is small (T5-small in the dry run) or the GPUs are big; best fidelity |
| LoRA | 16-bit, frozen | Small adapters | The model fits in 16 bits but full tuning does not; one adapter per task |
| QLoRA | 4-bit, frozen | Small adapters | The model barely fits, or does not fit, in 16 bits; single-GPU runs of big models |

The ladder still applies: a prompt, retrieval or tools first (entry 21).

**For the cluster.** Install `peft` (adapters), `bitsandbytes` (4-bit; built for NVIDIA GPUs, support elsewhere not checked) and `trl`, with a PyTorch matched to the GPU. Choose the GPU by memory. Adapter checkpoints are small, which makes saving often cheap (entry 29). Everything else carries over: the gate, the held-out set, the early go or no-go check, the curves, and a comparison with the base model. A LoRA run on a small model can be shown on a laptop; the 4-bit run needs an NVIDIA GPU.

**Exam traps (as plausible claims).**

- "LoRA updates all the original weights, just fewer of them": it freezes them and trains small added matrices.
- "Quantization loses nothing": it is lossy; QLoRA preserves task performance in its tests.
- "QLoRA is the same as LoRA": it adds a 4-bit quantized base model.
- "A higher rank is always better": it costs more and often matters little within the tested range.
- "LoRA makes the base model smaller": it adds an adapter; quantization shrinks the stored base.
- "Alpha is a second learning rate": it scales the adapter's contribution (alpha divided by r); it overlaps with the learning rate but is a different setting.
- "LoRA adapters slow down inference": they can be merged into the weights.

**Unchecked:** the arithmetic; the video's specific values and recommendations (rank, alpha, dropout) are the speaker's reading of the paper; the libraries' details; which of the cluster's GPUs have the memory a given model needs.

## 34. How far down can we quantize? Find out empirically (and what the QLoRA video adds)

**Bear's words (closely paraphrased), 2026-11-04.** He watched a second video (AI Bites) on QLoRA and says it is mostly quantization theory. How do we know how far down we can go in the number of bits? We always want to view these things empirically: we can try very quickly and see at what level we can... (the message was cut off; read as "go before the quality drops"; ask if he meant more).

**Claude's answer (not yet signed off).**

**What the video teaches.** Quantization rounds numbers onto a small set of levels (4 bits gives 16). If values clump or a few are extreme, different numbers land on the same level and information is lost, so *blockwise* quantization gives each block of 64 weights its own scale constant. Trained weights are roughly bell-shaped around zero, so **4-bit NormalFloat (NF4)** places its 16 levels by the normal distribution, close together near zero and far apart at the extremes, instead of evenly. **Double quantization** quantizes the constants too. **Paged optimizers** move the optimizer's state to CPU memory during a memory spike (a very long input) and back afterwards. In use, the weights are stored in 4 bits, converted to bfloat16 for each computation, and the gradients flow into the LoRA adapters (entry 33). On the tests it reports, NF4 with double quantization beat plain 4-bit floats and matched 16-bit full fine-tuning and 16-bit LoRA.

**Checked against the QLoRA paper's text today, two corrections.**

1. "LoRA needs 780 GB for a 65-billion-parameter model": the paper says *regular 16-bit fine-tuning* (all weights) needs more than 780 GB. LoRA needs far less. (The arithmetic in entry 33, 12 bytes per weight, gives 65 billion times 12 = 780 GB, which agrees.)
2. "Double quantization gains half a bit per parameter": with a block of 64 and 32-bit constants, the constants cost 0.5 bits per parameter; double quantization brings that to 0.127, a saving of **0.373** bits per parameter. The paper also says earlier quantization methods worked for inference but broke down in training; QLoRA works because the quantized base is frozen and only higher-precision adapters train.

**How far down can we go? Theory does not say; measure it.** It depends on the model (larger models are often reported to tolerate fewer bits, which I did not check here), the task, the method (block size, the data type) and how much loss you accept. Run a **bit ladder**:

1. Same model, same held-out sample, same generation settings. Change only the bits: 16, 8, 6, 5, 4, 3, 2.
2. Record the task score, a fast proxy such as the loss or perplexity on the sample, memory, and speed. Read a few outputs.
3. Plot score and memory against bits and look for the knee, where the score starts to fall.
4. **Decide the tolerance before you look** (for example, within a stated margin of the 16-bit score, larger than the run-to-run noise), and choose the lowest setting that meets it.
5. Choose on validation data; report the test set once. Check at the inputs you will really use (long ones, the languages you need), because an average can hide a failure.

Evaluating a quantized model is inference only, so a rung takes minutes. That is the point of the empirical approach: it costs a few minutes to find out, instead of arguing from theory. For QLoRA training the same question becomes: does the tuned 4-bit run match the 16-bit adapter run on held-out data? Only the bits change between runs, which is the one-object test again.

**Exam traps (as plausible claims).**

- "Theory tells you the minimum number of bits": it has to be measured for the model, task and method.
- "4-bit is always fine": it depends; test it.
- "LoRA needs 780 GB for a 65B model": that figure is for regular 16-bit fine-tuning.
- "Double quantization saves half a bit per parameter": with the paper's settings the saving is 0.373 bits.
- "NF4 spaces its levels evenly": it spaces them by the normal distribution, denser near zero.
- "A score within noise of the 16-bit score proves quantization lost nothing": it shows the loss is small on that test.
- "Quantization only saves memory": it can also change speed, depending on the hardware and software.

**Unchecked:** the claim that larger models tolerate fewer bits; the paged-optimizer setting names in the library; the video's step-by-step description beyond what the paper's text confirms.

## Topics to discuss later (Bear's list)

- **Loss versus reward** (2026-11-04). Bear: "I could note later to discuss loss versus reward and adjusting loss versus a" (the message was cut off after "versus a"; ask what he meant by the second half). Not discussed yet. Pointers for when we do: supervised fine-tuning lowers a loss on example pairs, while preference and reinforcement tuning optimize a reward (entry 20); chapter 9's gate names the objective, and the deck says the cost of each error belongs in the gate as a second objective, because a lower loss does not show the objective was the right one.
