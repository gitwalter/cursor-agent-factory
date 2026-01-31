# Changelog

All notable changes to the Cursor Agent Factory project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.2.4] - 2026-01-31

### Added - Team-Independent Knowledge Management for Generated Projects

Generated projects now include a complete, self-sufficient knowledge management system that allows teams to extend, evolve, and receive updates independently.

#### Three Knowledge Capabilities

| Capability | Agent | Direction | Commands |
|------------|-------|-----------|----------|
| **Extend** | `knowledge-extender` | Team → Project | "extend knowledge for [topic]" |
| **Evolve** | `knowledge-evolution` | Project → Future | "check knowledge status" |
| **Receive** | `factory-updates` | Factory → Project | "check for Factory updates" |

#### New Pattern Files

| File | Purpose |
|------|---------|
| `patterns/agents/knowledge-extender.json` | Add new knowledge to projects |
| `patterns/agents/knowledge-evolution.json` | Track and manage project knowledge |
| `patterns/agents/factory-updates.json` | Receive updates from Factory |
| `patterns/skills/extend-knowledge.json` | Core extension workflow |
| `patterns/skills/receive-updates.json` | Core update workflow |

#### New Knowledge & Templates

| File | Purpose |
|------|---------|
| `knowledge/factory-updates.json` | Update feed for generated projects |
| `templates/knowledge/manifest.json.tmpl` | Project manifest template |
| `templates/knowledge/project-info.json.tmpl` | Project origin tracking |

#### Updated Blueprints (5)

All major blueprints now include knowledge management:
- `python-fastapi`
- `typescript-react`
- `ai-agent-development`
- `java-spring`
- `csharp-dotnet`

Each blueprint now includes:
- `knowledge-extender` agent
- `knowledge-evolution` agent
- `factory-updates` agent
- `extend-knowledge` skill
- `receive-updates` skill

#### Documentation Updates

| Document | Changes |
|----------|---------|
| `docs/USAGE_GUIDE.md` | Added "Knowledge Management (Team-Independent)" and "Receiving Factory Updates" sections |
| `docs/reference/GENERATED_OUTPUT.md` | Updated section 3.5 with full knowledge system |
| `docs/EXTENSION_GUIDE.md` | Added chat-based extension workflow |
| `README.md` | Added "Factory → Generated Project Updates" section |

#### Factory Update Channel

Generated projects can now receive updates from the Factory:
- Update feed at `knowledge/factory-updates.json`
- Channels: `stable` (production) and `latest` (early adopters)
- Updates are filtered by blueprint applicability
- User confirms before applying updates

---

## [3.2.3] - 2026-01-31

### Improved - Comprehensive Artifact Dependency Tracking

Enhanced the artifact-dependencies.json to include documentation as dependent artifacts, enabling reliable detection of what needs updating.

#### Dependency Map Improvements (v1.1.0)

| Feature | Description |
|---------|-------------|
| `documentation_map` | Maps artifact types to their doc sections with regex patterns |
| `factory_artifact_detection` | Lists all Factory agents (9) and skills (21) for reliable detection |
| `post_extension_checklist` | 9-step checklist with specific conditions for each step |
| `factory_agent_created` rule | Explicit rule for Factory agents → FACTORY_COMPONENTS.md |
| `factory_skill_created` rule | Explicit rule for Factory skills → FACTORY_COMPONENTS.md |

#### Updated Artifacts

- `knowledge/artifact-dependencies.json` - Version 1.1.0 with comprehensive documentation tracking
- `.cursorrules` - Rule 6 now includes explicit documentation steps
- `.cursor/skills/extend-knowledge/SKILL.md` - Step 0 updated with Factory detection logic

---

## [3.2.2] - 2026-01-31

### Added - Algorithmic Trading Knowledge Extension

Extended trading patterns with advanced technical indicators, fundamental data fetching, backtesting frameworks, and strategy building patterns.

#### Knowledge Updates

| File | Version | Changes |
|------|---------|---------|
| `knowledge/trading-patterns.json` | 1.1.0 | Added 5 major sections |

#### New Sections

| Section | Description |
|---------|-------------|
| `technical_indicators_advanced` | Ichimoku, Fibonacci, VWAP, ATR stops, Heikin-Ashi, Elder Ray |
| `fundamental_data_fetching` | yfinance, Alpha Vantage, SEC EDGAR, Piotroski F-Score |
| `backtesting_frameworks` | VectorBT, Backtrader, walk-forward optimization, Monte Carlo |
| `strategy_building_patterns` | Base strategy, multi-factor, regime-aware, portfolio construction |
| `data_sources` | Free and paid data providers with caching patterns |

#### New Skill

| Skill | Description |
|-------|-------------|
| `.cursor/skills/algo-trading/SKILL.md` | Complete guide for building trading systems |

