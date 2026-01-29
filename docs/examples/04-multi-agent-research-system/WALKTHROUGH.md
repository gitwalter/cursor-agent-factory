# Multi-Agent Research System - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for building an orchestrated multi-agent research assistant with LangGraph.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for a multi-agent research assistant with supervisor pattern
```

---

### Pre-Phase: Axiom Selection (Layer 0)

**Factory Prompt:**
> Every agent system needs foundational axioms. Core axioms (A1-A5) are always included.
> Would you like to add optional axioms?

**Your Response:**
```
Yes, add A8 (Collaboration) and A10 (Learning)
```

**Rationale:**
- A8 (Collaboration): Essential for multi-agent coordination
- A10 (Learning): Systems improve through feedback

**Selected Axioms:**

| ID | Axiom | Application |
|----|-------|-------------|
| A1 | Verifiability | All agent outputs traceable |
| A2 | User Primacy | User goals drive coordination |
| A3 | Transparency | Agent decisions explainable |
| A4 | Non-Harm | No harmful content generation |
| A5 | Consistency | Uniform agent behavior |
| A8 | Collaboration | Effective agent coordination |
| A10 | Learning | Continuous system improvement |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To automate complex research tasks through coordinated specialist agents working under intelligent supervision
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
AI engineers building multi-agent systems and researchers needing automated research pipelines
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Complete multi-step research tasks with quality-reviewed outputs from coordinated agent teams
```

---

### Phase 0.5: Depth Selection

**Factory Prompt:**
> How deep should we define the remaining layers?

**Your Response:**
```
C (Comprehensive)
```

**Rationale:** Multi-agent systems are complex and benefit from enforcement and practices.

---

### Phases 0.6-0.7: Principles & Methodology (Layer 2-3)

**Factory Prompt:**
> What development methodology fits your team?

**Your Response:**
```
Research & Development
```

---

**Factory Prompt:**
> Team size?

**Your Response:**
```
2-4 developers
```

---

**Factory Prompt:**
> Exploration vs exploitation ratio?

**Your Response:**
```
70/30 - High exploration for agent coordination patterns
```

---

### Phases 0.8-0.9: Enforcement & Practices (Comprehensive)

**Factory Prompt:**
> Which enforcement patterns should be active?

**Your Response:**
```
Quality enforcement (for agent outputs) and integrity enforcement (for coordination)
```

---

**Factory Prompt:**
> Which practice patterns should be active?

**Your Response:**
```
Daily practices and craft practices for agent development
```

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
research-agent-team
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
Multi-agent research system with supervisor, researcher, analyst, writer, and critic agents
```

---

### Phase 2: Technology Stack

**Factory Prompt:**
> What is your primary programming language?

**Your Response:**
```
Python
```

---

**Factory Prompt:**
> What frameworks will you use?

**Your Response:**
```
LangGraph, LangChain, Streamlit
```

---

**Factory Prompt:**
> I found a matching blueprint: multi-agent-systems. Would you like to use it?

**Your Response:**
```
Yes
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
GitHub issues for agent improvements, experiment logs for coordination tuning
```

---

**Factory Prompt:**
> Would you like to configure MCP server integration?

**Your Response:**
```
Yes, configure DeepWiki for researching multi-agent patterns
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What multi-agent patterns should the system follow?

**Your Response:**
```
Supervisor/worker pattern, sequential handoffs, state persistence
```

---

### Phase 5: Agent & Skill Selection

**Factory Prompt:**
> Which agents should I include?

**Your Response:**
```
All available: code-reviewer, test-generator, documentation-agent, explorer
```

---

**Factory Prompt:**
> Which skills should be available?

