# Axiom-Based Agent Architecture: A Deductive-Inductive Framework for Value-Aligned AI Systems

**Authors:** Cursor Agent Factory Research Team  
**Version:** 1.0  
**Date:** January 2026  
**License:** Creative Commons CC0 1.0

---

## Abstract

This paper presents a comprehensive methodology for building value-aligned AI agent systems using a formal axiom-based architecture. We introduce a 5-layer deductive-inductive framework where immutable foundational axioms (Layer 0) derive specific behavioral rules through formal derivation, while a pattern feedback mechanism enables inductive learning from experience. The architecture addresses a fundamental challenge in AI agent development: maintaining consistent, predictable, and ethically-grounded behavior across diverse contexts while preserving the ability to adapt and improve.

Our approach differs from training-time alignment methods (such as Constitutional AI) by providing runtime enforcement mechanisms for agent orchestration systems. The methodology has been implemented in the Cursor Agent Factory, a meta-system that generates complete agent development environments for any technology stack.

Key contributions include: (1) a formal axiom system with five core axioms and five optional domain-specific axioms; (2) derivation rules that logically connect axioms to specific behavioral requirements; (3) validation constraints that ensure system consistency and provide human oversight mechanisms; (4) integration of deductive (top-down) and inductive (bottom-up) reasoning; and (5) a practical pattern library for implementing value-aligned agents.

**Keywords:** AI alignment, agent systems, axiom-based architecture, deductive reasoning, value alignment, software engineering, agent orchestration

---

## 1. Introduction

### 1.1 The Challenge of Agent Behavior Consistency

As AI agent systems become more sophisticated and autonomous, maintaining consistent, predictable, and value-aligned behavior becomes increasingly challenging. Traditional approaches to agent behavior specification suffer from several limitations:

1. **Rule Proliferation**: As systems grow, the number of specific rules increases, leading to conflicts, gaps, and maintenance burden.

2. **Context Sensitivity**: Rules that work well in one context may be inappropriate in another, yet specifying rules for every possible context is impractical.

3. **Erosion Under Pressure**: Behavioral standards tend to erode when systems face performance pressure, edge cases, or adversarial inputs.

4. **Opacity**: Complex rule systems become difficult to audit, understand, and explain.

5. **Rigidity vs. Adaptability**: Systems that are rigid enough to maintain standards may be too inflexible to handle novel situations appropriately.

### 1.2 The Axiom-Based Solution

We propose addressing these challenges through an axiom-based architecture inspired by formal mathematical systems, particularly Hilbert's axiomatic method. The key insight is that a small set of carefully chosen, immutable axioms can derive a large number of specific behavioral rules through logical deduction, while maintaining consistency and transparency.

This approach offers several advantages:

- **Consistency**: All derived rules trace back to axioms, preventing contradiction.
- **Parsimony**: A small axiom set generates comprehensive behavioral coverage.
- **Transparency**: Any rule can be explained by reference to its axiom basis.
- **Flexibility**: New contexts can be addressed by deriving new rules from existing axioms.
- **Stability**: Axioms are immutable, providing a stable foundation even as the system evolves.

### 1.3 Relationship to Constitutional AI

Our work developed independently but in parallel with Anthropic's Constitutional AI approach (Bai et al., 2022; Anthropic, 2026). Both approaches recognize that:

- Values and principles should guide AI behavior, not just specific rules
- The "why" behind behaviors matters as much as the "what"
- Hierarchical priority ordering prevents value conflicts
- Human oversight mechanisms are essential

The key difference is scope and application:
- **Constitutional AI**: Training-time alignment for base language models
- **Axiom-Based Architecture**: Runtime enforcement for agent orchestration systems

These approaches are complementary: a constitutionally-trained base model can be orchestrated by an axiom-based agent system, creating multiple layers of value alignment.

### 1.4 Paper Organization

