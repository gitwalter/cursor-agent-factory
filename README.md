# Cursor Agent Factory

A meta-system that generates complete Cursor AI agent development systems for any technology stack, workflow methodology, and knowledge domain.

## Overview

The Cursor Agent Factory is itself a Cursor agent system that produces other Cursor agent systems. It follows a systematic requirements gathering process and generates production-ready projects with:

- AI agent definitions (`.cursor/agents/`)
- Reusable skill definitions (`.cursor/skills/`)
- Structured knowledge files (`knowledge/`)
- Code and document templates (`templates/`)
- Workflow documentation (`workflows/`)
- LLM behavior rules (`.cursorrules`)

## Quick Start

### Chat-Based (Recommended)

1. Open this project in Cursor IDE
2. Say: **"Create a new agent system"**
3. Follow the 5-phase questionnaire
4. Specify output directory
5. Review generated project

### CLI (Advanced Users)

```powershell
# List available blueprints
C:\App\Anaconda\python.exe cli\factory_cli.py --list-blueprints

# Generate from a blueprint
C:\App\Anaconda\python.exe cli\factory_cli.py --blueprint python-fastapi --output C:\Projects\my-api

# Generate from configuration file
C:\App\Anaconda\python.exe cli\factory_cli.py --config project.yaml --output C:\Projects\my-project

# Interactive CLI mode
C:\App\Anaconda\python.exe cli\factory_cli.py --interactive --output C:\Projects\my-project
```

## Project Structure

```
cursor-agent-factory/
├── .cursor/
│   ├── agents/                  # Factory's own agents
│   │   ├── requirements-architect.md
│   │   ├── stack-builder.md
│   │   ├── workflow-designer.md
│   │   ├── knowledge-manager.md
│   │   └── template-generator.md
│   └── skills/                  # Factory's own skills
│       ├── requirements-gathering/
│       ├── stack-configuration/
│       ├── workflow-generation/
│       ├── agent-generation/
│       ├── skill-generation/
│       ├── knowledge-generation/
│       ├── template-generation/
│       └── cursorrules-generation/
├── patterns/                    # Reusable patterns
│   ├── agents/                 # Agent pattern definitions
│   ├── skills/                 # Skill pattern definitions
│   ├── workflows/              # Workflow patterns
│   ├── stacks/                 # Stack configurations
│   └── templates/              # Template patterns
├── blueprints/                  # Technology stack blueprints
│   ├── python-fastapi/
│   ├── typescript-react/
│   ├── java-spring/
│   ├── csharp-dotnet/
│   ├── sap-abap/
│   └── multi-stack/
├── knowledge/                   # Reference data
│   ├── stack-capabilities.json
│   ├── workflow-patterns.json
│   ├── mcp-servers-catalog.json
│   └── best-practices.json
├── templates/
│   └── factory/                # Factory templates
│       └── cursorrules-template.md
├── cli/
│   └── factory_cli.py          # CLI interface
├── scripts/
│   └── generate_project.py     # Generation engine
├── .cursorrules                 # Factory behavior rules
└── README.md                    # This file
```

## Available Blueprints

| Blueprint | Stack | Description |
|-----------|-------|-------------|
| `python-fastapi` | Python, FastAPI, SQLAlchemy | REST API development |
| `typescript-react` | TypeScript, React, Vite | Web application development |
| `java-spring` | Java, Spring Boot, JPA | Enterprise application development |
| `csharp-dotnet` | C#, .NET, Entity Framework | .NET application development |
| `sap-abap` | ABAP, RAP, CAP | SAP development |
| `multi-stack` | Multiple | Polyglot project development |

## Factory Agents

| Agent | Purpose |
|-------|---------|
| `requirements-architect` | Gather and validate project requirements through 5-phase questionnaire |
| `stack-builder` | Configure technology stack and select appropriate blueprints |
| `workflow-designer` | Design development workflows and trigger integrations |
| `knowledge-manager` | Structure domain knowledge and generate knowledge files |
| `template-generator` | Generate code and document templates |

## Factory Skills

