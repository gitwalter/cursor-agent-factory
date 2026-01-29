# Changelog

All notable changes to the Cursor Agent Factory project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-01-29

### Added

- **Onboarding Flow** - Non-destructive integration for existing repositories
  - CLI commands: `--analyze`, `--onboard`, `--dry-run`, `--rollback`
  - Repository analyzer to detect existing Cursor artifacts and tech stack
  - Backup manager with session-based rollback support
  - Merge strategy with interactive conflict resolution
  - 5 onboarding scenarios: FRESH, MINIMAL, PARTIAL, UPGRADE, COMPLETE

- **New Scripts**
  - `scripts/repo_analyzer.py` - Detect existing artifacts and technology stack
  - `scripts/backup_manager.py` - Backup/rollback session management
  - `scripts/merge_strategy.py` - Conflict detection and resolution

- **New Agent**
  - `onboarding-architect` - Orchestrates repository onboarding process

- **New Skill**
  - `onboarding-flow` - Step-by-step onboarding process skill

- **Documentation**
  - `docs/ONBOARDING_GUIDE.md` - Complete user guide for onboarding existing repos

- **Test Fixtures**
  - `tests/fixtures/existing_repo_fresh/` - FRESH scenario fixture
  - `tests/fixtures/existing_repo_minimal/` - MINIMAL scenario fixture
  - `tests/fixtures/existing_repo_partial/` - PARTIAL scenario fixture

### Changed

- Updated `cli/factory_cli.py` with onboarding commands
- Updated `scripts/generate_project.py` with onboarding mode support

## [2.0.0] - 2026-01-29

### Added

- **5-Layer Architecture** - Deductive-inductive architecture for grounded agent systems
  - Layer 0: Integrity & Logic - Core axioms (A1-A5), optional axioms (A6-A10), derivation rules
  - Layer 1: Purpose - Mission, stakeholders, success criteria (`PURPOSE.md`)
  - Layer 2: Principles - Ethical boundaries, quality standards, failure handling
  - Layer 3: Methodology - Agile/Kanban/R&D/Enterprise templates, enforcement, practices
  - Layer 4: Technical - Stack, agents, skills, templates

- **New Skills (7)**
  - `axiom-selection` - Layer 0 axiom configuration
  - `purpose-definition` - Layer 1 purpose definition
  - `methodology-selection` - Layer 3 methodology selection
  - `enforcement-selection` - Enforcement pattern configuration
  - `practice-selection` - Practice pattern configuration
  - `pattern-feedback` - Inductive learning from experience
  - `alignment-check` - Verify understanding before major changes

- **New Patterns**
  - `patterns/axioms/` - Core and optional axiom definitions
  - `patterns/principles/` - Ethical boundaries, quality standards, failure handling
  - `patterns/methodologies/` - Agile Scrum, Kanban, R&D, Enterprise Integration
  - `patterns/enforcement/` - Quality, Safety, Integrity enforcement patterns
  - `patterns/practices/` - Daily, Craft, Alignment practice patterns

- **New Blueprints**
  - `ai-agent-development` - LangChain/LangGraph AI agent development stack
  - `multi-agent-systems` - Orchestrated multi-agent systems with supervisor/worker patterns
  - `kotlin-spring` - Reactive Kotlin microservices with Spring Boot 3, WebFlux, and coroutines
  - `sap-cpi-pi` - SAP CPI/PI integration development with Groovy and Java

- **Example Walkthroughs** - Complete end-to-end examples in `docs/examples/`
  - `01-rest-api-service` - Python FastAPI with Jira integration (Agile Scrum)
  - `02-fullstack-nextjs-app` - Next.js 14 with Prisma (Kanban)
  - `03-rag-chatbot-agent` - LangChain RAG with Streamlit (R&D, A10 Learning)
  - `04-multi-agent-research-system` - LangGraph supervisor/worker (R&D, A8 Collaboration)
  - `05-sap-fiori-integration` - SAP RAP with MCP grounding (Enterprise, Comprehensive)
  - `06-dotnet-enterprise-api` - C# Clean Architecture (Agile Scrum)
  - `07-kotlin-spring-microservice` - Kotlin WebFlux (Kanban)
  - `08-sap-cpi-integration` - SAP CPI Groovy scripting (Kanban)
  - Each includes README.md, WALKTHROUGH.md, and expected-output/ reference files
  - Reference files use `.example` extension to prevent factory interference

