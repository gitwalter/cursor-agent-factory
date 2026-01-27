---
name: stack-configuration
description: Technology stack selection and configuration skill
type: skill
knowledge: [stack-capabilities.json]
---

# Stack Configuration Skill

Configures technology stack based on requirements and matches to available blueprints.

## When to Use

- When configuring a new project's technology stack
- When matching requirements to blueprints
- When customizing stack options

## Process

### Step 1: Parse Language Requirements
- Identify primary language
- Check for secondary languages
- Validate language is supported

### Step 2: Identify Frameworks
For each mentioned framework:
- Match to known frameworks in `stack-capabilities.json`
- Identify dependencies
- Check compatibility

### Step 3: Match Blueprint
Search blueprints for best match:

```python
for blueprint in blueprints:
    if blueprint.primaryLanguage == requirements.primaryLanguage:
        match_score = calculate_framework_match(blueprint, requirements)
        if match_score > threshold:
            return blueprint
```

### Step 4: Configure Tools
Based on stack, suggest:
- Test frameworks
- Linters
- Formatters
- Type checkers

### Step 5: Output Configuration
Generate stack configuration object:

```yaml
stack:
  primaryLanguage: "{LANGUAGE}"
  frameworks:
    - name: "{FRAMEWORK}"
      version: "{VERSION}"
  tools:
    testing: "{TEST_FRAMEWORK}"
    linting: "{LINTER}"
    formatting: "{FORMATTER}"
  blueprint: "{BLUEPRINT_ID}"
```

## Blueprint Matching Rules

| Primary Language | Key Framework | Blueprint |
|------------------|---------------|-----------|
| Python | FastAPI | `python-fastapi` |
| Python | Django | `python-django` |
| TypeScript | React | `typescript-react` |
| TypeScript | Next.js | `typescript-nextjs` |
| Java | Spring | `java-spring` |
| C# | .NET | `csharp-dotnet` |
| ABAP | (any) | `sap-abap` |

## Fallback Procedures

- **If language not supported**: Report and ask user for alternative
- **If no blueprint matches**: Create custom configuration from patterns
- **If frameworks conflict**: Report conflict and ask user to choose

## References

- `knowledge/stack-capabilities.json`
- `blueprints/*/blueprint.json`