| Skill | Description |
|-------|-------------|
| `requirements-gathering` | 5-phase interactive requirements elicitation |
| `stack-configuration` | Technology stack selection and configuration |
| `workflow-generation` | Workflow pattern generation and customization |
| `agent-generation` | Agent definition file generation |
| `skill-generation` | Skill definition with references generation |
| `knowledge-generation` | JSON knowledge file generation |
| `template-generation` | Code and document template generation |
| `cursorrules-generation` | .cursorrules file generation |

## Requirements Gathering Phases

### Phase 1: Project Context
- Project name and description
- Domain/Industry (Web, Mobile, SAP, etc.)
- Team size and experience level

### Phase 2: Technology Stack
- Primary programming language
- Frameworks and libraries
- Database/storage systems
- External APIs and services

### Phase 3: Workflow Methodology
- Development methodology (Agile, Kanban, etc.)
- Trigger sources (Jira, Confluence, GitHub, GitLab)
- Output artifacts (code, docs, tests)

### Phase 4: Knowledge Domain
- Domain-specific concepts and terminology
- Reference repositories and documentation
- Naming conventions and best practices

### Phase 5: Agent Capabilities
- Core agents needed (Code Reviewer, Test Generator, etc.)
- Skills required (Bugfix, Feature, TDD, Grounding)
- MCP server integrations

## Generated Project Structure

Generated projects follow this structure:

```
{PROJECT_NAME}/
├── .cursor/
│   ├── agents/           # AI agent definitions
│   └── skills/           # Reusable skill definitions
├── knowledge/            # Structured reference data (JSON)
├── templates/            # Code and document templates
├── workflows/            # Workflow documentation
├── scripts/              # Utility scripts
├── diagrams/             # Architecture diagrams
├── docs/                 # User documentation
├── src/                  # Source code
├── .cursorrules          # LLM agent behavior rules
└── README.md             # Project documentation
```

## MCP Server Integration

The factory can configure generated projects to use these MCP servers:

| Server | Purpose | Authentication |
|--------|---------|----------------|
| `atlassian` | Jira/Confluence integration | OAuth |
| `sap-documentation` | SAP Help Portal queries | None |
| `deepwiki` | GitHub repository analysis | None |
| `sequentialthinking` | Structured problem solving | None |

## Configuration File Format

You can create projects from YAML or JSON configuration:

```yaml
# project-config.yaml
project_name: my-api-project
project_description: REST API with FastAPI
domain: web-development
primary_language: python
frameworks:
  - fastapi
  - sqlalchemy
triggers:
  - jira
  - confluence
agents:
  - code-reviewer
  - test-generator
skills:
  - bugfix-workflow
  - feature-workflow
  - tdd
mcp_servers:
  - name: atlassian
    url: https://mcp.atlassian.com/v1/sse
    purpose: Jira/Confluence integration
```

## Extending the Factory

### Adding New Blueprints

1. Create directory: `blueprints/{blueprint-id}/`
2. Create `blueprint.json` with:
   - Metadata (name, description, tags)
   - Stack configuration
   - Agent and skill references
   - Template paths

### Adding New Patterns

1. Create pattern JSON in appropriate `patterns/` directory
2. Follow the pattern schema in `patterns/{type}/{type}-pattern.json`
3. Reference pattern in blueprints

### Adding New Skills

1. Create skill directory: `.cursor/skills/{skill-name}/`
2. Create `SKILL.md` with frontmatter and process documentation
3. Add to factory's skill registry

## Development

### Requirements

- Python 3.10+
- Cursor IDE
- PyYAML (for YAML config support)

### Running Tests

```powershell
# Run the CLI help
C:\App\Anaconda\python.exe cli\factory_cli.py --help

# List blueprints
C:\App\Anaconda\python.exe cli\factory_cli.py --list-blueprints

# List patterns
C:\App\Anaconda\python.exe cli\factory_cli.py --list-patterns
```

### Testing Generation

```powershell
# Generate test project
C:\App\Anaconda\python.exe cli\factory_cli.py --blueprint python-fastapi --output C:\Temp\test-project
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add patterns, blueprints, or skills
4. Test generation
5. Submit pull request

## License

MIT License

---

*Cursor Agent Factory v1.0.0*
*Meta-system for generating Cursor agent development systems*
