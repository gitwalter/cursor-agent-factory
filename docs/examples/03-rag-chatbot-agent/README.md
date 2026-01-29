# Example 03: RAG Chatbot Agent

Build an intelligent documentation Q&A chatbot using LangChain, ChromaDB for vector storage, and Streamlit for the user interface.

## What We're Building

A **Documentation Q&A Bot** that provides:

- Natural language queries against documentation
- Retrieval-Augmented Generation (RAG) for accurate answers
- Source citation for all responses
- Conversation memory for context-aware follow-ups
- Streamlit web interface for easy interaction

## Target Users

- **Primary**: Developers who need quick answers from documentation
- **Secondary**: Technical writers maintaining documentation quality

## Success Criteria

- Answer 80% of documentation questions accurately
- Provide source citations for all answers
- Response time under 3 seconds for typical queries

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| LLM Framework | LangChain 0.2+ |
| Vector Store | ChromaDB |
| Embeddings | OpenAI text-embedding-3-small |
| LLM | GPT-4 or GPT-4o |
| UI | Streamlit 1.30+ |
| Testing | pytest, LangSmith |

## Factory Configuration Summary

| Layer | Configuration |
|-------|---------------|
| **Layer 0 (Axioms)** | Core (A1-A5) + A10 (Learning) |
| **Layer 1 (Purpose)** | Enable accurate documentation Q&A |
| **Layer 2 (Principles)** | Default quality standards |
| **Layer 3 (Methodology)** | Research & Development, 70/30 exploration |
| **Layer 4 (Technical)** | ai-agent-development blueprint |

## Depth Level

**Standard** - Configures all layers with R&D methodology for experimental AI development.

## Key Axiom: A10 (Learning)

This example includes the **Learning** axiom because:
- AI systems improve through feedback
- Prompt optimization is iterative
- RAG quality improves with tuning

## Time to Complete

Following this walkthrough takes approximately **20-25 minutes**.

## Prerequisites

Before starting, ensure you have:

1. Cursor IDE installed
2. The cursor-agent-factory project opened in Cursor
3. Python 3.10+ installed (Anaconda recommended)
4. OpenAI API key configured
5. Basic familiarity with LangChain concepts

## Next Steps

1. Open [WALKTHROUGH.md](WALKTHROUGH.md) to begin the step-by-step process
2. Compare your results with [expected-output/](expected-output/) when complete
3. Customize the RAG pipeline for your specific documentation

## Related Examples

- [04 - Multi-Agent Research System](../04-multi-agent-research-system/) - Orchestrate multiple agents
- [01 - REST API Service](../01-rest-api-service/) - Add API endpoints to your chatbot