#### Updated Artifacts

- `knowledge/manifest.json` - Added trading-patterns.json entry (v1.1.0), updated file count to 67
- `knowledge/skill-catalog.json` - Registered algo-trading skill
- `docs/reference/KNOWLEDGE_FILES.md` - Added Trading/Quant category, updated count to 67
- `docs/reference/FACTORY_COMPONENTS.md` - Added knowledge-extender agent, knowledge-evolution agent, extend-knowledge skill, update-knowledge skill, Knowledge Extension flow diagram

---

## [3.2.1] - 2026-01-31

### Added - CrewAI Knowledge Extension & Post-Extension Automation

Extended CrewAI patterns with advanced orchestration features and integrated mandatory post-extension automation into the Factory system.

#### Knowledge Updates

| File | Changes |
|------|---------|
| `knowledge/crewai-patterns.json` | Added 5 new pattern sections (v1.1.0) |

#### New Sections in CrewAI Patterns

| Section | Description |
|---------|-------------|
| `flow_patterns` | State management with Flows (basic, conditional, parallel) |
| `pipeline_patterns` | Pipeline orchestration for chaining crews |
| `knowledge_patterns` | Adding knowledge sources (string, file, PDF) |
| `training_patterns` | Training crews for improved outputs |
| `kickoff_patterns` | Async and batch execution patterns |

#### New Skill

| Skill | Description |
|-------|-------------|
| `.cursor/skills/crewai-workflow/SKILL.md` | Step-by-step guide for CrewAI workflows |

#### Post-Extension Automation (MANDATORY)

Integrated systematic post-extension workflow into Factory rules (`.cursorrules` Rule 6):

| Step | Artifact | Action |
|------|----------|--------|
| 1 | `knowledge/manifest.json` | Bump version, update timestamp, add change_history |
| 2 | `knowledge/skill-catalog.json` | Register new skills, update category lists |
| 3 | `docs/reference/KNOWLEDGE_FILES.md` | Update descriptions for modified knowledge |
| 4 | `CHANGELOG.md` | Add version entry with change tables |
| 5 | JSON validation | Run `python -c "import json; json.load(...)"` |
| 6 | Git operations | Ask user before commit/push |

#### Artifact Dependency Map

Created `knowledge/artifact-dependencies.json` for systematic detection of what to update:

| Artifact Type | Must Update |
|---------------|-------------|
| New knowledge file | manifest.json, KNOWLEDGE_FILES.md, CHANGELOG.md |
| Extended knowledge | manifest.json (bump version), CHANGELOG.md |
| New skill | skill-catalog.json, CHANGELOG.md |
| New agent | CHANGELOG.md |
| New template | CHANGELOG.md |
| New blueprint | BLUEPRINTS.md, CHANGELOG.md |

#### Updated Artifacts

- `.cursorrules` - Added Rule 6: Post-Extension Automation
- `.cursor/skills/extend-knowledge/SKILL.md` - Added Post-Extension Automation section with detection
- `.cursor/agents/knowledge-extender.md` - Updated workflow diagram and rules
- `knowledge/artifact-dependencies.json` - NEW: Dependency mapping for automation
- `knowledge/manifest.json` - Version bumped to 1.1.0 for crewai-patterns.json, added artifact-dependencies
- `knowledge/skill-catalog.json` - Registered crewai-workflow skill
- `docs/reference/KNOWLEDGE_FILES.md` - Updated CrewAI description

---

## [3.2.0] - 2026-01-31

### Added - Knowledge Evolution System

This release introduces a comprehensive **Knowledge Evolution System** that automatically keeps the Factory's knowledge base current with the latest best practices from multiple trusted sources.

#### Core Components

| Component | Description |
|-----------|-------------|
| **Source Adapters** | GitHub, PyPI, NPM, official docs, community, user feedback |
| **Configuration Manager** | Unified settings with environment variable support |
| **Update Engine** | Merge, backup, rollback, conflict resolution |
| **Notification System** | Configurable alerts for available updates |
| **Changelog Generator** | Automatic documentation of all changes |

#### New Files

##### Scripts (`scripts/`)
- `config_manager.py` - Centralized configuration management
- `source_aggregator.py` - Multi-source update aggregation
- `update_engine.py` - Update processing and merging
- `conflict_resolver.py` - Conflict detection and resolution
- `notification_system.py` - User notification system
- `changelog_generator.py` - Automatic changelog generation

##### Adapters (`scripts/adapters/`)
- `base_adapter.py` - Abstract adapter interface
- `github_adapter.py` - GitHub releases and trending
- `pypi_adapter.py` - Python package updates
- `npm_adapter.py` - JavaScript/TypeScript packages
- `docs_adapter.py` - Official documentation
- `community_adapter.py` - Community sources
- `feedback_adapter.py` - User feedback learning

