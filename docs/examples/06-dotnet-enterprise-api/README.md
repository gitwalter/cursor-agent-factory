# Example 06: .NET Enterprise API

Build a production-ready enterprise API with ASP.NET Core 8, Clean Architecture, Entity Framework Core, and CQRS patterns.

## What We're Building

An **Enterprise Product Catalog API** that provides:

- Clean Architecture with clear layer separation
- CQRS pattern with MediatR
- Entity Framework Core with SQL Server
- FluentValidation for input validation
- Comprehensive API documentation with Swagger
- Security best practices

## Target Users

- **Primary**: .NET/C# developers in enterprise environments
- **Secondary**: Architects designing microservices

## Success Criteria

- Full Clean Architecture compliance
- 90% test coverage on business logic
- Zero security vulnerabilities in OWASP scan

## Technology Stack

| Component | Technology |
|-----------|------------|
| Framework | ASP.NET Core 8+ |
| Language | C# 12 |
| ORM | Entity Framework Core 8 |
| Validation | FluentValidation |
| CQRS | MediatR |
| Testing | xUnit, NSubstitute, FluentAssertions |

## Factory Configuration Summary

| Layer | Configuration |
|-------|---------------|
| **Layer 0 (Axioms)** | Core (A1-A5) + A6 (Minimalism) |
| **Layer 1 (Purpose)** | Enterprise-grade API development |
| **Layer 2 (Principles)** | Default quality standards |
| **Layer 3 (Methodology)** | Agile Scrum, 2-week sprints |
| **Layer 4 (Technical)** | csharp-dotnet blueprint |

## Depth Level

**Standard** - Configures all layers with Agile Scrum methodology.

## Time to Complete

Following this walkthrough takes approximately **20-25 minutes**.

## Prerequisites

Before starting, ensure you have:

1. Cursor IDE installed
2. The cursor-agent-factory project opened in Cursor
3. .NET 8 SDK installed
4. SQL Server or SQL Server Express
5. Familiarity with C# and ASP.NET Core

## Next Steps

1. Open [WALKTHROUGH.md](WALKTHROUGH.md) to begin the step-by-step process
2. Compare your results with [expected-output/](expected-output/) when complete
3. Customize the Clean Architecture structure for your domain

## Related Examples

- [01 - REST API Service](../01-rest-api-service/) - Similar pattern in Python
- [07 - Kotlin Spring Microservice](../07-kotlin-spring-microservice/) - JVM alternative