- **New Knowledge Files**
  - `knowledge/groovy-patterns.json` - Groovy scripting best practices for SAP CPI
  - `knowledge/iflow-patterns.json` - Integration flow design patterns

- **New Templates**
  - `templates/integration/groovy/base-script.groovy.tmpl` - Base Groovy script template
  - `templates/integration/groovy/message-mapping.groovy.tmpl` - Message mapping template
  - `templates/integration/test/script-test.groovy.tmpl` - Spock test template

- **New Knowledge Files**
  - `knowledge/langchain-patterns.json` - LangChain best practices
  - `knowledge/langgraph-workflows.json` - LangGraph state machine patterns
  - `knowledge/agent-coordination.json` - Multi-agent coordination patterns
  - `knowledge/prompt-engineering.json` - Prompt optimization techniques
  - `knowledge/augmented-coding-patterns.json` - AI collaboration patterns from lexler.github.io

- **New Templates**
  - `templates/ai/agent/base-agent.py.tmpl` - Base AI agent template
  - `templates/ai/prompt/system-prompt.md.tmpl` - System prompt template
  - `templates/ai/workflow/langgraph-graph.py.tmpl` - LangGraph workflow template
  - `templates/factory/PURPOSE.md.tmpl` - Purpose document template
  - `templates/factory/enforcement.yaml.tmpl` - Enforcement configuration template
  - `templates/factory/practices.yaml.tmpl` - Practices configuration template
  - `templates/methodology/methodology.yaml.tmpl` - Methodology configuration template

- **Documentation**
  - `docs/LAYERED_ARCHITECTURE.md` - Complete 5-layer architecture guide
  - `docs/LAYERED_ONBOARDING_CONCEPT.md` - Implementation blueprint
  - Acknowledgements section in README for external inspirations

- **Research Paper Series** - Comprehensive documentation of methodology (`docs/research/`)
  - `AXIOM_BASED_AGENT_ARCHITECTURE.md` - Core methodology: 5-layer system, axioms A1-A10, derivation rules, validation constraints (~30 pages)
  - `SACRED_PSYCHOLOGY_SOFTWARE_ENGINEERING.md` - Psychological enforcement, three-layer architecture, philosophical software techniques (~25 pages)
  - `CONSTITUTIONAL_AI_CONVERGENT_DISCOVERY.md` - Comparison with Anthropic Constitutional AI, convergent discovery analysis (~20 pages)
  - `BUILDING_VALUE_ALIGNED_AGENTS.md` - Practical step-by-step implementation guide (~35 pages)
  - `FUTURE_OF_VALUE_ALIGNED_AI.md` - Synthesis, unified framework, recommendations for AI companies/developers/researchers/policymakers (~20 pages)
  - `ARCHITECTURE_DIAGRAMS.md` - 10 Mermaid diagrams visualizing all architectures
  - `REFERENCES.md` - Complete academic bibliography with citations
  - All papers released under Creative Commons CC0 1.0

### Changed

- Updated `.cursorrules` with Active Partner and Check Alignment patterns
- Updated `templates/factory/cursorrules-template.md` with 5-layer structure
- Updated `.cursor/skills/requirements-gathering/SKILL.md` with layered onboarding flow
- Updated `README.md` with v2.0 features and Acknowledgements
- Updated `docs/USAGE_GUIDE.md` with 5-layer architecture guide
- Updated `patterns/skills/strawberry-verification.json` with Leon Chlon credits

### Credits