**Your Response:**
```
agent-coordination, task-decomposition, consensus-building, grounding, tdd
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\research-agent-team
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: research-agent-team                                   ║
║ Blueprint: multi-agent-systems                                 ║
║ Depth: Comprehensive                                           ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: A8 (Collaboration), A10 (Learning)                 ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Coordinated multi-agent research                    ║
║   Stakeholders: AI engineers, researchers                      ║
║   Success: Quality-reviewed research from agent teams          ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Research & Development                          ║
║   Exploration: 70%                                             ║
╠════════════════════════════════════════════════════════════════╣
║ ENFORCEMENT                                                    ║
║   Quality: Agent output validation                             ║
║   Integrity: Coordination protocol compliance                  ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: Python, LangGraph, LangChain, Streamlit               ║
║   Pattern: Supervisor/Worker with handoffs                     ║
║   Skills: agent-coordination, task-decomposition, consensus    ║
║   MCP: DeepWiki                                                ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\research-agent-team                        ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Generated Artifacts

```
research-agent-team/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── test-generator.md
│   │   ├── documentation-agent.md
│   │   └── explorer.md
│   └── skills/
│       ├── agent-coordination/
│       │   └── SKILL.md
│       ├── task-decomposition/
│       │   └── SKILL.md
│       ├── consensus-building/
│       │   └── SKILL.md
│       ├── grounding/
│       │   └── SKILL.md
│       └── tdd/
│           └── SKILL.md
├── knowledge/
│   ├── multi-agent-patterns.json    # Supervisor/worker patterns
│   ├── agent-handoffs.json          # Handoff protocols
│   ├── coordination-strategies.json # Coordination patterns
│   └── langgraph-workflows.json     # LangGraph patterns
├── agents/
│   ├── supervisor/
│   │   └── supervisor_agent.py      # Coordinator agent
│   └── workers/
│       ├── researcher_agent.py      # Information gathering
│       ├── analyst_agent.py         # Data synthesis
│       ├── writer_agent.py          # Report generation
│       └── critic_agent.py          # Quality review
├── graphs/
│   └── research_graph.py            # LangGraph orchestration
├── state/
│   └── research_state.py            # Shared state definition
├── coordination/
│   └── handoff_protocol.py          # Handoff logic
├── prompts/
│   ├── supervisor/
│   │   └── coordination_prompt.md
│   └── workers/
│       ├── researcher_prompt.md
│       ├── analyst_prompt.md
│       ├── writer_prompt.md
│       └── critic_prompt.md
├── apps/
│   └── streamlit_app.py             # UI for interaction
├── tests/
│   ├── agents/
│   ├── graphs/
│   └── coordination/
├── workflows/
│   └── methodology.yaml
├── .cursorrules
├── PURPOSE.md
├── enforcement.yaml
├── practices.yaml
└── README.md
```

---

## Multi-Agent Architecture

### Supervisor/Worker Pattern

```
                    ┌──────────────┐
                    │  Supervisor  │
                    │    Agent     │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │Researcher│───▶│ Analyst  │───▶│  Writer  │
    └──────────┘    └──────────┘    └──────────┘
                                          │
                                          ▼
                                   ┌──────────┐
                                   │  Critic  │
                                   └──────────┘
```

### LangGraph State Machine

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage

class ResearchState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], ...]
    task: str
    research_data: str
    analysis: str
    draft: str
    feedback: str
    final_output: str
    current_agent: str

# Build the graph
graph = StateGraph(ResearchState)

# Add nodes (agents)
graph.add_node("supervisor", supervisor_node)
graph.add_node("researcher", researcher_node)
graph.add_node("analyst", analyst_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

# Add edges (handoffs)
graph.add_edge("researcher", "analyst")
graph.add_edge("analyst", "writer")
graph.add_edge("writer", "critic")
graph.add_conditional_edges("critic", should_revise)

# Supervisor decides initial routing
graph.add_conditional_edges("supervisor", route_task)

graph.set_entry_point("supervisor")
```

---

## Using the Generated System

### Running a Research Task

**Example: Research Request**
```
Research the current state of multi-agent AI systems in production
```

The supervisor will:
1. Decompose the task
2. Assign researcher to gather information
3. Hand off to analyst for synthesis
4. Pass to writer for report
5. Critic reviews and may request revision
6. Return final output

### Debugging Coordination

Use LangSmith to trace:
- Handoff decisions
- State changes
- Agent reasoning
- Coordination efficiency

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Should include A8 (Collaboration) enforcement
2. `PURPOSE.md` - Should reflect multi-agent coordination mission
3. `graphs/` - Should contain LangGraph orchestration
4. `agents/` - Should have supervisor and workers

---

## Next Steps

1. Implement the agent team with LangGraph
2. Test individual agents
3. Test coordination and handoffs
4. Tune prompts based on output quality

**Congratulations!** You've generated a complete Cursor agent system for multi-agent orchestration.
