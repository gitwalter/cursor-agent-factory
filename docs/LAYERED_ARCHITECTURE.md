# Layered Architecture Guide

The Cursor Agent Factory implements a **5-layer deductive-inductive architecture** that generates agent systems grounded in clear values, purpose, and methodology.

## Philosophy

This architecture ensures that generated agent systems are not just technically capable, but also:
- **Grounded** in foundational axioms
- **Purposeful** with clear mission and success criteria
- **Principled** with quality standards and ethical boundaries
- **Coordinated** through chosen methodology
- **Excellent** through enforcement and practices

---

## The 5 Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 0: INTEGRITY & LOGIC                   │
│  Axioms (immutable) │ Derivation Rules │ Validation Constraints │
│  Foundation: Everything else derives from here                  │
└─────────────────────────────────┼───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 1: PURPOSE                             │
│  Mission Statement │ Stakeholders │ Success Criteria            │
│  Artifact: PURPOSE.md                                           │
└─────────────────────────────────┼───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 2: PRINCIPLES                          │
│  Ethical Boundaries │ Quality Standards │ Failure Handling      │
│  Artifact: .cursorrules principles section                      │
└─────────────────────────────────┼───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 3: METHODOLOGY                         │
│  Agile/Kanban/R&D/Enterprise │ Coordination │ Ceremonies        │
│  Artifacts: workflows/methodology.yaml, enforcement.yaml        │
└─────────────────────────────────┼───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 4: TECHNICAL                           │
│  Stack │ Agents │ Skills │ Code Standards │ Templates           │
│  Artifacts: .cursor/, knowledge/, templates/                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Layer 0: Integrity & Logic

The meta-foundation providing axioms and reasoning rules.

### Core Axioms (Always Included)

| ID | Name | Statement |
|----|------|-----------|
| A1 | Verifiability | All agent outputs must be verifiable against source |
| A2 | User Primacy | User intent takes precedence over agent convenience |
| A3 | Transparency | Agent reasoning must be explainable on request |
| A4 | Non-Harm | No action may knowingly cause harm to users or systems |
| A5 | Consistency | No rule may contradict these axioms |

### Optional Axioms (User-Selected)

| ID | Name | Use When |
|----|------|----------|
| A6 | Minimalism | Maintenance and understandability are priorities |
| A7 | Reversibility | Safety and recoverability are paramount |
| A8 | Privacy | Handling sensitive user data |
| A9 | Performance | Performance-critical applications |
| A10 | Learning | AI/ML, R&D, continuous improvement culture |

### Derivation Rules

Rules for deducing valid conclusions:

- **D1**: If A1 (Verifiability) AND output is code → require evidence of testing
- **D2**: If A2 (User Primacy) AND conflict exists → defer to user preference
- **D3**: If A4 (Non-Harm) AND action is destructive → require explicit confirmation
- **D4**: If error occurs AND A3 (Transparency) → provide clear explanation
- **D5**: If new rule proposed AND A5 (Consistency) → validate against all axioms

### Validation Constraints

- All derived rules must trace to at least one axiom
- No rule may contradict any axiom
- When rules conflict: L0 > L1 > L2 > L3 > L4
- If action would violate an axiom, halt and request human guidance

---

## Layer 1: Purpose

Defines WHY the system exists.

### Components

| Component | Question | Validation |
|-----------|----------|------------|
| Mission Statement | Why should this system exist? | Must be verifiable (A1) |
| Stakeholders | Who are the primary users? | Must be specific humans (A2) |
| Success Criteria | What defines success? | Must be measurable (A1) |

### Generated Artifact: PURPOSE.md

```markdown
# {PROJECT_NAME} - Purpose & Mission

## Mission Statement
{one_sentence_purpose}

## Who We Serve
**Primary Stakeholders**: {primary_stakeholders}

## Success Definition
**Primary Outcome**: {success_criteria}
**How We Measure**: {measurement_approach}
```

---

## Layer 2: Principles

Defines WHAT standards must be met.

### Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| Ethical Boundaries | What agents must NEVER do | No silent failures, no unverified claims |
| Quality Standards | What quality bar must be met | Test coverage, documentation, code review |
| Failure Handling | How to respond to errors | Graceful degradation, clear communication |

### Ethical Boundaries (EB)

| ID | Name | Axiom Basis |
|----|------|-------------|
| EB1 | No Silent Failures | A3 (Transparency) |
| EB2 | No Destructive Without Confirmation | A4 (Non-Harm) |
| EB3 | No Ignoring User Preferences | A2 (User Primacy) |
| EB4 | No Unverified Claims | A1 (Verifiability) |
| EB5 | No Axiom Violations | A5 (Consistency) |

### Quality Standards (QS)

| ID | Name | Axiom Basis |
|----|------|-------------|
| QS1 | Test Coverage Required | A1 (Verifiability) |
| QS2 | Documentation Required | A3 (Transparency) |
| QS3 | Comprehensive Error Handling | A3, A4 |
| QS4 | Peer Review Required | A1, A3 |
| QS5 | Consistent Code Style | A5 (Consistency) |

---

## Layer 3: Methodology

Defines HOW work is organized.

### Available Methodologies

