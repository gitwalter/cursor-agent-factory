# Cursor Agent Factory - Architecture Diagrams

This folder contains Mermaid diagrams documenting the Cursor Agent Factory architecture and workflows.

## Viewing Diagrams

All diagrams use [Mermaid](https://mermaid.js.org/) syntax and render automatically in:
- GitHub/GitLab markdown preview
- VS Code with Mermaid extension
- Cursor IDE with markdown preview
- Any Mermaid-compatible viewer

## Diagram Index

| File | Description |
|------|-------------|
| [factory-workflow.md](factory-workflow.md) | Factory generation workflow, 5-phase requirements gathering, CLI vs Chat modes |
| [verification-flow.md](verification-flow.md) | Strawberry verification, hallucination detection, grounding + verification pipeline |
| [agent-skill-architecture.md](agent-skill-architecture.md) | Agent/skill hierarchy, pattern library, skill composition model |
| [sap-grounding-architecture.md](sap-grounding-architecture.md) | 5-layer SAP grounding, specialized skills, MCP integration |

## Quick Reference

### Factory Workflow

```mermaid
flowchart LR
    A["User Request"] --> B["Requirements"] --> C["Blueprint"] --> D["Generation"] --> E["Project"]
```

### Verification Flow

```mermaid
flowchart LR
    E["Evidence"] --> S["Scrubbed Test"] --> F["Full Test"] --> R["Result"]
```

### Agent/Skill Model

```mermaid
flowchart LR
    A["Agent"] -->|"uses"| S["Skill"] -->|"queries"| K["Knowledge"]
```

### Grounding Layers

```mermaid
flowchart LR
    L1["Cache"] --> L2["Docs"] --> L3["Repos"] --> L4["Specs"] --> L5["Verify"]
```

## Updating Diagrams

When updating diagrams:
1. Edit the `.md` file directly
2. Use Mermaid syntax (validated at [mermaid.live](https://mermaid.live))
3. Keep diagrams focused and readable
4. Update cross-references in documentation

## Embedding in Documentation

To embed these diagrams in other documentation, you can:

1. **Link to the diagram file:**
   ```markdown
   See [Factory Workflow](diagrams/factory-workflow.md)
   ```

2. **Copy specific diagrams inline:**
   Copy the mermaid code block directly into your markdown file.

3. **Reference with relative paths:**
   ```markdown
   [../diagrams/verification-flow.md](../diagrams/verification-flow.md)
   ```
