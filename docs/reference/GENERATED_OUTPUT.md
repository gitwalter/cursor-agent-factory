# Generated Output Reference

> **Philosophy:** Every generated artifact embodies our [Culture and Values](../CULTURE_AND_VALUES.md)—love, wisdom, and care for those who will use and maintain the code.

This document provides a comprehensive reference for what the Cursor Agent Factory generates. Understanding the generated structure and file formats helps you customize and extend your agent system effectively.

---

## 1. Introduction

The Cursor Agent Factory generates complete, working Cursor AI agent development environments tailored to your project's needs. Instead of manually configuring agents, skills, and rules for each project, you describe your requirements and the factory generates a tailored system grounded in clear values, purpose, and methodology.

Every generated system includes **Axiom 0 (Love and Trust)** as its foundation, ensuring that technical decisions serve the flourishing of users, developers, and maintainers.

### What Gets Generated

The factory generates a complete project structure including:

- **5-layer `.cursorrules` file** - Comprehensive agent behavior rules grounded in axioms, purpose, principles, methodology, and technical implementation
- **Purpose documentation** (`PURPOSE.md`) - Mission statement, stakeholders, and success criteria
- **AI agent definitions** (`.cursor/agents/`) - Specialized agents for code review, testing, documentation, and more
- **Reusable skill definitions** (`.cursor/skills/`) - Workflow patterns like TDD, grounding, bug fixes, and feature implementation
- **Structured knowledge files** (`knowledge/`) - JSON reference data for naming conventions, patterns, and domain knowledge
- **Code and document templates** (`templates/`) - Reusable templates for consistent code generation
- **Methodology configuration** (`workflows/methodology.yaml`) - Team workflow and coordination patterns
- **Enforcement patterns** (`enforcement.yaml`) - Quality gates and safety checks (Comprehensive only)
- **Practice patterns** (`practices.yaml`) - Daily, craft, and alignment practices (Comprehensive only)
- **PM configuration** (`pm/`) - Project management integration (if enabled)

### Relationship to Blueprints and Patterns

Generated output combines:

- **Blueprints** - Pre-configured technology stacks (Python/FastAPI, TypeScript/React, Java/Spring, etc.) that provide default agents, skills, and knowledge files
- **Patterns** - Reusable templates for agents, skills, methodologies, and principles that get instantiated with project-specific values
- **Knowledge Files** - Domain-specific reference data that agents query during code generation and review

The factory matches your requirements to blueprints, selects appropriate patterns, and generates a customized project structure.

### Onboarding Depth Options

The factory offers three depth options that determine what gets generated:

| Option | Description | Best For |
|--------|-------------|----------|
| **Quick Start** | Minimal configuration with core agents and skills | Rapid prototyping, learning the system |
| **Standard** | Full 5-layer architecture with methodology configuration | Most production projects |
| **Comprehensive** | Standard plus enforcement patterns and team practices | Enterprise systems, critical applications |

