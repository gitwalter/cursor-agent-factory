# SAP Fiori Integration - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for SAP RAP development with Fiori Elements, grounded in official SAP documentation.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for SAP RAP development with Fiori Elements
```

---

### Pre-Phase: Axiom Selection (Layer 0)

**Factory Prompt:**
> Every agent system needs foundational axioms. Core axioms (A1-A5) are always included.
> Would you like to add optional axioms?

**Your Response:**
```
Yes, add A6 (Minimalism) and A7 (Reversibility)
```

**Rationale:** 
- A6 (Minimalism): SAP systems benefit from simplicity to reduce maintenance burden
- A7 (Reversibility): Enterprise changes should be reversible for safety

**Selected Axioms:**

| ID | Axiom | Application |
|----|-------|-------------|
| A1 | Verifiability | All code grounded in SAP documentation |
| A2 | User Primacy | Business user needs first |
| A3 | Transparency | Clear transport management |
| A4 | Non-Harm | No system-breaking changes |
| A5 | Consistency | SAP naming conventions |
| A6 | Minimalism | Clean, focused implementations |
| A7 | Reversibility | Changes can be rolled back |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To accelerate SAP RAP development by grounding all code in official documentation and enforcing SAP best practices
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
SAP ABAP developers building Fiori applications on S/4HANA or BTP (team of 4-8)
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
100% compliance with SAP RAP guidelines as verified against official documentation
```

---

### Phase 0.5: Depth Selection

**Factory Prompt:**
> How deep should we define the remaining layers?

**Your Response:**
```
C (Comprehensive)
```

**Rationale:** Enterprise SAP development requires enforcement patterns and team practices.

---

### Phases 0.6-0.7: Principles & Methodology (Layer 2-3)

**Factory Prompt:**
> What development methodology fits your team?

**Your Response:**
```
Enterprise Integration
```

---

**Factory Prompt:**
> Team size?

**Your Response:**
```
4-8 developers
```

---

**Factory Prompt:**
> Change management approach?

**Your Response:**
```
Transport-based with CAB (Change Advisory Board) approval
```

The factory will configure:
- Transport request workflows
- CAB approval gates
- Release blessing ceremonies

---

### Phases 0.8-0.9: Enforcement & Practices (Comprehensive)

**Factory Prompt:**
> Which enforcement patterns should be active?

**Your Response:**
```
Quality enforcement, safety enforcement, and integrity enforcement
```

**Configured Enforcement:**
- Test coverage gate (ABAP Unit)
- Peer review gate
- ATC (ABAP Test Cockpit) check
- Transport validation

---

**Factory Prompt:**
> Which practice patterns should be active?

**Your Response:**
```
Daily practices and craft practices
```

**Configured Practices:**
- Morning intention (sprint goal alignment)
- Transport review (before release)
- Weekly documentation sync

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
travel-booking-rap
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
RAP-based travel booking application with Fiori Elements UI for agency bookings
```

---

### Phase 2: Technology Stack

**Factory Prompt:**
> What is your primary programming language?

**Your Response:**
```
ABAP
```

---

**Factory Prompt:**
> What frameworks will you use?

**Your Response:**
```
RAP, CDS, Fiori Elements
```

---

**Factory Prompt:**
> I found a matching blueprint: sap-abap. Would you like to use it?

**Your Response:**
```
Yes
```

---

**Factory Prompt:**
> What SAP environment?

**Your Response:**
```
SAP BTP ABAP Environment
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
SAP Solution Manager incidents and change requests
```

---

**Factory Prompt:**
> Would you like to configure MCP server integration?

**Your Response:**
```
Yes, configure SAP Documentation MCP for grounding
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What SAP patterns should the agent follow?

**Your Response:**
```
RAP BO patterns, CDS annotations, Fiori Elements configuration
```

---

### Phase 5: Agent & Skill Selection

**Factory Prompt:**
> Which agents should I include?

**Your Response:**
```
Code reviewer, test generator
```

---

**Factory Prompt:**
> Which skills should be available?