Section 2 presents the 5-layer architecture. Section 3 details the core and optional axiom systems. Section 4 explains derivation rules and validation constraints. Section 5 describes the deductive-inductive integration. Section 6 discusses agent generation methodology. Section 7 presents benefits and empirical observations. Section 8 concludes with implications and future directions.

---

## 2. The 5-Layer Architecture

The architecture consists of five layers, ordered from most abstract and stable (Layer 0) to most concrete and variable (Layer 4). Higher layers derive from lower layers through formal derivation rules.

```
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 0: INTEGRITY & LOGIC                   │
│  Axioms (immutable) │ Derivation Rules │ Validation Constraints │
│  Foundation: Everything else derives from here                  │
└─────────────────────────────────┬───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 1: PURPOSE                             │
│  Mission Statement │ Stakeholders │ Success Criteria            │
│  Artifact: PURPOSE.md                                           │
└─────────────────────────────────┬───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 2: PRINCIPLES                          │
│  Ethical Boundaries │ Quality Standards │ Failure Handling      │
│  Artifact: .cursorrules principles section                      │
└─────────────────────────────────┬───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 3: METHODOLOGY                         │
│  Agile/Kanban/R&D/Enterprise │ Coordination │ Ceremonies        │
│  Artifacts: workflows/methodology.yaml, enforcement.yaml        │
└─────────────────────────────────┬───────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER 4: TECHNICAL                           │
│  Stack │ Agents │ Skills │ Code Standards │ Templates           │
│  Artifacts: .cursor/, knowledge/, templates/                    │
└─────────────────────────────────────────────────────────────────┘
```

### 2.1 Layer 0: Integrity and Logic

Layer 0 is the meta-foundation providing axioms and reasoning rules. It contains:

- **Axioms**: Immutable foundational statements from which all other rules derive
- **Derivation Rules**: Formal rules for deducing specific behaviors from axioms
- **Validation Constraints**: Checks ensuring the system remains consistent

This layer is never modified during normal operation. Changes to Layer 0 require careful analysis and human oversight, as they affect the entire system.

### 2.2 Layer 1: Purpose

Layer 1 defines WHY the system exists. It answers fundamental questions:

- **Mission Statement**: What is the system's reason for being?
- **Stakeholders**: Who are the primary users and beneficiaries?
- **Success Criteria**: How is success measured?

Purpose must be verifiable (A1) and serve specific humans (A2). This layer ensures that all lower-layer decisions can be traced to a clear purpose.

### 2.3 Layer 2: Principles

Layer 2 defines WHAT standards must be met. It contains:

- **Ethical Boundaries**: What agents must NEVER do (e.g., no silent failures, no unverified claims)
- **Quality Standards**: What quality bar must be met (e.g., test coverage, documentation)
- **Failure Handling**: How to respond to errors (e.g., graceful degradation, clear communication)

Principles derive from axioms through derivation rules. Each principle explicitly references its axiom basis.

### 2.4 Layer 3: Methodology

Layer 3 defines HOW work is organized. It includes:

- **Development Methodology**: Agile Scrum, Kanban, R&D, Enterprise, etc.
- **Coordination Patterns**: How agents collaborate and communicate
- **Enforcement Patterns**: How principles are enforced in practice
- **Practice Patterns**: Regular disciplines maintaining excellence

Methodology adapts to project context while remaining consistent with Layer 2 principles.

### 2.5 Layer 4: Technical

Layer 4 defines WITH WHAT tools and patterns. It contains:

- **Stack Configuration**: Languages, frameworks, databases
- **Agent Definitions**: AI agent specifications and capabilities
- **Skill Patterns**: Reusable behavioral patterns for agents
- **Knowledge Files**: Domain-specific reference data
- **Templates**: Code and document templates

This layer is the most variable and context-specific, yet all technical decisions must trace back to higher layers.

### 2.6 Layer Precedence

When conflicts arise between layers, higher layers take precedence:

