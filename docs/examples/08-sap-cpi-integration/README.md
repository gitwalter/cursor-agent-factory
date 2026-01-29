# Example 08: SAP CPI Integration

Build an S/4HANA to third-party REST integration using SAP Cloud Platform Integration with Groovy scripts, proper error handling, and testing.

## What We're Building

An **Order Replication Integration** that provides:

- Receive Sales Orders from S/4HANA via IDoc
- Transform to third-party JSON format using Groovy
- Call external REST API with OAuth authentication
- Handle errors with proper logging and alerting
- Unit tests for all Groovy scripts

## Target Users

- **Primary**: SAP CPI/PI integration developers
- **Secondary**: SAP consultants implementing integrations

## Success Criteria

- Zero unhandled exceptions in production
- All Groovy scripts have unit tests
- Complete logging for troubleshooting

## Technology Stack

| Component | Technology |
|-----------|------------|
| Platform | SAP Integration Suite / CPI |
| Scripting | Groovy |
| Testing | Spock Framework |
| Source | S/4HANA (IDoc) |
| Target | REST API (JSON) |
| Auth | OAuth 2.0 Client Credentials |

## Factory Configuration Summary

| Layer | Configuration |
|-------|---------------|
| **Layer 0 (Axioms)** | Core (A1-A5) + A6 (Minimalism) + A7 (Reversibility) |
| **Layer 1 (Purpose)** | Reliable SAP integrations |
| **Layer 2 (Principles)** | CPI best practices |
| **Layer 3 (Methodology)** | Kanban (interrupt-driven) |
| **Layer 4 (Technical)** | sap-cpi-pi blueprint |

## Depth Level

**Standard** - Configures all layers with Kanban for integration support work.

## Key Features

- **Groovy Scripting**: Message transformations with best practices
- **Error Handling**: Exception subprocess with alerting
- **Testing**: Spock-based unit tests for scripts
- **SAP Docs Grounding**: Verify code against official documentation

## Time to Complete

Following this walkthrough takes approximately **25 minutes**.

## Prerequisites

Before starting, ensure you have:

1. Cursor IDE installed
2. The cursor-agent-factory project opened in Cursor
3. Familiarity with SAP CPI/PI concepts
4. Groovy/Java basics

## Next Steps

1. Open [WALKTHROUGH.md](WALKTHROUGH.md) to begin the step-by-step process
2. Compare your results with [expected-output/](expected-output/) when complete
3. Customize for your integration scenario

## Related Examples

- [05 - SAP Fiori Integration](../05-sap-fiori-integration/) - SAP ABAP/RAP development
- [01 - REST API Service](../01-rest-api-service/) - Python API patterns