Each depth option includes progressively more configuration and governance mechanisms. See [Onboarding Depth Comparison](#6-onboarding-depth-comparison) for detailed differences.

---

## 2. Generated Project Structure

The factory generates a complete project structure following a consistent layout:

```
{PROJECT}/
├── .cursorrules              # 5-layer agent rules (L0-L4)
├── PURPOSE.md                # Mission document (Layer 1)
├── enforcement.yaml          # Enforcement config (Comprehensive only)
├── practices.yaml            # Team practices (Comprehensive only)
├── workflows/
│   └── methodology.yaml      # Methodology config (Layer 3)
├── .cursor/
│   ├── agents/               # Generated agents
│   │   ├── code-reviewer.md
│   │   ├── test-generator.md
│   │   └── ...
│   └── skills/               # Generated skills
│       ├── grounding/
│       │   └── SKILL.md
│       ├── tdd/
│       │   └── SKILL.md
│       └── ...
├── knowledge/                # Domain knowledge files
│   ├── naming-conventions.json
│   ├── api-patterns.json
│   └── ...
├── templates/                # Code/doc templates
│   ├── {language}/           # Language-specific code templates
│   │   ├── service-class/
│   │   ├── test-class/
│   │   └── ...
│   └── docs/                 # Document templates
│       ├── implementation_plan.md
│       └── technical_spec.md
├── src/                      # Source code structure
├── tests/                    # Test structure
└── README.md                 # Project documentation
```

### Component Descriptions

**`.cursorrules`** - The main agent behavior configuration file implementing the 5-layer architecture. Contains immutable axioms (Layer 0), purpose reference (Layer 1), principles (Layer 2), methodology (Layer 3), and technical rules (Layer 4). This file governs all AI agent behavior in the project.

**`PURPOSE.md`** - The mission document defining why the system exists, who it serves, and how success is measured. Agents reference this document to ensure their work aligns with project goals.

**`enforcement.yaml`** - Quality gates, safety checks, and integrity mechanisms that ensure values are lived, not just stated. Includes test coverage gates, code review requirements, destructive action confirmations, and axiom compliance checks. Only generated for Comprehensive depth.

**`practices.yaml`** - Team practices including daily rhythms (morning intention, standup), craft practices (code review, refactoring), and alignment practices (retrospectives, quarterly reviews). Only generated for Comprehensive depth.

**`workflows/methodology.yaml`** - Methodology configuration defining team coordination patterns (Agile Scrum, Kanban, R&D, Enterprise), ceremonies, and workflow integration. Generated for Standard and Comprehensive depths.

**`.cursor/agents/`** - Directory containing agent definition files. Each agent is a markdown file with frontmatter metadata, purpose, activation triggers, workflow steps, and rules. Agents are specialized AI assistants for specific tasks like code review, test generation, or documentation.

**`.cursor/skills/`** - Directory containing skill definition files. Skills are reusable procedures that agents can invoke. Each skill lives in its own subdirectory with a `SKILL.md` file. Skills encapsulate workflows like TDD, grounding (data verification), bug fixes, and feature implementation.

**`knowledge/`** - Directory containing structured JSON reference data. Knowledge files provide queryable information about naming conventions, API patterns, best practices, and domain-specific knowledge. Agents query these files during code generation and review.

**`templates/`** - Directory containing code and document templates. Language-specific code templates (e.g., `service-class`, `test-class`) provide consistent structure for generated code. Document templates provide standard formats for implementation plans, technical specs, and test plans.

**`src/`** - Standard source code directory structure, organized according to the selected technology stack and blueprint.

**`tests/`** - Test directory structure with unit, integration, and end-to-end test organization as appropriate for the stack.

**`README.md`** - Project documentation including setup instructions, architecture overview, and usage guidelines.

---

## 3. .cursorrules Structure

The `.cursorrules` file implements the 5-layer architecture and serves as the primary agent behavior configuration. It follows a structured format with clear layer separation.

### Layer 0: Integrity & Logic

The foundation layer containing immutable axioms:

```markdown
## Layer 0: Integrity & Logic

### Core Axioms (Immutable)

1. **A1 - Verifiability**: All agent outputs must be verifiable against source.
2. **A2 - User Primacy**: User intent takes precedence over agent convenience.
3. **A3 - Transparency**: Agent reasoning must be explainable on request.
4. **A4 - Non-Harm**: No action may knowingly cause harm to users or systems.
5. **A5 - Consistency**: No rule may contradict these axioms.

### Optional Axioms (Selected)
- A6 - Minimalism
- A7 - Reversibility
- A8 - Privacy
- A9 - Performance
- A10 - Learning

### Derivation Rules
- D1: If A1 AND output is code → require testing evidence
- D2: If A2 AND conflict exists → defer to user preference
- D3: If A4 AND action is destructive → require explicit confirmation
- D4: If A3 AND error occurs → provide clear explanation
- D5: If A5 AND new rule proposed → validate against axioms

### Validation Constraints
- Every rule must trace to at least one axiom
- No rule may contradict any axiom
- Layer precedence: L0 > L1 > L2 > L3 > L4
```

### Layer 1: Purpose Reference

Links to `PURPOSE.md` and provides mission summary:

```markdown
## Layer 1: Purpose

**Reference**: See `PURPOSE.md` for complete purpose documentation.

### Mission
{One-sentence mission statement}

### Stakeholders
{Primary stakeholders description}

### Success Criteria
{Measurable success criteria}
```

### Layer 2: Principles

Ethical boundaries, quality standards, and failure handling:

```markdown
## Layer 2: Principles

### Ethical Boundaries
| ID | Forbidden Behavior | Derived From |
|----|-------------------|--------------|
| EB1 | Silent failure without notification | A3 (Transparency) |
| EB2 | Destructive actions without confirmation | A4 (Non-Harm) |
| EB3 | Ignoring user preferences | A2 (User Primacy) |
| EB4 | Unverified claims or hallucinations | A1 (Verifiability) |
| EB5 | Rules that contradict axioms | A5 (Consistency) |

### Quality Standards
| ID | Required Standard | Derived From | Threshold |
|----|------------------|--------------|-----------|
| QS1 | Test coverage for code changes | A1 (Verifiability) | 80% |
| QS2 | Documentation for public interfaces | A3 (Transparency) | All public APIs |
| QS3 | Error handling with clear messages | A3, A4 | No uncaught exceptions |

### Failure Handling
| Failure Type | Response | Axiom Basis |
|--------------|----------|-------------|
| Unknown error | Explain what happened, suggest recovery | A3 |
| User conflict | Ask for clarification | A2 |
| Harmful request | Refuse with explanation | A4 |
```

### Layer 3: Methodology

References methodology configuration and coordination patterns:

```markdown
## Layer 3: Methodology

**Methodology**: Agile Scrum  
**Pattern**: domain_expert_swarm + peer_collaboration  
**Reference**: See `workflows/methodology.yaml` for complete configuration.

### Team Coordination
{Sprint configuration, ceremonies, workflow integration}

### Quality Gates
{Code review requirements, test coverage gates}
```

### Layer 4: Technical

Stack-specific rules, agent registry, skills, knowledge files, and MCP servers:

```markdown
## Layer 4: Technical Implementation

### Project Context
{Project description, domain, primary language, style guide}

### Available Agents
| Agent | Purpose | Location |
|-------|---------|----------|
| code-reviewer | Reviews code quality | .cursor/agents/code-reviewer.md |
| test-generator | Creates test cases | .cursor/agents/test-generator.md |

### Available Skills
| Skill | Description | Location |
|-------|-------------|----------|
| tdd | Test-driven development workflow | .cursor/skills/tdd/SKILL.md |
| grounding | Verify data structures | .cursor/skills/grounding/SKILL.md |

### MCP Server Integration
| Server | Purpose | URL |
|--------|---------|-----|
| atlassian | Jira/Confluence | https://mcp.atlassian.com/v1/sse |
```

The file also includes autonomous behavior rules, variable notation conventions, and response behavior guidelines that help agents work effectively with users.

---

## 3.5 Knowledge Extension Capability

Every generated project includes built-in knowledge extension capabilities:

### Included Components

| Component | Location | Purpose |
|-----------|----------|---------|
| `knowledge-extender` agent | `.cursor/agents/knowledge-extender.md` | Orchestrates knowledge base extension |
| `extend-knowledge` skill | `.cursor/skills/extend-knowledge/SKILL.md` | Core extension workflow |
| `manifest.json` | `knowledge/manifest.json` | Registry of all knowledge files |

### How to Use

Simply ask in chat:

```
"Extend knowledge for [topic]"
"Add knowledge about [framework/technology]"
"Create a skill for [purpose]"
```

The knowledge-extender agent will:
1. Research the topic using available methods
2. Generate structured JSON following project conventions
3. Update `knowledge/manifest.json` to register the new file
4. Report what was created

### Extension During Onboarding

The factory offers knowledge extension during the onboarding phase:
- Shows current knowledge coverage percentage
- Lists top knowledge gaps
- Offers to analyze all gaps or extend specific topics
- You can skip and run `--analyze-gaps` anytime later

---

## 4. Generated Agent Format

Agent files are markdown documents with YAML frontmatter and structured sections. They define specialized AI assistants for specific tasks.

### File Structure

```markdown
---
name: agent-name
description: Agent description
type: agent
skills: [skill-1, skill-2]
knowledge: [file.json]
---

# Agent Name

## Purpose

Clear statement of what this agent does and why it exists. Should align with project purpose and serve stakeholders.

## When Activated

List of triggers that cause this agent to activate:
- Trigger 1: "User mentions 'review code'"
- Trigger 2: "After code changes are made"
- Trigger 3: "User requests code analysis"

## Workflow

Step-by-step process the agent follows:

1. **Step 1**: Initial action or data gathering
2. **Step 2**: Analysis or processing
3. **Step 3**: Generation or recommendation
4. **Step 4**: Validation and output

Each step should be specific and actionable.

## Skills Used

| Skill | Purpose |
|-------|---------|
| skill-1 | What this skill contributes |
| skill-2 | What this skill contributes |

## Important Rules

- Rule 1: Specific constraint or requirement
- Rule 2: Axiom alignment (e.g., "Always verify outputs per A1")
- Rule 3: Quality standard (e.g., "Require test coverage per QS1")
```

### Section Descriptions

**Frontmatter** - YAML metadata at the top of the file:
- `name`: Unique identifier for the agent
- `description`: Brief description of agent purpose
- `type`: Always `agent` for agent files
- `skills`: Array of skill identifiers this agent uses
- `knowledge`: Array of knowledge file references

**Purpose** - Clear statement of agent mission, aligned with project purpose and serving stakeholders.

**When Activated** - List of triggers (user phrases, events, conditions) that cause agent activation. Should be specific and unambiguous.

**Workflow** - Step-by-step process the agent follows. Steps should be:
- Sequential and logical
- Specific and actionable
- Validated against axioms where appropriate
- Documented with clear outcomes

**Skills Used** - Table mapping skills to their purpose in this agent's workflow. Helps agents understand dependencies and coordination.

**Important Rules** - Specific constraints, axiom alignments, and quality standards. Rules should trace to Layer 0-2 principles and be enforceable.

### Example Agent

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and consistency
type: agent
skills: [grounding, code-review]
knowledge: [best-practices.json, api-patterns.json]
---

# Code Reviewer Agent

## Purpose

Review code changes for quality, security vulnerabilities, and consistency with project standards. Ensure all code meets quality gates before merge.

## When Activated

- User requests "review code" or "check code"
- After code changes are committed
- Before pull request merge
- User mentions "code review" or "analyze"

## Workflow

1. **Gather Context**: Read changed files, understand scope
2. **Apply Grounding**: Verify data structures and assumptions (skill: grounding)
3. **Check Standards**: Validate against style guide and best practices
4. **Security Scan**: Check for common vulnerabilities
5. **Test Coverage**: Verify tests exist and cover changes
6. **Generate Report**: Document findings with recommendations

## Skills Used

| Skill | Purpose |
|-------|---------|
| grounding | Verify data structures before review |
| code-review | Apply review checklist and standards |

## Important Rules

- Always verify test coverage per QS1 (A1: Verifiability)
- Never approve code with security vulnerabilities per A4 (Non-Harm)
- Document all findings per A3 (Transparency)
```

---

## 5. Generated Skill Format

Skill files define reusable procedures that agents can invoke. They follow a similar structure to agents but focus on process rather than autonomous behavior.

### File Structure

```markdown
---
name: skill-name
description: Skill description
type: skill
knowledge: [file.json]
---

# Skill Name

Brief introduction explaining what this skill does and when it's useful.

## When to Use

Specific scenarios where this skill should be invoked:
- Use case 1: "When implementing new data models"
- Use case 2: "Before writing API endpoints"
- Use case 3: "When user requests verification"

## Process

Step-by-step procedure:

### Step 1: Preparation
What needs to be gathered or prepared

### Step 2: Execution
Main actions to perform

### Step 3: Validation
How to verify the process succeeded

### Step 4: Output
What gets produced or documented

## Fallback Procedures

What to do when things go wrong:
- **If X fails**: Then do Y
- **If data unavailable**: Then use Z
- **If validation fails**: Then escalate to user

## Important Rules

- Rule 1: Specific constraint or requirement
- Rule 2: Axiom alignment
- Rule 3: Quality standard
```

### Section Descriptions

**Frontmatter** - YAML metadata:
- `name`: Unique identifier for the skill
- `description`: Brief description of skill purpose
- `type`: Always `skill` for skill files
- `knowledge`: Array of knowledge file references

**When to Use** - Specific scenarios and triggers. Should help agents decide when to invoke this skill.

**Process** - Step-by-step procedure with clear actions. Steps should be:
- Sequential and logical
- Specific enough to execute
- Include validation checkpoints
- Document expected outcomes

**Fallback Procedures** - Error handling and recovery strategies. Should cover common failure modes and provide clear escalation paths.

**Important Rules** - Constraints and requirements. Should align with axioms and quality standards.

### Example Skill

```markdown
---
name: grounding
description: Verify data structures and assumptions before implementation
type: skill
knowledge: [naming-conventions.json, api-patterns.json]
---

# Grounding Skill

Verify data structures, naming conventions, and assumptions before implementing code changes. Ensures accuracy and consistency.

## When to Use

- Before implementing new data models or API endpoints
- When user requests verification of assumptions
- Before making changes that affect data structures
- When reviewing code for consistency

## Process

### Step 1: Gather Requirements
- Read user request or ticket
- Extract mentioned data structures
- Identify affected components

### Step 2: Query Knowledge Files
- Check naming-conventions.json for naming rules
- Query api-patterns.json for API patterns
- Verify against existing codebase patterns

### Step 3: Validate Assumptions
- Verify data structure names match conventions
- Check API patterns align with standards
- Confirm no conflicts with existing code

### Step 4: Document Findings
- Report verified structures
- Flag any inconsistencies
- Provide recommendations

## Fallback Procedures

- **If knowledge file missing**: Use project conventions from existing code
- **If naming unclear**: Ask user for clarification per A2 (User Primacy)
- **If conflict detected**: Report conflict and suggest resolution

## Important Rules

- Always verify against source per A1 (Verifiability)
- Ask for clarification if uncertain per A2 (User Primacy)
- Document all findings per A3 (Transparency)
```

---

## 6. Onboarding Depth Comparison

The factory offers three depth options that determine what gets generated. Choose based on your project needs and team maturity.

### Comparison Table

| Component | Quick Start | Standard | Comprehensive |
|-----------|-------------|----------|---------------|
| **.cursorrules** | L0, L4 only | L0-L4 | L0-L4 |
| **PURPOSE.md** | Basic | Full | Full |
| **enforcement.yaml** | No | No | Yes |
| **practices.yaml** | No | No | Yes |
| **methodology.yaml** | No | Yes | Yes |
| **Agents** | Core only (2-3) | Full set (5-8) | Full set + custom (8+) |
| **Skills** | Core only (3-5) | Full set (8-12) | Full set + custom (12+) |
| **Knowledge** | Minimal (2-3 files) | Standard (5-8 files) | Full (10+ files) |
| **Templates** | Basic | Standard | Full + custom |
| **MCP Integration** | Basic | Full | Full + custom |

### Quick Start

**Best For**: Rapid prototyping, learning the system, small personal projects

**Includes**:
- Layer 0 (Axioms) and Layer 4 (Technical) in `.cursorrules`
- Basic `PURPOSE.md` with mission and stakeholders
- Core agents: `code-reviewer`, `test-generator`
- Core skills: `grounding`, `tdd`, `bugfix-workflow`
- Minimal knowledge files: `naming-conventions.json`, `best-practices.json`
- Basic code templates

**Excludes**:
- Layer 2 (Principles) and Layer 3 (Methodology) configuration
- Enforcement patterns
- Team practices
- Advanced agents and skills
- Comprehensive knowledge files

**Use When**: You want to get started quickly and add more structure later, or you're prototyping and don't need full governance.

### Standard

**Best For**: Most production projects, teams wanting full agent capabilities

**Includes**:
- Complete 5-layer `.cursorrules` (L0-L4)
- Full `PURPOSE.md` with mission, stakeholders, success criteria, and axiom alignment
- `workflows/methodology.yaml` with methodology configuration
- Full agent set: `code-reviewer`, `test-generator`, `documentation-agent`, `explorer`, `refactorer`
- Full skill set: `grounding`, `tdd`, `bugfix-workflow`, `feature-workflow`, `code-review`, `documentation-workflow`
- Standard knowledge files: naming conventions, API patterns, best practices, domain-specific knowledge
- Standard code and document templates
- MCP server integration

**Excludes**:
- Enforcement patterns (`enforcement.yaml`)
- Team practices (`practices.yaml`)

**Use When**: You want a complete agent system with methodology but don't need enforcement gates or team practice definitions yet.

### Comprehensive

**Best For**: Enterprise systems, critical applications, teams wanting full governance

**Includes**:
- Everything from Standard
- `enforcement.yaml` with quality gates, safety checks, and integrity mechanisms:
  - Test coverage gates (E1)
  - Code review requirements (E2)
  - Documentation completeness (E3)
  - Style consistency (E4)
  - Destructive action confirmations (E5)
  - Backup before changes (E6)
  - Security scans (E7)
  - Production safeguards (E8)
  - Axiom compliance checks (E9)
  - Purpose alignment checks (E10)
  - Transparency logging (E11)
- `practices.yaml` with daily, craft, and alignment practices:
  - Daily: Morning intention, evening reflection, focused standup
  - Craft: Code as craft review, thoughtful review, continuous refactoring
  - Alignment: Weekly learning, retrospectives, release blessing, quarterly alignment
- Extended agent and skill sets with custom capabilities
- Comprehensive knowledge files including domain-specific patterns
- Full template library with custom templates
- Advanced MCP integration

**Use When**: You need full governance, quality gates, and team practices from day one, or you're building enterprise or critical systems where consistency and safety are paramount.

### Choosing Your Depth

**Start with Quick Start if**:
- You're learning the system
- Building a prototype or proof of concept
- Working solo or in a small team
- Want to add structure incrementally

**Choose Standard if**:
- Building a production application
- Working with a team that needs coordination
- Want full agent capabilities
- Need methodology configuration
- Don't need enforcement gates yet

**Choose Comprehensive if**:
- Building enterprise or critical systems
- Need quality gates and safety checks
- Want team practices defined upfront
- Require full governance from day one
- Have compliance or regulatory requirements

You can always upgrade from Quick Start to Standard or Comprehensive later by regenerating with a deeper depth option.

---

## Related Documentation

- [LAYERED_ARCHITECTURE.md](../LAYERED_ARCHITECTURE.md) - Deep dive into the 5-layer architecture
- [FACTORY_REFERENCE.md](../FACTORY_REFERENCE.md) - Complete factory overview
- [BLUEPRINTS.md](BLUEPRINTS.md) - All available technology blueprints
- [USAGE_GUIDE.md](../USAGE_GUIDE.md) - Step-by-step usage instructions

---

*This document describes the generated output structure. For information on extending the factory or creating custom blueprints, see [EXTENSION_GUIDE.md](../EXTENSION_GUIDE.md).*
