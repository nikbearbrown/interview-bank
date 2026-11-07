# Report: new jargon sets j05, j06, j07 (written from scratch)

Counts: j05 14 MA, j06 14 MA, j07 16 MA (44 total). No old files converted, so dropped 0 and essays 0. All three pass check_format (0 problems) and the absolute-word grep on statements. True-counts per file: j05 1/5/5/3 (one/two/three/four true), j06 1/5/5/3, j07 2/5/6/3. Note: the handshake questions use the initialize / initialized model; the later stateless revision is not tested.

## Jargon test: MCP (j05)
- host :: the AI application the person runs; it creates and manages the clients
- MCP client :: the connector inside the host that holds the connection to one server
- MCP server :: the program that exposes tools, resources or prompts
- transport :: the channel that carries the messages, separate from the messages
- stdio :: transport where the client starts the server as a local child process and talks over standard input and output
- HTTP transport :: transport for a remote server reached over a network
- JSON-RPC request :: message with an id that expects a response with the same id
- JSON-RPC response :: reply carrying the request's id and either a result or an error
- notification :: one-way message with no id and no reply
- initialize :: request from the client that starts the session; the server answers with protocol version and capabilities
- initialized :: notification from the client saying it is ready for ordinary requests
- capabilities :: what each side declares it supports during the handshake
- tool :: function the model decides to call (model-controlled)
- resource :: data the application chooses to attach as context (application-controlled)
- prompt (MCP) :: reusable template the user picks (user-controlled)
- tool description :: server-written text the model reads to choose a tool; a claim, not a guarantee, and it uses context
- JSON-RPC error :: the protocol-level request failed
- isError :: flag on a tool result meaning the call ran and the tool reported a failure
- interoperability :: whether host and server can exchange messages both understand
- authorization :: whether this server and tool belong in the task; decided by a person
- discovery (tools/list) :: client asks the server what it offers at run time
- function calling :: how a model asks for a tool; something else still runs it

## Jargon test: evaluation, approval gates and governance (j06)
- test :: fixed expectation that passes or fails the same way each run
- eval :: scoring of model output quality over a set of cases, often as a rate
- benchmark :: shared fixed task set with a scoring method for comparing systems
- rubric :: criteria with descriptions of each score level
- LLM-as-judge :: a language model scoring another output against criteria; needs checking against human labels
- regression :: a change that breaks something that worked; a regression eval reruns earlier cases
- hallucination :: fluent output stating something false or unsupported as if true
- error (engineering) :: a failure the system reports, such as an exception
- groundedness :: claims supported by supplied source material, which is not the same as true
- permission :: standing rule on whether an agent may use a tool or path (allow, deny, ask)
- approval gate :: point where a person reviews and decides before the action proceeds
- human in the loop :: a person able to stop or approve before the action, not only reading afterward
- audit log :: record of who or what did what and when, for later review; it records, it does not block
- accountability :: being answerable for the outcome; stays with the person who delegates
- responsibility :: duty to do the work; can be handed to an agent
- bias :: systematic skew in outputs favouring or disadvantaging groups
- privacy :: protecting personal information about people
- data leakage :: information reaching where it should not (security sense), or test data reaching training (evaluation sense)
- red team :: group that deliberately attacks a system to find failures before users do

## Jargon test: saying it exactly to Claude Code (j07)
- diff :: lines added and removed compared with the earlier version
- diff review :: reading a diff and judging it against requirements
- commit :: recording staged changes with a message in git history (distinct from push)
- push :: sending commits to a remote
- scope :: the boundary of what a task covers
- file :: a named unit of content
- directory (folder) :: a container holding files and other directories
- test vs eval :: fixed pass/fail expectation versus scoring of varying output
- tool :: a capability the model can call
- permission :: rule governing whether a tool may be used
- memory file (CLAUDE.md) :: file of standing instructions read at the start of a session
- context :: the text currently in the model's window for this session
- subagent :: separate Claude instance with its own context window that returns a result
- hook :: command the harness runs automatically at a defined event
- slash command :: command the user invokes by typing a name starting with a slash
- checkpoint :: in Claude Code, recorded file state before an edit so it can be rewound; in training, a snapshot of weights and optimizer state
- verification :: checking against evidence confirmable apart from the producer
- acceptance criteria :: conditions for accepting a result, stated before the work
- plan mode / planning before acting :: researching without editing and presenting a plan for approval before a change
