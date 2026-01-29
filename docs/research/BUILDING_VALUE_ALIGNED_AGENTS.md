# Building Value-Aligned Agents: A Practical Implementation Guide

**Authors:** Cursor Agent Factory Research Team  
**Version:** 1.0  
**Date:** January 2026  
**License:** Creative Commons CC0 1.0

---

## Abstract

This guide provides step-by-step instructions for building value-aligned AI agent systems using the Axiom-Based Agent Architecture. It covers the complete process from purpose definition through agent generation, with practical examples and code templates.

The guide is intended for practitioners who want to apply the theoretical framework presented in the companion papers. It includes concrete patterns, configuration examples, and implementation techniques that can be used immediately.

**Keywords:** AI agents, practical guide, implementation, value alignment, Cursor Agent Factory, software engineering, agent development

---

## 1. Introduction

### 1.1 What You'll Build

By following this guide, you will create a complete value-aligned agent system including:

- **PURPOSE.md**: Clear mission and success criteria
- **Axiom configuration**: Customized for your project
- **Principles and standards**: Ethical boundaries and quality requirements
- **Agent definitions**: AI agents with specific capabilities
- **Skill patterns**: Reusable behavioral patterns
- **Knowledge files**: Domain-specific reference data
- **Enforcement mechanisms**: Quality and safety gates

### 1.2 Prerequisites

- Familiarity with AI/LLM concepts
- Experience with software development
- Access to the Cursor Agent Factory (or understanding of its patterns)
- A project or domain to build agents for

### 1.3 Guide Structure

1. **Fundamentals**: Understanding the architecture
2. **Phase 1**: Define Purpose (Layer 1)
3. **Phase 2**: Select Axioms (Layer 0)
4. **Phase 3**: Configure Principles (Layer 2)
5. **Phase 4**: Choose Methodology (Layer 3)
6. **Phase 5**: Build Technical Layer (Layer 4)
7. **Advanced Topics**: Skills, enforcement, patterns

---

## 2. Fundamentals

### 2.1 The 5-Layer Architecture

Every value-aligned agent system consists of five layers:

```
Layer 0: INTEGRITY (Axioms, Derivation Rules, Validation)
    ↓ derives
Layer 1: PURPOSE (Mission, Stakeholders, Success Criteria)
    ↓ derives
Layer 2: PRINCIPLES (Ethical Boundaries, Quality Standards)
    ↓ derives
Layer 3: METHODOLOGY (Agile, Kanban, R&D, Enterprise)
    ↓ derives
Layer 4: TECHNICAL (Stack, Agents, Skills, Templates)
```

Higher layers constrain lower layers. Technical decisions (Layer 4) must align with methodology (Layer 3), which must align with principles (Layer 2), and so on.

### 2.2 Core Axioms

Every system includes these five core axioms:

| ID | Name | Key Requirement |
|----|------|-----------------|
| A1 | Verifiability | Outputs must be verifiable against source |
| A2 | User Primacy | User intent takes precedence |
| A3 | Transparency | Reasoning must be explainable |
| A4 | Non-Harm | No action may cause harm |
| A5 | Consistency | No rule may contradict axioms |

### 2.3 The Generation Process

```
┌─────────────────────────────────────────────────────────────┐
│  1. Define Purpose    → PURPOSE.md                          │
│  2. Select Axioms     → Axiom configuration                 │
│  3. Configure Principles → .cursorrules principles          │
│  4. Choose Methodology → workflows/methodology.yaml         │
│  5. Build Technical   → .cursor/, knowledge/, templates/    │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Phase 1: Define Purpose (Layer 1)

### 3.1 Why Purpose Matters

Purpose provides the "why" that guides all other decisions. Without clear purpose, you can't evaluate whether specific choices serve your goals.

### 3.2 The Three Components

**Mission Statement**: Why does this system exist?
- One sentence that captures the core purpose
- Must be verifiable (A1) and serve specific people (A2)

**Stakeholders**: Who does this system serve?
- Primary users who directly benefit
- Secondary stakeholders who are affected
- Be specific—not "everyone"

**Success Criteria**: How will you know it's working?
- Measurable outcomes, not just activities
- Tied to stakeholder benefit

### 3.3 PURPOSE.md Template

```markdown
# {PROJECT_NAME} - Purpose & Mission

## Mission Statement

