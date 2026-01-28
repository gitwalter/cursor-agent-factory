# SAP Professional Grounding System

## Overview

The SAP Professional Grounding System is a comprehensive, multi-layered verification framework designed to prevent hallucinations and ensure accurate SAP development. It verifies all SAP artifacts against authoritative sources before code generation.

## The Problem

LLM-based development assistants can "hallucinate" - producing plausible but incorrect information such as:
- Non-existent tables, fields, or structures
- Wrong method signatures or parameters
- Invalid API operations or entity sets
- Incorrect CDS annotations or RAP behavior definitions
- Objects that don't exist in the target SAP system/release

Without systematic verification, these hallucinations can lead to runtime errors, failed implementations, and wasted development effort.

## Solution Architecture

The grounding system uses a **5-layer verification architecture** with **14 specialized skills**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    Layer 5: Strawberry Verification             │
│           Mathematical hallucination detection (budget_gap)     │
├─────────────────────────────────────────────────────────────────┤
│                    Layer 4: Project Specifications              │
│              Confluence, Excel mappings via Atlassian MCP       │
├─────────────────────────────────────────────────────────────────┤
│                    Layer 3: Reference Repositories              │
│             abap-cheat-sheets, best practices, samples          │
├─────────────────────────────────────────────────────────────────┤
│                    Layer 2: SAP Documentation                   │
│               SAP Help Portal via SAP Documentation MCP         │
├─────────────────────────────────────────────────────────────────┤
│                    Layer 1: Knowledge Cache                     │
│              Pre-verified definitions in knowledge files        │
└─────────────────────────────────────────────────────────────────┘
```

## Grounding Skills

### Specialized Skills (12)

| # | Skill | Artifact Types | Location |
|---|-------|----------------|----------|
| 1 | `ddic-grounding` | Tables, structures, data elements, domains, search helps, lock objects | `patterns/skills/ddic-grounding.json` |
| 2 | `cds-grounding` | CDS views, annotations, access control | `patterns/skills/cds-grounding.json` |
| 3 | `rap-grounding` | Behavior definitions, actions, determinations, validations | `patterns/skills/rap-grounding.json` |
| 4 | `class-grounding` | Classes, interfaces, exception classes, methods | `patterns/skills/class-grounding.json` |
| 5 | `function-grounding` | Function modules, function groups, BAPIs | `patterns/skills/function-grounding.json` |
| 6 | `api-grounding` | OData services, service bindings, SOAP | `patterns/skills/api-grounding.json` |
| 7 | `enhancement-grounding` | Enhancement spots, BAdIs | `patterns/skills/enhancement-grounding.json` |
| 8 | `message-grounding` | Message classes and numbers | `patterns/skills/message-grounding.json` |
| 9 | `authorization-grounding` | Authorization objects and fields | `patterns/skills/authorization-grounding.json` |
| 10 | `mapping-grounding` | Field/structure mapping specifications | `patterns/skills/mapping-grounding.json` |
| 11 | `existence-grounding` | Repository object existence, release contracts | `patterns/skills/existence-grounding.json` |
| 12 | `fiori-grounding` | Fiori apps, semantic objects, UI5 components | `patterns/skills/fiori-grounding.json` |

### Coordinator and Verification (2)

| Skill | Purpose | Location |
|-------|---------|----------|
| `sap-grounding` | Orchestrates all 12 specialized skills | `patterns/skills/sap-grounding.json` |
| `strawberry-verification` | Mathematical hallucination detection | `patterns/skills/strawberry-verification.json` |

## Knowledge Catalogs

Pre-verified artifact definitions are stored in knowledge catalogs:

| Catalog | Contents | Location |
|---------|----------|----------|
| `ddic-catalog.json` | Common SAP tables, structures, data elements | `knowledge/ddic-catalog.json` |
| `class-catalog.json` | Released ABAP classes and interfaces | `knowledge/class-catalog.json` |
| `rap-catalog.json` | RAP behavior patterns | `knowledge/rap-catalog.json` |
| `api-catalog.json` | OData services, BAPIs | `knowledge/api-catalog.json` |
| `released-apis.json` | C0/C1/C2 release contracts | `knowledge/released-apis.json` |
| `mapping-spec-schema.json` | Mapping specification format | `knowledge/mapping-spec-schema.json` |
| `grounding-result-schema.json` | Standard result format | `knowledge/grounding-result-schema.json` |

## Release Contracts

For ABAP Cloud/BTP compatibility, the system verifies release contracts:

| Contract | Name | Description | Required For |
|----------|------|-------------|--------------|
| C0 | Extend | Can be extended (inherited, implemented) | Subclassing, interface implementation |
| C1 | System-Internal | Can be used within same system | ABAP Cloud development |
| C2 | Remote API | Can be accessed remotely | External API access |

## Strawberry Verification (Native Implementation)

The system includes a native implementation of Strawberry-style verification that runs within Cursor's LLM flow - no external API keys required.

### Concept: Procedural Hallucination Detection

Detects cases where the AI "knows but doesn't use" information correctly. Example: Ask to count r's in "strawberry". AI writes "s-t-r-a-w-b-e-r-r-y", identifies each r, counts 3. Then outputs "2".

### How It Works

1. **Evidence Collection**: Gather verification evidence as numbered spans (S0, S1, S2...)
2. **Scrubbed Test**: Replace identifiers with placeholders, check if claim still holds
3. **Full Test**: Use complete evidence with all identifiers
4. **Interpretation**: If scrubbed test passes too easily, evidence may not be essential

### Two-Pass Verification

| Pass | Description | Purpose |
|------|-------------|---------|
| Scrubbed | Replace "MARA" with "{TABLE}", "MATNR" with "{FIELD}" | Tests if claim depends on specific evidence |
| Full | Use original evidence with all identifiers | Tests if evidence actually supports claim |

### Status Interpretation

| Status | Meaning | Action |
|--------|---------|--------|
| VERIFIED | Scrubbed fails, full passes | Evidence essential - proceed |
| PLAUSIBLE | Moderate support from both | Proceed with caution |
| SUSPICIOUS | Scrubbed works almost as well | May be confabulating - warning |
| UNSUPPORTED | Neither test supports | STOP - do not proceed |

### Implementation

The `strawberry-verification` skill is implemented natively as a skill pattern that instructs the Cursor LLM how to perform the verification. No external dependencies required.

**Skill Location:** `patterns/skills/strawberry-verification.json`

## Verification Protocol

### Core Principles

1. **Never assume without verification** - All artifacts must be verified before use
2. **Fail-safe behavior** - If unverified, STOP and ASK user
3. **Source citation** - Always document verification sources
4. **Release awareness** - Check C0/C1/C2 for ABAP Cloud
5. **Confidence tracking** - Track HIGH/MEDIUM/LOW confidence
6. **Cache updates** - Store verified results for reuse

### Confidence Levels

| Level | Definition |
|-------|------------|
| HIGH | Found in SAP official documentation with exact match |
| MEDIUM | Found in community resources or partial match |
| LOW | Inferred from patterns or limited sources |

## Using the Grounding System

### Automatic Invocation

The grounding system is automatically invoked by the SAP blueprint before any implementation.

### Manual Invocation

```
@grounding-verifier Verify: table MARA, class CL_ABAP_TYPEDESCR, CDS I_Product
```

### Verification Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| `full` | Complete verification with Strawberry | Before implementation |
| `quick` | Fast existence and release check | During coding |
| `mapping` | Validate against specification | Spec implementation |
| `release` | Check ABAP Cloud compatibility | BTP projects |

## Grounding Verifier Agent

The `grounding-verifier` agent is a dedicated agent for comprehensive SAP artifact verification:

- **Location**: `patterns/agents/grounding-verifier.json`
- **Skills**: All 14 grounding skills
- **MCP Servers**: sap-documentation, atlassian
- **Native Skills**: strawberry-verification (no external API required)

## Best Practices

1. **Always verify before implementing** - Invoke grounding at the start of any task
2. **Use appropriate skill** - Route to specialized skill for artifact type
3. **Check release status** - Especially for ABAP Cloud projects
4. **Document sources** - Maintain traceability for all verifications
5. **Update catalogs** - Add newly verified objects to knowledge catalogs
6. **Review Strawberry flags** - Take budget_gap warnings seriously

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Object not found | May be custom or hallucinated | ASK USER to confirm |
| Not released | Object not available in ABAP Cloud | Use released alternative |
| Type mismatch | Wrong data type assumed | Verify against DDIC catalog |
| High budget_gap | Claim not well supported | Gather more evidence |

### Fallback Procedures

- **If verification fails**: STOP and ASK user before proceeding
- **If Strawberry unavailable**: Proceed with domain grounding only (add warning)
- **If object is custom (Y/Z)**: Cannot verify automatically - ask user

## Related Documentation

- [SAP Help Portal - Released APIs](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/ABENRELEASED_APIS.html)
- [Pythea/Strawberry Repository](https://github.com/leochlon/pythea) - Original inspiration for verification approach
- [Confluence: SAP Development Workflows with Cursor IDE](https://fielmann.atlassian.net/wiki/spaces/SAP/pages/8281292816/SAP+Development+Workflows+with+Cursor+IDE)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01-28 | Initial comprehensive grounding system with 14 skills |