##### Schemas (`knowledge/schemas/`)
- `versioning-schema.json` - Knowledge file versioning
- `changelog-schema.json` - Changelog format

##### Configuration
- `.cursor/config/settings.json` - Unified configuration (migrates from tools.json)
- `.cursor/config/settings-schema.json` - Configuration schema

##### Skills
- `.cursor/skills/system-configuration/SKILL.md` - Interactive system configuration
- `.cursor/skills/update-knowledge/SKILL.md` - Knowledge update management

##### Agents
- `.cursor/agents/knowledge-evolution.md` - Orchestrates knowledge updates

##### Documentation
- `docs/KNOWLEDGE_EVOLUTION.md` - Complete system documentation
- `knowledge/manifest.json` - Central version tracking

#### Update Modes

| Mode | Description |
|------|-------------|
| `stability_first` | Lock versions, explicit approval required |
| `awareness_hybrid` | Notify of updates, user approves (default) |
| `freshness_first` | Auto-apply non-breaking changes |
| `subscription` | Subscribe to specific knowledge files |

#### Features

- **Multi-source aggregation** - Parallel fetching from all configured sources
- **Configurable merge strategies** - Conservative, balanced, aggressive
- **Full rollback support** - Backup before update, easy restore
- **Conflict resolution** - Detect and resolve merge conflicts
- **User customization preservation** - Don't overwrite user changes
- **Schema validation** - All updates validated
- **Source traceability** - Full attribution for every change

#### Tests

- `tests/unit/test_config_manager.py` - Configuration tests
- `tests/unit/test_adapters.py` - Adapter unit tests

---

## [3.1.0] - 2026-01-31

### Added - Enhanced Onboarding Experience

This release transforms the onboarding experience into a more delightful, professional journey that captures team spirit and wisdom.

#### New Onboarding Paths

- **Unified Portal** (`docs/GETTING_STARTED.md`) - Single entry point that guides users to their ideal onboarding path
- **Express Lane** (`.cursor/skills/express-onboarding/SKILL.md`) - 10-15 minute individual onboarding with guided prompts and celebrations
- **Team Huddle** (`.cursor/skills/team-huddle-onboarding/SKILL.md`) - 1-2 hour condensed workshop for small teams (2-5 people)
- **Wisdom Harvest** (`.cursor/skills/wisdom-harvest/SKILL.md`) - Structured knowledge capture for team lessons learned and best practices

#### New Documentation

- `docs/GETTING_STARTED.md` - Unified onboarding portal with path selection guide
- `docs/FIRST_WEEK_GUIDE.md` - Post-onboarding coaching for days 1-5
- `templates/factory/celebration-messages.json` - Celebration moments and visual elements

#### New Skills

| Skill | Duration | Description |
|-------|----------|-------------|
| `express-onboarding` | 10-15 min | Fast individual setup with values, stack, and wisdom capture |
| `team-huddle-onboarding` | 1-2 hours | Condensed team workshop with mini-games |
| `wisdom-harvest` | 5-30 min | Structured capture of team knowledge and lessons |

#### Improvements

- Added celebration moments throughout onboarding flows
- Updated README.md with new onboarding paths
- Updated QUICKSTART.md with cross-references
- Updated USAGE_GUIDE.md with new quick links
- Updated .cursorrules with new skills

### Path Comparison

| Path | Team Size | Duration | Best For |
|------|-----------|----------|----------|
| Express Lane | 1 person | 10-15 min | Quick personal setup |
| Team Huddle | 2-5 people | 1-2 hours | Small team alignment |
| Workshop Series | 6+ people | 11-15 hours | Enterprise transformation |

## [3.0.0] - 2026-01-31

### Added - AI/ML Factory Expansion

This major release adds comprehensive AI/ML capabilities with 12 new knowledge files and 8 new blueprints.

#### New Knowledge Files (12 files)

**Foundational ML:**
- `ml-workflow-patterns.json` - Framework-agnostic ML patterns (train/test, cross-validation, pipelines)
- `deep-learning-patterns.json` - PyTorch/TensorFlow training, optimization, checkpointing
- `mlops-patterns.json` - MLflow, Weights & Biases, TensorBoard experiment tracking
- `llm-provider-comparison.json` - OpenAI, Anthropic, Google, Ollama comparison with pricing

**AI Application Patterns:**
- `vector-database-patterns.json` - ChromaDB, Qdrant, Pinecone, FAISS, pgvector
- `huggingface-patterns.json` - Transformers, Datasets, PEFT, Hub integration
- `rag-patterns.json` - RAG architecture, chunking, retrieval, RAGAS evaluation
- `multi-agent-patterns.json` - Consolidated CrewAI, AutoGen, LangGraph patterns

