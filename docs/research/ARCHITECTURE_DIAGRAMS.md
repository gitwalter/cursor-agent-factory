# Architecture Diagrams

Visual representations of the Value-Aligned AI Agent Systems architecture.

---

## 1. The 5-Layer Architecture

```mermaid
flowchart TB
    subgraph L0[Layer 0: INTEGRITY]
        A[Axioms A1-A5]
        D[Derivation Rules D1-D5]
        V[Validation Constraints VC1-VC5]
    end
    
    subgraph L1[Layer 1: PURPOSE]
        M[Mission Statement]
        S[Stakeholders]
        SC[Success Criteria]
    end
    
    subgraph L2[Layer 2: PRINCIPLES]
        EB[Ethical Boundaries]
        QS[Quality Standards]
        FH[Failure Handling]
    end
    
    subgraph L3[Layer 3: METHODOLOGY]
        MET[Agile/Kanban/R&D/Enterprise]
        ENF[Enforcement Patterns]
        PRA[Practice Patterns]
    end
    
    subgraph L4[Layer 4: TECHNICAL]
        STK[Stack Configuration]
        AGT[Agent Definitions]
        SKL[Skill Patterns]
        KNW[Knowledge Files]
    end
    
    L0 -->|derives| L1
    L1 -->|derives| L2
    L2 -->|derives| L3
    L3 -->|derives| L4
    
    style L0 fill:#e1f5fe
    style L1 fill:#f3e5f5
    style L2 fill:#fff3e0
    style L3 fill:#e8f5e9
    style L4 fill:#fce4ec
```

---

## 2. Layer Precedence

```mermaid
flowchart LR
    L0[L0: Integrity] --> L1[L1: Purpose]
    L1 --> L2[L2: Principles]
    L2 --> L3[L3: Methodology]
    L3 --> L4[L4: Technical]
    
    L0 -.->|"HIGHEST PRIORITY"| note1[Cannot be overridden]
    L4 -.->|"LOWEST PRIORITY"| note2[Must yield to higher layers]
```

**Precedence Rule**: L0 > L1 > L2 > L3 > L4

When conflicts arise, higher layers always take precedence.

---

## 3. Core Axiom System

```mermaid
flowchart TB
    subgraph CoreAxioms[Core Axioms - Always Apply]
        A1[A1: Verifiability<br/>Outputs must be verifiable]
        A2[A2: User Primacy<br/>User intent takes precedence]
        A3[A3: Transparency<br/>Reasoning must be explainable]
        A4[A4: Non-Harm<br/>No action may cause harm]
        A5[A5: Consistency<br/>No rule may contradict axioms]
    end
    
    subgraph OptionalAxioms[Optional Axioms - Context-Dependent]
        A6[A6: Minimalism]
        A7[A7: Reversibility]
        A8[A8: Privacy]
        A9[A9: Performance]
        A10[A10: Learning]
    end
    
    CoreAxioms --> Rules[Derived Rules]
    OptionalAxioms --> Rules
    
    Rules --> Behavior[Agent Behavior]
```

---

## 4. Derivation Flow

```mermaid
flowchart TB
    subgraph Axiom[Layer 0: Axiom]
        AX[A4: Non-Harm<br/>No action may cause harm]
    end
    
    subgraph Derivation[Derivation Rule]
        DR[D3: If A4 AND action is destructive<br/>THEN require confirmation]
    end
    
    subgraph Principle[Layer 2: Principle]
        PR[EB2: No Destructive Actions<br/>Without Confirmation]
    end
    
    subgraph Enforcement[Layer 3: Enforcement]
        EN[E5: Destructive Confirmation Gate<br/>Block until user confirms]
    end
    
    subgraph Technical[Layer 4: Technical]
        TE[confirm_destructive_action<br/>function in codebase]
    end
    
    Axiom -->|"derives via"| Derivation
    Derivation -->|"produces"| Principle
    Principle -->|"implemented by"| Enforcement
    Enforcement -->|"coded as"| Technical
```

---

## 5. Deductive-Inductive Integration

```mermaid
flowchart TB
    subgraph Deductive[Deductive Direction - Top Down]
        AX[Axioms]
        AX -->|derive| PR[Principles]
        PR -->|derive| RU[Rules]
        RU -->|derive| BE[Behavior]
    end
    
    subgraph Inductive[Inductive Direction - Bottom Up]
        OB[Observations]
        OB -->|generalize| PA[Proposed Patterns]
        PA -->|validate| VA[Validated Patterns]
        VA -->|integrate| UP[Updated Rules]
    end
    
    BE --> OB
    UP --> RU
    
    VA -.->|"check against"| AX
```

---

## 6. Validation Constraints

