---
name: skill-generation
description: Skill definition file generation skill
type: skill
knowledge: [best-practices.json]
templates: [patterns/skills/]
---

# Skill Generation Skill

Generates skill definition files from patterns for target projects.

## When to Use

- When generating skills for a new project
- When customizing skill behavior
- When creating new skill types

## Process

### Step 1: Load Skill Pattern
For each requested skill:
1. Load pattern from `patterns/skills/{skill-id}.json`
2. Parse metadata, frontmatter, and sections
3. Identify customization points

### Step 2: Apply Customizations
If customizations specified:
- Override frontmatter values
- Modify knowledge references
- Update MCP tool references

### Step 3: Render Markdown
Convert pattern to markdown format:

```markdown
---
name: {name}
description: {description}
type: skill
skills: [{skills}]
knowledge: [{knowledge}]
---

# {title}

{introduction}

## When to Use
{whenToUse}

## Process
{process steps}

## Fallback Procedures
{fallbacks}

## Important Rules
{rules}
```

### Step 4: Create Skill Directory
Create skill directory structure:

```
{TARGET}/.cursor/skills/{skill-name}/
├── SKILL.md           # Main skill definition
└── references/        # Optional reference docs
```

## Output Format

Skill markdown file with:
- YAML frontmatter with metadata
- Introduction
- When to Use section
- Process steps with actions
- Fallback Procedures
- Important Rules

## Fallback Procedures

- **If pattern not found**: Report error, skip skill
- **If customization fails**: Use default pattern values

## References

- `patterns/skills/*.json`
- `knowledge/best-practices.json`
