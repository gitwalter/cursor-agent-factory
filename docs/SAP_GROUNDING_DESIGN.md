# SAP Grounding System Design

> **Reference Tag:** `sap-grounding-v1.0` in cursor-agent-factory
> **Target Repository:** cursor-sap-development-workflow

## Overview

This document captures the comprehensive SAP grounding system design created in the Cursor Agent Factory. The full implementation is preserved in git tag `sap-grounding-v1.0`.

## Architecture

For complete visual diagrams, see [../diagrams/sap-grounding-architecture.md](../diagrams/sap-grounding-architecture.md).

### 5-Layer Grounding Architecture

The grounding system uses a tiered approach, starting with fast cached lookups and escalating to more thorough verification:

```mermaid
flowchart TB
    subgraph Query["Grounding Query"]
        Q["Verify: Does table BSEG have field DMBTR?"]
    end

    subgraph L1["Layer 1: Knowledge Cache"]
        L1D["knowledge/*.json"]
        L1R["Instant lookup, HIGH confidence"]
    end

    subgraph L2["Layer 2: SAP Documentation"]
        L2D["SAP Help Portal via MCP"]
        L2R["Fast lookup, HIGH confidence"]
    end

    subgraph L3["Layer 3: Reference Repositories"]
        L3D["abap-cheat-sheets via DeepWiki"]
        L3R["Fast lookup, MEDIUM confidence"]
    end

    subgraph L4["Layer 4: Project Specifications"]
        L4D["Confluence/Excel via Atlassian MCP"]
        L4R["Medium lookup, HIGH project-specific"]
    end

    subgraph L5["Layer 5: Strawberry Verification"]
        L5D["Two-pass hallucination detection"]
        L5R["Final verification layer"]
    end

    Q --> L1 -->|"Not found"| L2 -->|"Not found"| L3 -->|"Not found"| L4 --> L5

    style L1 fill:#c8e6c9
    style L2 fill:#a5d6a7
    style L3 fill:#fff9c4
    style L4 fill:#ffcc80
    style L5 fill:#ce93d8
```

### Skill Hierarchy

The SAP grounding coordinator routes verification requests to specialized skills:

```mermaid
flowchart TB
    subgraph Coordinator["sap-grounding (Coordinator)"]
        C["Routes based on artifact type"]
    end

    subgraph Technical["Technical Skills"]
        DDIC["ddic-grounding<br/>Tables, structures, data elements"]
        CDS["cds-grounding<br/>CDS views, annotations, DCL"]
        RAP["rap-grounding<br/>Behavior definitions, actions"]
        CLASS["class-grounding<br/>Classes, interfaces, exceptions"]
        FUNC["function-grounding<br/>Function modules, BAPIs, RFCs"]
        API["api-grounding<br/>OData services, bindings"]
    end

    subgraph Support["Support Skills"]
        ENH["enhancement-grounding<br/>BAdIs, enhancement spots"]
        MSG["message-grounding<br/>Message classes, numbers"]
        AUTH["authorization-grounding<br/>Auth objects, fields"]
        MAP["mapping-grounding<br/>Field mappings"]
        EXIST["existence-grounding<br/>TADIR, release contracts"]
        FIORI["fiori-grounding<br/>Apps, semantic objects"]
    end

    subgraph Verify["Verification"]
        STRAW["strawberry-verification<br/>Hallucination detection"]
    end

    C --> DDIC & CDS & RAP & CLASS & FUNC & API
    C --> ENH & MSG & AUTH & MAP & EXIST & FIORI
    
    DDIC & CDS & RAP & CLASS & FUNC & API --> STRAW

    style Coordinator fill:#e3f2fd
    style Technical fill:#e8f5e9
    style Support fill:#fff3e0
    style Verify fill:#f3e5f5
```

## Specialized Skills

### 1. DDIC Grounding (`ddic-grounding`)
**Purpose:** Verify SAP Data Dictionary objects

**Artifacts:**
- Transparent tables, pooled/cluster tables
- Structures and table types
- Data elements and domains
- Search helps

**Key Verifications:**
- Field existence and data types
- Key field relationships
- Foreign key constraints
- Value ranges from domains

### 2. CDS Grounding (`cds-grounding`)
**Purpose:** Verify CDS entity definitions

**Artifacts:**
- CDS view entities
- CDS projections
- Annotations (@UI, @OData, @Semantics)
- Access control definitions (DCL)