**Advanced AI:**
- `llm-evaluation-patterns.json` - RAGAS, LLM-as-judge, automated testing
- `model-serving-patterns.json` - FastAPI, vLLM, BentoML deployment
- `llm-fine-tuning-patterns.json` - LoRA, QLoRA, DPO, ORPO patterns
- `prompt-library.json` - Reusable prompt templates for common tasks

#### New Blueprints (8 blueprints)

**Production AI/ML:**
- `python-ml-experimentation` - ML research with PyTorch, scikit-learn, MLflow
- `python-deep-learning` - Deep learning with Transformers, PEFT, Accelerate
- `python-rag-system` - Production RAG with LangChain, vector databases
- `python-multi-agent` - Multi-agent systems with CrewAI, AutoGen, LangGraph
- `python-fine-tuning` - LLM fine-tuning with LoRA, QLoRA, TRL

**Starter/Onboarding Blueprints:**
- `starter-ml-classification` - Beginner ML classification (notebooks + patterns)
- `starter-chatbot` - Beginner LLM chatbot with OpenAI and Streamlit
- `starter-rag` - Beginner RAG application with LangChain and ChromaDB

#### Enhanced Blueprints

- `ai-agent-development` - Updated to v2.0.0 with expanded knowledge files and latest LLM models

### Framework Coverage

**Foundational Frameworks:** PyTorch, TensorFlow/Keras, scikit-learn, Hugging Face  
**Orchestration Frameworks:** LangChain, LangGraph, CrewAI, AutoGen  
**Infrastructure:** MLflow, W&B, ChromaDB, Qdrant, Pinecone, vLLM, BentoML  
**LLM Providers:** OpenAI (GPT-4o, o1), Anthropic (Claude 3.5), Google (Gemini), Ollama

### Documentation

- Updated `docs/reference/BLUEPRINTS.md` with new AI/ML blueprints
- Updated `docs/reference/KNOWLEDGE_FILES.md` with new AI/ML knowledge
- Updated `README.md` with AI/ML blueprint listings
- Updated `docs/QUICKSTART.md` with new blueprint options

---

## [2.8.0] - 2026-01-30

### Added

- **Generalized Grounding Verification System** - Universal two-pass verification for all LLM grounding scenarios
  - Base pattern `grounding-verification.json` with confidence delta algorithm
  - 5 verification profiles: strawberry, code, documentation, data, security
  - Configurable thresholds per profile (standard, relaxed, strict, very strict)
  - Trigger options: always, on_medium_confidence, on_critical_claim, on_conflict, manual

- **Grounding Verification Skill** - New base skill for unified verification
  - `.cursor/skills/grounding-verification/SKILL.md` - Comprehensive skill documentation
  - Profile-based verification with domain-specific scrubbing rules
  - Error handling with fallbacks for parse failures and conflicting verdicts

- **Profile-Specific Scrubbing Rules**
  - `strawberry`: Tables, fields, classes, functions, numbers, strings, paths, URLs
  - `code`: Classes, functions, methods, variables, types, paths, line numbers, modules
  - `documentation`: Versions, endpoints, config keys, parameters, values, commands
  - `data`: Tables, columns, data types, constraints, indexes, schemas
  - `security`: CVEs, vulnerabilities, attack vectors, algorithms, keys, permissions

### Changed

- **Strawberry Verification Pattern** - Refactored to extend base pattern (v3.0.0)
  - Now references `grounding-verification.json` as base
  - Profile-specific implementation with strawberry defaults
  - Reduced duplication by inheriting shared components

- **Grounding Skill** - Now opts into verification with data profile (v1.1.0)
  - Added `verification.enabled: true, profile: data, trigger: on_medium_confidence`
  - New Step 5: Run Grounding Verification before handling unverified claims

- **Security Audit Skill** - Now opts into verification with security profile (v1.1.0)
  - Added `verification.enabled: true, profile: security, trigger: always`
  - New Step 8: Verify Security Claims with very strict thresholds (delta >= 0.4)
  - Report now includes verification summary section

### Philosophy

This release generalizes the Pythea/Strawberry verification concept into a **universal grounding verification system**:

> "If removing specific identifiers from evidence doesn't significantly change LLM confidence, the evidence may not have been used - indicating potential confabulation."

Key design principles:
- **Configurable** - Skills opt-in by selecting a profile matching their domain
- **DRY** - Core algorithm defined once, reused across all profiles
- **Extensible** - New profiles can be added without modifying base pattern
- **Non-breaking** - Existing skills work unchanged; verification is opt-in

### Credits

