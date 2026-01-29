# SAP CPI Integration - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for SAP CPI/PI integration development with Groovy scripting.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for SAP CPI integration development with Groovy
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
- A6 (Minimalism): Keep scripts focused and simple
- A7 (Reversibility): Transport-based deployment enables rollback

**Selected Axioms:**

| ID | Axiom | Application |
|----|-------|-------------|
| A1 | Verifiability | All code tested with Spock |
| A2 | User Primacy | Business requirements first |
| A3 | Transparency | Clear logging for troubleshooting |
| A4 | Non-Harm | Proper error handling, no data loss |
| A5 | Consistency | CPI patterns throughout |
| A6 | Minimalism | Simple, focused scripts |
| A7 | Reversibility | Transport rollback capability |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To build reliable SAP integrations with proper error handling, monitoring, and maintainability
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
SAP integration developers and the business processes that depend on reliable data flow
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Zero unhandled exceptions with complete logging for rapid troubleshooting
```

---

### Phase 0.5: Depth Selection

**Factory Prompt:**
> How deep should we define the remaining layers?

**Your Response:**
```
B (Standard)
```

---

### Phases 0.6-0.7: Principles & Methodology (Layer 2-3)

**Factory Prompt:**
> What development methodology fits your team?

**Your Response:**
```
Kanban
```

**Rationale:** Integration support is often interrupt-driven with varying priorities.

---

**Factory Prompt:**
> Team size?

**Your Response:**
```
2-4 developers
```

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
order-replication-cpi
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
S/4HANA Sales Order replication to third-party system via REST API
```

---

### Phase 2: Technology Stack

**Factory Prompt:**
> What is your primary programming language?

**Your Response:**
```
Groovy
```

---

**Factory Prompt:**
> What frameworks will you use?

**Your Response:**
```
SAP CPI Groovy SDK, Spock for testing
```

---

**Factory Prompt:**
> I found a matching blueprint: sap-cpi-pi. Would you like to use it?

**Your Response:**
```
Yes
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
Jira tickets for integration issues and enhancements
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
> What patterns should the agent follow?

**Your Response:**
```
CPI Groovy patterns, iFlow error handling, message transformation best practices
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
groovy-scripting, error-handling, grounding, tdd
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\order-replication-cpi
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: order-replication-cpi                                 ║
║ Blueprint: sap-cpi-pi                                          ║
║ Depth: Standard                                                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: A6 (Minimalism), A7 (Reversibility)                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Reliable SAP integrations                           ║
║   Stakeholders: Integration developers, business processes     ║
║   Success: Zero unhandled exceptions                           ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Kanban                                          ║
║   WIP Limit: 3 per developer                                   ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: Groovy, SAP CPI, Spock                                ║
║   Agents: code-reviewer, test-generator                        ║
║   Skills: groovy-scripting, error-handling, grounding          ║
║   MCP: SAP Documentation                                       ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\order-replication-cpi                      ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Generated Artifacts

```
order-replication-cpi/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   └── test-generator.md
│   └── skills/
│       ├── groovy-scripting/
│       │   └── SKILL.md
│       ├── error-handling/
│       │   └── SKILL.md
│       ├── grounding/
│       │   └── SKILL.md
│       └── tdd/
│           └── SKILL.md
├── knowledge/
│   ├── groovy-patterns.json      # Groovy best practices
│   ├── iflow-patterns.json       # iFlow design patterns
│   └── cpi-error-handling.json   # Error handling patterns
├── src/
│   ├── main/groovy/
│   │   ├── scripts/              # Processing scripts
│   │   └── mappings/             # Transformation scripts
│   └── test/groovy/              # Spock tests
├── iflows/
│   └── OrderReplication/         # iFlow artifacts
├── docs/
│   └── interface-spec.md         # Interface documentation
├── workflows/
│   └── methodology.yaml
├── build.gradle                   # Gradle for testing
├── .cursorrules.example
└── PURPOSE.md.example
```

---

## Key Groovy Patterns

### Message Transformation

```groovy
import com.sap.gateway.ip.core.customdev.util.Message
import groovy.json.JsonBuilder

def Message processData(Message message) {
    def messageLog = messageLogFactory.getMessageLog(message)
    
    try {
        // Parse IDoc XML
        def body = message.getBody(String)
        def idoc = new XmlSlurper().parseText(body)
        
        // Transform to JSON
        def builder = new JsonBuilder()
        builder {
            orderId idoc.IDOC.E1EDK01.BELNR.text()
            customer idoc.IDOC.E1EDK01.KUNNR.text()
            items idoc.IDOC.E1EDP01.collect { item ->
                [
                    material: item.MATNR.text(),
                    quantity: item.MENGE.text().toBigDecimal()
                ]
            }
        }
        
        message.setBody(builder.toString())
        
    } catch (Exception e) {
        message.setProperty('ErrorMessage', e.message)
        throw e
    }
    
    return message
}
```

### Error Handling

```groovy
def Message handleError(Message message) {
    def messageLog = messageLogFactory.getMessageLog(message)
    
    // Get error details
    def errorMessage = message.getProperty('CamelExceptionCaught')?.message ?: 'Unknown error'
    def errorStep = message.getProperty('SAP_ErrorModelStepID') ?: 'Unknown'
    
    // Log error details
    messageLog.addAttachmentAsString('ErrorDetails', """
        Error: ${errorMessage}
        Step: ${errorStep}
        Timestamp: ${new Date()}
        Message ID: ${message.getProperty('SAP_MessageProcessingLogID')}
    """.stripIndent(), 'text/plain')
    
    // Set properties for alerting
    message.setProperty('AlertRequired', 'true')
    message.setProperty('AlertSeverity', 'HIGH')
    
    return message
}
```

---

## Using the Generated System

### Creating a New Script

**Example: Create Mapping Script**
```
Create a Groovy script to map IDoc ORDERS05 to JSON format
```

The agent will:
1. Query knowledge/groovy-patterns.json for patterns
2. Use SAP Documentation MCP to verify IDoc structure
3. Generate script with proper error handling
4. Include logging for debugging

### Testing Scripts

**Example: Generate Tests**
```
Generate Spock tests for the order mapping script
```

The test-generator will:
1. Create test class with mock CPI environment
2. Add test cases for valid input
3. Add test cases for null handling
4. Add test cases for error conditions

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Should have CPI-specific rules and logging patterns
2. `PURPOSE.md` - Should reflect integration reliability mission
3. `knowledge/` - Should contain Groovy and iFlow patterns

---

## Next Steps

1. Set up the Gradle project for local testing
2. Import scripts into CPI tenant
3. Configure iFlow with proper error handling
4. Deploy and test with sample data

**Congratulations!** You've generated a complete Cursor agent system for SAP CPI integration development.