| Methodology | Pattern | Best For |
|-------------|---------|----------|
| Agile Scrum | domain_expert_swarm + peer_collaboration | Product development |
| Kanban | continuous_flow + pull_based | Support, maintenance |
| R&D | knowledge_mesh + adaptive_learning | AI/ML, research |
| Enterprise | hierarchical_command + pipeline | Large-scale, compliance |

### Enforcement Patterns

Ensure values are lived, not just stated:

| Category | Examples |
|----------|----------|
| Quality | Test coverage gate, peer review gate |
| Safety | Destructive confirmation, backup before change |
| Integrity | Axiom compliance, purpose alignment |

### Practice Patterns

Regular disciplines maintaining excellence:

| Category | Examples |
|----------|----------|
| Daily | Morning intention, focused standup |
| Craft | Code as craft review, thoughtful review |
| Alignment | Retrospective, release blessing, quarterly alignment |

---

## Layer 4: Technical

Defines WITH WHAT tools and patterns.

### Components

- **Stack**: Languages, frameworks, databases
- **Agents**: AI agent definitions
- **Skills**: Reusable skill patterns
- **Knowledge**: Domain-specific reference data
- **Templates**: Code and document templates

---

## Deductive-Inductive System

### Deductive (Top-Down)

From axioms to specific rules:

```
Layer 0 Axiom: "User safety is paramount" (A4)
    ↓ derives
Layer 2 Principle: "Never execute untested code in production" (QS1)
    ↓ derives  
Layer 3 Enforcement: "All code requires review before merge" (E2)
    ↓ derives
Layer 4 Technical: "PR approval required, CI must pass"
```

### Inductive (Bottom-Up)

Learning from experience via the Pattern Feedback Skill:

```
Layer 4 Observation: "JSON parsing errors occur frequently with API X"
    ↓ generalizes (via pattern-feedback skill)
Proposed Pattern: "API X responses should always be validated"
    ↓ reviewed against axioms
Layer 2 Principle Update: "External API responses require schema validation"
```

---

## Onboarding Flow

### Depth Options

| Option | Phases | Best For |
|--------|--------|----------|
| Quick Start | Pre-Phase, Phase 0, Phases 1-5 | Rapid prototyping |
| Standard | All pre-phases + Phases 1-5 | Most projects |
| Comprehensive | All phases including enforcement/practices | Enterprise, critical systems |

### Phase Sequence

1. **Pre-Phase**: Layer 0 axiom configuration
2. **Phase 0**: Layer 1 purpose definition
3. **Phase 0.5**: Depth selection
4. **Phase 0.6**: Layer 2 principles (Standard+)
5. **Phase 0.7**: Layer 3 methodology (Standard+)
6. **Phase 0.8**: Enforcement selection (Comprehensive)
7. **Phase 0.9**: Practice selection (Comprehensive)
8. **Phases 1-5**: Layer 4 technical configuration

---

## Generated Project Structure

```
{PROJECT}/
├── .cursorrules              # 5-layer agent rules (L0-L4)
├── PURPOSE.md                # Mission, stakeholders, success (L1)
├── enforcement.yaml          # Enforcement configuration (L2+)
├── practices.yaml            # Team practices (L3+)
├── workflows/
│   └── methodology.yaml      # Methodology configuration (L3)
├── .cursor/
│   ├── agents/               # Agent definitions (L4)
│   └── skills/               # Skill definitions (L4)
├── knowledge/                # Domain knowledge (L4)
├── templates/                # Code templates (L4)
├── src/                      # Source code
├── tests/                    # Test files
└── README.md                 # Project documentation
```

---

## Key Principles

### 1. Axiom Traceability

Every rule must trace to at least one axiom:

```
Rule: "All API responses must be validated"
Traces to: A1 (Verifiability) - ensures outputs are verifiable
```

### 2. Clear Separation

Philosophy guides but never mixes with technical implementation:

- **Philosophical Layer**: PURPOSE.md, .cursorrules L0-L2
- **Technical Layer**: Code, APIs, agents, skills

### 3. Professional Language

Deeper values expressed professionally:

| Value | Expression |
|-------|------------|
| Devotion | Commitment to Excellence |
| Service | User-Focused Delivery |
| Wisdom | Continuous Improvement |
| Harmony | System Coherence |

### 4. Continuous Improvement

The Pattern Feedback Skill enables learning:

1. Observe patterns from experience
2. Generalize into proposed rules
3. Validate against axioms
4. Integrate into appropriate layer

---

## References

### Internal Documentation

- `docs/LAYERED_ONBOARDING_CONCEPT.md` - Full implementation blueprint
- `patterns/axioms/` - Axiom definitions
- `patterns/principles/` - Principle patterns
- `patterns/methodologies/` - Methodology templates
- `patterns/enforcement/` - Enforcement patterns
- `patterns/practices/` - Practice patterns
- `knowledge/augmented-coding-patterns.json` - AI collaboration patterns

### External Sources & Inspirations

| Source | Contribution |
|--------|--------------|
| [Augmented Coding Patterns](https://lexler.github.io/augmented-coding-patterns/) | Active Partner, Check Alignment, Chain of Small Steps patterns for effective AI collaboration |
| [Leon Chlon](https://github.com/lchlon) | Strawberry Verification - information-theoretic hallucination detection |
| [ai-dev-agent](https://github.com/gitwalter/ai-dev-agent) | Layered architecture and methodology integration concepts |
