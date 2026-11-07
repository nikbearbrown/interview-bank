# Conversion report: ch14-governance-and-ethics (MA-ch14)

- Old MA: 64. Old essays: 61. New MA: 36. Dropped/merged: 28 old MA merged into other questions or removed as non-vocabulary (for example MA-ch14.43 review-capacity arithmetic, MA-ch14.53 date computation, MA-ch14.10 and .12 code trivia merged into the isinstance and allowlist items, MA-ch14.17 and .18 merged into one test-first item).
- Essays: 61 old; 57 folded by shared contrast into the 36 items. NOT CONVERTED (4, pure calculation): ES-ch14.16 (failure count from pass rate), ES-ch14.27 (PPV arithmetic; the term pair base rate and PPV is kept in a term question), ES-ch14.38 (review capacity gap), ES-ch14.52 (retention date computation; the start-event term is kept).
- True-count spread: 1 true x3, 2 true x10, 3 true x16, 4 true x7.

## Terms especially tested (governance and ethics)
owner :: the person who answers for a workflow as it runs and has authority to pause or change it
approver :: the person who gives the authorized yes to a specific proposal
incident contact :: the person, or documented backup, who receives and acknowledges an alert about harm
AI-use register :: the record of an AI workflow's purpose, roles, data, thresholds, retention and recourse
accountability :: responsibility accepted by a named person who has authority to act
completeness vs compliance :: filled-in fields versus a legal and institutional determination
validator status (incomplete / review-required / ready-for-human-review) :: structural check results; the last means ready to be reviewed, not reviewed or approved
threshold / trigger / signal :: an observable condition, how it is measured, and the response it sets off
stop rule :: a trigger that can fire on a single confirmed severe event
aggregate rate vs severity :: an average that weights each failure equally and hides rare severe harm
pause authority :: the power to halt a workflow, only usable when incentives support it
escalation path / backup / acknowledgment window :: who gets the alert next and the time within which it should be acknowledged
fail closed :: route what the system cannot classify to a person
allowlist vs denylist :: permit only approved values versus block only listed values
structural check vs adequacy judgment :: what code can refuse exactly versus what people judge
truthy / falsy :: Python values that test true or false in a condition; 0 and empty containers are falsy
isinstance vs exact type check; bool is a subclass of int :: a subclass instance passes isinstance but not type(x) is int
test-first / specification :: tests written from intent before the implementation exists
claim no stronger than the evidence :: wording that matches what a check actually established
purpose / scope change :: the stated boundary of use; a new data type or audience needs re-review
retention lifecycle :: the life of data across logs, backups, exports, derived artifacts and provider copies
zero retention :: a design intent that must say what it means and does not prove no copies exist
derived data :: embeddings, summaries and hashes made from source data
minimal audit record / trace :: identifiers and references to evidence, not full content
action surface :: the systems and audiences an agent's actions can reach
reversibility :: how hard an action is to undo
fabrication (hallucination) vs abstention :: a statement unsupported by sources versus leaving the answer out
false positive / false negative :: an unwarranted positive versus a missed real positive, borne by different people
base rate / positive predictive value :: share of positives in a group; share of positive predictions that are correct
fairness criterion :: a chosen definition of fair that numbers alone do not select
generic risk vs concrete harm :: a vague concern versus who is harmed, what happens and how
matched mitigation :: a control that reduces the named harm's likelihood or severity
consultation vs simulated stakeholder :: asking affected people versus model role-play that is not evidence
stakeholder :: a person or group affected by or able to influence the workflow
recourse / contest / remedy :: a path to a human, a challenge to a decision and an outcome
meaningful human review vs rubber stamp :: review with time, authority and a record versus a click
least privilege :: the narrowest permissions a task requires
approval gate vs permission :: a human pause at the moment of action versus a rule about what is allowed
prompt injection / untrusted input :: instructions hidden in content the agent reads
sign-off :: a named person's claim, listing what was checked, not checked and not claimed
control plane vs documentation :: a register that changes system behavior versus one that only describes
decision note :: a record separating model proposal from human input, with evidence and affected interests
retention clock start event :: the event (creation, last use) from which a retention period is counted
