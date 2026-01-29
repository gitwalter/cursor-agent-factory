# Full-Stack Next.js App - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for a Next.js 14+ full-stack application with TypeScript and Prisma.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for a Next.js full-stack task management app
```

---

### Pre-Phase: Axiom Selection (Layer 0)

**Factory Prompt:**
> Every agent system needs foundational axioms. Core axioms (A1-A5) are always included.
> Would you like to add optional axioms?

**Your Response:**
```
No, use only core axioms
```

**Rationale:** For a straightforward full-stack app, core axioms provide sufficient grounding without additional complexity.

**Selected Axioms:**

| ID | Axiom | Application |
|----|-------|-------------|
| A1 | Verifiability | All code traceable to requirements |
| A2 | User Primacy | User experience prioritized |
| A3 | Transparency | Clear component structure |
| A4 | Non-Harm | Secure authentication |
| A5 | Consistency | Consistent patterns throughout |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To accelerate full-stack React development with type-safe patterns from database to UI
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
Full-stack developers building modern React applications (team of 2-4)
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Implement complete features from database to UI in under 2 hours with full type safety
```

---

### Phase 0.5: Depth Selection

**Factory Prompt:**
> How deep should we define the remaining layers?

**Your Response:**
```
B (Standard)
```

---

### Phases 0.6-0.7: Principles & Methodology (Layer 2-3)

**Factory Prompt:**
> What development methodology fits your team?

**Your Response:**
```
Kanban
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
> WIP limits?

**Your Response:**
```
3 items in progress per developer
```

The factory will configure:
- Pull-based workflow
- Continuous deployment
- WIP limits for flow optimization

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
taskflow-app
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
Task management application with projects, tasks, and team collaboration
```

---

### Phase 2: Technology Stack

**Factory Prompt:**
> What is your primary programming language?

**Your Response:**
```
TypeScript
```

---

**Factory Prompt:**
> What frameworks will you use?

**Your Response:**
```
Next.js 14, React, Prisma, NextAuth.js, Tailwind CSS
```

---

**Factory Prompt:**
> I found a matching blueprint: nextjs-fullstack. Would you like to use it?

**Your Response:**
```
Yes
```

---

**Factory Prompt:**
> What database will you use?

**Your Response:**
```
PostgreSQL with Prisma ORM
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
GitHub issues and pull requests
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What patterns should the agent follow?

**Your Response:**
```
React Server Components, Server Actions, App Router conventions
```

---

### Phase 5: Agent & Skill Selection

**Factory Prompt:**
> Which agents should I include?

**Your Response:**
```
Code reviewer, test generator, documentation agent
```

---

**Factory Prompt:**
> Which skills should be available?

**Your Response:**
```
feature-workflow, tdd
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\taskflow-app
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: taskflow-app                                          ║
║ Blueprint: nextjs-fullstack                                    ║
║ Depth: Standard                                                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: None                                               ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Accelerate full-stack React development             ║
║   Stakeholders: Full-stack developers (2-4)                    ║
║   Success: Feature implementation in < 2 hours                 ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Kanban                                          ║
║   WIP Limit: 3 per developer                                   ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: TypeScript, Next.js 14, Prisma, Tailwind              ║
║   Agents: code-reviewer, test-generator, documentation-agent   ║
║   Skills: feature-workflow, tdd                                ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\taskflow-app                               ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Generated Artifacts

```
taskflow-app/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── test-generator.md
│   │   └── documentation-agent.md
│   └── skills/
│       ├── feature-workflow/
│       │   └── SKILL.md
│       └── tdd/
│           └── SKILL.md
├── knowledge/
│   ├── nextjs-patterns.json      # Next.js 14 patterns
│   ├── prisma-patterns.json      # Prisma best practices
│   └── react-patterns.json       # React component patterns
├── src/
│   ├── app/                      # Next.js App Router
│   │   ├── (auth)/               # Auth route group
│   │   ├── (dashboard)/          # Dashboard route group
│   │   ├── api/                  # API routes
│   │   └── layout.tsx
│   ├── components/               # React components
│   ├── lib/                      # Utilities
│   └── server/                   # Server-side code
├── prisma/
│   └── schema.prisma             # Database schema
├── tests/
│   ├── unit/
│   └── e2e/
├── workflows/
│   └── methodology.yaml          # Kanban configuration
├── .cursorrules
├── PURPOSE.md
├── package.json
└── README.md
```

---

## Using the Generated System

### Feature Implementation

**Example: Add Task Feature**
```
Implement a feature to create new tasks with title, description, and due date
```

The agent will:
1. Create Prisma model if needed
2. Generate Server Action for creation
3. Build React component with form
4. Add Tailwind styling
5. Generate tests

### Type-Safe Development

The system enforces type safety:
- Prisma generates TypeScript types
- Server Actions are fully typed
- Components use typed props
- API responses are validated

---

## Key Patterns

### Server Action Pattern

```typescript
// src/server/actions/tasks.ts
"use server"

import { prisma } from "@/lib/prisma"
import { revalidatePath } from "next/cache"

export async function createTask(data: CreateTaskInput) {
  const task = await prisma.task.create({
    data: {
      title: data.title,
      description: data.description,
      dueDate: data.dueDate,
    },
  })
  
  revalidatePath("/tasks")
  return task
}
```

### React Server Component Pattern

```typescript
// src/app/(dashboard)/tasks/page.tsx
import { prisma } from "@/lib/prisma"
import { TaskList } from "@/components/tasks/TaskList"

export default async function TasksPage() {
  const tasks = await prisma.task.findMany({
    orderBy: { createdAt: "desc" },
  })

  return <TaskList tasks={tasks} />
}
```

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Should have core axioms only
2. `PURPOSE.md` - Should reflect full-stack mission
3. `knowledge/` - Should contain Next.js and Prisma patterns

---

## Next Steps

1. Initialize the Next.js project with the generated structure
2. Run Prisma migrations
3. Start building features using the agents
4. Use TDD skill for component development

**Congratulations!** You've generated a complete Cursor agent system for full-stack Next.js development.
