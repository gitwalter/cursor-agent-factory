# Cursor Agent Factory - Complete Reference

Welcome to the comprehensive reference for the Cursor Agent Factory. This document provides an overview of the factory's architecture, components, and generation process, with links to detailed subdocuments.

> **Our Philosophy:** Before diving into technical details, we invite you to understand our **[Culture and Values](CULTURE_AND_VALUES.md)**—the lived philosophy of love, wisdom, and care that grounds everything we build.

> **Tool Paths:** Commands in this document use default Windows paths from `.cursor/config/tools.json`.
> See [Configuration Guide](CONFIGURATION.md) to customize for your environment.

## Table of Contents

1. [Introduction](#introduction)
2. [The 5-Layer Architecture](#the-5-layer-architecture)
3. [Generation Process](#generation-process)
4. [Component Reference](#component-reference)
5. [Quick Start](#quick-start)
6. [Extending the Factory](#extending-the-factory)

---

## Introduction

### What is Cursor Agent Factory?

Cursor Agent Factory is a **meta-system** that generates complete, working Cursor agent development environments. Instead of manually configuring agents, skills, and rules for each project, you describe your project's needs and the factory generates a tailored system grounded in clear values, purpose, and methodology.

### Core Value Proposition

- **Consistency**: Every generated project follows the same architectural principles
- **Grounding**: Agent systems are built on explicit axioms that prevent harmful or inconsistent behavior
- **Productivity**: Pre-configured agents and skills accelerate development from day one
- **Customization**: 27 technology blueprints cover common stacks, with full extensibility
- **Project Management**: Integrated PM system supports Agile, Kanban, and hybrid methodologies

### Key Concepts

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CURSOR AGENT FACTORY                          │
│                                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐       │
│  │Blueprints│ +  │ Patterns │ +  │Knowledge │ =  │ Generated│       │
│  │ (stacks) │    │(templates│    │  Files   │    │  Project │       │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘       │
│       │               │               │               │              │
│       └───────────────┴───────────────┴───────────────┘              │
│                               │                                      │
│                        Requirements                                  │
│                        Gathering                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The 5-Layer Architecture

The factory implements a **5-layer deductive-inductive architecture** ensuring generated agent systems are grounded, purposeful, and excellent.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER 0: INTEGRITY & LOGIC                        │
│  Axioms (immutable) │ Derivation Rules │ Validation Constraints      │
│  Foundation: Everything else derives from here                       │
└─────────────────────────────────┬───────────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER 1: PURPOSE                                  │
│  Mission Statement │ Stakeholders │ Success Criteria                 │
│  Artifact: PURPOSE.md                                                │
└─────────────────────────────────┬───────────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER 2: PRINCIPLES                               │
│  Ethical Boundaries │ Quality Standards │ Failure Handling           │
│  Artifact: .cursorrules principles section                           │
└─────────────────────────────────┬───────────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER 3: METHODOLOGY                              │
│  Agile/Kanban/R&D/Enterprise │ Coordination │ Ceremonies             │
│  Artifacts: workflows/methodology.yaml, enforcement.yaml             │
└─────────────────────────────────┬───────────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER 4: TECHNICAL                                │
│  Stack │ Agents │ Skills │ Code Standards │ Templates                │
│  Artifacts: .cursor/, knowledge/, templates/                         │
└─────────────────────────────────────────────────────────────────────┘
```

### Layer Summary

| Layer | Name | Purpose | Key Artifacts |
|-------|------|---------|---------------|
| L0 | Integrity & Logic | Immutable axioms (A1-A5), derivation rules | Built into .cursorrules |
| L1 | Purpose | Why the system exists | PURPOSE.md |
| L2 | Principles | Quality and ethical standards | .cursorrules principles |
| L3 | Methodology | How work is organized | methodology.yaml |
| L4 | Technical | Implementation details | .cursor/, knowledge/, templates/ |

### Foundation Axiom (Layer 0)

| ID | Name | Statement |
|----|------|-----------|
| **A0** | **Love and Trust** | **All technical decisions shall be grounded in love for those who depend on our work, and trust in our collaborative process** |

This foundation axiom precedes and grounds all other axioms. See [Culture and Values](CULTURE_AND_VALUES.md) for the philosophical basis.

### Core Axioms (Layer 0)

| ID | Name | Statement | Derived From A0 |
|----|------|-----------|-----------------|
| A1 | Verifiability | All agent outputs must be verifiable against source | Love demands honesty |
| A2 | User Primacy | User intent takes precedence over agent convenience | Love serves others |
| A3 | Transparency | Agent reasoning must be explainable on request | Love is open |
| A4 | Non-Harm | No action may knowingly cause harm to users or systems | Love protects |
| A5 | Consistency | No rule may contradict these axioms | Love is coherent |

### Optional Axioms

| ID | Name | Use When |
|----|------|----------|
| A6 | Minimalism | Maintenance and understandability are priorities |
| A7 | Reversibility | Safety and recoverability are paramount |
| A8 | Collaboration | Multi-agent or team coordination is needed |
| A9 | Performance | Performance-critical applications |
| A10 | Learning | AI/ML, R&D, continuous improvement culture |

### Deductive-Inductive System

**Deductive (Top-Down)**: From axioms to specific rules
```
Layer 0 Axiom: "User safety is paramount" (A4)
    ↓ derives
Layer 2 Principle: "Never execute untested code in production"
    ↓ derives  
Layer 3 Enforcement: "All code requires review before merge"
    ↓ derives
Layer 4 Technical: "PR approval required, CI must pass"
```

**Inductive (Bottom-Up)**: Learning from experience via the Pattern Feedback Skill
```
Layer 4 Observation: "JSON parsing errors occur frequently"
    ↓ generalizes
Proposed Pattern: "API responses should always be validated"
    ↓ reviewed against axioms
Layer 2 Principle Update: "External API responses require schema validation"
```

---

## Generation Process

### Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │────▶│ Requirements│────▶│  Blueprint  │────▶│  Generated  │
│   Request   │     │  Gathering  │     │  Matching   │     │   Project   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### Requirements Gathering Phases

| Phase | Name | What's Captured |
|-------|------|-----------------|
| Pre-Phase | Axiom Configuration | Core + optional axioms selection |
| Phase 0 | Purpose Definition | Mission, stakeholders, success criteria |
| Phase 0.5 | Depth Selection | Quick Start, Standard, or Comprehensive |
| Phase 0.6 | Principles | Ethical boundaries, quality standards |
| Phase 0.7 | Methodology | Agile, Kanban, R&D, or Enterprise |
| Phase 0.8 | Enforcement | Quality gates, safety checks (Comprehensive) |
| Phase 0.9 | Practices | Daily, craft, alignment practices (Comprehensive) |
| Phase 1 | Project Context | Name, description, domain, team |
| Phase 2 | Technology Stack | Language, frameworks, databases |
| Phase 3 | Workflow | Methodology, triggers, artifacts |
| Phase 4 | Knowledge Domain | Concepts, references, conventions |
| Phase 5 | Agent Capabilities | Agents, skills, MCP servers |

### Onboarding Depth Options

| Option | Phases Included | Best For |
|--------|-----------------|----------|
| Quick Start | Pre-Phase, Phase 0, Phases 1-5 | Rapid prototyping |
| Standard | All pre-phases + Phases 1-5 | Most projects |
| Comprehensive | All phases including enforcement/practices | Enterprise, critical systems |

### Blueprint Matching

When requirements are gathered, the factory matches against available blueprints:

1. **Primary Language** - Must match
2. **Framework Alignment** - Frameworks should overlap
3. **Project Type** - API, web app, AI, integration, etc.
4. **Customization** - Blueprint serves as starting point, can be customized

---

## Component Reference

### Detailed Documentation

| Document | Description | Link |
|----------|-------------|------|
| **Culture & Values** | Our lived philosophy: love, wisdom, and care | [CULTURE_AND_VALUES.md](CULTURE_AND_VALUES.md) |
| **Blueprints** | All 27 technology blueprints with stack details, agents, skills | [reference/BLUEPRINTS.md](reference/BLUEPRINTS.md) |
| **Patterns** | Agent, skill, axiom, methodology, PM, and other patterns | [reference/PATTERNS.md](reference/PATTERNS.md) |
| **Knowledge Files** | All 66 knowledge files with categories and purposes | [reference/KNOWLEDGE_FILES.md](reference/KNOWLEDGE_FILES.md) |
| **Factory Components** | The factory's own agents and skills | [reference/FACTORY_COMPONENTS.md](reference/FACTORY_COMPONENTS.md) |
| **Generated Output** | Project structure, file formats, examples | [reference/GENERATED_OUTPUT.md](reference/GENERATED_OUTPUT.md) |
| **PM System** | Integrated project management for generated systems | [pm-system/README.md](pm-system/README.md) |
| **Templates** | Code and document templates | [reference/TEMPLATES.md](reference/TEMPLATES.md) |

### Quick Component Overview

#### Blueprints (27)

| Category | Blueprints |
|----------|------------|
| Backend/API | python-fastapi, java-spring, kotlin-spring, csharp-dotnet |
| Frontend/Full-Stack | typescript-react, nextjs-fullstack, python-streamlit |
| AI/Agent | ai-agent-development, multi-agent-systems, python-multi-agent |
| ML/Deep Learning | python-deep-learning, python-ml-experimentation, python-fine-tuning |
| RAG/LLM | python-rag-system, starter-rag, starter-chatbot, starter-ml-classification |
| SAP | sap-abap, sap-cpi-pi, sap-cap, sap-rap |
| Blockchain/DeFi | solidity-ethereum, solana-rust, defi-protocols |
| Finance/Trading | financial-ai-agents, quantitative-trading |
| Automation | n8n-automation |

#### Pattern Types

| Type | Count | Examples |
|------|-------|----------|
| Agent Patterns | 5+ | code-reviewer, test-generator, explorer |
| Skill Patterns | 9+ | grounding, tdd, bugfix-workflow |
| Methodology Patterns | 4 | agile-scrum, kanban, research-development, hybrid |
| Axiom Patterns | 2 | core-axioms (A0-A5), optional-axioms (A6-A10) |
| PM Patterns | 4+ | agile-scrum, kanban, waterfall, hybrid |
| Other | 15+ | principles, enforcement, practices, workshops |

#### Knowledge Files (66)

| Category | Examples |
|----------|----------|
| Stack-Specific | fastapi-patterns, nextjs-patterns, dotnet-patterns, spring-patterns |
| AI/Agent | langchain-patterns, langgraph-workflows, mcp-patterns, crewai-patterns |
| ML/Deep Learning | deep-learning-patterns, huggingface-patterns, llm-fine-tuning-patterns |
| Blockchain/DeFi | solidity-patterns, defi-patterns, erc-standards, ethereum-security |
| Finance/Trading | quantitative-finance, trading-patterns, risk-management |
| Integration | groovy-patterns, iflow-patterns, n8n-patterns, sap-cap-patterns |
| Core | design-patterns, security-checklist, tdd-patterns, bdd-patterns |
| PM/Metrics | pm-metrics, team-dynamics, workflow-patterns |
| Factory Meta | skill-catalog, stack-capabilities, mcp-servers-catalog |

---

## Quick Start

### Using the CLI

```powershell
# List available blueprints
C:\App\Anaconda\python.exe cli\factory_cli.py --list-blueprints

# Generate a project with a specific blueprint
C:\App\Anaconda\python.exe cli\factory_cli.py --blueprint python-fastapi --output C:\Projects\my-api

# Interactive requirements gathering
C:\App\Anaconda\python.exe cli\factory_cli.py --interactive --output C:\Projects\my-project
```

### Using Cursor Agents

1. Open the factory in Cursor
2. Ask: "Create a new agent system for [your project description]"
3. The **Requirements Architect** agent guides you through requirements
4. The **Stack Builder** matches your needs to a blueprint
5. The **Template Generator** creates your project

### Generated Project Structure

```
my-project/
├── .cursorrules              # 5-layer agent rules
├── PURPOSE.md                # Mission document
├── .cursor/
│   ├── agents/               # AI agents
│   └── skills/               # Reusable skills
├── knowledge/                # JSON reference data
├── templates/                # Code templates
├── workflows/
│   └── methodology.yaml      # Team methodology
├── src/                      # Source code
├── tests/                    # Test files
└── README.md                 # Documentation
```

---

## Extending the Factory

### Adding New Blueprints

1. Create `blueprints/{blueprint-id}/blueprint.json`
2. Define metadata, stack, agents, skills, knowledge, templates
3. Test with: `python cli/factory_cli.py --blueprint {blueprint-id} --output test-output`

See [EXTENSION_GUIDE.md](EXTENSION_GUIDE.md) for complete instructions.

### Adding New Patterns

Patterns live in `patterns/{type}/`:
- `patterns/agents/` - Agent patterns
- `patterns/skills/` - Skill patterns
- `patterns/methodologies/` - Methodology patterns
- `patterns/axioms/` - Axiom patterns

Each pattern is a JSON file following the respective schema.

### Adding New Knowledge Files

1. Create JSON file in `knowledge/`
2. Include `$schema`, `title`, `description`, `version`
3. Structure data for easy agent querying
4. Reference in relevant blueprints

---

## Philosophy

> *"Create working software that spreads love, harmony, and growth."*
> — The Fundamental Telos

The Cursor Agent Factory is built on a comprehensive philosophy that unites Western analytical philosophy (Russell, Wittgenstein, Carnap, Quine, Searle), empiricism (Hume, Comte, Popper), ancient wisdom traditions (Chinese, Buddhist, Abrahamic), and modern research in sacred psychology and AI alignment.

**Core Beliefs:**

- **Love as foundation** (A0): All technical decisions grounded in care for those who depend on our work
- **Grounded** in explicit, traceable values that derive from first principles
- **Transparent** in reasoning—Wittgenstein's language games for different contexts
- **Consistent** in behavior—Quine's web of belief, changes propagate correctly
- **Action-oriented**—Austin and Searle's speech acts: agent messages ARE actions
- **Empirically validated**—Hume and Comte: observe, measure, improve

Every generated agent system inherits these qualities through the 5-layer architecture, ensuring that AI assistance enhances rather than undermines software quality and developer experience.

For the complete philosophical foundation, see **[Culture and Values](CULTURE_AND_VALUES.md)**.

---

## Project Management Integration

Generated projects can include integrated project management support:

| Feature | Description |
|---------|-------------|
| **Multi-Backend** | Supports Jira, Linear, GitHub Issues, Azure DevOps |
| **Methodology Flexibility** | Agile Scrum, Kanban, Waterfall, or Hybrid |
| **AI-Powered Agents** | Sprint planning, task breakdown, progress tracking |
| **Axiom 0 Grounded** | PM enhances development, not burdens it |

PM integration is configured during requirements gathering or can be added to existing projects. See [PM System Documentation](pm-system/README.md) for details.

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [CULTURE_AND_VALUES.md](CULTURE_AND_VALUES.md) | Our lived philosophy |
| [USAGE_GUIDE.md](USAGE_GUIDE.md) | Step-by-step usage instructions |
| [EXTENSION_GUIDE.md](EXTENSION_GUIDE.md) | How to extend the factory |
| [LAYERED_ARCHITECTURE.md](LAYERED_ARCHITECTURE.md) | Deep dive into the 5-layer architecture |
| [TESTING.md](TESTING.md) | Testing the factory |
| [ONBOARDING_GUIDE.md](ONBOARDING_GUIDE.md) | Onboarding existing repositories |
| [TEAM_WORKSHOP_GUIDE.md](TEAM_WORKSHOP_GUIDE.md) | Collaborative team workshops |
| [pm-system/README.md](pm-system/README.md) | Project management integration |

---

*This document is the entry point to comprehensive factory documentation. For detailed information on any component, follow the links to the subdocuments in [Component Reference](#component-reference).*

*Built with love, for love, in service of love. SDG.*
