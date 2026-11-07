# Conversion report: ch08-mcp-from-scratch (MA-ch08)

Old MA: 64. Old essays: 60. New MA: 36. Dropped or merged MA: 28 (merged into other questions or removed as non-vocabulary).
Output: /Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/info-7375-prompt-engineering-for-generative-ai/multiple-answer/ch08-mcp-from-scratch.md (check_format: 0 problems; forbidden-word grep clean apart from "read-only" hyphen matches).
True-count spread: one true 3, two true 11, three true 15, four true 7.

## Dropped or merged old MA (examples)
- Non-vocabulary (arithmetic, state-table counting): MA-ch08.12, .13, .64 (flag tables, pair counts, which-code-first).
- Merged as near-duplicates: .2/.18/.19/.20/.60 into description, tools/list and annotation questions; .5/.6/.7/.8 into initialize and lifecycle questions; .29/.30 into four-question questions; .33/.34/.37 into evidence-type questions; .44/.46/.47/.48 into the trust-laundering question; .49/.50/.51 into the discrepancies-not-verdict question; .53 and .56 (checkable condition, unspecified behavior) removed as process opinion.
- Practice-only items dropped: .16, .61 (how to test a stdio server safely), partly kept in transport and constructed-versus-live questions.

## Essays
Converted (folded into MA content): ES-1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 38 (partly), 43 (as the Claude Code rewrite question), 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 58, 59.
NOT CONVERTED:
- ES-9, ES-57: calculation of state and message pairs.
- ES-10, ES-20, ES-28: test-suite design and coverage opinion (only the term-level points were kept).
- ES-35, 36, 37, 39, 40, 41, 42, 46: procedure or design of a review process and records, with little new vocabulary.
- ES-55, 56, 60: design opinion and evaluation-question writing.
- ES-29: how to record an integration (kept only as one statement in the constructed-versus-live question).

## Terms especially tested
### MCP and agent tool use
host :: the application that runs the model and mediates between it and MCP servers, deciding which tools are exposed and what enters context
MCP client :: the component inside the host that holds the connection to one MCP server
MCP server :: the program that implements capabilities (tools, resources, prompts) and describes them to clients
tool :: a callable action a server offers, which the model can ask the host to run
resource :: data a server exposes for context, identified by a URI
prompt (MCP) :: a reusable template offered by a server, not the host's system prompt
transport :: the channel carrying protocol messages; stdio for a local subprocess, HTTP for a remote server
stdio :: transport in which the client launches the server as a subprocess and exchanges one JSON message per line over standard input and output
framing :: the rule for where one message ends and the next begins (newline per message on stdio)
standard error :: the separate stream for diagnostics, kept out of the protocol stream
JSON-RPC 2.0 :: the message format of MCP, with requests, responses and notifications
request :: a message with a method and an id that expects a response
notification :: a message with a method and no id that receives no response
id :: the identifier a response echoes so a request and its reply can be paired
parse error (-32700), invalid request (-32600), method not found (-32601), invalid params (-32602) :: standard JSON-RPC error codes for unparseable text, a malformed request object, an unknown method and bad parameters
-32000 to -32099 :: range reserved for implementation-defined server errors
initialize :: the request that opens a session, carrying requested protocol version, capabilities and client information
notifications/initialized :: the client's notification that it has finished initialization
protocol version negotiation :: the server replies with a version it supports and the client decides whether to continue or disconnect
capability negotiation :: each side declares optional features so both know what may be used
listChanged :: the sub-capability announcing that a server may notify when its tool list changes
tools/list, tools/call :: requests to discover tools and to invoke one
inputSchema :: JSON Schema describing the argument shape of a tool
tool description :: server-supplied free text, a claim and not verified evidence
annotation (readOnlyHint, destructiveHint) :: advisory metadata a server publishes, not enforced by the protocol
isError :: flag in a successful tool result reporting that the tool ran but failed at its task
lifecycle, request and task failure :: the three layers of failure: wrong time, wrong method or arguments, and a valid call with a negative outcome
tool poisoning :: injection carried in tool metadata that the model reads as context
prompt injection through tool output :: instructions embedded in returned content, which is untrusted data
### Security, review and evidence
discovery versus permission :: learning that a tool exists does not allow calling it; policy decides
authorization versus interoperability :: whether a capability may run for a task versus whether parties understand each other's messages
allow-list :: host policy naming which servers and tools may run
least privilege :: exposing to a task only the capabilities it needs
approval gate :: a host-side step requiring human approval before a consequential tool runs
enforcement outside the model :: controls in the host or process that hold even if the model is steered, unlike prompt instructions
conformance :: behaving as the specification requires across states, not merely matching example message shapes
four questions :: protocol, capability, permission, evidence, kept separate in a connection review
evidence types :: advertised (the server's claim), source-inspected, executed (limited to the run, input and version), independently sourced, uninspected
uninspected :: the honest entry for an item not examined, in place of asserting absence
ground truth :: the declared source data a returned value is compared with, as opposed to a plausibility judgment
independent check :: a check that fails differently from what it checks
provenance :: where a value or server came from
constructed versus live :: hand-written test messages versus messages from a real host session, labeled apart
decision versus sign-off :: the decision concerns the server; the signed statement concerns the evidence behind it
re-review trigger :: a change, such as a new version, new tool or wider data scope, that reopens a decision
scoped claim :: a statement limited to what the evidence covers, avoiding words like secure or verified without criterion
discrepancy request :: asking an assistant to list disagreements with quoted lines and withholding a verdict
specification before implementation :: writing expected responses before reading the code
fine-tuning versus connecting a tool :: training changes weights; a tool connection adds context and actions without changing them
