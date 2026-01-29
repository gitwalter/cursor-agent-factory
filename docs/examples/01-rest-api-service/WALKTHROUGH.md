# REST API Service - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for a Python FastAPI REST API project.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active (Cursor reads this automatically)
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for a Python FastAPI REST API
```

The factory will begin the layered questionnaire process.

---

### Pre-Phase: Axiom Selection (Layer 0)

The factory will present the axiom configuration:

**Factory Prompt:**
> Every agent system needs foundational axioms. Core axioms (A1-A5) are always included.
> Would you like to add optional axioms?

**Your Response:**
```
Yes, add A6 (Minimalism)
```

**Rationale:** For an API project, minimalism helps avoid over-engineering. We want clean, focused code without unnecessary abstractions.

**Selected Axioms:**

| ID | Axiom | Why Selected |
|----|-------|--------------|
| A1 | Verifiability | All outputs must be verifiable (always included) |
| A2 | User Primacy | User intent takes precedence (always included) |
| A3 | Transparency | Reasoning must be explainable (always included) |
| A4 | Non-Harm | No harmful actions (always included) |
| A5 | Consistency | No rule contradictions (always included) |
| A6 | Minimalism | Simplest solution that works (optional, selected) |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To accelerate REST API development by automating boilerplate, enforcing best practices, and integrating with team workflows
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
Backend developers on the engineering team (4-6 people) building and maintaining the API
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Reduce time from API design to working implementation by 50% while maintaining quality standards
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

**Rationale:** Standard depth is ideal for most projects. It configures methodology without the overhead of detailed enforcement and practice definitions.

---

### Phases 0.6-0.7: Principles & Methodology (Layer 2-3)

**Factory Prompt:**
> What development methodology fits your team?

**Your Response:**
```
Agile Scrum
```

---

**Factory Prompt:**
> Team size?

**Your Response:**
```
4-6 developers
```

---

**Factory Prompt:**
> Sprint length?

**Your Response:**
```
2 weeks
```

The factory will configure:
- Sprint planning ceremonies
- Daily standups
- Sprint retrospectives
- Code review gates

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
user-api-service
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
REST API for user management with authentication, profiles, and role-based access control
```

---

**Factory Prompt:**
> What domain does this project serve?

**Your Response:**
```
Web backend / API development
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
FastAPI, SQLAlchemy, Pydantic, Alembic
```

---

**Factory Prompt:**
> I found a matching blueprint: python-fastapi. Would you like to use it?

**Your Response:**
```
Yes
```

---

**Factory Prompt:**
> What database will you use?

**Your Response:**
```
PostgreSQL for production, SQLite for development
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
Jira tickets for bugs and features, Confluence specs for larger features
```

---

**Factory Prompt:**
> Would you like to configure MCP server integration for Jira/Confluence?

**Your Response:**
```
Yes, configure Atlassian MCP
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What naming conventions should the agent follow?

**Your Response:**
```
PEP 8 for Python, snake_case for functions and variables, PascalCase for classes
```

---

**Factory Prompt:**
> Any specific API patterns to enforce?

**Your Response:**
```
RESTful conventions, consistent error responses, OpenAPI documentation
```

---

### Phase 5: Agent & Skill Selection

**Factory Prompt:**
> Which agents should I include?

**Your Response:**
```
Code reviewer and test generator
```

---

**Factory Prompt:**
> Which skills should be available?

**Your Response:**
```
bugfix-workflow, feature-workflow, tdd, grounding
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\user-api-service
```

(Adjust path for your system)

---

## Review Summary

Before generation, the factory presents a summary:

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: user-api-service                                      ║
║ Blueprint: python-fastapi                                      ║
║ Depth: Standard                                                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5 (Verifiability, User Primacy, Transparency,      ║
║          Non-Harm, Consistency)                                ║
║   Optional: A6 (Minimalism)                                    ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Accelerate REST API development                     ║
║   Stakeholders: Backend developers (4-6)                       ║
║   Success: 50% reduction in implementation time                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Agile Scrum                                     ║
║   Sprint Length: 2 weeks                                       ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: Python, FastAPI, SQLAlchemy, Pydantic                 ║
║   Agents: code-reviewer, test-generator                        ║
║   Skills: bugfix-workflow, feature-workflow, tdd, grounding    ║
║   MCP: Atlassian (Jira/Confluence)                             ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\user-api-service                           ║
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
user-api-service/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md       # Code review agent
│   │   └── test-generator.md      # Test generation agent
│   └── skills/
│       ├── bugfix-workflow/
│       │   └── SKILL.md           # Jira-driven bug fix process
│       ├── feature-workflow/
│       │   └── SKILL.md           # Confluence-driven feature process
│       ├── tdd/
│       │   └── SKILL.md           # Test-driven development
│       └── grounding/
│           └── SKILL.md           # Data structure verification
├── knowledge/
│   ├── naming-conventions.json    # Python naming rules
│   ├── api-patterns.json          # FastAPI patterns
│   └── test-patterns.json         # pytest patterns
├── templates/
│   └── python/
│       ├── service/               # Service class templates
│       ├── repository/            # Repository templates
│       ├── router/                # FastAPI router templates
│       └── test/                  # Test templates
├── workflows/
│   └── methodology.yaml           # Agile Scrum configuration
├── src/                           # Your application code
├── tests/                         # Test files
├── .cursorrules                   # 5-layer agent behavior rules
├── PURPOSE.md                     # Mission and purpose document
├── pyproject.toml                 # Python project configuration
└── README.md                      # Project documentation
```

---

## Using the Generated System

### Activating Agents

Once you open the generated project in Cursor, the agents are automatically available.

**Example: Code Review**
```
Review the user authentication endpoint for security issues
```

The code-reviewer agent will:
1. Read the grounding skill to understand verification requirements
2. Analyze the endpoint code
3. Check against knowledge/api-patterns.json
4. Provide actionable feedback

**Example: Bug Fix Workflow**
```
Fix bug PROJ-123
```

The bugfix-workflow skill will:
1. Fetch ticket details from Jira (via MCP)
2. Analyze the issue
3. Propose a fix
4. Generate tests
5. Update the ticket status

**Example: Test Generation**
```
Generate tests for the user service
```

The test-generator agent will:
1. Use the tdd skill
2. Reference knowledge/test-patterns.json
3. Create pytest tests with fixtures
4. Include edge cases and error scenarios

---

## Customization Tips

### Adding a New Endpoint

1. Describe the endpoint to the agent
2. The agent uses templates/python/router/ to scaffold
3. It checks knowledge/api-patterns.json for consistency
4. It generates tests using the tdd skill

### Modifying Methodology

Edit `workflows/methodology.yaml` to adjust:
- Sprint length
- Ceremony schedules
- Code review requirements

### Adding Custom Knowledge

Add JSON files to `knowledge/` for domain-specific patterns:
- `auth-patterns.json` - Authentication best practices
- `error-handling.json` - Error response standards

---

## Verification

Compare your generated files with the reference in [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension (e.g., `.cursorrules.example`) to prevent interference with the factory. Your generated files will not have this extension.

1. `.cursorrules` - Should contain 5-layer structure (compare with `.cursorrules.example`)
2. `PURPOSE.md` - Should reflect your mission statement
3. Agent files - Should reference correct skills
4. Knowledge files - Should contain FastAPI patterns

---

## Next Steps

1. Open the generated project in Cursor
2. Start building your API endpoints
3. Use the agents to review and test your code
4. Iterate on the knowledge files as you learn patterns

**Congratulations!** You've successfully generated a complete Cursor agent system for REST API development.
