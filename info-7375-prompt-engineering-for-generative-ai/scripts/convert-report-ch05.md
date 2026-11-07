# Conversion report: ch05-tools-and-permissions (MA-ch05)

Old MA: 62. Old essays: 62. New MA: 36. Dropped/merged: 26 old MA (merged near-duplicates, mostly the many path-traversal / prefix / symlink variants and boundary-matrix tracing items; non-vocabulary arithmetic and code-trivia items removed).
Essays converted: 59, folded into the 36 questions by shared contrast. NOT CONVERTED: ES-ch05.19 (attention-cost arithmetic), ES-ch05.39 (enumeration count calculation), ES-ch05.46 (write a permission policy: design opinion), ES-ch05.61 (record-keeping for an experiment: procedure). the policy-writing and experiment-record items are design/procedure, not term contrasts.

## Terms especially tested (permissions and tool use)
path traversal :: using parent components in a requested path to climb out of an approved directory
parent component (`..`) vs current directory (`.`) :: two dots move up one level; one dot stays
symbolic link :: a directory entry that stores a pointer to another path
hard link :: a second name for the same underlying file contents
resolve :: follow links and dot components to the real absolute destination
normalize :: lexical clean-up of dot components without consulting the filesystem
canonical path :: the single absolute form with dot components removed and links followed
strict vs non-strict resolve :: strict raises when part of the path is missing; non-strict computes a destination anyway
containment check :: test that a resolved target lies inside a resolved root, compared by path components
sibling-directory (prefix) flaw :: string prefix matching accepts /data/course-private for root /data/course
approved root :: the directory a tool is allowed to reach; chosen by a responsible person
fail closed :: when unsure or on error, refuse
allowlist vs denylist :: permit only what is named versus refuse only what is named
default deny :: a request not explicitly permitted is refused
least privilege :: grant the smallest set of capabilities the task needs
need to know :: give the agent the information the task requires and no more
instruction vs control :: a prompt request versus enforcement by code outside the model
deterministic check :: gives the same verdict for the same input, so it is testable
permission vs approval :: what the policy allows versus a person's consent to one specific action
scoped approval :: consent bound to the exact action and target shown
approval gate :: a point where a person decides before an action runs (preventive)
audit log :: record of operations, targets and decisions for later review (detective)
reversibility :: how readily an action's effect can be undone
confused deputy :: an authorised program acts on a request from a less-trusted party
indirect prompt injection :: instructions arriving through content the model reads
tool_use / tool_result :: the model's structured request to call a tool, and the output returned to it
MCP server vs client :: the server exposes tools; the client in the host connects and applies policy
tenant isolation / identity from session :: identity comes from the authenticated application, not a model argument
TOCTOU :: time-of-check to time-of-use race between a check and a later use
preflight check :: a function that decides whether an operation is allowed without performing it
allow / ask / deny rules, deny first :: allow proceeds, ask prompts a person, deny refuses; deny is evaluated first
bypass (skip-prompts) mode and sandbox :: removes the approval gate; a sandbox limits reach at the operating-system level
schema vs policy :: schema validates argument shape; enforcement belongs in the tool code
call budget :: a limit on how many tool calls occur, distinct from a per-call permission verdict
defense in depth :: independent stacked layers so one failure does not expose everything
rubber-stamping / approval fatigue :: approving without reading because prompts are too frequent
independence of checkers :: separate checks that do not repeat the same mistake
seam :: the handoff between pipeline stages
authorized vs correct :: permission answers whether an action is allowed, not whether the change is right