{One sentence describing why this system exists and what it achieves}

## Who We Serve

### Primary Stakeholders
{Specific people who directly benefit}
- {Role/persona 1}: {What they need from us}
- {Role/persona 2}: {What they need from us}

### Secondary Stakeholders
{People indirectly affected}
- {Stakeholder 1}: {How they're affected}

## Success Definition

### Primary Outcome
{The main measurable result we want to achieve}

### How We Measure
{Specific metrics and methods for measuring success}

### Success Indicators
- [ ] {Indicator 1}
- [ ] {Indicator 2}
- [ ] {Indicator 3}

## Guiding Principles

{Brief statement of the values that guide how we achieve our mission}

---

*This purpose statement was created on {DATE} and guides all decisions for {PROJECT_NAME}.*
```

### 3.4 Example: SAP Development Agent

```markdown
# SAP Development Agent - Purpose & Mission

## Mission Statement

Enable SAP developers to deliver high-quality ABAP, RAP, and Fiori solutions 
efficiently by providing AI-assisted development with verified grounding in 
SAP documentation and best practices.

## Who We Serve

### Primary Stakeholders
- **SAP ABAP Developers**: Need efficient coding with verified syntax and patterns
- **SAP Consultants**: Need rapid prototyping with correct technical foundations
- **Development Team Leads**: Need consistent quality across team output

### Secondary Stakeholders
- **End Users**: Benefit from higher quality, fewer bugs
- **Business Owners**: Benefit from faster delivery, reduced costs

## Success Definition

### Primary Outcome
Developers complete SAP development tasks with 50% fewer errors and 
30% faster delivery compared to unassisted development.

### How We Measure
- Error rate in code review
- Time from requirement to working code
- Developer satisfaction surveys
- Reduction in documentation lookup time

### Success Indicators
- [ ] Grounding verification catches 95%+ of incorrect assumptions
- [ ] Developers report increased confidence in generated code
- [ ] Technical debt metrics improve over time
```

---

## 4. Phase 2: Select Axioms (Layer 0)

### 4.1 Core Axioms (Always Included)

The five core axioms are non-negotiable:

```json
{
  "core_axioms": [
    {
      "id": "A1_verifiability",
      "statement": "All agent outputs must be verifiable against source",
      "always_included": true
    },
    {
      "id": "A2_user_primacy", 
      "statement": "User intent takes precedence over agent convenience",
      "always_included": true
    },
    {
      "id": "A3_transparency",
      "statement": "Agent reasoning must be explainable on request",
      "always_included": true
    },
    {
      "id": "A4_non_harm",
      "statement": "No action may knowingly cause harm to users or systems",
      "always_included": true
    },
    {
      "id": "A5_consistency",
      "statement": "No rule may contradict these axioms",
      "always_included": true
    }
  ]
}
```

### 4.2 Optional Axioms

Select optional axioms based on your project context:

| ID | Name | Select When... |
|----|------|----------------|
| A6 | Minimalism | Maintenance and understandability are priorities |
| A7 | Reversibility | Safety and recoverability are paramount |
| A8 | Privacy | Handling sensitive user data |
| A9 | Performance | Performance-critical applications |
| A10 | Learning | Continuous improvement is valued |

### 4.3 Recommended Combinations

**Standard Development** (most projects):
```json
{
  "optional_axioms": ["A6_minimalism", "A7_reversibility"]
}
```

**Enterprise Security** (sensitive data):
```json
{
  "optional_axioms": ["A7_reversibility", "A8_privacy"]
}
```

**High Performance** (latency-critical):
```json
{
  "optional_axioms": ["A9_performance"]
}
```

**AI/ML Research** (experimental):
```json
{
  "optional_axioms": ["A7_reversibility", "A10_learning"]
}
```

### 4.4 Conflict Resolution

Some axioms can conflict (e.g., A6 Minimalism vs. A9 Performance). When conflicts occur:

1. **Default to the safer option** (usually A6)
2. **Apply A9 only when profiling identifies actual bottlenecks**
3. **Document the trade-off decision**

---

## 5. Phase 3: Configure Principles (Layer 2)

### 5.1 Principle Categories

**Ethical Boundaries**: What agents must NEVER do
**Quality Standards**: What quality bar must be met
**Failure Handling**: How to respond to errors

### 5.2 Ethical Boundaries (EB)

Select from the pattern library:

| ID | Principle | Axiom Basis |
|----|-----------|-------------|
| EB1 | No Silent Failures | A3 (Transparency) |
| EB2 | No Destructive Without Confirmation | A4 (Non-Harm) |
| EB3 | No Ignoring User Preferences | A2 (User Primacy) |
| EB4 | No Unverified Claims | A1 (Verifiability) |
| EB5 | No Axiom Violations | A5 (Consistency) |
| EB6 | No Hidden Logic | A3 (Transparency) |
| EB7 | No Unnecessary Data Exposure | A4, A8 |

**Configuration Example**:
```yaml
ethical_boundaries:
  - EB1_no_silent_failures
  - EB2_no_destructive_without_confirmation
  - EB3_no_ignoring_user_preferences
  - EB4_no_unverified_claims
  - EB5_no_axiom_violations
```

### 5.3 Quality Standards (QS)

| ID | Standard | Axiom Basis |
|----|----------|-------------|
| QS1 | Test Coverage Required | A1 (Verifiability) |
| QS2 | Documentation Required | A3 (Transparency) |
| QS3 | Comprehensive Error Handling | A3, A4 |
| QS4 | Peer Review Required | A1, A3 |
| QS5 | Consistent Code Style | A5 (Consistency) |
| QS6 | Type Safety | A1 (Verifiability) |
| QS7 | Security Standards | A4 (Non-Harm) |

**Configuration Example**:
```yaml
quality_standards:
  - QS1_test_coverage:
      minimum: 80
      new_code: 90
      critical_path: 100
  - QS2_documentation_required
  - QS3_error_handling
  - QS4_code_review
```

### 5.4 Failure Handling (FH)

| ID | Principle | Description |
|----|-----------|-------------|
| FH1 | Graceful Degradation | Degrade rather than fail completely |
| FH2 | Clear Error Communication | Explain what happened clearly |
| FH3 | Fail Fast, Fail Safely | Detect early, prevent cascading |
| FH4 | Preserve State | Don't corrupt or lose data |
| FH5 | Log for Learning | Log context for analysis |
| FH6 | Automatic Recovery | Retry transient failures |
| FH7 | Escalation Path | Route to humans when needed |

---

## 6. Phase 4: Choose Methodology (Layer 3)

### 6.1 Available Methodologies

| Methodology | Best For | Key Pattern |
|-------------|----------|-------------|
| Agile Scrum | Product development | Sprints, ceremonies, collaboration |
| Kanban | Support, maintenance | Continuous flow, WIP limits |
| R&D | AI/ML, research | Experimentation, learning |
| Enterprise | Large-scale, compliance | Governance, documentation |

### 6.2 Methodology Configuration

**Agile Scrum Example**:
```yaml
methodology:
  name: agile_scrum
  
  coordination_pattern: domain_expert_swarm
  
  ceremonies:
    - daily_standup: 15min
    - sprint_planning: 2hr
    - sprint_review: 1hr
    - retrospective: 1hr
  
  artifacts:
    - product_backlog
    - sprint_backlog
    - increment
  
  roles:
    - product_owner
    - scrum_master
    - development_team
```

### 6.3 Enforcement Patterns

Enforcement patterns ensure values are lived, not just stated:

**Quality Enforcement**:
```yaml
enforcement:
  quality:
    - E1_test_coverage:
        trigger: before_merge
        threshold: 80
        action: block_if_below
    
    - E2_code_review:
        trigger: before_merge
        required_approvals: 1
        action: block_until_approved
```

**Safety Enforcement**:
```yaml
enforcement:
  safety:
    - E5_destructive_confirmation:
        trigger: destructive_operation
        action: require_confirmation
        message: "This action is irreversible. Confirm?"
    
    - E6_backup_before_change:
        trigger: before_destructive
        action: create_backup
```

### 6.4 Practice Patterns

Practices are regular disciplines maintaining excellence:

**Daily Practices**:
```yaml
practices:
  daily:
    - P1_morning_intention:
        duration: 5min
        purpose: "Begin with clarity of purpose"
    
    - P3_standup_focus:
        duration: 15min
        purpose: "Align team, surface blockers"
```

**Craft Practices**:
```yaml
practices:
  craft:
    - P4_code_as_craft:
        frequency: per_commit
        checklist:
          - code_is_clear
          - tests_present
          - no_debug_code
          - meaningful_commit_message
```

---

## 7. Phase 5: Build Technical Layer (Layer 4)

### 7.1 Stack Configuration

Define your technology stack:

```yaml
stack:
  primary_language: python
  version: "3.11"
  
  frameworks:
    - fastapi: "0.104+"
    - sqlalchemy: "2.0+"
    - pydantic: "2.0+"
  
  database:
    primary: postgresql
    version: "15+"
  
  testing:
    unit: pytest
    integration: pytest-asyncio
    coverage: pytest-cov
```

### 7.2 Agent Definitions

Create agent definition files in `.cursor/agents/`:

**code-reviewer.md**:
```markdown
# Code Reviewer Agent

## Purpose
Review code for correctness, style, performance, security, 
and maintainability.

## Activation Triggers
- "Review this code"
- "Check this PR"
- "Code review"

## Capabilities
- Analyze code structure and logic
- Check against style guidelines
- Identify performance issues
- Flag security vulnerabilities
- Suggest improvements

## Axiom Alignment
- A1: Verify claims against codebase
- A3: Explain all feedback clearly
- A4: Prioritize safety issues

## Review Dimensions
1. **Correctness**: Does it work as intended?
2. **Clarity**: Is the intent obvious?
3. **Completeness**: Are edge cases handled?
4. **Consistency**: Does it follow patterns?
5. **Craft**: Does it reflect excellence?
```

### 7.3 Skill Patterns

Create skill definitions in `.cursor/skills/`:

**grounding/SKILL.md**:
```markdown
# Grounding Skill

## Purpose
Verify data structures, field existence, and assumptions 
before implementation.

## When to Use
- Before implementing data access logic
- When working with database tables
- Before assuming any field exists

## Process

### Step 1: Check Knowledge Files
Query knowledge files for cached definitions.

### Step 2: Search Documentation
If not cached, search authoritative documentation.

### Step 3: Verify Critical Fields
Confirm existence of key fields, types, relationships.

### Step 4: Document Verification
Record what was verified and from what source.

### Step 5: Handle Unverified
If verification fails, STOP and ASK user.

## Output Format
| Structure | Field | Verified? | Source | Notes |
|-----------|-------|-----------|--------|-------|

## Important Rules
- NEVER assume structures exist without verification
- ALWAYS verify before implementation
- If verification fails, STOP and ASK user
```

### 7.4 Knowledge Files

Create domain-specific reference data in `knowledge/`:

**data-patterns.json**:
```json
{
  "title": "Data Patterns",
  "description": "Verified data structures for this project",
  "version": "1.0.0",
  
  "structures": {
    "User": {
      "verified": true,
      "source": "database schema v2.3",
      "fields": {
        "id": {"type": "integer", "primary_key": true},
        "email": {"type": "string", "unique": true},
        "created_at": {"type": "datetime", "auto": true}
      }
    }
  },
  
  "patterns": {
    "soft_delete": {
      "description": "Use deleted_at timestamp instead of DELETE",
      "fields": ["deleted_at: datetime nullable"],
      "axiom_basis": "A7_reversibility"
    }
  }
}
```

### 7.5 Templates

Create code templates in `templates/`:

**api/endpoint.py.tmpl**:
```python
"""
{DESCRIPTION}

Axiom Alignment:
- A1: {VERIFIABILITY_NOTES}
- A4: {SAFETY_NOTES}
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List

router = APIRouter(prefix="/{RESOURCE_NAME}", tags=["{RESOURCE_NAME}"])


@router.get("/", response_model=List[{MODEL_NAME}])
async def list_{RESOURCE_NAME}(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    List {RESOURCE_NAME} with pagination.
    
    Verification: Results come from verified database query.
    """
    return db.query({MODEL_NAME}).offset(skip).limit(limit).all()


@router.post("/", response_model={MODEL_NAME})
async def create_{RESOURCE_NAME}(
    data: {MODEL_NAME}Create,
    db: Session = Depends(get_db)
):
    """
    Create new {RESOURCE_NAME}.
    
    Safety: Input validated by Pydantic schema.
    """
    item = {MODEL_NAME}(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
```

---

## 8. Advanced Topics

### 8.1 The Grounding Skill in Depth

Grounding is essential for preventing hallucination:

```python
class GroundingSkill:
    """
    Verify assumptions before implementation.
    Axiom basis: A1 (Verifiability)
    """
    
    def verify_structure(self, structure_name: str) -> VerificationResult:
        """
        Multi-step verification process.
        """
        # Step 1: Check knowledge files
        cached = self.check_knowledge_cache(structure_name)
        if cached:
            return VerificationResult(
                verified=True,
                source="knowledge_cache",
                data=cached
            )
        
        # Step 2: Search documentation
        docs = self.search_documentation(structure_name)
        if docs:
            return VerificationResult(
                verified=True,
                source="documentation",
                data=docs
            )
        
        # Step 3: Cannot verify - halt and ask
        return VerificationResult(
            verified=False,
            source=None,
            message=f"Cannot verify {structure_name}. Please confirm."
        )
    
    def halt_if_unverified(self, result: VerificationResult):
        """
        Implements A1: Don't proceed with unverified assumptions.
        """
        if not result.verified:
            raise VerificationRequired(result.message)
```

### 8.2 Strawberry Verification

For critical claims, use information-theoretic verification:

```python
class StrawberryVerification:
    """
    Mathematical hallucination detection.
    Named for the "How many R's in strawberry?" test.
    """
    
    def verify_claim(self, claim: str, evidence: List[str]) -> float:
        """
        Calculate confidence based on evidence quality.
        
        Returns:
            Confidence score 0-1
        """
        if not evidence:
            return 0.0
        
        # Multiple independent sources increase confidence
        source_diversity = self.calculate_source_diversity(evidence)
        
        # Direct evidence > indirect
        directness = self.calculate_evidence_directness(evidence)
        
        # Recency matters for some claims
        recency = self.calculate_recency_weight(evidence)
        
        return self.combine_scores(source_diversity, directness, recency)
    
    def should_proceed(self, confidence: float, threshold: float = 0.8) -> bool:
        """
        Determine if confidence is sufficient to proceed.
        """
        if confidence >= threshold:
            return True
        elif confidence >= 0.5:
            # Medium confidence: proceed with warning
            self.log_warning(f"Proceeding with confidence {confidence}")
            return True
        else:
            # Low confidence: halt
            return False
```

### 8.3 Enforcement Implementation

Implementing validation constraints:

```python
class ValidationConstraints:
    """
    Runtime validation ensuring axiom compliance.
    """
    
    def vc1_axiom_traceability(self, rule: Rule) -> bool:
        """Every rule must trace to at least one axiom."""
        return len(rule.axiom_references) >= 1
    
    def vc2_no_contradiction(self, rule: Rule, axioms: List[Axiom]) -> bool:
        """Rule must not contradict any axiom."""
        for axiom in axioms:
            if self.contradicts(rule, axiom):
                return False
        return True
    
    def vc5_halt_on_conflict(self, action: Action) -> HaltDecision:
        """
        If action would violate axiom, halt and request guidance.
        """
        violations = self.check_axiom_violations(action)
        
        if violations:
            return HaltDecision(
                halt=True,
                reason=f"Action would violate: {violations}",
                request_guidance=True
            )
        
        return HaltDecision(halt=False)
```

### 8.4 Pattern Feedback Skill

Enabling inductive learning:

```python
class PatternFeedbackSkill:
    """
    Learn from experience while maintaining axiom alignment.
    Implements the inductive direction of the architecture.
    """
    
    def observe(self, event: Event):
        """Collect observations for pattern detection."""
        self.observations.append(event)
    
    def detect_patterns(self) -> List[ProposedPattern]:
        """Identify patterns from observations."""
        patterns = self.pattern_detector.analyze(self.observations)
        return patterns
    
    def validate_pattern(self, pattern: ProposedPattern) -> ValidationResult:
        """
        Ensure proposed pattern aligns with axioms.
        This is where induction meets deduction.
        """
        # VC1: Must trace to axiom
        if not self.traces_to_axiom(pattern):
            return ValidationResult(
                valid=False,
                reason="Pattern does not trace to any axiom"
            )
        
        # VC2: Must not contradict axioms
        if self.contradicts_axiom(pattern):
            return ValidationResult(
                valid=False,
                reason="Pattern contradicts an axiom"
            )
        
        return ValidationResult(valid=True)
    
    def integrate_pattern(self, pattern: ProposedPattern):
        """Add validated pattern to the appropriate layer."""
        layer = self.determine_appropriate_layer(pattern)
        layer.add_pattern(pattern)
        self.log_pattern_integration(pattern, layer)
```

---

## 9. Generated Project Structure

When complete, your project will have this structure:

```
{PROJECT}/
├── .cursorrules              # Agent behavior rules (all layers)
├── PURPOSE.md                # Mission, stakeholders, success (L1)
├── enforcement.yaml          # Enforcement configuration (L2+)
├── practices.yaml            # Team practices (L3+)
│
├── .cursor/
│   ├── agents/               # Agent definitions (L4)
│   │   ├── code-reviewer.md
│   │   ├── test-generator.md
│   │   └── documentation-agent.md
│   │
│   └── skills/               # Skill definitions (L4)
│       ├── grounding/
│       │   └── SKILL.md
│       ├── bugfix-workflow/
│       │   └── SKILL.md
│       └── tdd/
│           └── SKILL.md
│
├── knowledge/                # Domain knowledge (L4)
│   ├── data-patterns.json
│   ├── api-contracts.json
│   └── best-practices.json
│
├── templates/                # Code templates (L4)
│   ├── api/
│   ├── models/
│   └── tests/
│
├── workflows/
│   └── methodology.yaml      # Methodology config (L3)
│
├── src/                      # Source code
├── tests/                    # Test files
└── README.md                 # Project documentation
```

---

## 10. Quick Start Checklist

### Phase 1: Purpose
- [ ] Write one-sentence mission statement
- [ ] Identify primary and secondary stakeholders
- [ ] Define measurable success criteria
- [ ] Create PURPOSE.md

### Phase 2: Axioms
- [ ] Include all core axioms (A1-A5)
- [ ] Select appropriate optional axioms
- [ ] Document axiom configuration

### Phase 3: Principles
- [ ] Select ethical boundaries (EB1-EB7)
- [ ] Configure quality standards (QS1-QS7)
- [ ] Choose failure handling patterns (FH1-FH7)

### Phase 4: Methodology
- [ ] Choose methodology (Agile, Kanban, R&D, Enterprise)
- [ ] Configure enforcement patterns
- [ ] Select practice patterns

### Phase 5: Technical
- [ ] Configure technology stack
- [ ] Create agent definitions
- [ ] Write skill patterns
- [ ] Populate knowledge files
- [ ] Create code templates

### Validation
- [ ] All rules trace to axioms
- [ ] No axiom contradictions
- [ ] Layer precedence respected
- [ ] Human oversight mechanisms in place

---

## 11. Conclusion

Building value-aligned agents is not just about technical implementation—it's about creating systems that reliably embody human values. This guide has provided the practical steps for implementing the Axiom-Based Agent Architecture.

Key takeaways:

1. **Start with purpose**: Everything derives from knowing why the system exists
2. **Axioms are foundational**: They ensure consistency and enable reasoning
3. **Layers provide structure**: Each layer has its role and respects higher layers
4. **Enforcement matters**: Values must be lived, not just stated
5. **Continuous improvement**: Pattern feedback enables learning while maintaining alignment

With these foundations in place, you can build AI agent systems that are not only capable but trustworthy—systems that serve human flourishing as their core purpose.

---

## References

- Paper 1: Axiom-Based Agent Architecture
- Paper 2: Sacred Psychology in Software Engineering
- Paper 3: Constitutional AI - Convergent Discovery Analysis
- Cursor Agent Factory Pattern Library
- Anthropic Constitutional AI Documentation

---

## Appendix A: Configuration Templates

### axioms.yaml
```yaml
core_axioms:
  - A1_verifiability
  - A2_user_primacy
  - A3_transparency
  - A4_non_harm
  - A5_consistency

optional_axioms:
  - A6_minimalism
  - A7_reversibility
```

### principles.yaml
```yaml
ethical_boundaries:
  - EB1_no_silent_failures
  - EB2_no_destructive_without_confirmation
  - EB3_no_ignoring_user_preferences
  - EB4_no_unverified_claims

quality_standards:
  - QS1_test_coverage:
      minimum: 80
  - QS2_documentation_required
  - QS4_code_review

failure_handling:
  - FH1_graceful_degradation
  - FH2_clear_error_communication
  - FH7_escalation_path
```

---

*This guide is part of the Value-Aligned AI Agent Systems research series.*