- [Leon Chlon](https://github.com/leochlon) - Original Pythea/Strawberry concept

---

## [2.7.0] - 2026-01-30

### Added

- **BDD/TDD Translation and Traceability System** - Configurable testing modes with bidirectional translation
  - 6 testing modes: `tdd-only`, `bdd-only`, `layered`, `bdd-drives-tdd`, `tdd-documents-bdd`, `synchronized`
  - Bidirectional translation between Gherkin scenarios and unit tests
  - Full traceability linking with `@trace-id`, `@implements`, `@scenario` metadata
  - Coverage matrix and orphan detection reports

- **Test Translation Skill** - New skill for BDD/TDD conversion
  - `patterns/skills/test-translation.json` - Translation workflow and modes
  - `knowledge/test-traceability.json` - Traceability metadata schemas and patterns

- **Translation Templates** - Templates for generated artifacts
  - `templates/translation/generated-test-python.py.tmpl` - BDD→TDD test generation
  - `templates/translation/generated-feature.feature.tmpl` - TDD→BDD feature generation
  - `templates/translation/traceability-report.md.tmpl` - Coverage and traceability reports

### Changed

- **Updated test-generator agent** - Now supports all 6 testing modes with translation workflow
- **Updated BDD skill** - Added traceability and translation sections
- **Updated TDD skill** - Added traceability and translation sections
- **Updated stack-configuration skill** - Expanded mode selection UI with all 6 options
- **Updated 5 blueprints** - python-fastapi, typescript-react, java-spring, csharp-dotnet, kotlin-spring
  - All now include `test-translation` skill and 6-mode configuration
- **Updated PATTERNS.md** - Documented Test Translation skill and all modes

---

## [2.6.0] - 2026-01-30

### Added

- **Comprehensive MCP Server Catalog** - Expanded from 10 to 50+ servers across 6 categories
  - Core: filesystem, git, memory, time, fetch, brave-search, exa, sequentialthinking
  - Code: github, gitlab, sentry, playwright, puppeteer, openapi, context7, deepwiki
  - Data: postgresql, sqlite, mongodb, prisma, supabase, firebase, bigquery, snowflake, pinecone, qdrant, chromadb
  - Cloud: docker, terraform, pulumi, datadog
  - Collab: atlassian, linear, asana, todoist, notion, slack, discord, gmail, google-calendar, figma, canva
  - AI/ML: huggingface, mlflow, wandb, langsmith, jupyter, langgraph, knowledge-graph, neo4j, ollama

- **MCP Starter Packs** - Pre-configured server bundles for quick setup
  - Minimal (3 servers): filesystem, git, memory
  - Web Developer (6 servers): + github, postgresql, playwright
  - Data Science (6 servers): + jupyter, bigquery, pinecone
  - AI Agent (6 servers): + langgraph, knowledge-graph, chromadb
  - Enterprise (7 servers): + atlassian, slack, sentry
  - DevOps (6 servers): + docker, terraform, github, datadog

- **Role-Based MCP Recommendations** - Smart server suggestions for 8 developer roles
  - Full-Stack Developer, Frontend Developer, Backend Developer
  - Data Scientist, ML Engineer, Agent Developer
  - DevOps Engineer, SAP Developer

- **MCP Selection Skill** - Interactive skill for guided server selection
  - `.cursor/skills/mcp-selection/SKILL.md`
  - Role-based recommendations
  - Category browsing
  - Custom/local server support

- **MCP Server Templates** - Setup guides and configuration templates
  - `templates/mcp/filesystem/setup-guide.md`
  - `templates/mcp/git/setup-guide.md`
  - `templates/mcp/memory/setup-guide.md`
  - `templates/mcp/brave-search/setup-guide.md` + env.template

- **MCP Documentation** - Comprehensive guide for all servers
  - `docs/MCP-SERVERS.md` - Quick start, catalog, and setup instructions

- **AISuite Integration Guide** - Andrew Ng's unified LLM library with MCP support
  - `knowledge/aisuite-integration.json` - Configuration and usage guide
  - Multi-provider LLM access (OpenAI, Anthropic, Google, etc.)
  - Native MCP client support for tool calling

- **MCP Selection Guide Knowledge File** - Decision tree and recommendations
  - `knowledge/mcp-selection-guide.json`
  - Role-to-category mappings
  - Stack recommendations
  - Authentication summaries

### Changed

- **CLI Phase 6** - Enhanced MCP server selection in interactive mode
  - Starter pack selection (6 options)
  - Category browsing for custom selection
  - Auto-add based on PM backend and triggers
  - Custom/local server input support

- **MCP Catalog Schema** - Enhanced with new fields
  - `setupDocs`: Link to official documentation
  - `setupSteps`: Step-by-step setup instructions
  - `envVariables`: Required environment variables
  - `category`: Server category grouping
  - `transport`: stdio, sse, or http

### Documentation

- Added `docs/MCP-SERVERS.md` - Comprehensive MCP server guide
- All server entries now include setup documentation links
- Role-based recommendations table in docs

## [2.5.0] - 2026-01-30

### Added

- **Project Management System** - Complete PM system as optional factory product
  - Multi-backend support: GitHub, Jira, Confluence, Azure DevOps, Linear
  - Methodology support: Scrum, Kanban, Hybrid, Waterfall, SAFe
  - Backend abstraction layer with unified PM operations interface
  - Questionnaire-driven configuration (8 adaptive questions)

- **PM Agents** - Four specialized agents for project management
  - `product-owner` - Creates/refines stories, prioritizes backlog, accepts work
  - `sprint-master` - Facilitates planning, standups, retros, sprint transitions
  - `task-manager` - Breaks down stories, extracts TODOs, updates status
  - `reporting-agent` - Generates burndowns, velocity reports, health indicators

- **PM Skills** - Nine backend-agnostic project management skills
  - `create-epic`, `create-story`, `create-task` - Work item creation
  - `estimate-task` - Story point estimation suggestions
  - `plan-sprint`, `close-sprint` - Sprint lifecycle management
  - `run-standup` - Daily standup status reporting
  - `generate-burndown` - Sprint burndown chart data
  - `health-check` - Team health indicators and metrics

- **CLI PM Flags** - New command-line options for PM configuration
  - `--pm-enabled` - Enable project management system
  - `--pm-backend` - Select PM backend (github/jira/azure-devops/linear)
  - `--pm-doc-backend` - Select documentation backend
  - `--pm-methodology` - Select methodology (scrum/kanban/hybrid/waterfall)

- **MCP Server Templates** - Configuration templates for all backends
  - GitHub: npx @modelcontextprotocol/server-github
  - Atlassian: Remote (mcp.atlassian.com) and local (mcp-atlassian)
  - Azure DevOps: @mcp-apps/azure-devops-mcp-server
  - Linear: Remote (mcp.linear.app/sse)
  - Multi-backend combined configurations

- **PM Metrics System** - Comprehensive metrics with formulas
  - Velocity metrics: velocity, trend, completion rate, carry-over
  - Flow metrics: lead time, cycle time, throughput, WIP
  - Quality metrics: bug ratio, rework rate, escaped defects
  - Predictive metrics: sprint forecast, release prediction, risk score
  - Team health metrics: blocker frequency, stale items, assignment balance

- **PM Documentation** - Complete user and reference documentation
  - `docs/pm-system/README.md` - Overview and quick start
  - `docs/pm-system/USER_GUIDE.md` - Setup and daily usage
  - `docs/pm-system/METHODOLOGY_REFERENCE.md` - Links to official sources
  - `docs/pm-system/METRICS_REFERENCE.md` - Formulas and interpretation
  - Backend-specific setup guides (6 guides)
  - Agent reference documentation (4 agents)

- **PM Tests** - 73 tests covering the PM system
  - Schema validation tests for all PM JSON files
  - Unit tests for PM configuration and adapters
  - Integration tests for CLI PM flags

### Changed

- **ProjectConfig** - Added PM fields (pm_enabled, pm_backend, pm_doc_backend, pm_methodology)
  - New `get_all_agents()` method returns agents including PM agents when enabled
  - New `get_all_skills()` method returns skills including PM skills when enabled

- **onboarding-flow skill** - Added Step 3.5 for optional PM system setup

- **team-workshop-onboarding skill** - Added Project Flow section to Stack Safari
  - Methodology Match game (15 min) - Detect team's preferred methodology
  - Tool Territory game (10 min) - Identify PM and documentation backends

- **Interactive CLI mode** - Added PM configuration in Phase 5

### Integration Points

The PM system is seamlessly integrated into existing factory flows:
- Individual onboarding: Optional Step 3.5 after blueprint selection
- Team workshops: Project Flow section in Stack Safari (Workshop 3)
- CLI quick start: PM flags available for programmatic configuration

### Philosophy

This release continues the tradition of **love and care** by making project management
accessible and non-burdensome:

> "Project management should enhance development, not burden it."

Key principles applied:
- Optional by default - PM is always opt-in, never forced
- Backend-agnostic - Use the tools your team already knows
- Methodology-flexible - Adapt to how your team works
- Transparent - All metrics formulas and interpretations documented

## [2.4.0] - 2026-01-30

### Added

- **AI Development Skills** - Four new skill patterns for building LLM-powered agents
  - `prompt-engineering` - Systematic prompt design, testing, and optimization
  - `agent-coordination` - Multi-agent orchestration (supervisor-worker, hierarchical, collaborative)
  - `task-decomposition` - Breaking complex tasks for specialized agents
  - `consensus-building` - Multi-agent voting, debate, and synthesis protocols

- **SAP Skill Categories** - 12 new SAP-specific skills registered in skill catalog
  - SAP RAP: behavior-design, draft-handling, fiori-annotations, testing
  - SAP CAP: cds-modeling, service-handlers, fiori-integration, deployment
  - SAP CPI/PI: iflow-development, groovy-scripting, error-handling, b2b-integration

- **Intelligent Test Packaging** - Fast error detection in CI pipeline
  - 3-stage pipeline: fast tests first, then integration, then coverage
  - Parallel test execution with pytest-xdist
  - Auto-applied markers (fast/medium/slow) based on test location
  - `pipeline-error-fix` skill for systematic debugging

- **Zero-Config Quick Start** - See the factory in action in under 5 minutes
  - New `--quickstart` CLI command for instant demo project generation
  - `--quickstart-blueprint` option to use different blueprints
  - `--quickstart-output` option to specify output directory
  - Warm, welcoming CLI output with guided next steps

- **Developer Experience Documentation**
  - `docs/PREREQUISITES.md` - Centralized setup guide with platform-specific instructions
  - `docs/TROUBLESHOOTING.md` - Common issues with caring, helpful solutions
  - `docs/QUICKSTART.md` - Detailed guide for the quick start experience

- **Mini Workshop Option** - 2-3 hour condensed team workshop for teams with limited time
  - Vision Express (30 min) - Lightning headlines and mission draft
  - Values Snapshot (30 min) - Rapid value ranking and one dilemma discussion
  - Stack & Team Assembly (45 min) - Blueprint selection and agent quick picks
  - Generation & Demo (30 min) - Create system and walkthrough
  - Next Steps & Gratitude (15 min) - Action planning and appreciation circle

- **Quick Start Tests** - 12 new integration tests for quickstart functionality

### Changed

- **README.md restructured** for better user experience
  - New "Start Here" routing table at the top for quick navigation
  - Warm, welcoming introduction grounded in Axiom 0
  - Improved mermaid diagram showing 5-layer architecture
  - All original advanced content preserved below for experts

- **CLI enhanced** with caring, user-friendly messaging
  - Welcome messages that celebrate user exploration
  - Success celebrations on project generation
  - Helpful error messages with solutions

- **Team Workshop skill** now offers format choice (Full Series or Mini Workshop)

### Philosophy

This release embeds **love and care** as a foundational principle in the user experience:

> "Every message, every error, every piece of documentation should feel like guidance from a trusted friend who wants to see users succeed."

Key principles applied:
- Warm welcome - First impressions set the tone
- Gentle guidance - Never make users feel lost
- Encouraging errors - Mistakes become learning moments
- Progressive disclosure - Show essentials first, reveal depth when ready
- Celebrate success - Acknowledge achievements

## [2.3.1] - 2026-01-30

### Added

- **New SAP CAP Blueprint** (`blueprints/sap-cap/`)
  - Dedicated blueprint for SAP Cloud Application Programming Model
  - Covers CDS modeling, Node.js/Java services, Fiori Elements, BTP deployment
  - Parity with SAP RAP blueprint for consistent SAP coverage

### Changed

- Updated `sap-abap` blueprint to focus on classic ABAP (removed CAP references)
- Updated `docs/reference/BLUEPRINTS.md` with SAP CAP blueprint
- Updated `docs/USAGE_GUIDE.md` with all 4 SAP blueprints

## [2.3.0] - 2026-01-30

### Added

- **New SAP RAP Blueprint** (`blueprints/sap-rap/`)
  - Dedicated blueprint for RESTful ABAP Programming (RAP) development
  - Covers CDS views, behavior definitions, Fiori Elements, ABAP Cloud
  - Separate from general ABAP blueprint for focused RAP development

- **SAP Knowledge Files** (10 new files in `knowledge/`)
  - `cpi-error-handling.json` - Exception handling, retry strategies, circuit breaker patterns
  - `mapping-patterns.json` - XML/JSON/IDoc mapping and transformation patterns
  - `b2b-patterns.json` - EDI (EDIFACT/X12), AS2 protocol, partner management
  - `security-patterns.json` - OAuth 2.0, certificates, encryption, credential management
  - `naming-conventions.json` - Clean ABAP and Hungarian notation conventions
  - `common-table-patterns.json` - SAP table structures, delivery classes, audit fields
  - `tadir-object-types.json` - ABAP repository object types reference
  - `cdhdr-object-classes.json` - Change document patterns for audit trails
  - `service-class-catalog.json` - Service class, repository, factory patterns
  - `sap-reference-repos.json` - Curated SAP sample repositories

- **RAP Templates** (16 files in `templates/abap/rap/`)
  - Behavior definitions: basic, draft, validation, determination, action, authorization
  - Behavior implementations: basic, validation, determination, action
  - CDS views: entity, interface-view, projection
  - Fiori annotations: list-report, object-page
  - Tests: behavior test template

- **CPI Templates** (16 files in `templates/integration/`)
  - Groovy error handling: exception-handling, retry-logic
  - Groovy message processing: json-parser, json-builder, xml-to-json, structured-logging, credential-access
  - iFlow patterns: exception-subprocess, content-router
  - B2B integration: idoc-processing, edi-processor
  - Documentation: iflow-spec, mapping-spec

- **CAP Node.js Templates** (14 files in `templates/cap/`)
  - CDS schemas: entity, entity-associations, aspect, schema
  - Services: service.cds, service-handler.js, service-handler.ts
  - Event handlers: before-create, after-create, on-action
  - MTA deployment: mta.yaml, xs-security.json, package.json
  - Tests: service-test

- **Clean ABAP Templates** (8 files in `templates/abap/clean-abap/`)
  - service-class, global-class, exception-class, factory-class
  - test-class, report, enhancement, interface

### Changed

- Updated `sap-abap` blueprint - now focuses on classic ABAP patterns, Clean ABAP
- Updated `sap-cpi-pi` blueprint - references new template structure
- Updated `docs/reference/BLUEPRINTS.md` - added SAP RAP blueprint
- Updated `docs/reference/KNOWLEDGE_FILES.md` - added 10 new SAP knowledge files

### Summary

This release adds comprehensive SAP template coverage with **66 new files** and **8,045 lines of code**, including:
- 1 new blueprint (SAP RAP)
- 10 new knowledge files
- 54 new templates across RAP, CPI, CAP, and ABAP domains

## [2.2.1] - 2026-01-30

### Added

- **Comprehensive Factory Reference Documentation**
  - `docs/FACTORY_REFERENCE.md` - Master entry point with architecture overview and quick start
  - `docs/reference/BLUEPRINTS.md` - Detailed reference for all 12 technology blueprints (~800 lines)
  - `docs/reference/PATTERNS.md` - Complete patterns reference: agents, skills, axioms, methodologies (~700 lines)
  - `docs/reference/KNOWLEDGE_FILES.md` - All 32 knowledge files categorized and explained
  - `docs/reference/FACTORY_COMPONENTS.md` - Factory's 7 agents and 18 skills documented
  - `docs/reference/GENERATED_OUTPUT.md` - Project structure, file formats, and examples

### Changed

- Updated `README.md` with comprehensive reference documentation section
- Updated `docs/USAGE_GUIDE.md` with quick links to reference documentation

### Documentation

This release adds ~2,460 lines of comprehensive reference documentation, enabling users and contributors to fully understand the factory's blueprints, patterns, knowledge files, and generation process.

## [2.2.0] - 2026-01-30

### Added

- **Team Workshop Onboarding** - Collaborative 5-workshop series for teams to co-create their Cursor agent system
  - Workshop 1: Vision Quest (mission, stakeholders, success criteria)
  - Workshop 2: Ethics Arena (values, boundaries, ethical framework)
  - Workshop 3: Stack Safari (technology selection, architecture)
  - Workshop 4: Agent Assembly (agent trading cards, skill bingo)
  - Workshop 5: Integration Celebration (demo derby, gratitude circle)

- **New Agent**
  - `workshop-facilitator` - Orchestrates team workshops with games and facilitation

- **New Skill**
  - `team-workshop-onboarding` - Complete workshop series skill with detailed facilitation guides

- **New Documentation**
  - `docs/TEAM_WORKSHOP_GUIDE.md` - Comprehensive facilitator's manual (~1200 lines)

- **New Knowledge Files**
  - `knowledge/workshop-facilitation.json` - Facilitation techniques and prompts
  - `knowledge/game-mechanics.json` - Game rules, variations, and mechanics
  - `knowledge/team-dynamics.json` - Team collaboration patterns and adaptations

- **New Patterns**
  - `patterns/axioms/axiom-zero.json` - Axiom 0: Love and Trust foundation
  - `patterns/games/` - 11 workshop games (creative, strategic, collaborative)
  - `patterns/team-formats/` - Small (2-5), medium (6-12), large (13+) team adaptations
  - `patterns/workshops/` - 5 workshop pattern definitions

### Philosophy

This release introduces **Axiom 0: Love and Trust** as the philosophical foundation:

> "Before verification, before user primacy, before all rules - we act from love for humanity and trust in each other."

Workshop activities are designed to make onboarding fun and engaging through play, debate, and celebration.

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