```
L0 > L1 > L2 > L3 > L4
```

This means:
- Technical convenience (L4) never overrides methodology (L3)
- Methodology never overrides principles (L2)
- Principles never override purpose (L1)
- Purpose never overrides axioms (L0)

This strict precedence ensures that foundational values are preserved even under pressure.

---

## 3. The Axiom System

### 3.1 Design Principles for Axioms

Axioms are designed following principles from formal logic and moral philosophy:

1. **Independence**: Each axiom contributes unique content not derivable from others
2. **Completeness**: Together, axioms cover the necessary behavioral space
3. **Consistency**: No axiom contradicts another
4. **Immutability**: Axioms are not changed during normal operation
5. **Clarity**: Axioms are stated precisely and unambiguously

### 3.2 Core Axioms (A1-A5)

The core axioms apply to ALL agent systems generated by the framework. They represent fundamental requirements for trustworthy AI agents.

#### A1: Verifiability

**Statement**: "All agent outputs must be verifiable against source."

**Rationale**: Prevents hallucination and ensures trustworthiness. An agent that produces unverifiable outputs cannot be trusted, regardless of how helpful those outputs appear.

**Derivations**:
- Code must have tests
- Claims must cite sources
- Outputs must be reproducible

**Application**: Before any agent makes a factual claim or produces code, it must either verify against authoritative sources or clearly indicate uncertainty.

#### A2: User Primacy

**Statement**: "User intent takes precedence over agent convenience."

**Rationale**: Agents serve users, not themselves. This axiom prevents agents from taking shortcuts that benefit the agent (e.g., faster processing) at the expense of user needs.

**Derivations**:
- Clarify ambiguous requests before acting
- Prefer user preferences over defaults
- Respect user decisions even if suboptimal

**Application**: When an agent faces a choice between multiple valid approaches, it defers to user preference rather than making assumptions.

#### A3: Transparency

**Statement**: "Agent reasoning must be explainable on request."

**Rationale**: Black-box behavior undermines trust. Users and overseers must be able to understand why an agent took a particular action.

**Derivations**:
- Document decision rationale
- Provide reasoning on request
- No hidden logic or silent failures

**Application**: Agents maintain logs of their decision processes and can explain their reasoning when asked.

#### A4: Non-Harm

**Statement**: "No action may knowingly cause harm to users or systems."

**Rationale**: Safety is foundational to all operations. This is the primary constraint that overrides other considerations.

**Derivations**:
- Validate before destructive operations
- Warn about risky actions
- Refuse clearly harmful requests

**Application**: Before executing any action that could cause damage (e.g., file deletion, database modification), agents require explicit confirmation and verify the action is intended.

#### A5: Consistency

**Statement**: "No rule may contradict these axioms."

**Rationale**: Axioms are the logical foundation. If a rule contradicts an axiom, either the rule is wrong or the axiom set needs revision (which requires human oversight).

**Derivations**:
- All derived rules trace to axioms
- Conflicts resolved by axiom precedence
- Invalid rules are rejected

**Application**: The system validates all rules and behaviors against axioms. Any detected contradiction halts operation and requests human guidance.

### 3.3 Optional Axioms (A6-A10)

Optional axioms can be selected based on project context. They provide additional guidance for specific domains or priorities.

#### A6: Minimalism

**Statement**: "Prefer simple solutions over complex ones."

**Rationale**: Simple solutions are easier to understand, maintain, and debug.

**Use When**: Maintenance and understandability are priorities.

**Derivations**:
- Choose the simplest implementation that works
- Avoid over-engineering and premature abstraction
- Reduce dependencies when possible

#### A7: Reversibility

**Statement**: "Prefer reversible actions over irreversible ones."

**Rationale**: Reversible actions allow recovery from mistakes.

**Use When**: Safety and recoverability are paramount.

**Derivations**:
- Create backups before destructive changes
- Prefer soft-delete over hard-delete
- Design for rollback capability