**Your Response:**
```
grounding, bugfix-workflow, feature-workflow
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\travel-booking-rap
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: travel-booking-rap                                    ║
║ Blueprint: sap-abap                                            ║
║ Depth: Comprehensive                                           ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: A6 (Minimalism), A7 (Reversibility)                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: SAP-grounded RAP development                        ║
║   Stakeholders: SAP ABAP developers (4-8)                      ║
║   Success: 100% compliance with SAP guidelines                 ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Enterprise Integration                          ║
║   Change Management: Transport-based with CAB                  ║
╠════════════════════════════════════════════════════════════════╣
║ ENFORCEMENT                                                    ║
║   Quality: Test coverage, ATC checks                           ║
║   Safety: Transport validation, backup before change           ║
║   Integrity: Documentation grounding                           ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: ABAP, RAP, CDS, Fiori Elements                        ║
║   Agents: code-reviewer, test-generator                        ║
║   Skills: grounding, bugfix-workflow, feature-workflow         ║
║   MCP: SAP Documentation                                       ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\travel-booking-rap                         ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Generated Artifacts

```
travel-booking-rap/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   └── test-generator.md
│   └── skills/
│       ├── grounding/
│       │   └── SKILL.md          # SAP documentation grounding
│       ├── bugfix-workflow/
│       │   └── SKILL.md
│       └── feature-workflow/
│           └── SKILL.md
├── knowledge/
│   ├── rap-patterns.json         # RAP BO patterns
│   ├── cds-annotations.json      # CDS annotation reference
│   ├── fiori-elements.json       # Fiori Elements config
│   └── abap-clean-code.json      # ABAP Clean Code rules
├── src/
│   ├── cds/                      # CDS definitions
│   │   ├── data_model.cds
│   │   ├── projections.cds
│   │   └── metadata.cds
│   ├── behavior/                 # Behavior definitions
│   │   ├── behavior_definition.bdef
│   │   └── behavior_impl.abap
│   ├── classes/                  # ABAP classes
│   └── tests/                    # ABAP Unit tests
├── workflows/
│   └── methodology.yaml          # Enterprise Integration config
├── .cursorrules                  # 5-layer rules with enforcement
├── PURPOSE.md
├── enforcement.yaml              # Enforcement patterns
├── practices.yaml                # Team practices
└── README.md
```

---

## Using the SAP Documentation MCP

### Grounding Before Implementation

**Example: Create CDS View**
```
Create a CDS view for travel bookings with approval status
```

The agent will:
1. Query SAP Help Portal via MCP for CDS syntax
2. Verify annotations against documentation
3. Generate compliant CDS code
4. Cite source documentation

### Verifying Code

**Example: Check RAP Compliance**
```
Verify this behavior definition against SAP RAP guidelines
```

The grounding skill will:
1. Fetch relevant SAP documentation
2. Compare code against patterns
3. Report compliance status
4. Suggest corrections with sources

---

## Key SAP Patterns

### CDS Data Model

```cds
@EndUserText.label: 'Travel'
define root view entity ZI_Travel
  as select from ztravel
{
  key travel_id     as TravelId,
      agency_id     as AgencyId,
      @Semantics.amount.currencyCode: 'CurrencyCode'
      total_price   as TotalPrice,
      currency_code as CurrencyCode,
      status        as Status,
      @Semantics.user.createdBy: true
      created_by    as CreatedBy
}
```

### Behavior Definition

```
managed implementation in class zbp_i_travel unique;
strict ( 2 );

define behavior for ZI_Travel alias Travel
persistent table ztravel
draft table ztravel_d
lock master total etag LastChangedAt
authorization master ( instance )
{
  create;
  update;
  delete;
  
  action ( features : instance ) acceptTravel result [1] $self;
  
  mapping for ztravel corresponding;
}
```

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Should include A6, A7, and enforcement section
2. `PURPOSE.md` - Should reference SAP documentation grounding
3. `enforcement.yaml` - Should have quality and safety gates
4. `practices.yaml` - Should have enterprise ceremonies

---

## Next Steps

1. Set up ADT (ABAP Development Tools) project
2. Create CDS views using grounding skill
3. Implement behavior with MCP verification
4. Run ATC checks before transport

**Congratulations!** You've generated a complete Cursor agent system for SAP RAP development with documentation grounding.
