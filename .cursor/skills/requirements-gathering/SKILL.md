---
name: requirements-gathering
description: Systematic 5-phase requirements elicitation for Cursor agent system generation
type: skill
knowledge: [stack-capabilities.json, workflow-patterns.json, mcp-servers-catalog.json, best-practices.json]
---

# Requirements Gathering Skill

Executes a structured 5-phase questionnaire to capture all requirements for generating a new Cursor agent development system.

## When to Use

- When starting a new project generation
- When the `requirements-architect` agent needs to gather information
- When user requests to create a new agent system
- When customizing an existing blueprint

## Phase Structure Overview

```
Phase 1: Project Context    → Who, What, Where
Phase 2: Technology Stack   → Languages, Frameworks, Tools
Phase 3: Workflow Method    → Triggers, Artifacts, Process
Phase 4: Knowledge Domain   → Concepts, References, Conventions
Phase 5: Agent Capabilities → Agents, Skills, Integrations
```

## Phase 1: Project Context

### Questions

| # | Question | Variable | Validation |
|---|----------|----------|------------|
| 1 | What is the name of your project? | `{PROJECT_NAME}` | Valid directory name, no special chars |
| 2 | Briefly describe what this project will do | `{PROJECT_DESCRIPTION}` | Non-empty, < 500 chars |
| 3 | What domain or industry is this for? | `{DOMAIN}` | Match to known domains |
| 4 | Team size and experience level? | `{TEAM_CONTEXT}` | Optional |

### Domain Options

Suggest these common domains:
- Web Development
- Mobile Development
- Data Science / ML
- SAP / Enterprise
- DevOps / Infrastructure
- Game Development
- IoT / Embedded
- Custom (specify)

### Output

```yaml
projectContext:
  name: "{PROJECT_NAME}"
  description: "{PROJECT_DESCRIPTION}"
  domain: "{DOMAIN}"
  teamContext: "{TEAM_CONTEXT}"
```

## Phase 2: Technology Stack

### Questions

| # | Question | Variable | Reference |
|---|----------|----------|-----------|
| 1 | Primary programming language? | `{PRIMARY_LANGUAGE}` | Check blueprints |
| 2 | Frameworks or libraries? | `{FRAMEWORKS}` | Stack-specific |
| 3 | Database or storage systems? | `{DATABASES}` | Optional |
| 4 | External APIs or services? | `{EXTERNAL_APIS}` | Optional |

### Language Options

- Python
- TypeScript / JavaScript
- Java
- C# / .NET
- Go
- Rust
- ABAP (SAP)
- Multiple (polyglot)

### Blueprint Matching

After capturing stack info, check `blueprints/` for matches:

```
IF primaryLanguage == "python" AND "fastapi" IN frameworks:
    suggest blueprint: "python-fastapi"
IF primaryLanguage == "typescript" AND "react" IN frameworks:
    suggest blueprint: "typescript-react"
IF primaryLanguage == "java" AND "spring" IN frameworks:
    suggest blueprint: "java-spring"
```

### Output

```yaml
technologyStack:
  primaryLanguage: "{PRIMARY_LANGUAGE}"
  frameworks: ["{FRAMEWORK_1}", "{FRAMEWORK_2}"]
  databases: ["{DATABASE_1}"]
  externalApis: ["{API_1}"]
  matchedBlueprint: "{BLUEPRINT_ID}" | null
```

## Phase 3: Workflow Methodology

### Questions

| # | Question | Variable | Options |
|---|----------|----------|---------|
| 1 | Development methodology? | `{METHODOLOGY}` | Agile, Kanban, Waterfall, Custom |
| 2 | What triggers tasks? | `{TRIGGER_SOURCES}` | Jira, Confluence, GitHub, GitLab, Manual |
| 3 | Output artifacts? | `{OUTPUT_ARTIFACTS}` | Code, Docs, Tests, Diagrams |

### Trigger Source Details

For each selected trigger, gather:

| Trigger | Additional Info Needed |
|---------|----------------------|
| Jira | Project key pattern (e.g., `PROJ-###`) |
| Confluence | Space key |
| GitHub | Repository URL pattern |
| GitLab | Repository URL pattern |

### Output

```yaml
workflowMethodology:
  methodology: "{METHODOLOGY}"
  triggerSources:
    - type: "jira"
      pattern: "{PROJECT_KEY}-{NUMBER}"
    - type: "confluence"
      spaceKey: "{SPACE_KEY}"
  outputArtifacts: ["code", "docs", "tests"]
```

## Phase 4: Knowledge Domain