**Key Verifications:**
- Association targets exist
- Annotation syntax correctness
- Access control field references

### 3. RAP Grounding (`rap-grounding`)
**Purpose:** Verify RAP behavior definitions

**Artifacts:**
- Behavior definitions (BDEF)
- Actions and functions
- Determinations and validations
- Draft handling

**Key Verifications:**
- CDS entity references
- Action parameter types
- Feature control fields

### 4. Class Grounding (`class-grounding`)
**Purpose:** Verify ABAP OO artifacts

**Artifacts:**
- Global classes (ZCL_*, CL_*)
- Interfaces (ZIF_*, IF_*)
- Exception classes (ZCX_*, CX_*)
- Method signatures

**Key Verifications:**
- Class/interface existence
- Method signatures match
- Exception class hierarchy
- Release status (C0/C1/C2)

### 5. Function Grounding (`function-grounding`)
**Purpose:** Verify function modules and BAPIs

**Artifacts:**
- Function modules
- Function groups
- BAPIs
- RFCs

**Key Verifications:**
- Parameter signatures
- Table parameters
- Exception handling
- BAPI return structures

### 6. API Grounding (`api-grounding`)
**Purpose:** Verify SAP APIs and services

**Artifacts:**
- OData V2/V4 services
- Service definitions (SRVD)
- Service bindings (SRVB)
- SOAP services

**Key Verifications:**
- Entity set names
- Navigation properties
- Operation names
- Protocol version

### 7. Enhancement Grounding (`enhancement-grounding`)
**Purpose:** Verify enhancement points

**Artifacts:**
- Enhancement spots
- BAdI definitions and implementations
- Enhancement sections
- Implicit enhancement points

**Key Verifications:**
- BAdI filter values
- Enhancement option availability
- Fallback class behavior

### 8. Message Grounding (`message-grounding`)
**Purpose:** Verify message classes

**Artifacts:**
- Message classes
- Message numbers
- Message texts
- Placeholder variables

**Key Verifications:**
- Message class exists
- Message number valid
- Placeholder count matches

### 9. Authorization Grounding (`authorization-grounding`)
**Purpose:** Verify authorization objects

**Artifacts:**
- Authorization objects
- Authorization fields
- Authorization checks

**Key Verifications:**
- Object and field existence
- Valid field values
- Check implementation pattern

### 10. Mapping Grounding (`mapping-grounding`)
**Purpose:** Verify field mappings against specifications

**Artifacts:**
- Source/target field mappings
- Transformation rules
- Confluence specifications
- Excel mapping sheets

**Key Verifications:**
- Source fields exist
- Target fields exist
- Data type compatibility
- Transformation logic validity

### 11. Existence Grounding (`existence-grounding`)
**Purpose:** Verify repository object existence

**Artifacts:**
- Any TADIR object
- Package assignments
- Transport assignments

**Key Verifications:**
- Object exists in repository
- Release contract status (C0/C1/C2)
- Deprecation status
- ABAP Cloud compatibility

### 12. Fiori Grounding (`fiori-grounding`)
**Purpose:** Verify Fiori/UI5 artifacts

**Artifacts:**
- Fiori app IDs
- Semantic objects and actions
- UI5 component IDs
- Launchpad tiles

**Key Verifications:**
- App registration
- Semantic object mapping
- Component availability

## Strawberry Verification

For detailed verification flow diagrams, see [../diagrams/verification-flow.md](../diagrams/verification-flow.md).

### Concept
Detects "procedural hallucinations" where the LLM generates correct information but ignores it in the final output.

### Two-Pass Verification Method

```mermaid
flowchart LR
    subgraph Evidence["Evidence Collection"]
        E["S0, S1, S2..."]
    end

    subgraph Pass1["Pass 1: Scrubbed"]
        P1["Replace identifiers<br/>with placeholders"]
        Q1["Evaluate claim"]
        R1{{"Confidence p0"}}
    end

    subgraph Pass2["Pass 2: Full"]
        P2["Use complete<br/>evidence"]
        Q2["Evaluate claim"]
        R2{{"Confidence p1"}}
    end

    subgraph Result["Analysis"]
        CMP["Compare p0 vs p1"]
    end

    E --> P1 --> Q1 --> R1 --> CMP
    E --> P2 --> Q2 --> R2 --> CMP

    style Pass1 fill:#fff3e0
    style Pass2 fill:#e8f5e9
```

### Decision Matrix

