# RAG Chatbot Agent - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for building an AI-powered documentation chatbot with RAG capabilities.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Have an OpenAI API key ready
4. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for an AI documentation chatbot with RAG
```

The factory will begin the layered questionnaire process.

---

### Pre-Phase: Axiom Selection (Layer 0)

**Factory Prompt:**
> Every agent system needs foundational axioms. Core axioms (A1-A5) are always included.
> Would you like to add optional axioms?

**Your Response:**
```
Yes, add A10 (Learning)
```

**Rationale:** For AI agent development, continuous learning and improvement from feedback is essential. A10 ensures the system is designed to evolve.

**Selected Axioms:**

| ID | Axiom | Why Selected |
|----|-------|--------------|
| A1 | Verifiability | All outputs must cite sources (always included) |
| A2 | User Primacy | User questions take precedence (always included) |
| A3 | Transparency | Explain reasoning and sources (always included) |
| A4 | Non-Harm | No harmful or misleading information (always included) |
| A5 | Consistency | Consistent behavior across queries (always included) |
| A10 | Learning | Improve from user feedback (optional, selected) |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To enable developers to get accurate, sourced answers from documentation through natural language queries
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
Developers who need quick, accurate answers from technical documentation
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Answer 80% of documentation questions accurately with proper source citations
```

---

### Phase 0.5: Depth Selection

**Factory Prompt:**
> How deep should we define the remaining layers?
> - A) Quick Start - Use defaults, go to technical
> - B) Standard - Define principles, select methodology
> - C) Comprehensive - Define all layers including enforcement and practices

**Your Response:**
```
B (Standard)
```

**Rationale:** Standard depth with R&D methodology is ideal for AI experimentation.

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
1-3 developers
```

---

**Factory Prompt:**
> Exploration vs exploitation ratio?

**Your Response:**
```
70/30 - More exploration for prompt and RAG tuning
```

The factory will configure:
- Spike reviews for experimental work
- Hypothesis-driven development
- Experiment tracking
- Feedback integration loops

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
doc-qa-bot
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
RAG-powered chatbot for documentation Q&A with source citations and conversation memory
```

---

**Factory Prompt:**
> What domain does this project serve?

**Your Response:**
```
AI/ML development, developer tools
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
LangChain, Streamlit, ChromaDB
```

---

**Factory Prompt:**
> I found a matching blueprint: ai-agent-development. Would you like to use it?

**Your Response:**
```
Yes
```

---

**Factory Prompt:**
> What LLM provider will you use?

**Your Response:**
```
OpenAI with GPT-4
```

---

**Factory Prompt:**
> What vector store will you use?

**Your Response:**
```
ChromaDB for local development, with option for Pinecone in production
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
GitHub issues for bugs and features, experiment logs for prompt iterations
```

---

**Factory Prompt:**
> Would you like to configure MCP server integration?

**Your Response:**
```
Yes, configure DeepWiki for GitHub repository analysis
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What LLM patterns should the agent follow?

**Your Response:**
```
Chain-of-thought prompting, retrieval-augmented generation, conversation memory
```

---

**Factory Prompt:**
> Any specific prompt engineering patterns to enforce?

**Your Response:**
```
Always cite sources, admit uncertainty, provide structured responses
```

---

### Phase 5: Agent & Skill Selection

**Factory Prompt:**
> Which agents should I include?

**Your Response:**
```
Code reviewer, test generator, and explorer for research
```

---

**Factory Prompt:**
> Which skills should be available?

**Your Response:**
```
prompt-engineering, agent-coordination, grounding, tdd
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\doc-qa-bot
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: doc-qa-bot                                            ║
║ Blueprint: ai-agent-development                                ║
║ Depth: Standard                                                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: A10 (Learning)                                     ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Enable accurate documentation Q&A                   ║
║   Stakeholders: Developers                                     ║
║   Success: 80% accuracy with source citations                  ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Research & Development                          ║
║   Exploration: 70%                                             ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: Python, LangChain, ChromaDB, Streamlit                ║
║   LLM: OpenAI GPT-4                                            ║
║   Agents: code-reviewer, test-generator, explorer              ║
║   Skills: prompt-engineering, agent-coordination, grounding    ║
║   MCP: DeepWiki                                                ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\doc-qa-bot                                 ║
╚════════════════════════════════════════════════════════════════╝

Proceed with generation? (yes/no)
```

**Your Response:**
```
Yes
```

---

## Generated Artifacts

After generation, your project will contain:

```
doc-qa-bot/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── test-generator.md
│   │   └── explorer.md           # Research agent
│   └── skills/
│       ├── prompt-engineering/
│       │   └── SKILL.md          # Prompt optimization
│       ├── agent-coordination/
│       │   └── SKILL.md          # Multi-component coordination
│       ├── grounding/
│       │   └── SKILL.md          # Data verification
│       └── tdd/
│           └── SKILL.md
├── knowledge/
│   ├── langchain-patterns.json   # LangChain best practices
│   ├── prompt-engineering.json   # Prompt techniques
│   └── rag-patterns.json         # RAG architecture patterns
├── agents/
│   └── qa_agent.py               # Main Q&A agent implementation
├── prompts/
│   ├── system/
│   │   └── qa_system.md          # System prompt
│   └── templates/
│       └── qa_template.md        # Query template
├── workflow/
│   └── rag_chain.py              # LangChain RAG workflow
├── apps/
│   └── streamlit_app.py          # Streamlit UI
├── knowledge_base/               # Document storage
├── tests/
│   ├── test_rag_chain.py
│   └── test_prompts.py
├── workflows/
│   └── methodology.yaml          # R&D methodology config
├── .cursorrules                  # 5-layer agent rules
├── PURPOSE.md                    # Mission and purpose
├── pyproject.toml
└── README.md
```

---

## Using the Generated System

### Building the RAG Pipeline

**Example: Create RAG Chain**
```
Create a RAG chain for querying Python documentation with conversation memory
```

The agent will:
1. Use knowledge/langchain-patterns.json for chain patterns
2. Use knowledge/rag-patterns.json for retrieval setup
3. Generate the chain with proper error handling
4. Add conversation memory for follow-up questions

### Prompt Optimization

**Example: Improve Prompt**
```
Optimize the system prompt to reduce hallucinations and improve source citations
```

The prompt-engineering skill will:
1. Analyze current prompt effectiveness
2. Apply patterns from knowledge/prompt-engineering.json
3. Suggest specific improvements
4. Track changes for A10 (Learning)

### Research Mode

**Example: Explore Techniques**
```
Research best practices for chunking strategies in RAG systems
```

The explorer agent will:
1. Use DeepWiki MCP to analyze relevant repositories
2. Synthesize findings
3. Propose experiments to test

---

## Key Patterns for RAG Development

### Document Loading and Chunking

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
```

### Vector Store Setup

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory="./chroma_db"
)
```

### RAG Chain with Memory

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    return_source_documents=True
)
```

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Should include A10 (Learning) axiom
2. `PURPOSE.md` - Should reflect documentation Q&A mission
3. `knowledge/` - Should contain LangChain and RAG patterns
4. Agent files - Should include explorer for research

---

## Next Steps

1. Load your documentation into the vector store
2. Test the RAG chain with sample queries
3. Iterate on prompts using the prompt-engineering skill
4. Track improvements per A10 (Learning)

**Congratulations!** You've generated a complete Cursor agent system for RAG-powered documentation Q&A.
