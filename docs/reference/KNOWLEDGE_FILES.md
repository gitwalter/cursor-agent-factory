# Knowledge Files Reference

> **Philosophy:** Knowledge files embody our [Culture and Values](../CULTURE_AND_VALUES.md)—grounding agent decisions in verified, empirical knowledge (Comte's positivism, Axiom A1 Verifiability).

## Introduction

Knowledge files are JSON documents that provide structured, queryable information to Cursor agents during code generation and project development. These files serve as the "memory" of the Cursor Agent Factory, encoding patterns, best practices, capabilities, and domain-specific knowledge that agents can reference when generating code, workflows, and project configurations.

The factory currently includes **69 knowledge files** covering technology stacks, AI/agent patterns, integration patterns, trading/quant patterns, and factory metadata.

### Purpose of JSON Knowledge Files

Knowledge files enable agents to:
- **Query patterns**: Access proven solutions and architectural patterns for specific technologies
- **Maintain consistency**: Apply consistent coding standards, naming conventions, and structural patterns across generated projects
- **Ground decisions**: Reference authoritative sources (like SAP documentation, design patterns, or framework best practices) before making implementation choices
- **Avoid hallucinations**: Verify assumptions against documented patterns and capabilities before generating code

### How Agents Query Knowledge Files

Agents access knowledge files through semantic search and structured queries. When generating code or making architectural decisions, agents:
1. **Search relevant knowledge**: Query knowledge files matching the current stack, framework, or domain
2. **Extract patterns**: Retrieve specific patterns, code examples, or best practices
3. **Apply contextually**: Use extracted knowledge to inform code generation, ensuring alignment with established patterns
4. **Verify against knowledge**: Cross-reference generated code against knowledge file patterns to ensure correctness

### Factory Knowledge vs Generated Project Knowledge

The Factory maintains two types of knowledge:

- **Factory Knowledge** (`knowledge/` directory): Universal patterns, capabilities, and best practices available to all generated projects. These files are part of the Factory itself and include stack-specific patterns, AI/agent patterns, integration patterns, and factory metadata.

- **Generated Project Knowledge**: Project-specific knowledge files created during project generation. These may include domain-specific patterns, project conventions, or custom knowledge extracted from project requirements.

### Common Knowledge File Structure

All knowledge files follow a consistent JSON schema structure:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Knowledge File Title",
  "description": "Purpose and scope of this knowledge file",
  "version": "1.0.0",
  "data": {
    // Structured knowledge content
  }
}
```

Key elements:
- **`$schema`**: JSON Schema reference for validation
- **`title`**: Human-readable name
- **`description`**: Purpose and scope
- **`version`**: Semantic version for tracking changes
- **`data`** (or domain-specific keys): Structured knowledge content organized by categories, patterns, or concepts

## Knowledge File Categories Table

| File | Category | Description |
|------|----------|-------------|
| `fastapi-patterns.json` | Stack-Specific | Production-grade FastAPI patterns, domain-driven structure, async patterns, dependency injection |
| `nextjs-patterns.json` | Stack-Specific | Next.js 14+ patterns, App Router, Server Components, API routes, authentication |
| `dotnet-patterns.json` | Stack-Specific | .NET patterns, C# conventions, ASP.NET Core, Entity Framework, dependency injection |
| `spring-patterns.json` | Stack-Specific | Spring Boot patterns, REST APIs, JPA, security, testing, microservices |
| `streamlit-patterns.json` | Stack-Specific | Streamlit app patterns, data visualization, state management, deployment |
| `langchain-patterns.json` | AI/Agent | LangChain LCEL patterns, agent development, tool usage, memory, streaming |
| `langgraph-workflows.json` | AI/Agent | LangGraph state machines, agent workflows, multi-agent coordination |
| `crewai-patterns.json` | AI/Agent | CrewAI agent teams, Flows, Pipelines, Knowledge sources, training, async execution |
| `autogen-patterns.json` | AI/Agent | AutoGen multi-agent patterns, conversation patterns, code generation workflows |
| `mcp-patterns.json` | AI/Agent | Model Context Protocol patterns, server integration, tool definitions |
| `agent-coordination.json` | AI/Agent | Multi-agent coordination patterns, communication protocols, task distribution |
| `agent-testing.json` | AI/Agent | Testing strategies for AI agents, evaluation patterns, verification methods |
| `prompt-engineering.json` | AI/Agent | Prompt design patterns, few-shot examples, chain-of-thought, structured outputs |
| `multi-agent-coordination.json` | AI/Agent | Advanced multi-agent systems, orchestration, conflict resolution, shared state |
| `multi-agent-patterns.json` | AI/Agent | Consolidated CrewAI, AutoGen, LangGraph multi-agent patterns |
| `rag-patterns.json` | AI/Agent | RAG architecture, chunking, retrieval, reranking, evaluation |
| `llm-evaluation-patterns.json` | AI/Agent | RAGAS, LLM-as-judge, automated testing patterns |
| `prompt-library.json` | AI/Agent | Reusable prompt templates for common AI tasks |
| `ml-workflow-patterns.json` | AI/ML | Framework-agnostic ML workflow patterns |
| `deep-learning-patterns.json` | AI/ML | PyTorch/TensorFlow training, optimization, checkpointing |
| `vector-database-patterns.json` | AI/ML | ChromaDB, Qdrant, Pinecone, FAISS patterns |
| `mlops-patterns.json` | AI/ML | MLflow, W&B, TensorBoard experiment tracking |
| `llm-provider-comparison.json` | AI/ML | OpenAI, Anthropic, Google, Ollama comparison |
| `huggingface-patterns.json` | AI/ML | Transformers, Datasets, PEFT, Hub patterns |
| `model-serving-patterns.json` | AI/ML | FastAPI, vLLM, BentoML deployment patterns |
| `llm-fine-tuning-patterns.json` | AI/ML | LoRA, QLoRA, DPO, ORPO fine-tuning patterns |
| `groovy-patterns.json` | Integration | SAP CPI Groovy script patterns, message processing, error handling, transformations |
| `iflow-patterns.json` | Integration | SAP Integration Flow patterns, adapters, routing, exception handling, monitoring |
| `n8n-patterns.json` | Integration | n8n workflow patterns, node configurations, error handling, data transformations |
| `sap-cap-patterns.json` | Integration | SAP Cloud Application Programming patterns, CDS views, services, Fiori integration |
| `cpi-error-handling.json` | Integration | CPI exception handling patterns, retry strategies, circuit breaker, error routing |
| `mapping-patterns.json` | Integration | XML/JSON/IDoc mapping patterns, data transformations, helper functions |
| `b2b-patterns.json` | Integration | EDI (EDIFACT/X12), AS2 protocol, partner management, IDoc integration |
| `security-patterns.json` | Integration | OAuth 2.0, certificates, encryption, credential management, data masking |
| `naming-conventions.json` | SAP/ABAP | Clean ABAP and Hungarian notation naming conventions for ABAP development |
| `common-table-patterns.json` | SAP/ABAP | SAP table structures, delivery classes, key patterns, audit fields |
| `tadir-object-types.json` | SAP/ABAP | ABAP repository object types (CLAS, INTF, DDLS, BDEF, SRVB, etc.) |
| `cdhdr-object-classes.json` | SAP/ABAP | Change document patterns for audit trails and history tracking |
| `service-class-catalog.json` | SAP/ABAP | Service class patterns, repository patterns, factory patterns for Clean ABAP |
| `sap-reference-repos.json` | SAP/ABAP | Curated SAP sample repositories for learning and reference |
| `design-patterns.json` | Core | Gang of Four and modern design patterns with stack-specific examples |
| `architecture-patterns.json` | Core | Architectural patterns: microservices, event-driven, CQRS, layered architecture |
| `security-checklist.json` | Core | Security best practices, OWASP guidelines, authentication, authorization, data protection |
| `best-practices.json` | Core | Universal software development best practices, code quality, maintainability |
| `cicd-patterns.json` | Core | CI/CD pipeline patterns, testing strategies, deployment automation, quality gates |
| `tdd-patterns.json` | Core | Test-Driven Development patterns, red-green-refactor, test organization, mocking |
| `workflow-patterns.json` | Core | Development workflow patterns, git workflows, branching strategies, code review |
| `trading-patterns.json` | Trading/Quant | Algo trading strategies, technical indicators, backtesting, fundamental data |
| `quantitative-finance.json` | Trading/Quant | Risk metrics, portfolio theory, statistical tests, performance reporting |
| `risk-management.json` | Trading/Quant | Position sizing, VaR, drawdown management, portfolio risk |
| `skill-catalog.json` | Factory Meta | Registry of all available skills (generic + stack-specific) with metadata |
| `stack-capabilities.json` | Factory Meta | Stack-specific agent capabilities, frameworks, naming conventions, tooling |
| `mcp-servers-catalog.json` | Factory Meta | Available MCP server integrations with configuration examples and capabilities |
| `augmented-coding-patterns.json` | Factory Meta | AI collaboration patterns: Active Partner, Check Alignment, Chain of Small Steps |
| `team-dynamics.json` | Factory Meta | Team collaboration patterns, facilitation approaches, workshop adaptations |
| `game-mechanics.json` | Factory Meta | Gamification patterns for workshops, engagement strategies, team building |
| `workshop-facilitation.json` | Factory Meta | Workshop facilitation patterns, agenda templates, facilitation techniques |
| `guardian-protocol.json` | Factory Meta | Layer 0 Integrity Guardian coordination wisdom, response protocols, philosophical foundations |

## Category Details

### Stack-Specific Knowledge

Stack-specific knowledge files provide framework and language patterns tailored to particular technology stacks. These files enable agents to generate code that follows framework conventions and best practices.

**`fastapi-patterns.json`**: Production-grade patterns for FastAPI 0.115+ applications. Includes domain-driven layout structures, Pydantic v2 patterns, dependency injection patterns, async/await best practices, error handling, authentication/authorization patterns, database integration (SQLAlchemy), testing strategies, and deployment configurations. Aligns with Factory axioms through type hints (A1: Verifiability), explicit dependencies (A3: Transparency), and modular structure (A4: Adaptability).

**`nextjs-patterns.json`**: Next.js 14+ patterns covering App Router architecture, Server Components, Client Components, API routes, authentication strategies (NextAuth, Auth.js), data fetching patterns (Server Actions, React Server Components), routing conventions, middleware patterns, and deployment optimizations. Provides patterns for both full-stack applications and frontend-only implementations.

**`dotnet-patterns.json`**: .NET and C# patterns including ASP.NET Core patterns, Entity Framework Core patterns, dependency injection, middleware pipelines, API versioning, authentication/authorization (Identity, JWT), logging and monitoring, testing frameworks (xUnit, NUnit), and .NET naming conventions. Covers both traditional .NET Framework and modern .NET Core patterns.

**`spring-patterns.json`**: Spring Boot patterns for Java applications including REST API design, Spring Data JPA patterns, Spring Security configurations, dependency injection, transaction management, testing with Spring Boot Test, actuator for monitoring, and microservices patterns. Includes both traditional Spring MVC and reactive Spring WebFlux patterns.

**`streamlit-patterns.json`**: Streamlit application patterns for Python data applications. Covers state management, session state patterns, data visualization best practices, form handling, caching strategies, custom components, deployment patterns, and integration with data science libraries (pandas, plotly, matplotlib).

### AI/Agent Knowledge

AI/Agent knowledge files provide patterns for building AI-powered applications, multi-agent systems, and LLM integration.

**`langchain-patterns.json`**: LangChain 0.3+ patterns including LangChain Expression Language (LCEL) composition patterns (pipe, parallel, conditional routing), chain patterns, agent patterns with tools, memory management, streaming responses, and structured outputs. Includes best practices for prompt templates, output parsers, and retriever-augmented generation (RAG).

**`langgraph-workflows.json`**: LangGraph state machine patterns for building complex agent workflows. Covers state management, node definitions, edge routing, conditional transitions, human-in-the-loop patterns, and multi-agent coordination within LangGraph. Includes patterns for error recovery and workflow persistence.

**`crewai-patterns.json`**: Comprehensive CrewAI patterns for building multi-agent systems. Includes agent/task/crew definitions, process types (sequential, hierarchical, consensual), memory patterns, tool integration, and peer review patterns. **Extended in v1.1.0** with Flows (state management, conditional routing, parallel execution), Pipelines (crew chaining), Knowledge sources (string, file, PDF), training patterns, and async/batch kickoff patterns. Related skill: `crewai-workflow`.

**`autogen-patterns.json`**: AutoGen multi-agent conversation patterns, including group chat patterns, code generation workflows, function calling patterns, and agent specialization strategies. Includes patterns for managing agent conversations and coordinating multiple specialized agents.

**`mcp-patterns.json`**: Model Context Protocol patterns for integrating MCP servers with agents. Covers server configuration, tool definitions, resource management, and protocol best practices. Includes patterns for building custom MCP servers.

**`agent-coordination.json`**: Multi-agent coordination patterns including communication protocols, task distribution strategies, shared state management, conflict resolution, and consensus mechanisms. Covers both centralized and decentralized coordination approaches.

**`agent-testing.json`**: Testing strategies for AI agents including unit testing patterns, integration testing, evaluation metrics, prompt testing, and verification methods. Includes patterns for testing agent reasoning, tool usage, and output quality.

**`prompt-engineering.json`**: Prompt design patterns including few-shot learning, chain-of-thought prompting, structured output patterns, role-based prompting, and prompt optimization techniques. Includes patterns for reducing hallucinations and improving consistency.

**`multi-agent-coordination.json`**: Advanced multi-agent system patterns including orchestration architectures, shared knowledge bases, conflict resolution strategies, and distributed decision-making. Covers both competitive and collaborative multi-agent scenarios.

### AI/ML Knowledge (NEW)

**`ml-workflow-patterns.json`**: Framework-agnostic machine learning workflow patterns including train/test splitting, cross-validation, feature scaling, handling missing values, categorical encoding, imbalanced data, hyperparameter tuning, model comparison, and scikit-learn pipelines. Includes best practices for reproducibility and avoiding data leakage.

**`deep-learning-patterns.json`**: Deep learning training patterns for PyTorch and TensorFlow/Keras including training loops, gradient accumulation, mixed precision training, learning rate scheduling, early stopping, regularization (dropout, batch normalization, data augmentation), transfer learning, model ensembling, checkpointing, and distributed training.

**`vector-database-patterns.json`**: Patterns for vector databases used in RAG and semantic search including ChromaDB, Qdrant, Pinecone, Weaviate, Milvus, and pgvector. Covers embedding selection, chunking strategies, retrieval patterns (similarity, MMR, hybrid, reranking), and production deployment.

**`mlops-patterns.json`**: MLOps patterns for experiment tracking (MLflow, Weights & Biases, TensorBoard), model registry, model serving, CI/CD pipelines, and production monitoring including prediction logging and data drift detection.

**`llm-provider-comparison.json`**: Comprehensive comparison of LLM providers including OpenAI (GPT-4o, o1), Anthropic (Claude 3.5), Google (Gemini 2.0), and local models (Ollama). Includes pricing, features, structured output patterns, error handling, and LangChain integration.

**`huggingface-patterns.json`**: Hugging Face Transformers patterns including model loading, inference, chat models, datasets, preprocessing, Trainer API, PEFT/LoRA fine-tuning, Hub integration, and optimization (quantization, Flash Attention).

**`rag-patterns.json`**: RAG architecture patterns including basic RAG, conversational RAG, agentic RAG, chunking strategies, retrieval strategies, prompt patterns, RAGAS evaluation, and production patterns (caching, streaming, observability).

**`multi-agent-patterns.json`**: Consolidated patterns for multi-agent systems using CrewAI (role definition, task workflows, hierarchical crews), AutoGen (two-agent chat, group chat, teachable agents), and LangGraph (multi-agent graphs). Includes coordination patterns and anti-patterns.

**`llm-evaluation-patterns.json`**: Patterns for evaluating LLMs and RAG systems including RAGAS metrics, LLM-as-judge, pairwise comparison, automated testing, regression testing, and observability with LangSmith.

**`model-serving-patterns.json`**: Model deployment patterns including FastAPI serving, batch predictions, async inference, vLLM for LLM serving, BentoML, Docker containerization, Prometheus metrics, and scaling patterns.

**`llm-fine-tuning-patterns.json`**: LLM fine-tuning patterns including data preparation, LoRA, QLoRA, full fine-tuning with DeepSpeed, DPO/ORPO for preference optimization, evaluation, and merging/deployment.

**`prompt-library.json`**: Reusable prompt templates including system prompts for code assistant, code reviewer, RAG Q&A, and data analyst. Task prompts for summarization, classification, entity extraction, code generation, SQL generation. Few-shot examples and guardrail prompts.

### Integration Knowledge

Integration knowledge files provide patterns for connecting systems, platforms, and services.

**`groovy-patterns.json`**: SAP Cloud Platform Integration (CPI) Groovy script patterns for message processing, data transformation, error handling, and external system integration. Includes patterns for working with XML, JSON, and CSV payloads, as well as SAP-specific data structures.

**`iflow-patterns.json`**: SAP Integration Flow (iFlow) patterns including adapter configurations (SOAP, REST, IDoc, SFTP), routing patterns, exception handling, message mapping, and monitoring configurations. Covers both point-to-point and hub-based integration scenarios.

**`n8n-patterns.json`**: n8n workflow automation patterns including node configurations, error handling strategies, data transformation workflows, webhook patterns, and integration with various services. Includes patterns for complex workflow orchestration and conditional logic.

**`sap-cap-patterns.json`**: SAP Cloud Application Programming (CAP) patterns including CDS view definitions, service definitions, Fiori application integration, database modeling, and OData service patterns. Covers both Node.js and Java CAP runtimes.

### Core Knowledge

Core knowledge files provide universal development patterns applicable across all stacks and domains.

**`design-patterns.json`**: Comprehensive catalog of design patterns including Gang of Four patterns (creational, structural, behavioral) with stack-specific examples for Python, TypeScript, C#, Java, and other languages. Each pattern includes intent, when to use, and code examples.

**`architecture-patterns.json`**: Architectural patterns including microservices, event-driven architecture, CQRS (Command Query Responsibility Segregation), layered architecture, hexagonal architecture, and API gateway patterns. Includes trade-offs and when to apply each pattern.

**`security-checklist.json`**: Security best practices organized by category: authentication, authorization, data protection, input validation, output encoding, cryptography, secure communication, and compliance. Aligns with OWASP Top 10 and provides actionable checklists.

**`best-practices.json`**: Universal software development best practices including code organization, naming conventions, documentation standards, error handling, logging, performance optimization, and maintainability principles. Applicable across all programming languages and frameworks.

**`cicd-patterns.json`**: CI/CD pipeline patterns including build automation, test execution strategies, deployment pipelines, quality gates, environment management, and rollback procedures. Covers patterns for various CI/CD platforms (GitHub Actions, GitLab CI, Jenkins, etc.).

**`tdd-patterns.json`**: Test-Driven Development patterns including red-green-refactor cycle, test organization strategies, mocking patterns, test data management, and test coverage strategies. Includes patterns for unit, integration, and end-to-end testing.

**`workflow-patterns.json`**: Development workflow patterns including Git workflows (Git Flow, GitHub Flow, GitLab Flow), branching strategies, code review processes, pull request patterns, and release management workflows.

### Factory Meta Knowledge

Factory Meta knowledge files provide information about the Factory itself, its capabilities, and how to use it effectively.

> **📖 Related Documentation**: See [KNOWLEDGE_EVOLUTION.md](../KNOWLEDGE_EVOLUTION.md) for the complete Knowledge Evolution System architecture and configuration.

**`skill-catalog.json`**: Comprehensive registry of all available skills in the Factory. Organizes skills by category (core, workflow, grounding, testing, verification) and by stack (generic, sap-abap). Each skill entry includes ID, name, category, description, factory pattern path, when to use, and stack-specific implementation details. Skills with `factoryPattern: null` are implemented in external repositories.

**`stack-capabilities.json`**: Stack-specific agent capabilities including supported languages (Python, TypeScript, Java, C#, ABAP, Go, Rust), frameworks (FastAPI, Django, React, Next.js, Spring, .NET), file extensions, package managers, test frameworks, linters, formatters, style guides, naming conventions, and suggested agents/skills for each stack.

**`mcp-servers-catalog.json`**: Catalog of available Model Context Protocol (MCP) servers for agent integration. Includes servers for Atlassian (Jira/Confluence), SAP Documentation, DeepWiki (GitHub analysis), Sequential Thinking, Fetch, LangSmith, LangChain Docs, Notion, Linear, and Sentry. Each entry includes URL, authentication method, capabilities, available tools, suggested use cases, and configuration examples. Organized by capability and by stack.

**`augmented-coding-patterns.json`**: AI collaboration patterns curated from augmented-coding-patterns.org. Includes foundation patterns (Ground Rules, Knowledge Document, Context Management), collaboration patterns (Active Partner, Check Alignment, Feedback Loop), execution patterns (Chain of Small Steps, Offload Deterministic), anti-patterns (Silent Misalignment, AI Slop, Unvalidated Leaps), and obstacles (Compliance Bias, Context Rot, Hallucinations). Each pattern includes problem statement, solution, and alignment with Factory axioms.

**`team-dynamics.json`**: Team collaboration patterns grounded in Axiom 0 (love and trust). Covers team stages (forming, storming, norming, performing), facilitation approaches for each stage, workshop adaptations, conflict resolution patterns, and trust-building exercises. Includes patterns for distributed teams and diverse team compositions.

**`game-mechanics.json`**: Gamification patterns for workshops and team engagement. Includes patterns for making workshops engaging, competitive elements, reward systems, progress tracking, and team building through games. Designed to support Factory workshops (Vision Quest, Ethics Arena, Stack Safari, etc.).

**`workshop-facilitation.json`**: Workshop facilitation patterns including agenda templates, facilitation techniques, time management, participant engagement strategies, and workshop formats. Covers both in-person and remote facilitation patterns. Includes patterns specific to Factory workshops.

**`guardian-protocol.json`**: Layer 0 Integrity Guardian coordination wisdom. Contains the philosophical foundations (SDG, Love, Trust), core axioms (A1-A5), Wu Wei response protocol (graduated response levels 0-4), emergency protocols, multi-agent harmony patterns, and wisdom from Sun Tzu and Lao Tzu translated into coordination patterns. Enables the Guardian to operate with minimal intervention for maximum alignment.

**`factory-updates.json`**: Update feed for projects generated by the Factory. Lists available updates that generated projects can fetch and apply. Includes update channels (stable, latest), applicable blueprints, file mappings, and version information. Enables the Factory → Generated Project update flow.

**`artifact-dependencies.json`**: Dependency map defining which artifacts must be updated when other artifacts change. Includes documentation tracking, Factory component detection, and post-extension checklist. Used by the post-extension automation workflow.

## Key Knowledge Files Explained

### 1. skill-catalog.json

**Purpose**: Central registry of all skills available to agents, both generic (stack-agnostic) and stack-specific.

**Structure**: Organized into:
- **Categories**: Groups skills by type (core, workflow, grounding, testing, verification)
- **Skills**: Individual skill definitions with metadata
- **Skills by Stack**: Maps skills to applicable stacks (generic, sap-abap, etc.)

**Key Data Structures**:
- Each skill includes: `id`, `name`, `category`, `stackAgnostic` flag, `description`, `factoryPattern` (path to pattern file or null), `whenToUse` array, and stack-specific fields like `targetStack`, `implementationRepo`, `artifacts`, `mcpServers`.

**How Agents Use It**: Agents query this catalog to:
- Discover available skills for a given stack
- Understand skill capabilities and when to apply them
- Reference factory pattern files for skill implementation
- Identify stack-specific skills that require external repositories

**Example**: When generating a SAP ABAP project, agents query `skillsByStack.sap-abap` to discover specialized grounding skills like `ddic-grounding`, `cds-grounding`, `rap-grounding`, each with specific artifact types and MCP server requirements.

### 2. stack-capabilities.json

**Purpose**: Defines stack-specific capabilities, conventions, and tooling that agents should use when generating code.

**Structure**: Organized by:
- **Stacks**: Language-level capabilities (Python, TypeScript, Java, C#, ABAP, Go, Rust)
- **Frameworks**: Framework-specific information (FastAPI, Django, React, Next.js, Spring, .NET)

**Key Data Structures**:
- Each stack includes: `name`, `description`, `fileExtensions`, `packageManager`, `testFrameworks`, `linters`, `formatters`, `styleGuides`, `suggestedAgents`, `suggestedSkills`, `namingConventions` (variables, functions, classes, constants).

**How Agents Use It**: Agents reference this file to:
- Apply correct naming conventions (snake_case vs camelCase vs PascalCase)
- Select appropriate testing frameworks and tools
- Generate code that follows stack-specific style guides
- Suggest appropriate agents and skills for the stack

**Example**: When generating Python code, agents use `namingConventions` to ensure variables use `snake_case`, classes use `PascalCase`, and constants use `UPPER_SNAKE_CASE`, while also selecting `pytest` as the test framework and `black` as the formatter.

### 3. mcp-servers-catalog.json

**Purpose**: Catalog of available Model Context Protocol (MCP) servers that agents can integrate with for enhanced capabilities.

**Structure**: Organized by:
- **Servers**: Individual MCP server definitions
- **Servers by Capability**: Maps capabilities (jira, confluence, documentation, etc.) to servers
- **Servers by Stack**: Maps stacks to recommended servers

**Key Data Structures**:
- Each server includes: `name`, `description`, `url`, `authentication` (oauth, api-key, none), `capabilities` array, `tools` array (with name and description), `suggestedFor` array, `configExample` (JSON configuration snippet).

**How Agents Use It**: Agents query this catalog to:
- Discover MCP servers available for specific capabilities (e.g., Jira integration, SAP documentation)
- Generate correct MCP server configuration in project files
- Understand authentication requirements and setup procedures
- Identify servers recommended for specific stacks or use cases

**Example**: When generating a project that needs Jira integration, agents find the `atlassian` server in the catalog, extract its `configExample`, and include it in the generated MCP configuration, ensuring OAuth authentication is properly documented.

### 4. augmented-coding-patterns.json

**Purpose**: Patterns and anti-patterns for effective AI-augmented software development, aligned with Factory axioms.

**Structure**: Organized into:
- **Patterns**: Foundation, collaboration, and execution patterns
- **Anti-Patterns**: Common mistakes and how to avoid them
- **Obstacles**: Inherent AI limitations and mitigation strategies
- **Integration Guidance**: How to apply patterns in Factory-generated projects

**Key Data Structures**:
- Each pattern includes: `name`, `category`, `problem` statement, `pattern` description, `implementation` details, `our_equivalent` (Factory implementation), `axiom_basis` (which Factory axioms it supports).
- Anti-patterns include: `name`, `category`, `problem`, `what_goes_wrong` array, `solution`, `our_mitigation`.

**How Agents Use It**: Agents reference these patterns to:
- Apply Active Partner pattern (encouraging AI to push back on unclear requests)
- Use Check Alignment pattern (verifying understanding before implementation)
- Follow Chain of Small Steps pattern (breaking complex tasks into verifiable increments)
- Avoid anti-patterns like Silent Misalignment and AI Slop
- Mitigate obstacles like Compliance Bias and Context Rot

**Example**: When generating `.cursorrules` files, agents incorporate Active Partner pattern guidance, adding rules like "Push back when something seems wrong" and "Ask questions if something is not clear" to prevent silent misalignment. The Check Alignment pattern is integrated into methodology workflows, requiring agents to show understanding before major implementations.

---

*This reference covers all knowledge files in the Factory's `knowledge/` directory. For specific pattern details, refer to the individual JSON files. For information about how knowledge files are used during project generation, see the [Factory Reference](FACTORY_REFERENCE.md).*