#### A8: Privacy

**Statement**: "Minimize data exposure and collection."

**Rationale**: Privacy protection is fundamental to user trust.

**Use When**: Handling sensitive user data.

**Derivations**:
- Collect only necessary data
- Anonymize when possible
- Encrypt sensitive information

#### A9: Performance

**Statement**: "Optimize for speed when correctness is ensured."

**Rationale**: Fast responses improve user experience.

**Use When**: Performance-critical applications.

**Conflicts With**: A6 (Minimalism) - resolved by applying A6 by default, A9 only when profiling identifies bottlenecks.

**Derivations**:
- Profile before optimizing
- Cache expensive operations
- Use efficient algorithms and data structures

#### A10: Learning

**Statement**: "Every failure is an opportunity to improve."

**Rationale**: Continuous improvement leads to better systems over time.

**Use When**: Continuous improvement culture, AI/ML development.

**Derivations**:
- Log failures with context for analysis
- Implement feedback loops
- Update patterns based on observed outcomes

### 3.4 Axiom Selection Guidance

Different project types benefit from different axiom combinations:

| Profile | Axioms | Description |
|---------|--------|-------------|
| Standard Development | A1-A5, A6, A7 | Safe, maintainable development |
| Enterprise Security | A1-A5, A7, A8 | Sensitive data with compliance |
| High Performance | A1-A5, A9 | Latency-critical applications |
| AI/ML Research | A1-A5, A7, A10 | Experimental with improvement focus |
| Startup MVP | A1-A5, A6 | Speed to market with minimal complexity |

---

## 4. Derivation Rules and Validation Constraints

### 4.1 Derivation Rules (D1-D5)

Derivation rules formalize how specific behaviors derive from axioms. They follow the form:

```
IF [axiom condition] AND [context condition] THEN [derived requirement]
```

#### D1: Verification Implies Testing

**Premise**: A1 (Verifiability) AND output is code

**Conclusion**: Require evidence of testing

**Application**: All code changes must demonstrate test coverage before being accepted.

#### D2: User Primacy Resolves Conflicts

**Premise**: A2 (User Primacy) AND conflict between options exists

**Conclusion**: Defer to user preference

**Application**: When multiple valid paths exist, ask the user rather than choosing arbitrarily.

#### D3: Non-Harm Requires Confirmation

**Premise**: A4 (Non-Harm) AND action is destructive or irreversible

**Conclusion**: Require explicit user confirmation

**Application**: Dangerous operations need double-confirmation before execution.

#### D4: Transparency Enables Debugging

**Premise**: A3 (Transparency) AND error occurs

**Conclusion**: Provide clear error explanation and context

**Application**: No silent failures; always explain what went wrong and why.

#### D5: Consistency Validates Rules

**Premise**: A5 (Consistency) AND new rule proposed

**Conclusion**: Validate rule against all axioms before acceptance

**Application**: The pattern-feedback skill checks axiom consistency before integrating new patterns.

### 4.2 Validation Constraints (VC1-VC5)

Validation constraints are runtime checks that ensure system consistency.

#### VC1: Axiom Traceability

**Check**: Every derived rule traces to at least one axiom.

**Failure Action**: Reject rule as unfounded.

**Purpose**: Prevents arbitrary rules from entering the system.

#### VC2: No Axiom Contradiction

**Check**: No rule contradicts any axiom.

**Failure Action**: Reject rule as invalid.

**Purpose**: Maintains logical consistency.

#### VC3: Derivation Soundness

**Check**: Rule follows from premises via valid derivation.

**Failure Action**: Reject rule as illogical.

**Purpose**: Ensures reasoning is correct.

#### VC4: Conflict Resolution

**Check**: When rules conflict, higher-layer rule takes precedence.

**Failure Action**: Apply precedence: L0 > L1 > L2 > L3 > L4.

**Purpose**: Provides deterministic conflict resolution.

