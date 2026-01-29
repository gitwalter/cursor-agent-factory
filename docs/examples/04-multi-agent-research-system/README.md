# Example 04: Multi-Agent Research System

Build an orchestrated multi-agent research assistant using LangGraph with a supervisor pattern, specialized worker agents, and collaborative coordination.

## What We're Building

A **Research Assistant System** that provides:

- Supervisor agent coordinating specialized workers
- Researcher agent for information gathering
- Analyst agent for data synthesis
- Writer agent for report generation
- Critic agent for quality review
- Handoff protocols between agents
- Streamlit UI for interaction

## Target Users

- **Primary**: AI engineers building complex multi-agent systems
- **Secondary**: Research teams needing automated research pipelines

## Success Criteria

- Complete research tasks with 3-5 coordinated agents
- Maintain coherent state across all agent handoffs
- Produce quality-reviewed research outputs

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Orchestration | LangGraph 0.1+ |
| Agent Framework | LangChain 0.2+ |
| LLM | GPT-4 (supervisor), GPT-3.5 (workers) |
| UI | Streamlit |
| Tracing | LangSmith |

## Factory Configuration Summary

| Layer | Configuration |
|-------|---------------|
| **Layer 0 (Axioms)** | Core (A1-A5) + A8 (Collaboration) + A10 (Learning) |
| **Layer 1 (Purpose)** | Coordinated multi-agent research |
| **Layer 2 (Principles)** | Quality standards for AI outputs |
| **Layer 3 (Methodology)** | Research & Development |
| **Layer 4 (Technical)** | multi-agent-systems blueprint |

## Depth Level

**Comprehensive** - Includes enforcement patterns and practices for reliable multi-agent coordination.

## Key Axiom: A8 (Collaboration)

This example includes the **Collaboration** axiom because:
- Multiple agents must work together effectively
- Handoffs require clear protocols
- Agent coordination is the core concern

## Time to Complete

Following this walkthrough takes approximately **30 minutes**.

## Prerequisites

Before starting, ensure you have:

1. Cursor IDE installed
2. The cursor-agent-factory project opened in Cursor
3. Python 3.10+ installed
4. OpenAI API key configured
5. LangSmith account (for tracing)

## Next Steps

1. Open [WALKTHROUGH.md](WALKTHROUGH.md) to begin the step-by-step process
2. Compare your results with [expected-output/](expected-output/) when complete
3. Customize the agent team for your research domain

## Related Examples

- [03 - RAG Chatbot Agent](../03-rag-chatbot-agent/) - Single agent for simpler use cases
- [01 - REST API Service](../01-rest-api-service/) - Add API endpoints for agent access
