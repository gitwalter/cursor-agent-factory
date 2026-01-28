# Grounding Strategy Section for Confluence

**Target Page:** [SAP Development Workflows with Cursor IDE](https://fielmann.atlassian.net/wiki/spaces/SAP/pages/8281292816/SAP+Development+Workflows+with+Cursor+IDE)

**Instructions:** Add the following section to the Confluence page.

---

## SAP Professional Grounding System

The grounding system is a comprehensive framework that verifies all SAP artifacts against authoritative sources before code generation, preventing hallucinations and ensuring accurate development.

### Architecture Overview

The system uses a 5-layer verification architecture:

| Layer | Purpose | Source |
|-------|---------|--------|
| 1 | Knowledge Cache | Pre-verified definitions in repository |
| 2 | SAP Documentation | SAP Help Portal via MCP |
| 3 | Reference Repositories | abap-cheat-sheets, best practices |
| 4 | Project Specifications | Confluence, Excel mappings |
| 5 | Strawberry Verification | Mathematical hallucination detection |

### Grounding Skills (14 Total)

**Specialized Skills (12):**

| Skill | Artifact Types |
|-------|----------------|
| ddic-grounding | Tables, structures, data elements, domains, search helps, lock objects |
| cds-grounding | CDS views, annotations, access control |
| rap-grounding | Behavior definitions, actions, determinations, validations |
| class-grounding | Classes, interfaces, exception classes, methods |
| function-grounding | Function modules, function groups, BAPIs |
| api-grounding | OData services, service bindings, SOAP |
| enhancement-grounding | Enhancement spots, BAdIs |
| message-grounding | Message classes and numbers |
| authorization-grounding | Authorization objects and fields |
| mapping-grounding | Field/structure mapping specifications |
| existence-grounding | Repository object existence, release contracts |
| fiori-grounding | Fiori apps, semantic objects, UI5 components |

**Coordinator and Verification (2):**

| Skill | Purpose |
|-------|---------|
| sap-grounding | Orchestrates all 12 specialized skills |
| strawberry-verification | Mathematical hallucination detection |

### Release Contracts (ABAP Cloud)

For ABAP Cloud/BTP projects, the system verifies release contracts:

| Contract | Name | Required For |
|----------|------|--------------|
| C0 | Extend | Subclassing, interface implementation |
| C1 | System-Internal | ABAP Cloud development (mandatory) |
| C2 | Remote API | External API access |

### Verification Protocol

**Core Principles:**

1. Never assume without verification
2. Fail-safe behavior - STOP and ASK if unverified
3. Source citation - Document all verification sources
4. Release awareness - Check C0/C1/C2 for ABAP Cloud
5. Confidence tracking - HIGH/MEDIUM/LOW

**Confidence Levels:**

| Level | Definition |
|-------|------------|
| HIGH | Found in SAP official documentation |
| MEDIUM | Found in community resources |
| LOW | Inferred from patterns |

### Strawberry Integration

The system integrates Pythea/Strawberry for mathematical hallucination detection:

**Budget Gap Interpretation:**

| Budget Gap | Status | Action |
|------------|--------|--------|
| < 2 | OK | Proceed with implementation |
| 2-10 | WARNING | Proceed with caution |
| > 10 | FAIL | STOP - Do not proceed |

### Usage

**Automatic:** Grounding is automatically invoked before implementation.

**Manual:** `@grounding-verifier Verify: table MARA, class CL_ABAP_TYPEDESCR`

### Repository Documentation

Full documentation: [GROUNDING_STRATEGY.md](link-to-repo/docs/GROUNDING_STRATEGY.md)

---

**Note:** This section should be added to the Confluence page manually when authentication is available.