```mermaid
flowchart TB
    subgraph Action[Proposed Action]
        ACT[Agent wants to take action]
    end
    
    subgraph Validation[Validation Constraints]
        VC1[VC1: Rule traces to axiom?]
        VC2[VC2: No axiom contradiction?]
        VC3[VC3: Derivation sound?]
        VC4[VC4: Layer precedence respected?]
        VC5[VC5: Would violate axiom?]
    end
    
    subgraph Outcomes[Outcomes]
        PASS[PASS: Proceed]
        FAIL[FAIL: Reject]
        HALT[HALT: Request Human Guidance]
    end
    
    ACT --> VC1
    VC1 -->|yes| VC2
    VC1 -->|no| FAIL
    VC2 -->|yes| VC3
    VC2 -->|no| FAIL
    VC3 -->|yes| VC4
    VC3 -->|no| FAIL
    VC4 -->|yes| VC5
    VC4 -->|no| FAIL
    VC5 -->|no violation| PASS
    VC5 -->|would violate| HALT
```

---

## 7. The Complete Stack (Unified Framework)

```mermaid
flowchart TB
    subgraph Layer1[Layer 1: BASE MODEL]
        CAI[Constitutional AI Training]
        RLAIF[RLAIF Process]
        CONST[Published Constitution]
        PRI1[Safe > Ethical > Compliant > Helpful]
    end
    
    subgraph Layer2[Layer 2: AGENT ORCHESTRATION]
        ABA[Axiom-Based Architecture]
        FIVE[5-Layer System]
        VAL[Validation Constraints]
        HALT[Halt-on-Conflict]
    end
    
    subgraph Layer3[Layer 3: TEAM CULTURE]
        SAC[Sacred Psychology]
        PHI[Philosophical Techniques]
        SEP[Layer Separation]
        CUL[Excellence Culture]
    end
    
    Layer1 -->|"provides aligned base model"| Layer2
    Layer2 -->|"sustained by"| Layer3
    
    Layer1 -.->|"Training Time"| note1[Values embedded in model]
    Layer2 -.->|"Runtime"| note2[Values enforced at orchestration]
    Layer3 -.->|"Culture"| note3[Values lived in team]
```

---

## 8. Constitutional AI vs Axiom-Based Comparison

```mermaid
flowchart LR
    subgraph CAI[Constitutional AI]
        C1[Training-time alignment]
        C2[Natural language constitution]
        C3[RLAIF learning]
        C4[Single model focus]
        C5[Behavior stability post-training]
    end
    
    subgraph ABA[Axiom-Based Architecture]
        A1x[Runtime enforcement]
        A2x[Formal logical axioms]
        A3x[Pattern feedback learning]
        A4x[Multi-agent systems]
        A5x[Context-configurable values]
    end
    
    subgraph Shared[Convergent Principles]
        S1[Values over rules]
        S2[Explain WHY not just WHAT]
        S3[Hierarchical priority]
        S4[Human oversight]
        S5[Self-improvement]
        S6[Character framing]
    end
    
    CAI --> Shared
    ABA --> Shared
```

---

## 9. Three-Layer Sacred Psychology Architecture

```mermaid
flowchart TB
    subgraph Internal[Layer 1: SACRED ENFORCEMENT]
        S1[Sacred Language]
        S2[Maximum Commitment]
        S3[Team Culture]
        S4[Internal Docs]
    end
    
    subgraph Professional[Layer 2: PROFESSIONAL INTERFACE]
        P1[Technical Language]
        P2[Clean Experience]
        P3[Public Documentation]
        P4[APIs]
    end
    
    subgraph Technical[Layer 3: IMPLEMENTATION]
        T1[Measurable Standards]
        T2[Code and Systems]
        T3[Automated Checks]
        T4[Technical Specs]
    end
    
    Internal -->|"implements"| Technical
    Technical -->|"exposed via"| Professional
    
    Internal -.->|"Audience: Team"| note1[Hidden from users]
    Professional -.->|"Audience: Users"| note2[Clean professional experience]
```

---

## 10. Agent Generation Workflow

```mermaid
flowchart LR
    subgraph Phase1[Phase 1]
        P1[Define Purpose]
        P1A[Mission]
        P1B[Stakeholders]
        P1C[Success Criteria]
    end
    
    subgraph Phase2[Phase 2]
        P2[Select Axioms]
        P2A[Core A1-A5]
        P2B[Optional A6-A10]
    end
    
    subgraph Phase3[Phase 3]
        P3[Configure Principles]
        P3A[Ethical Boundaries]
        P3B[Quality Standards]
    end
    
    subgraph Phase4[Phase 4]
        P4[Choose Methodology]
        P4A[Agile/Kanban/etc]
        P4B[Enforcement]
    end
    
    subgraph Phase5[Phase 5]
        P5[Build Technical]
        P5A[Agents]
        P5B[Skills]
        P5C[Knowledge]
    end
    
    subgraph Output[Generated System]
        OUT[Complete Agent System]
    end
    
    Phase1 --> Phase2
    Phase2 --> Phase3
    Phase3 --> Phase4
    Phase4 --> Phase5
    Phase5 --> Output
```

---

## Usage

These diagrams are written in Mermaid markdown format and can be rendered by:
- GitHub/GitLab markdown preview
- Mermaid Live Editor (https://mermaid.live)
- VS Code with Mermaid extension
- Most modern documentation systems

To embed in other documents, copy the mermaid code blocks.

---

*Part of the Value-Aligned AI Agent Systems research series.*
