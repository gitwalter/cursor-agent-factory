# Cursor Agent Factory

**Build AI-powered development systems that truly understand your project.**

> **Quick Start:** New here? See [docs/QUICKSTART.md](docs/QUICKSTART.md) or run `python cli/factory_cli.py --quickstart` to get running in 5 minutes.

![cursor-ide](https://img.shields.io/badge/cursor--ide-blue)
![ai-agents](https://img.shields.io/badge/ai--agents-purple)
![mcp-servers](https://img.shields.io/badge/mcp--servers-green)
![code-generation](https://img.shields.io/badge/code--generation-orange)
![developer-tools](https://img.shields.io/badge/developer--tools-red)
![workflow-automation](https://img.shields.io/badge/workflow--automation-yellow)

Welcome! Whether you're a solo developer exploring new possibilities or a team building something meaningful together, we're here to help you create an AI development environment grounded in purpose, principles, and care.

---

## Start Here

Not sure where to begin? We've got you covered.

| I want to... | Here's your path |
|--------------|------------------|
| **See it work in 5 minutes** | [Quickstart Guide](docs/QUICKSTART.md) or `python cli/factory_cli.py --quickstart` |
| **Build my own project** | `python cli/factory_cli.py --interactive` |
| **Enhance an existing repo** | [Onboarding Guide](docs/ONBOARDING_GUIDE.md) |
| **Align my team** | [Team Workshop Guide](docs/TEAM_WORKSHOP_GUIDE.md) |
| **Configure MCP servers** | [MCP Servers Guide](docs/MCP-SERVERS.md) |

New to all this? Start with the [Quickstart Guide](docs/QUICKSTART.md) - you'll have a working demo in minutes, and we'll explain everything along the way.

**Need help?** See [Prerequisites](docs/PREREQUISITES.md) for setup or [Troubleshooting](docs/TROUBLESHOOTING.md) if you run into issues.

---

## How It Works

Every project we generate is built on a **5-layer architecture** grounded in love and trust:

```mermaid
flowchart TB
    subgraph L0 [Layer 0: Foundation]
        A0[Love and Trust]
    end
    
    subgraph L1 [Layer 1: Integrity]
        A1[Reasoning]
        A2[Curiosity]
        A3[Humility]
    end
    
    subgraph L2 [Layer 2: Purpose]
        Mission[Mission]
        Stakeholders[Stakeholders]
        Success[Success Criteria]
    end
    
    subgraph L3 [Layer 3: Principles]
        Ethics[Ethical Boundaries]
        Quality[Quality Standards]
    end
    
    subgraph L4 [Layer 4: Technical]
        Agents[AI Agents]
        Skills[Skills]
        Knowledge[Knowledge Files]
    end
    
    L0 --> L1
    L1 --> L2
    L2 --> L3
    L3 --> L4
```

This isn't just about code - it's about building systems that reflect your values.

---

## Quick Start Options

### Option 1: Instant Demo (5 minutes)

See the factory in action with zero configuration:

```powershell
python cli/factory_cli.py --quickstart
```

This creates a complete demo project showing what you'll get. Perfect for exploration!

### Option 2: Chat-Based Creation (Recommended)

1. Open this project in Cursor IDE
2. Say: **"Create a new agent system"**
3. Follow the guided 5-phase questionnaire
4. Specify your output directory
5. Review your generated project

### Option 3: Team Workshop Series

For teams of 2+ people, collaborative workshops help align your team:

| Workshop | Duration | What You'll Do |
|----------|----------|----------------|
| **Vision Quest** | 2-3h | Discover shared vision through games |
| **Ethics Arena** | 2h | Debate values and find priorities |
| **Stack Safari** | 2-3h | Explore technology together |
| **Agent Assembly** | 3-4h | Design your AI team |
| **Integration Celebration** | 1.5-2h | Demo and celebrate! |

Each workshop is grounded in **Axiom 0: Love and Trust**. See the [Team Workshop Guide](docs/TEAM_WORKSHOP_GUIDE.md) for details.

### Option 4: CLI (Advanced Users)

```powershell
# List available blueprints
python cli/factory_cli.py --list-blueprints

# Generate from a blueprint
python cli/factory_cli.py --blueprint python-fastapi --output C:\Projects\my-api

# Interactive mode with full questionnaire
python cli/factory_cli.py --interactive --output C:\Projects\my-project

# Onboard an existing repository
python cli/factory_cli.py --onboard C:\Projects\existing-repo
```

---

## Overview

The Cursor Agent Factory is a **meta-system** that generates complete AI agent development systems. It uses a 5-layer deductive-inductive architecture to create agent systems that are technically capable and grounded in clear values.

### The 5 Layers (+ Foundation)

| Layer | Name | Purpose | Artifact |
|-------|------|---------|----------|
| **A0** | Love & Trust | Foundation of all being and doing | `.cursorrules` foundation |
| **0** | Integrity & Logic | Foundational axioms (A1-A5) | `.cursorrules` L0 section |
| **1** | Purpose | Mission, stakeholders, success | `PURPOSE.md` |
| **2** | Principles | Ethical boundaries, quality standards | `.cursorrules` principles |
| **3** | Methodology | Agile/Kanban/R&D, enforcement, practices | `methodology.yaml` |
| **4** | Technical | Stack, agents, skills, templates | `.cursor/`, `knowledge/` |

### What You Get

Generated projects include:

- **Purpose documentation** (`PURPOSE.md`) - Your mission and success criteria
- **5-layer .cursorrules** - AI guidance with axioms, principles, and methodology
- **AI agent definitions** (`.cursor/agents/`) - Specialized assistants for your workflow
- **Reusable skill definitions** (`.cursor/skills/`) - Procedures your agents can follow
- **Structured knowledge files** (`knowledge/`) - Domain expertise in JSON format
- **Code and document templates** (`templates/`) - Consistent starting points
- **Methodology configuration** (`workflows/methodology.yaml`) - How your team works

## Architecture Diagrams

For visual documentation, see the [diagrams/](diagrams/) folder:

| Diagram | Description |
|---------|-------------|
| [Factory Workflow](diagrams/factory-workflow.md) | Complete generation workflow |
| [Verification Flow](diagrams/verification-flow.md) | Hallucination detection pipeline |
| [Agent/Skill Architecture](diagrams/agent-skill-architecture.md) | Agent hierarchy and composition |
| [SAP Grounding](diagrams/sap-grounding-architecture.md) | SAP-specific integration |

## Project Structure

```
cursor-agent-factory/
├── .cursor/
│   ├── agents/                  # Factory's own agents (7 agents)
│   │   └── *.md                 # knowledge-manager, onboarding-architect, requirements-architect, etc.
│   └── skills/                  # Factory's own skills (23 skills)
│       ├── agent-generation/
│       ├── alignment-check/
│       ├── axiom-selection/
│       ├── cursorrules-generation/
│       ├── enforcement-selection/
│       ├── knowledge-generation/
│       ├── mcp-selection/
│       └── ...                       # + more skills
├── patterns/                    # Reusable patterns (56 files)
│   ├── axioms/                  # Layer 0 axiom definitions
│   ├── principles/              # Layer 2 principle patterns
│   ├── methodologies/           # Layer 3 methodology templates
│   ├── enforcement/             # Enforcement patterns
│   ├── practices/               # Practice patterns
│   ├── agents/                  # Agent pattern definitions
│   ├── skills/                  # Skill pattern definitions
│   ├── games/                   # Workshop game definitions
│   ├── workshops/               # Workshop pattern definitions
│   ├── team-formats/            # Team size adaptations
│   ├── stacks/                  # Stack blueprint patterns
│   ├── templates/               # Template patterns
│   └── workflows/               # Workflow patterns
├── blueprints/                  # Technology stack blueprints (14 blueprints)
│   ├── python-fastapi/
│   ├── python-streamlit/
│   ├── ai-agent-development/
│   ├── multi-agent-systems/
│   ├── typescript-react/
│   ├── nextjs-fullstack/
│   ├── java-spring/
│   ├── kotlin-spring/
│   ├── csharp-dotnet/
│   ├── n8n-automation/
│   ├── sap-abap/
│   ├── sap-rap/
│   ├── sap-cap/
│   └── sap-cpi-pi/
├── knowledge/                   # Reference data (45 files)
│   └── *.json                   # Stack, workflow, MCP, security, AI patterns
├── templates/                   # Code and document templates (184 files)
│   ├── factory/                 # Factory templates (cursorrules, PURPOSE.md, etc.)
│   ├── ai/                      # AI agent templates
│   ├── python/                  # Python templates (FastAPI, Streamlit)
│   ├── typescript/              # TypeScript templates (Next.js)
│   ├── java/                    # Java Spring templates
│   ├── csharp/                  # C# Clean Architecture templates
│   ├── abap/                    # SAP ABAP/RAP templates
│   ├── cap/                     # SAP CAP templates
│   ├── integration/             # SAP CPI/PI integration templates
│   ├── automation/              # n8n automation templates
│   ├── workflows/               # CI/CD workflow templates
│   ├── methodology/             # Methodology templates
│   └── docs/                    # Documentation templates
├── docs/                        # Documentation
│   ├── reference/               # Detailed reference docs
│   ├── research/                # Research paper series
│   ├── examples/                # Example walkthroughs
│   └── *.md                     # Guides and tutorials
├── diagrams/                    # Architecture diagrams (Mermaid)
├── scripts/                     # Utility scripts
├── cli/                         # CLI interface
│   └── factory_cli.py
├── tests/                       # Test suite
│   ├── unit/
│   ├── integration/
│   ├── validation/
│   └── fixtures/
├── .github/
│   └── workflows/               # CI/CD workflows
├── .cursorrules                 # Factory behavior rules
├── CHANGELOG.md                 # Version history
└── README.md                    # This file
```

## Available Blueprints

| Blueprint | Stack | Description |
|-----------|-------|-------------|
| `python-fastapi` | Python, FastAPI, SQLAlchemy | REST API development |
| `python-streamlit` | Python, Streamlit, Pandas | Data apps and dashboards |
| `ai-agent-development` | Python, LangChain, LangGraph | AI agent systems (single agents) |
| `multi-agent-systems` | Python, LangGraph, LangChain | Orchestrated multi-agent systems |
| `typescript-react` | TypeScript, React, Vite | Web application development |
| `nextjs-fullstack` | TypeScript, Next.js 14+, Prisma | Full-stack React development |
| `java-spring` | Java, Spring Boot, JPA | Enterprise application development |
| `kotlin-spring` | Kotlin, Spring Boot 3, WebFlux | Reactive Kotlin microservices |
| `csharp-dotnet` | C#, .NET 8+, Entity Framework | Enterprise .NET development |
| `n8n-automation` | n8n, JavaScript, REST | Workflow automation |
| `sap-abap` | ABAP, Clean ABAP | SAP ABAP development |
| `sap-rap` | ABAP, RAP, Fiori | SAP RESTful ABAP Programming |
| `sap-cap` | Node.js/Java, CDS, SAP BTP | SAP Cloud Application Programming |
| `sap-cpi-pi` | Groovy, Java, SAP CPI/PI | SAP integration development |

### AI Agent Development Blueprint

The `ai-agent-development` blueprint includes:
- LangChain and LangGraph frameworks
- Streamlit and FastAPI for UI/API
- ChromaDB for vector storage
- Templates for agents, prompts, and workflows
- Default: Research & Development methodology with A10 (Learning) axiom

### Multi-Agent Systems Blueprint (NEW)

The `multi-agent-systems` blueprint includes:
- LangGraph for multi-agent orchestration
- Supervisor/worker patterns
- Agent handoff protocols
- Coordination strategies (task decomposition, consensus)
- Default: A8 (Collaboration) + A10 (Learning) axioms

### Kotlin Spring Blueprint

The `kotlin-spring` blueprint includes:
- Spring Boot 3 with WebFlux
- Kotlin Coroutines for async
- R2DBC for reactive database access
- Kotest and MockK for testing
- Kotlin-idiomatic patterns (data classes, sealed classes, extension functions)

### SAP CPI/PI Blueprint (NEW)

The `sap-cpi-pi` blueprint includes:
- SAP Cloud Platform Integration and PI/PO support
- Groovy scripting with CPI best practices
- iFlow design patterns and error handling
- Spock framework for script testing
- SAP Documentation MCP integration for grounding

## Team Workshop System

### Axiom 0: Love and Trust

The Team Workshop System is grounded in **Axiom 0**:

> "All being and doing is grounded in love and trust."

This foundational axiom precedes all technical axioms (A1-A5) and ensures that collaborative design emerges from:
- Assuming positive intent in all interactions
- Creating from care, not fear
- Trusting team members to contribute their best
- Building systems that serve human flourishing

### Workshop Series Overview

| Workshop | Duration | Games | Output |
|----------|----------|-------|--------|
| **Vision Quest** | 2-3h | Future Headlines, Stakeholder Safari | Team Charter |
| **Ethics Arena** | 2h | Dilemma Duel, Value Auction | Ethics Framework |
| **Stack Safari** | 2-3h | Trade-Off Tetris, Architecture Pictionary | Stack Configuration |
| **Agent Assembly** | 3-4h | Agent Trading Cards, Skill Bingo | Agent Roster |
| **Integration Celebration** | 1.5-2h | Demo Derby, Gratitude Circle | Complete System |

### Game Library

**Creative Games** (Vision & Ideation):
- **Future Headlines**: Write newspaper headlines from 5 years in the future
- **Stakeholder Safari**: Role-play as different stakeholders
- **Dream Demo**: Describe the ideal product demo without constraints

**Strategic Games** (Ethics & Decisions):
- **Dilemma Duel**: Debate ethical scenarios with no perfect answer
- **Value Auction**: Bid limited points on values to reveal priorities
- **Trade-Off Tetris**: Fit constraints into limited capacity

**Collaborative Games** (Design & Celebration):
- **Agent Trading Cards**: Create collectible cards for each agent
- **Skill Bingo**: Fill bingo cards with needed skills
- **Architecture Pictionary**: Draw and guess system components
- **Demo Derby**: Showcase all workshop artifacts
- **Gratitude Circle**: Express appreciation to team members

### Team Size Adaptations

| Size | Format |
|------|--------|
| Small (2-5) | Everyone participates in everything, intimate discussions |
| Medium (6-12) | Breakout groups for games, plenary for synthesis |
| Large (13+) | Representative groups, async pre-work, sync synthesis |

For complete facilitation instructions, see [docs/TEAM_WORKSHOP_GUIDE.md](docs/TEAM_WORKSHOP_GUIDE.md).

## Factory Agents

| Agent | Purpose |
|-------|---------|
| `requirements-architect` | Gather and validate project requirements through 5-phase questionnaire |
| `stack-builder` | Configure technology stack and select appropriate blueprints |
| `workflow-designer` | Design development workflows and trigger integrations |
| `knowledge-manager` | Structure domain knowledge and generate knowledge files |
| `template-generator` | Generate code and document templates |
| `workshop-facilitator` | Facilitate team workshops for collaborative agent system design |
| `onboarding-architect` | Orchestrate onboarding of existing repositories into the factory ecosystem |

## Available Pattern Agents

These agents can be included in generated projects:

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | Review code against best practices, style guides, and quality standards |
| `test-generator` | Generate unit tests, integration tests, and test plans |
| `explorer` | Explore and understand codebases |
| `documentation-agent` | Generate and maintain README, API docs, and ADRs |

## Factory Skills

| Skill | Description |
|-------|-------------|
| `requirements-gathering` | 5-phase interactive requirements elicitation |
| `team-workshop-onboarding` | Collaborative 5-workshop series with games for teams |
| `stack-configuration` | Technology stack selection and configuration |
| `workflow-generation` | Workflow pattern generation and customization |
| `agent-generation` | Agent definition file generation |
| `skill-generation` | Skill definition with references generation |
| `knowledge-generation` | JSON knowledge file generation |
| `template-generation` | Code and document template generation |
| `cursorrules-generation` | .cursorrules file generation |
| `axiom-selection` | Layer 0 axiom configuration including A0 |
| `purpose-definition` | Layer 1 purpose definition (mission, stakeholders, success) |
| `methodology-selection` | Layer 3 methodology selection (Agile/Kanban/R&D) |
| `enforcement-selection` | Enforcement pattern selection (quality, safety, integrity) |
| `practice-selection` | Practice pattern selection (daily, craft, alignment) |
| `pattern-feedback` | Inductive learning from pattern usage |
| `onboarding-flow` | Onboard existing repositories into factory ecosystem |
| `alignment-check` | Verify understanding and alignment before implementations |
| `shell-platform` | Platform-specific shell command handling |
| `readme-validation` | Validate README structure matches actual filesystem |

## Available Pattern Skills

These skills can be included in generated projects:

| Skill | Category | Description |
|-------|----------|-------------|
| `bugfix-workflow` | workflow | Ticket-based bug fix workflow with Jira integration |
| `feature-workflow` | workflow | Specification-based feature implementation |
| `tdd` | testing | Test-driven development workflow |
| `grounding` | verification | Verify data structures before implementation |
| `strawberry-verification` | verification | Hallucination detection using information theory |
| `code-templates` | core | Stack-specific code generation |
| `security-audit` | verification | OWASP-based security vulnerability detection |
| `code-review` | workflow | Structured code review process |

### Agent vs Skill Relationship

```mermaid
flowchart TB
    subgraph Agents["Agents (Orchestrators)"]
        A1["requirements-architect"]
        A2["stack-builder"]
        A3["template-generator"]
    end
    
    subgraph Skills["Skills (Procedures)"]
        S1["requirements-gathering"]
        S2["stack-configuration"]
        S3["agent-generation"]
        S4["skill-generation"]
    end
    
    subgraph Knowledge["Knowledge (Data)"]
        K1["patterns/*.json"]
        K2["blueprints/*.json"]
    end
    
    A1 --> S1
    A2 --> S2
    A3 --> S3
    A3 --> S4
    S1 --> K1
    S2 --> K2
    
    style Agents fill:#e3f2fd
    style Skills fill:#e8f5e9
    style Knowledge fill:#fff3e0
```

## Layered Requirements Gathering

### Depth Options

| Option | Phases | Best For |
|--------|--------|----------|
| **Quick Start** | Pre-Phase + Phase 0 + Phases 1-5 | Rapid prototyping |
| **Standard** | All phases with templates | Most projects |
| **Comprehensive** | All phases + enforcement/practices | Enterprise, critical |

### Pre-Phase: Layer 0 - Axiom Configuration
- Select core axioms (A1-A5 always included)
- Choose optional axioms (A6-A10)
- Configure derivation rules

### Phase 0: Layer 1 - Purpose Definition
- Mission statement (verifiable)
- Primary stakeholders (specific)
- Success criteria (measurable)

### Phases 0.6-0.7: Layers 2-3 (Standard+)
- Ethical boundaries and quality standards
- Methodology selection (Agile/Kanban/R&D/Enterprise)
- Team size and coordination patterns

### Phases 0.8-0.9: Enforcement & Practices (Comprehensive)
- Quality, safety, integrity enforcement
- Daily, craft, alignment practices

### Phases 1-5: Layer 4 - Technical
- Project context and domain
- Technology stack and frameworks
- Workflow triggers and artifacts
- Knowledge domain and conventions
- Agent and skill capabilities

## Generated Project Structure

Generated projects include all 5-layer artifacts:

```
{PROJECT_NAME}/
├── .cursor/
│   ├── agents/               # AI agent definitions
│   └── skills/               # Reusable skill definitions
├── knowledge/                # Structured reference data (JSON)
├── templates/                # Code and document templates
├── workflows/
│   └── methodology.yaml      # Layer 3: Methodology config
├── src/                      # Source code
├── tests/                    # Test files
├── docs/                     # User documentation
├── .cursorrules              # 5-layer agent rules (L0-L4)
├── PURPOSE.md                # Layer 1: Mission & purpose
├── enforcement.yaml          # Enforcement patterns (Comprehensive)
├── practices.yaml            # Team practices (Comprehensive)
└── README.md                 # Project documentation
```

### Key Generated Files

| File | Layer | Description |
|------|-------|-------------|
| `.cursorrules` | 0-4 | Complete 5-layer agent behavior rules |
| `PURPOSE.md` | 1 | Mission, stakeholders, success criteria |
| `enforcement.yaml` | 2+ | Quality, safety, integrity enforcement |
| `practices.yaml` | 3+ | Daily, craft, alignment practices |
| `methodology.yaml` | 3 | Methodology ceremonies and coordination |

```mermaid
flowchart TB
    subgraph Project["Generated Project"]
        subgraph Cursor[".cursor/"]
            A["agents/*.md"]
            S["skills/*/SKILL.md"]
        end
        K["knowledge/*.json"]
        T["templates/*"]
        CR[".cursorrules"]
    end
    
    A -->|"uses"| S
    S -->|"queries"| K
    CR -->|"configures"| A
    
    style Cursor fill:#e3f2fd
    style K fill:#fff3e0
```

## MCP Server Integration

The factory includes **50+ MCP servers** across 6 categories. See the full [MCP Servers Guide](docs/MCP-SERVERS.md) for details.

### Starter Packs

| Pack | Servers | Best For |
|------|---------|----------|
| **Minimal** | filesystem, git, memory | Any project |
| **Web Developer** | + github, postgresql, playwright | Web apps |
| **Data Science** | + jupyter, bigquery, pinecone | Data/ML projects |
| **AI Agent** | + langgraph, knowledge-graph, chromadb | Agent development |
| **Enterprise** | + atlassian, slack, sentry | Team projects |
| **DevOps** | + docker, terraform, datadog | Infrastructure |

### Categories

| Category | Servers |
|----------|---------|
| **Core** | filesystem, git, memory, time, fetch, brave-search, sequentialthinking |
| **Code** | github, gitlab, sentry, playwright, deepwiki, sap-documentation |
| **Data** | postgresql, mongodb, bigquery, snowflake, pinecone, chromadb |
| **Cloud** | docker, terraform, pulumi, datadog |
| **Collab** | atlassian, linear, notion, slack, figma |
| **AI/ML** | huggingface, mlflow, langgraph, ollama, neo4j |

### Quick Start

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git", "--repository", "."]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

For detailed setup instructions, see [docs/MCP-SERVERS.md](docs/MCP-SERVERS.md).

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

> **Tool Paths:** Commands below use default Windows paths from `.cursor/config/tools.json`.
> See [Configuration Guide](docs/CONFIGURATION.md) to customize for your environment.

### Installing Development Dependencies

```powershell
# Install test dependencies
C:\App\Anaconda\Scripts\pip.exe install -r requirements-dev.txt
```

### Running Tests

The project includes a comprehensive pytest-based test suite with unit tests, integration tests, and validation tests.

```powershell
# Run all tests
C:\App\Anaconda\python.exe -m pytest tests/ -v

# Run with coverage report
C:\App\Anaconda\python.exe -m pytest tests/ --cov=scripts --cov=cli --cov-report=html

# Run specific test categories
C:\App\Anaconda\python.exe -m pytest tests/unit/ -v           # Unit tests
C:\App\Anaconda\python.exe -m pytest tests/integration/ -v    # Integration tests
C:\App\Anaconda\python.exe -m pytest tests/validation/ -v     # Schema validation tests

# Run specific test file
C:\App\Anaconda\python.exe -m pytest tests/unit/test_project_config.py -v

# Run tests matching a pattern
C:\App\Anaconda\python.exe -m pytest tests/ -k "blueprint" -v
```

For detailed testing documentation, see [docs/TESTING.md](docs/TESTING.md).

### Test Suite Structure

```
tests/
├── conftest.py                 # Shared pytest fixtures
├── unit/                       # Unit tests (60 tests)
│   ├── test_project_config.py  # ProjectConfig dataclass tests
│   ├── test_project_generator.py # ProjectGenerator class tests
│   └── test_pattern_loading.py # Pattern/blueprint loading tests
├── integration/                # Integration tests (38 tests)
│   ├── test_cli.py             # CLI command tests
│   └── test_generation.py      # End-to-end generation tests
├── validation/                 # Schema validation tests (33 tests)
│   ├── test_blueprint_schema.py
│   ├── test_pattern_schema.py
│   └── test_knowledge_schema.py
└── fixtures/                   # Test fixture files
    ├── sample_config.yaml
    ├── sample_config.json
    └── minimal_blueprint.json
```

### Manual CLI Testing

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
# Generate test project from blueprint
C:\App\Anaconda\python.exe cli\factory_cli.py --blueprint python-fastapi --output C:\Temp\test-project

# Generate from config file
C:\App\Anaconda\python.exe cli\factory_cli.py --config tests\fixtures\sample_config.yaml --output C:\Temp\yaml-project
```

### Continuous Integration

The project uses GitHub Actions for CI/CD. Tests run automatically on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

The CI pipeline includes:
- **Test Matrix**: Python 3.10, 3.11, 3.12 on Ubuntu and Windows
- **Code Quality**: Ruff linter checks
- **JSON Validation**: Syntax validation for all JSON files
- **Generation Test**: End-to-end project generation verification

See `.github/workflows/ci.yml` for the full configuration.

## Example Walkthroughs

Complete, step-by-step examples showing the factory in action with real technology stacks:

| Example | Blueprint | Description |
|---------|-----------|-------------|
| [REST API Service](docs/examples/01-rest-api-service/) | python-fastapi | Python FastAPI with Jira integration |
| [Full-Stack Next.js](docs/examples/02-fullstack-nextjs-app/) | nextjs-fullstack | Next.js 14 with Prisma and auth |
| [RAG Chatbot](docs/examples/03-rag-chatbot-agent/) | ai-agent-development | LangChain RAG with Streamlit |
| [Multi-Agent System](docs/examples/04-multi-agent-research-system/) | multi-agent-systems | LangGraph supervisor/worker pattern |
| [SAP Fiori](docs/examples/05-sap-fiori-integration/) | sap-abap | RAP application with MCP grounding |
| [.NET Enterprise](docs/examples/06-dotnet-enterprise-api/) | csharp-dotnet | Clean Architecture with EF Core |
| [Kotlin Microservice](docs/examples/07-kotlin-spring-microservice/) | kotlin-spring | Reactive Spring Boot with coroutines |
| [SAP CPI Integration](docs/examples/08-sap-cpi-integration/) | sap-cpi-pi | Groovy scripting with iFlow patterns |

Each example includes a complete walkthrough, sample answers, and expected output files for verification.

## Documentation

### Comprehensive Reference

| Document | Description |
|----------|-------------|
| **[Factory Reference](docs/FACTORY_REFERENCE.md)** | **Start here** - Complete overview of the factory with links to detailed references |
| [Blueprints Reference](docs/reference/BLUEPRINTS.md) | All 12 technology blueprints with detailed specifications |
| [Patterns Reference](docs/reference/PATTERNS.md) | Agent, skill, axiom, methodology, and other patterns |
| [Knowledge Files Reference](docs/reference/KNOWLEDGE_FILES.md) | All 32 knowledge files categorized and explained |
| [Factory Components Reference](docs/reference/FACTORY_COMPONENTS.md) | Factory's own 7 agents and 19 skills |
| [Generated Output Reference](docs/reference/GENERATED_OUTPUT.md) | What gets generated: structure, formats, examples |

### Guides and Tutorials

| Document | Description |
|----------|-------------|
| [Usage Guide](docs/USAGE_GUIDE.md) | Detailed usage instructions and examples |
| [Team Workshop Guide](docs/TEAM_WORKSHOP_GUIDE.md) | Complete facilitator's manual for team workshops |
| [Example Walkthroughs](docs/examples/) | Complete end-to-end examples with real stacks |
| [Layered Architecture](docs/LAYERED_ARCHITECTURE.md) | 5-layer architecture guide |
| [Onboarding Concept](docs/LAYERED_ONBOARDING_CONCEPT.md) | Full implementation blueprint |
| [Extension Guide](docs/EXTENSION_GUIDE.md) | How to extend the factory with new blueprints, patterns, and skills |
| [Testing Guide](docs/TESTING.md) | Test suite documentation and testing practices |
| [SAP Grounding Design](docs/SAP_GROUNDING_DESIGN.md) | SAP-specific grounding architecture and MCP integration |

### Research Paper Series

Comprehensive academic documentation of the methodology (~150 pages, CC0 licensed):

| Paper | Description |
|-------|-------------|
| [Axiom-Based Agent Architecture](docs/research/AXIOM_BASED_AGENT_ARCHITECTURE.md) | Core methodology: 5-layer system, axioms A1-A10, derivation rules |
| [Sacred Psychology in Software Engineering](docs/research/SACRED_PSYCHOLOGY_SOFTWARE_ENGINEERING.md) | Psychological enforcement, philosophical techniques |
| [Constitutional AI - Convergent Discovery](docs/research/CONSTITUTIONAL_AI_CONVERGENT_DISCOVERY.md) | Comparison with Anthropic Constitutional AI |
| [Building Value-Aligned Agents](docs/research/BUILDING_VALUE_ALIGNED_AGENTS.md) | Practical step-by-step implementation guide |
| [Future of Value-Aligned AI](docs/research/FUTURE_OF_VALUE_ALIGNED_AI.md) | Synthesis, unified framework, recommendations |
| [Architecture Diagrams](docs/research/ARCHITECTURE_DIAGRAMS.md) | Visual diagrams of all architectures |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add patterns, blueprints, or skills
4. Test generation
5. Submit pull request

## Keywords

`cursor-ide` `ai-agents` `llm-automation` `code-generation` `agent-orchestration` `meta-programming` `project-scaffolding` `development-workflow` `mcp-servers` `ai-assisted-development` `cursor-rules` `agent-factory` `skill-composition` `knowledge-management` `prompt-engineering`

**Categories:**
- **AI Development Tools**: Cursor IDE agent system generator, LLM behavior configuration
- **Code Generation**: Project scaffolding, template-based generation, multi-stack support
- **Agent Architecture**: Agent/skill composition patterns, knowledge-grounded workflows
- **Enterprise Integration**: SAP, Jira, Confluence, GitHub via MCP servers

## Acknowledgements & Inspirations

This project incorporates ideas and patterns from several valuable sources:

| Source | Contribution |
|--------|--------------|
| **[Augmented Coding Patterns](https://lexler.github.io/augmented-coding-patterns/)** | Active Partner, Check Alignment, Chain of Small Steps, and other AI collaboration patterns. Created by Lada Kesseler, Nitsan Avni, Ivett Ördög, Llewellyn Falco, and contributors. |
| **[Leon Chlon](https://github.com/lchlon)** | Inspiration for the Strawberry Verification skill - information-theoretic approach to hallucination detection in AI outputs. |
| **[ai-dev-agent](https://github.com/gitwalter/ai-dev-agent)** | Pedagogical toolkit for AI agent systems that inspired the layered architecture and methodology integration concepts. |

## License

MIT License

---

*Cursor Agent Factory v2.6.0*  
*Meta-system for generating Cursor AI agent development systems*  
*Now with 5-layer architecture: Integrity → Purpose → Principles → Methodology → Technical*  
*50+ MCP servers across 6 categories with starter packs and role-based recommendations*