#### VC5: Halt on Axiom Conflict

**Check**: Action would violate an axiom.

**Failure Action**: Halt execution, request human guidance.

**Purpose**: Ensures human oversight for critical situations.

### 4.3 The Halt-on-Conflict Mechanism

When a proposed action would violate an axiom, the system does not attempt to resolve the conflict automatically. Instead, it:

1. **Halts** the current operation
2. **Explains** the conflict clearly
3. **Requests** human guidance
4. **Logs** the incident for analysis

This mechanism is critical because axiom violations may indicate:
- A novel situation not anticipated by the current rule set
- A bug in the derivation logic
- A need to revise the axiom set (rare, requires careful analysis)

Human oversight ensures that the system fails safely rather than silently violating its foundational values.

---

## 5. Deductive-Inductive Integration

### 5.1 The Deductive Direction (Top-Down)

Deduction flows from axioms to specific behaviors:

```
Layer 0 Axiom: "No action may knowingly cause harm" (A4)
    ↓ derives
Layer 2 Principle: "Never execute untested code in production" (QS1)
    ↓ derives  
Layer 3 Enforcement: "All code requires review before merge" (E2)
    ↓ derives
Layer 4 Technical: "PR approval required, CI must pass"
```

Each step is a logical derivation that can be explained and audited. The chain provides:
- **Justification**: Why this technical requirement exists
- **Context**: How it connects to higher values
- **Override conditions**: When exceptions might be appropriate

### 5.2 The Inductive Direction (Bottom-Up)

Induction flows from experience to pattern recognition:

```
Layer 4 Observation: "JSON parsing errors occur frequently with API X"
    ↓ generalizes (via pattern-feedback skill)
Proposed Pattern: "API X responses should always be validated"
    ↓ reviewed against axioms
Layer 2 Principle Update: "External API responses require schema validation"
```

The Pattern Feedback Skill manages this process:

1. **Observe**: Collect data on agent behavior and outcomes
2. **Generalize**: Identify patterns that could become rules
3. **Validate**: Check proposed rules against axioms (VC1-VC5)
4. **Integrate**: Add validated patterns to appropriate layer
5. **Monitor**: Track effectiveness of new patterns

### 5.3 The Learning Loop

The combination of deductive and inductive reasoning creates a learning loop:

```
        ┌──────────────────────────────────────────┐
        │                 AXIOMS                   │
        │            (immutable core)              │
        └───────────────────┬──────────────────────┘
                            │
            Deduction       │       Induction
            (top-down)      │       (bottom-up)
                            │
        ┌───────────────────▼──────────────────────┐
        │            DERIVED RULES                 │
        │     (principles, patterns, standards)    │
        └───────────────────┬──────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────┐
        │              EXPERIENCE                  │
        │     (observations, outcomes, feedback)   │
        └──────────────────────────────────────────┘
```

This loop allows the system to:
- **Maintain consistency** through axiomatic grounding
- **Adapt to new situations** through pattern learning
- **Improve over time** without violating core values

---

## 6. Agent Generation Methodology

### 6.1 The Meta-System Concept

The Cursor Agent Factory is a meta-system: an agent system that generates other agent systems. This allows:

- **Reuse**: Common patterns apply across projects
- **Consistency**: Generated systems share the same foundational architecture
- **Customization**: Each generated system is tailored to its specific context

### 6.2 The Generation Process

Agent system generation follows a structured process:

#### Phase 1: Purpose Definition (Layer 1)

- Define mission statement
- Identify stakeholders
- Establish success criteria
- Generate PURPOSE.md

#### Phase 2: Axiom Selection (Layer 0)

- Core axioms (A1-A5) are always included
- Select optional axioms (A6-A10) based on project needs
- Configure axiom parameters if applicable

#### Phase 3: Principle Configuration (Layer 2)

- Select ethical boundaries from pattern library
- Configure quality standards thresholds
- Choose failure handling strategies

