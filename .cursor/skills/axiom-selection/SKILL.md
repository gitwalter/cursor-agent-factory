# Axiom Selection Skill

## Overview

This skill handles the **Pre-Phase (Layer 0)** of the onboarding process, where users configure the foundational axioms that will govern their agent system.

## Purpose

Guide users through selecting the core and optional axioms that form the logical foundation of their generated agent system. All derived principles, methodologies, and behaviors will trace back to these axioms.

## Trigger

- Start of new project generation
- User mentions "axioms", "foundation", or "layer 0"
- Explicit request to configure foundational rules

## Process

### Step 1: Explain Layer 0

Present the concept of foundational axioms:

```
Every agent system needs foundational axioms - self-evident truths that cannot be violated.

Core Axioms (A1-A5) are always included:
- A1: Verifiability - All outputs must be verifiable against source
- A2: User Primacy - User intent takes precedence
- A3: Transparency - Reasoning must be explainable
- A4: Non-Harm - No action may cause harm
- A5: Consistency - No rule may contradict axioms

These ensure your agents are trustworthy, user-focused, and safe.
```

### Step 2: Offer Optional Axioms

Present optional axioms based on project type:

```
Optional axioms customize your agent's values. Select any that apply:

[ ] A6: Minimalism - Prefer simple solutions over complex ones
    → Good for: Maintenance-focused, MVP, startup projects

[ ] A7: Reversibility - Prefer reversible actions over irreversible
    → Good for: Safety-critical, data-sensitive projects

[ ] A8: Privacy - Minimize data exposure and collection
    → Good for: GDPR compliance, healthcare, finance

[ ] A9: Performance - Optimize for speed when correctness is ensured
    → Good for: High-throughput, latency-sensitive applications

[ ] A10: Learning - Every failure is an opportunity to improve
    → Good for: AI/ML, R&D, continuous improvement culture
```

### Step 3: Handle Conflicts

If user selects conflicting axioms, explain:

```
Note: A6 (Minimalism) and A9 (Performance) can sometimes conflict.

When both are selected, we apply this resolution:
- Default to A6 (simple solutions)
- Apply A9 only when profiling identifies a bottleneck

Is this acceptable, or would you prefer to choose only one?
```

### Step 4: Confirm and Store

Confirm selections and store in project configuration:

```yaml
layer0_configuration:
  core_axioms: ["A1", "A2", "A3", "A4", "A5"]  # Always included
  optional_axioms: ["A6", "A7"]  # User selected
  conflict_resolutions:
    - "A6_A9: Apply A6 by default, A9 only when profiling indicates"
```

## Outputs

1. **Axiom Configuration** - Stored in project requirements
2. **Layer 0 Section** - Generated for `.cursorrules`
3. **Axiom Alignment Notes** - For `PURPOSE.md`

## Layer 0 Template Output

Generate this section for the `.cursorrules` file:

```markdown
## Layer 0: Integrity & Logic

### Core Axioms (Immutable)

These axioms govern all agent behavior and cannot be overridden:

1. **A1 - Verifiability**: All agent outputs must be verifiable against source.
2. **A2 - User Primacy**: User intent takes precedence over agent convenience.
3. **A3 - Transparency**: Agent reasoning must be explainable on request.
4. **A4 - Non-Harm**: No action may knowingly cause harm to users or systems.
5. **A5 - Consistency**: No rule may contradict these axioms.

### Selected Optional Axioms

{FOR EACH SELECTED OPTIONAL AXIOM}
6. **{AXIOM_ID} - {AXIOM_NAME}**: {AXIOM_STATEMENT}
{END FOR}

### Derivation Rules

When making decisions, derive conclusions from axioms:

- **D1**: If output is code AND A1 applies → Require evidence of testing
- **D2**: If conflict exists AND A2 applies → Defer to user preference
- **D3**: If action is destructive AND A4 applies → Require explicit confirmation
- **D4**: If error occurs AND A3 applies → Provide clear explanation

### Validation Constraints

- Every rule must trace to at least one axiom
- No rule may contradict any axiom
- When rules conflict, higher-layer rules take precedence (L0 > L1 > L2 > L3 > L4)
- If action would violate an axiom, halt and request human guidance
```

## Integration Points

- **Input from**: User during onboarding
- **Reads**: `patterns/axioms/core-axioms.json`, `patterns/axioms/optional-axioms.json`
- **Outputs to**: Project configuration, `.cursorrules` template
- **Next skill**: `purpose-definition`

## Best Practices

1. Always include all 5 core axioms
2. Recommend axiom combinations based on project type
3. Explain conflicts clearly before confirming
4. Keep explanations concise but complete
5. Store rationale for axiom selections