```mermaid
flowchart TD
    subgraph Matrix["Verification Outcomes"]
        A["Scrubbed FAIL + Full PASS"] --> V["✓ VERIFIED<br/>Evidence essential"]
        B["Scrubbed PASS + Full PASS"] --> S["⚠ SUSPICIOUS<br/>May be confabulating"]
        C["Both FAIL"] --> U["✗ UNSUPPORTED<br/>Gather more evidence"]
    end

    style V fill:#c8e6c9
    style S fill:#ffcc80
    style U fill:#ef9a9a
```

### Interpretation
| Scrubbed | Full | Status | Action |
|----------|------|--------|--------|
| FAIL | PASS | VERIFIED | Evidence essential, proceed |
| PASS | PASS | SUSPICIOUS | May be confabulating, add warning |
| FAIL | FAIL | UNSUPPORTED | STOP, gather more evidence |

## Knowledge Catalogs

### Required Catalogs
| Catalog | Purpose |
|---------|---------|
| `ddic-catalog.json` | Cached DDIC object definitions |
| `class-catalog.json` | Common class signatures |
| `api-catalog.json` | API/service definitions |
| `rap-catalog.json` | RAP behavior patterns |
| `released-apis.json` | C0/C1/C2 release contracts |

### Schema Files
| Schema | Purpose |
|--------|---------|
| `grounding-result-schema.json` | Standard verification output format |
| `mapping-spec-schema.json` | Mapping specification format |

## MCP Server Integration

```mermaid
flowchart LR
    subgraph Skills["Grounding Skills"]
        S1["ddic/cds/rap-grounding"]
        S2["class/function-grounding"]
        S3["mapping-grounding"]
    end

    subgraph MCP["MCP Servers"]
        SAP["sap-documentation<br/>search, fetch, sap_help_search"]
        ATL["atlassian<br/>getConfluencePage, searchCql"]
        DW["deepwiki<br/>ask_question, read_wiki"]
    end

    S1 --> SAP
    S2 --> SAP
    S2 --> DW
    S3 --> ATL

    style Skills fill:#e3f2fd
    style MCP fill:#e8f5e9
```

| Server | Purpose | Tools |
|--------|---------|-------|
| `sap-documentation` | SAP Help Portal | search, fetch, sap_help_search |
| `atlassian` | Confluence specs | getConfluencePage, searchConfluenceUsingCql |
| `deepwiki` | Reference repos | ask_question, read_wiki_contents |

## Implementation Checklist

### Phase 1: Enhance Existing Skills
- [ ] Update `sap-grounding` to coordinator pattern
- [ ] Add strawberry-verification skill
- [ ] Enhance grounding-verifier agent

### Phase 2: Add Specialized Skills
- [ ] ddic-grounding
- [ ] cds-grounding  
- [ ] rap-grounding
- [ ] class-grounding
- [ ] function-grounding
- [ ] api-grounding

### Phase 3: Add Remaining Skills
- [ ] enhancement-grounding
- [ ] message-grounding
- [ ] authorization-grounding
- [ ] mapping-grounding
- [ ] existence-grounding
- [ ] fiori-grounding

### Phase 4: Add Knowledge Catalogs
- [ ] ddic-catalog.json
- [ ] class-catalog.json
- [ ] api-catalog.json
- [ ] rap-catalog.json
- [ ] released-apis.json

## How to Access Full Implementation

```bash
# From cursor-agent-factory repo
git checkout sap-grounding-v1.0 -- patterns/skills/
git checkout sap-grounding-v1.0 -- knowledge/
git checkout sap-grounding-v1.0 -- docs/GROUNDING_STRATEGY.md

# Or view individual files
git show sap-grounding-v1.0:patterns/skills/sap-grounding.json
git show sap-grounding-v1.0:patterns/skills/ddic-grounding.json
```

## Grounding Result Format

```markdown
### Grounding Verification Report

**Verification ID:** {UUID}
**Timestamp:** {TIMESTAMP}
**Artifacts Analyzed:** {COUNT}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Artifacts | {COUNT} |
| Verified (HIGH) | {COUNT} |
| Verified (MEDIUM) | {COUNT} |
| Unverified | {COUNT} |
| Issues | {COUNT} |
| Strawberry Status | {PASSED/WARNING/FAILED} |

---

## RECOMMENDATION: {PROCEED|PROCEED_WITH_WARNINGS|STOP|ASK_USER}

**Reason:** {RECOMMENDATION_REASON}
```