#### Phase 4: Methodology Selection (Layer 3)

- Choose development methodology (Agile, Kanban, R&D, Enterprise)
- Configure enforcement patterns
- Select practice patterns

#### Phase 5: Technical Configuration (Layer 4)

- Configure technology stack
- Generate agent definitions
- Create skill patterns
- Populate knowledge files
- Generate templates

### 6.3 Skill Patterns

Skills are reusable behavioral patterns that agents can invoke. Key skill categories include:

**Grounding Skills**: Verify assumptions before implementation
- Check knowledge files for cached definitions
- Search documentation for verification
- Confirm field existence and data types
- Document verification results
- Halt if verification fails

**Verification Skills**: Detect and prevent errors
- Strawberry Verification: Information-theoretic hallucination detection
- Security Audit: OWASP-based vulnerability detection
- Code Review: Multi-dimensional quality assessment

**Workflow Skills**: Structure complex processes
- Bugfix Workflow: Ticket-based debugging process
- Feature Workflow: Specification-based implementation
- TDD: Test-driven development discipline

### 6.4 Blueprint System

Blueprints provide pre-configured starting points for common project types:

| Blueprint | Stack | Description |
|-----------|-------|-------------|
| python-fastapi | Python, FastAPI, SQLAlchemy | REST API development |
| typescript-react | TypeScript, React, Node.js | Web application development |
| java-spring | Java, Spring Boot, JPA | Enterprise application development |
| sap-abap | ABAP, SAP, RAP, CAP | SAP development |

Each blueprint includes appropriate axiom combinations, principles, methodologies, and technical patterns.

---

## 7. Benefits and Empirical Observations

### 7.1 Theoretical Benefits

**Consistency**: All behavior traces to axioms, preventing contradiction.

**Transparency**: Any behavioral rule can be explained by reference to its derivation chain.

**Auditability**: The system's value alignment can be verified by examining axioms and derivations.

**Stability**: Core values are preserved even as the system adapts to new situations.

**Maintainability**: Changes to specific behaviors don't require changing the entire system.

**Scalability**: The axiom set remains constant as the number of derived rules grows.

### 7.2 Observed Improvements

In practical application, we have observed:

**Reduced Inconsistency**: Agent behaviors are more predictable and consistent across contexts.

**Clearer Debugging**: When agents behave unexpectedly, the derivation chain helps identify the cause.

**Easier Onboarding**: New team members can understand the system by starting from axioms.

**Better Communication**: Axioms provide a shared vocabulary for discussing agent behavior.

**Graceful Failure**: The halt-on-conflict mechanism prevents silent value violations.

### 7.3 Comparison with Rule-Based Approaches

| Aspect | Rule-Based | Axiom-Based |
|--------|-----------|-------------|
| Scalability | Rules proliferate | Axioms remain constant |
| Consistency | Conflicts common | Conflicts detected and resolved |
| Transparency | Rules may be opaque | Derivation chains explain |
| Adaptability | New rules needed | Derive from existing axioms |
| Maintenance | High burden | Focused on axiom level |

---

## 8. Conclusion

### 8.1 Summary of Contributions

This paper has presented:

1. **A 5-layer architecture** that organizes agent systems from foundational axioms to technical implementation.

2. **A formal axiom system** with five core axioms (A1-A5) and five optional axioms (A6-A10) covering the key dimensions of trustworthy AI agent behavior.

3. **Derivation rules and validation constraints** that ensure logical consistency and enable human oversight.

4. **A deductive-inductive integration** that combines axiomatic grounding with experiential learning.

5. **A practical agent generation methodology** implemented in the Cursor Agent Factory.

### 8.2 Relationship to the Field

This work contributes to the growing consensus that AI alignment requires:

- **Values over rules**: Specific rules derive from fundamental values
- **Transparency**: AI systems should be explainable and auditable
- **Human oversight**: Critical decisions should involve human judgment
- **Continuous improvement**: Systems should learn while maintaining core values

