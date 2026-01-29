# Cursor Agent Factory - Example Walkthroughs

This directory contains complete, reproducible examples showing how to use the Cursor Agent Factory from start to finish with real technology stacks.

## Quick Reference

| # | Example | Blueprint | Category | Depth | Best For |
|---|---------|-----------|----------|-------|----------|
| 01 | [REST API Service](01-rest-api-service/) | python-fastapi | Web Backend | Standard | Backend developers building APIs |
| 02 | [Full-Stack Next.js App](02-fullstack-nextjs-app/) | nextjs-fullstack | Full-Stack | Standard | Full-stack developers |
| 03 | [RAG Chatbot Agent](03-rag-chatbot-agent/) | ai-agent-development | AI/ML | Standard | AI engineers building single agents |
| 04 | [Multi-Agent Research System](04-multi-agent-research-system/) | multi-agent-systems | AI/ML | Comprehensive | AI engineers building orchestrated systems |
| 05 | [SAP Fiori Integration](05-sap-fiori-integration/) | sap-abap | Enterprise | Comprehensive | SAP developers |
| 06 | [.NET Enterprise API](06-dotnet-enterprise-api/) | csharp-dotnet | Enterprise | Standard | .NET/C# developers |
| 07 | [Kotlin Spring Microservice](07-kotlin-spring-microservice/) | kotlin-spring | JVM | Standard | Kotlin/JVM developers |
| 08 | [SAP CPI Integration](08-sap-cpi-integration/) | sap-cpi-pi | SAP | Standard | SAP integration developers |

## How to Use These Examples

Each example contains:

```
XX-example-name/
├── README.md           # Scenario overview and context
├── WALKTHROUGH.md      # Complete step-by-step process
└── expected-output/    # Reference generated files
    ├── .cursorrules.example      # Example rules (rename to use)
    ├── PURPOSE.md.example        # Example purpose doc
    ├── .cursor/
    │   ├── agents/*.md.example   # Example agents
    │   └── skills/*/SKILL.md.example
    └── workflows/*.yaml.example  # Example methodology
```

### Important: The `.example` Extension

All configuration files in `expected-output/` use the `.example` extension to **prevent interference** with the factory's actual behavior:

| File in expected-output/ | What it represents |
|--------------------------|-------------------|
| `.cursorrules.example` | What `.cursorrules` would look like |
| `code-reviewer.md.example` | What the agent file would contain |
| `SKILL.md.example` | What the skill file would contain |
| `methodology.yaml.example` | What the methodology config would contain |

**When using in your own project**, rename these files by removing the `.example` suffix.

### Recommended Approach

1. **Read the README.md** - Understand the scenario and what we're building
2. **Follow the WALKTHROUGH.md** - Execute each phase in your own Cursor session
3. **Compare with expected-output/** - Verify your results match the reference
4. **To use files**: Rename by removing `.example` suffix in your own project
5. **Customize** - Modify the generated system for your specific needs

## Choosing an Example

### By Experience Level

| Level | Recommended Examples |
|-------|---------------------|
| **Beginner** | Start with 01 (REST API) or 02 (Next.js) |
| **Intermediate** | Try 03 (RAG Chatbot) or 06 (.NET) |
| **Advanced** | Explore 04 (Multi-Agent) or 05 (SAP) |

### By Use Case

| If you want to... | Use Example |
|-------------------|-------------|
| Build a REST API with Python | 01 - REST API Service |
| Create a full-stack web app | 02 - Full-Stack Next.js |
| Build an AI chatbot with RAG | 03 - RAG Chatbot Agent |
| Orchestrate multiple AI agents | 04 - Multi-Agent Research System |
| Develop SAP applications | 05 - SAP Fiori Integration |
| Build enterprise .NET APIs | 06 - .NET Enterprise API |
| Create Kotlin microservices | 07 - Kotlin Spring Microservice |
| Build SAP CPI/PI integrations | 08 - SAP CPI Integration |

### By Depth Level

| Depth | What's Configured | Examples |
|-------|-------------------|----------|
| **Standard** | Layers 0-4 with methodology selection | 01, 02, 03, 06, 07 |
| **Comprehensive** | All layers + enforcement + practices | 04, 05 |

## The 5-Layer Architecture

Each example demonstrates the factory's 5-layer architecture:

```
Layer 0: INTEGRITY & LOGIC    →  Axioms (A1-A5 core, A6-A10 optional)
Layer 1: PURPOSE              →  Mission, stakeholders, success criteria
Layer 2: PRINCIPLES           →  Ethical boundaries, quality standards
Layer 3: METHODOLOGY          →  Agile/Kanban/R&D, enforcement, practices
Layer 4: TECHNICAL            →  Stack, agents, skills, templates
```

## Example Comparison Matrix

### Axiom Selection

| Example | Core (A1-A5) | A6 Minimalism | A7 Reversibility | A8 Collaboration | A10 Learning |
|---------|--------------|---------------|------------------|------------------|--------------|
| 01 REST API | Yes | Yes | - | - | - |
| 02 Next.js | Yes | - | - | - | - |
| 03 RAG Chatbot | Yes | - | - | - | Yes |
| 04 Multi-Agent | Yes | - | - | Yes | Yes |
| 05 SAP | Yes | Yes | Yes | - | - |
| 06 .NET | Yes | Yes | - | - | - |
| 07 Kotlin | Yes | Yes | - | - | - |

### Methodology Selection

| Example | Methodology | Team Size | Key Ceremonies |
|---------|-------------|-----------|----------------|
| 01 REST API | Agile Scrum | 4-6 | Sprint planning, daily standup, retrospective |
| 02 Next.js | Kanban | 2-4 | WIP limits, continuous flow |
| 03 RAG Chatbot | Research & Development | 1-3 | 70/30 exploration, spike reviews |
| 04 Multi-Agent | Research & Development | 2-4 | Experiment cycles, hypothesis testing |
| 05 SAP | Enterprise Integration | 4-8 | Change advisory, release gates |
| 06 .NET | Agile Scrum | 4-8 | Sprint planning, code review gates |
| 07 Kotlin | Kanban | 2-4 | Pull-based flow, continuous deployment |

## Prerequisites

Before following any example, ensure you have:

1. **Cursor IDE** installed and configured
2. **This factory project** opened in Cursor
3. **Python 3.10+** (Anaconda recommended)
4. **Stack-specific tools** (see each example's prerequisites)

## Related Documentation

- [Usage Guide](../USAGE_GUIDE.md) - Complete factory usage documentation
- [Layered Architecture](../LAYERED_ARCHITECTURE.md) - Deep dive into the 5-layer system
- [Extension Guide](../EXTENSION_GUIDE.md) - How to create custom blueprints and patterns

---

*These examples are designed to be followed exactly as written. Once you've completed an example successfully, you'll have the confidence to customize the factory for your specific needs.*