### Questions

| # | Question | Variable | Purpose |
|---|----------|----------|---------|
| 1 | Domain-specific concepts? | `{DOMAIN_CONCEPTS}` | Build knowledge files |
| 2 | Reference repositories/docs? | `{REFERENCE_SOURCES}` | DeepWiki integration |
| 3 | Naming conventions? | `{CONVENTIONS}` | Style guide setup |

### Reference Source Types

- GitHub repositories (for DeepWiki queries)
- Documentation URLs
- Internal wikis
- Style guides

### Output

```yaml
knowledgeDomain:
  concepts: ["{CONCEPT_1}", "{CONCEPT_2}"]
  referenceSources:
    - type: "github"
      url: "{REPO_URL}"
    - type: "documentation"
      url: "{DOC_URL}"
  conventions:
    styleGuide: "{STYLE_GUIDE}"
    namingPattern: "{NAMING_PATTERN}"
```

## Phase 5: Agent Capabilities

### Questions

| # | Question | Variable | Options |
|---|----------|----------|---------|
| 1 | Core agents needed? | `{CORE_AGENTS}` | Multi-select |
| 2 | Workflow skills needed? | `{CORE_SKILLS}` | Multi-select |
| 3 | MCP server integrations? | `{MCP_INTEGRATIONS}` | Multi-select |

### Agent Options

| Agent | Description | When to Suggest |
|-------|-------------|-----------------|
| `code-reviewer` | Reviews code quality | Always |
| `test-generator` | Creates test cases | When tests in artifacts |
| `documentation-agent` | Generates documentation | When docs in artifacts |
| `explorer` | Searches external docs | When external APIs used |

### Skill Options

| Skill | Description | When to Suggest |
|-------|-------------|-----------------|
| `bugfix-workflow` | Ticket-based bug fixes | When Jira trigger |
| `feature-workflow` | Spec-based features | When Confluence trigger |
| `grounding` | Data model verification | Data-heavy projects |
| `tdd` | Test-driven development | When tests important |
| `code-templates` | Code generation | Always |

### MCP Server Options

| Server | Purpose | Reference |
|--------|---------|-----------|
| `atlassian` | Jira/Confluence | `knowledge/mcp-servers-catalog.json` |
| `deepwiki` | GitHub analysis | `knowledge/mcp-servers-catalog.json` |
| `sequentialthinking` | Structured reasoning | `knowledge/mcp-servers-catalog.json` |

### Output

```yaml
agentCapabilities:
  agents: ["code-reviewer", "test-generator"]
  skills: ["bugfix-workflow", "feature-workflow", "tdd"]
  mcpIntegrations: ["atlassian", "deepwiki"]
```

## Final Validation

Before proceeding to generation:

### Completeness Check

- [ ] Project name is valid
- [ ] At least one language specified
- [ ] At least one trigger source
- [ ] At least one agent selected
- [ ] At least one skill selected

### Target Directory

1. Ask: "Where should I create the project?"
2. Validate:
   - Path is accessible
   - Path is NOT within factory directory
   - Directory can be created if needed
3. Confirm with user

### Generate Summary

```markdown
## Requirements Summary

### Project
- **Name:** {PROJECT_NAME}
- **Description:** {PROJECT_DESCRIPTION}
- **Domain:** {DOMAIN}

### Technology Stack
- **Language:** {PRIMARY_LANGUAGE}
- **Frameworks:** {FRAMEWORKS}
- **Blueprint:** {MATCHED_BLUEPRINT}

### Workflow
- **Triggers:** {TRIGGER_SOURCES}
- **Artifacts:** {OUTPUT_ARTIFACTS}

### Agents & Skills
- **Agents:** {CORE_AGENTS}
- **Skills:** {CORE_SKILLS}
- **MCP Servers:** {MCP_INTEGRATIONS}

### Output
- **Target:** {TARGET_DIR}
```

## Important Rules

1. **Ask one phase at a time** - Don't overwhelm user
2. **Provide examples** - Help user understand options
3. **Validate inputs** - Check before proceeding
4. **Suggest blueprints** - Match to existing blueprints
5. **Confirm summary** - Review before generation
6. **Never assume** - Ask if uncertain

## References

- `knowledge/stack-capabilities.json` - Stack-specific capabilities
- `knowledge/workflow-patterns.json` - Workflow pattern definitions
- `knowledge/mcp-servers-catalog.json` - Available MCP servers
- `knowledge/best-practices.json` - Cross-stack best practices
- `blueprints/` - Available technology blueprints