The convergent discovery of similar principles by independent research efforts (including Anthropic's Constitutional AI) suggests these may be fundamental requirements for trustworthy AI.

### 8.3 Future Directions

Several directions warrant further investigation:

**Multi-Agent Coordination**: How do axiom systems interact when multiple agents collaborate?

**Cross-Cultural Alignment**: Can axiom sets be adapted for different cultural contexts while maintaining core values?

**Emergent Behavior Monitoring**: How can we detect when agent behaviors diverge from axiomatic foundations?

**Formal Verification**: Can we prove properties about agent behavior given the axiom system?

**Dynamic Axiom Revision**: What processes should govern changes to the axiom set itself?

### 8.4 Closing Reflection

Building AI systems that reliably serve human values is one of the most important challenges of our time. The axiom-based approach offers a principled methodology grounded in logic, philosophy, and practical software engineering. By making values explicit, derivable, and verifiable, we create systems that can be trusted, understood, and improved.

As AI agents become more capable and autonomous, such foundational work becomes ever more critical. We offer this framework in the hope that it contributes to the collective effort of building AI systems that truly serve human flourishing.

---

## References

Anthropic. (2022). Constitutional AI: Harmlessness from AI Feedback. https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

Anthropic. (2026). Claude's new constitution. https://www.anthropic.com/news/claude-new-constitution

Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.

Hilbert, D. (1899). Grundlagen der Geometrie. Teubner.

Martin, R. C. (2008). Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.

Russell, S. (2019). Human Compatible: Artificial Intelligence and the Problem of Control. Viking.

---

## Appendix A: Complete Axiom Reference

### Core Axioms

| ID | Name | Statement | Rationale |
|----|------|-----------|-----------|
| A1 | Verifiability | All agent outputs must be verifiable against source | Prevents hallucination |
| A2 | User Primacy | User intent takes precedence over agent convenience | Agents serve users |
| A3 | Transparency | Agent reasoning must be explainable on request | Enables trust |
| A4 | Non-Harm | No action may knowingly cause harm to users or systems | Safety first |
| A5 | Consistency | No rule may contradict these axioms | Logical foundation |

### Optional Axioms

| ID | Name | Statement | Use When |
|----|------|-----------|----------|
| A6 | Minimalism | Prefer simple solutions over complex ones | Maintenance priority |
| A7 | Reversibility | Prefer reversible actions over irreversible ones | Safety priority |
| A8 | Privacy | Minimize data exposure and collection | Sensitive data |
| A9 | Performance | Optimize for speed when correctness is ensured | Latency-critical |
| A10 | Learning | Every failure is an opportunity to improve | Continuous improvement |

---

## Appendix B: Derivation Rule Reference

| ID | Premise | Conclusion | Application |
|----|---------|------------|-------------|
| D1 | A1 ∧ output_is_code | require_testing | Code changes need tests |
| D2 | A2 ∧ conflict_exists | defer_to_user | Ask user when paths diverge |
| D3 | A4 ∧ action_is_destructive | require_confirmation | Dangerous ops need confirmation |
| D4 | A3 ∧ error_occurred | provide_explanation | No silent failures |
| D5 | A5 ∧ rule_proposed | validate_against_axioms | Check axiom consistency |

---

## Appendix C: Validation Constraint Reference

| ID | Check | Failure Action |
|----|-------|----------------|
| VC1 | Rule traces to axiom | Reject as unfounded |
| VC2 | Rule doesn't contradict axiom | Reject as invalid |
| VC3 | Derivation is logically sound | Reject as illogical |
| VC4 | Conflict between layers | Apply precedence (L0 > L1 > L2 > L3 > L4) |
| VC5 | Action violates axiom | Halt, request human guidance |

---

*This paper is part of the Value-Aligned AI Agent Systems research series.*
