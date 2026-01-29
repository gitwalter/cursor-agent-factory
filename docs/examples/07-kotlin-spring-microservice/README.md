# Example 07: Kotlin Spring Microservice

Build a modern reactive microservice with Kotlin, Spring Boot 3, WebFlux, and coroutines.

## What We're Building

A **Product Inventory Microservice** that provides:

- Reactive REST API with Spring WebFlux
- Kotlin coroutines for async operations
- R2DBC for non-blocking database access
- Kotlin-idiomatic code patterns
- Kotest for testing with descriptive specs

## Target Users

- **Primary**: Kotlin developers building microservices
- **Secondary**: Java developers transitioning to Kotlin

## Success Criteria

- Fully reactive (non-blocking) implementation
- 100% Kotlin idiomatic code (no Java patterns)
- 85% test coverage with Kotest

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Kotlin 1.9+ |
| Framework | Spring Boot 3.2+ |
| Web | Spring WebFlux |
| Database | PostgreSQL with R2DBC |
| Async | Kotlin Coroutines |
| Testing | Kotest, MockK |
| Build | Gradle Kotlin DSL |

## Factory Configuration Summary

| Layer | Configuration |
|-------|---------------|
| **Layer 0 (Axioms)** | Core (A1-A5) + A6 (Minimalism) |
| **Layer 1 (Purpose)** | Kotlin-idiomatic microservices |
| **Layer 2 (Principles)** | Kotlin coding standards |
| **Layer 3 (Methodology)** | Kanban, continuous flow |
| **Layer 4 (Technical)** | kotlin-spring blueprint |

## Depth Level

**Standard** - Configures all layers with Kanban for continuous delivery.

## Key Kotlin Features

- **Null Safety**: Leveraged throughout the codebase
- **Data Classes**: For DTOs and value objects
- **Coroutines**: For all async operations
- **Extension Functions**: For utility methods
- **Sealed Classes**: For result types

## Time to Complete

Following this walkthrough takes approximately **20 minutes**.

## Prerequisites

Before starting, ensure you have:

1. Cursor IDE installed
2. The cursor-agent-factory project opened in Cursor
3. JDK 21+ installed
4. Gradle 8+ installed
5. Basic familiarity with Kotlin and Spring Boot

## Next Steps

1. Open [WALKTHROUGH.md](WALKTHROUGH.md) to begin the step-by-step process
2. Compare your results with [expected-output/](expected-output/) when complete
3. Customize the microservice for your domain

## Related Examples

- [01 - REST API Service](../01-rest-api-service/) - Similar pattern in Python
- [06 - .NET Enterprise API](../06-dotnet-enterprise-api/) - Enterprise patterns in .NET
