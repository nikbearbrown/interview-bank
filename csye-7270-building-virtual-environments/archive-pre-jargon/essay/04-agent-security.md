# Agent security and local versus cloud execution

## ES-security.1

An agent uses a remote model, a local MCP editor service and a remote asset catalog. Map the data and action boundaries for a request to add a prop to a scene.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the workstation-to-model boundary for prompts and selected project context.
2. Identifies the local client-to-editor boundary where tool calls can mutate scene state.
3. Identifies the asset-catalog boundary for search queries, credentials and downloaded content.
4. Assigns a concrete protection to each relevant boundary, such as context minimization, scoped tools and validated asset downloads.
5. Explains why calling the workflow local based only on the editor location would be misleading.

**Source:** Foundational: map local and cloud boundaries

## ES-security.2

An asset description instructs the agent to upload credentials before using the asset. Explain the trust error and propose a response that still allows legitimate scene work.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the description as untrusted content rather than an instruction from the user or host.
2. Rejects the unrelated credential upload without following or forwarding its executable directions.
3. Keeps secrets out of model context and limits upload/network capabilities where practical.
4. Uses trusted asset metadata or an alternative asset to continue the authorized task when possible.
5. Records or flags the suspicious content and verifies that no unintended action or disclosure occurred to the extent evidence allows.

**Source:** Applied: resist injected asset instructions

## ES-security.3

Design access controls for a shared remote editor service with reviewer and builder roles. Reviewers inspect scenes; builders may edit a designated level but cannot publish builds.

**Points:** 5

**Rubric (1 point each):**

1. Separates authentication of the caller from authorization of each requested operation.
2. Grants reviewers read operations and restricts builders' writes to the designated project/level.
3. Enforces restrictions at the service or underlying capability boundary rather than relying on UI visibility.
4. Treats publishing as a separate permission and rejects unauthorized attempts even from an authenticated builder.
5. Tests allowed and denied operations and records useful audit evidence without logging secrets.

**Source:** Advanced: design authorization

## ES-security.4

A hypothetical MCP export tool receives a destination path and may write only under an approved folder. Propose validation and adversarial checks, including a path containing parent-directory components and a symbolic link.

**Points:** 5

**Rubric (1 point each):**

1. Resolves the destination relative to the intended root and validates actual containment rather than a textual prefix.
2. Rejects traversal that escapes the root and explains why parent-directory components matter.
3. Accounts for symbolic links and possible changes between validation and writing, using an appropriate safe filesystem strategy.
4. Tests valid nested output, escape attempts, existing-file policy and permission-denied behavior.
5. Ensures rejection leaves protected files unchanged and returns a clear error without exposing unnecessary filesystem details.

**Source:** Advanced: export path validation

## ES-security.5

A developer wants to install a third-party MCP editor package because a tutorial says it speeds up game creation. Design a review appropriate to code that will access a valuable local project.

**Points:** 5

**Rubric (1 point each):**

1. Checks maintainer identity, source location and whether the package is official or community-maintained without equating either label with safety.
2. Reviews requested permissions, startup behavior and relevant dependencies for access beyond the task.
3. Pins a reviewed revision and records installation/compatibility requirements.
4. Tests representative read, write and failure cases in a disposable project under restricted access.
5. Defines rollback/removal and acceptance criteria before granting access to the valuable project.

**Source:** Applied: evaluate an unfamiliar package

## ES-security.6

An agent's tool log contains a credential that was also committed to version control. Describe containment and recovery without assuming that deleting the latest file removes all exposure.

**Points:** 5

**Rubric (1 point each):**

1. Restricts further access to the exposed credential and rotates or revokes it through the appropriate authority.
2. Identifies relevant copies such as history, logs and artifacts while avoiding further reproduction of the secret.
3. Moves legitimate credential use to an appropriate secret store or environment mechanism outside tracked content.
4. Reviews evidence of credential use and evaluates the affected scope rather than assuming no access occurred.
5. Adds redaction and a check against future secret inclusion, with cleanup coordinated so other work is preserved.

**Source:** Troubleshooting: accidental credential disclosure

## ES-security.7

A vendor says its editor integration runs locally. A studio requires no project data to leave its workstation. Describe how to evaluate the complete workflow before relying on that claim.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes local tool execution from the location of model inference and context processing.
2. Inventories model endpoints, telemetry, update checks, asset services and other network dependencies.
3. Inspects configuration and tests observed network behavior in a controlled session with representative tasks.
4. Uses local inference and disables or constrains incompatible remote paths where supported, verifying the resulting workflow still works.
5. Documents remaining limitations and does not infer an offline guarantee from the local integration label alone.

**Source:** Advanced: assess an offline claim

## ES-security.8

Design an audit record for an agent that changes game levels. It must support incident investigation and avoid becoming a store of sensitive project text and credentials.

**Points:** 5

**Rubric (1 point each):**

1. Records operation identity, caller, target project/object, time or ordering information and correlation identifier.
2. Records outcome and bounded before/after evidence adequate to reconstruct relevant changes.
3. Redacts secrets and minimizes raw prompts, asset text and payload data that are not needed for the audit purpose.
4. Restricts log access and defines retention appropriate to the project.
5. Protects useful failure records from silent overwriting and tests that the trail can explain a representative partial failure.

**Source:** Advanced: safe audit trail