- [Augmented Coding Patterns](https://lexler.github.io/augmented-coding-patterns/) - Lada Kesseler, Nitsan Avni, Ivett Ördög, Llewellyn Falco
- [Leon Chlon](https://github.com/lchlon) - Strawberry Verification inspiration (Pythea)
- [ai-dev-agent](https://github.com/gitwalter/ai-dev-agent) - Layered architecture concepts

## [1.2.0] - 2026-01-28

### Added

- **New Knowledge Files**
  - `knowledge/design-patterns.json` - Gang of Four and modern design patterns with stack-specific examples
  - `knowledge/security-checklist.json` - OWASP Top 10, authentication patterns, and security best practices
  - `knowledge/architecture-patterns.json` - Microservices, monolith, serverless, and deployment patterns

- **New Blueprints**
  - `nextjs-fullstack` - Full-stack TypeScript development with Next.js 14+, Prisma, and Tailwind CSS
  - `csharp-dotnet` - Enterprise .NET 8+ development with ASP.NET Core, Entity Framework, and Clean Architecture

- **New Agent Pattern**
  - `documentation-agent` - Auto-generate and maintain READMEs, API docs, ADRs, and changelogs

- **New Skill Patterns**
  - `security-audit` - OWASP-based security vulnerability detection and remediation guidance
  - `code-review` - Structured code review covering correctness, style, performance, security, and maintainability

- **New MCP Server Integrations**
  - `notion` - Notion workspace integration for docs and databases
  - `linear` - Linear issue tracking and project management
  - `sentry` - Error tracking and performance monitoring

### Changed

- Updated `mcp-servers-catalog.json` with new servers and stack mappings
- Updated `README.md` with new blueprints, agents, skills, and MCP servers
- Updated `docs/USAGE_GUIDE.md` with new blueprint options

## [1.1.0] - 2026-01-28

### Added

- **Comprehensive Test Suite** - 131 pytest-based tests covering:
  - Unit tests (60 tests) for `ProjectConfig` and `ProjectGenerator` classes
  - Integration tests (38 tests) for CLI commands and end-to-end generation
  - Validation tests (33 tests) for JSON schema validation of blueprints, patterns, and knowledge files

- **Test Infrastructure**
  - `tests/` directory with organized test structure
  - `tests/conftest.py` with shared pytest fixtures
  - `tests/fixtures/` with sample configuration files for testing

- **CI/CD Pipeline**
  - `.github/workflows/ci.yml` - GitHub Actions workflow
  - Test matrix: Python 3.10, 3.11, 3.12 on Ubuntu and Windows
  - Code quality checks with Ruff linter
  - JSON syntax validation
  - End-to-end generation verification
  - Coverage reporting with Codecov integration

- **Documentation**
  - `docs/TESTING.md` - Comprehensive testing documentation
  - `requirements-dev.txt` - Development dependencies (pytest, pytest-cov, jsonschema)
  - Updated `README.md` with test running instructions and CI badge

### Changed

- Updated `README.md` with:
  - CI status badge
  - Detailed test running instructions
  - Test suite structure documentation
  - Link to testing documentation
  - Continuous Integration section

## [1.0.0] - 2026-01-XX

### Added

- Initial release of Cursor Agent Factory
- Project generation engine (`scripts/generate_project.py`)
- CLI interface (`cli/factory_cli.py`)
- Blueprint system for technology stacks:
  - `python-fastapi`
  - `typescript-react`
  - `java-spring`
  - `sap-abap`
- Pattern library for agents and skills
- Knowledge files for skill catalog, stack capabilities, and best practices
- Factory agents: requirements-architect, stack-builder, workflow-designer, knowledge-manager, template-generator
- Factory skills: requirements-gathering, stack-configuration, workflow-generation, agent-generation, skill-generation, knowledge-generation, template-generation, cursorrules-generation
- MCP server integration support (Atlassian, SAP Documentation, DeepWiki, SequentialThinking)
- `.cursorrules` template for generated projects
- Documentation: README.md, USAGE_GUIDE.md, EXTENSION_GUIDE.md, SAP_GROUNDING_DESIGN.md
