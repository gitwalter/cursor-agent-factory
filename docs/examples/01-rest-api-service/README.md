# Example 01: REST API Service

Build a complete user management REST API with Python FastAPI, including authentication, CRUD operations, and Jira integration for workflow tracking.

## What We're Building

A **User Management API** that provides:

- User registration and authentication (JWT)
- CRUD operations for user profiles
- Role-based access control
- Integration with Jira for bug tracking workflows
- Comprehensive test coverage with pytest

## Target Users

- **Primary**: Backend developers on a small engineering team (4-6 people)
- **Secondary**: DevOps engineers deploying and monitoring the API

## Success Criteria

- Reduce time from API design to working implementation by 50%
- Achieve 80% test coverage on all endpoints
- Zero critical security vulnerabilities in OWASP scan

## Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Framework | FastAPI 0.100+ |
| ORM | SQLAlchemy 2.0+ |
| Validation | Pydantic 2.0+ |
| Database | PostgreSQL (prod), SQLite (dev) |
| Testing | pytest, pytest-asyncio |
| Linting | ruff |

## Factory Configuration Summary

| Layer | Configuration |
|-------|---------------|
| **Layer 0 (Axioms)** | Core (A1-A5) + A6 (Minimalism) |
| **Layer 1 (Purpose)** | Accelerate API development with quality |
| **Layer 2 (Principles)** | Default quality standards |
| **Layer 3 (Methodology)** | Agile Scrum, 2-week sprints |
| **Layer 4 (Technical)** | python-fastapi blueprint |

## Depth Level

**Standard** - Configures all layers with methodology selection, uses sensible defaults for enforcement and practices.

## Time to Complete

Following this walkthrough takes approximately **15-20 minutes**.

## Prerequisites

Before starting, ensure you have:

1. Cursor IDE installed
2. The cursor-agent-factory project opened in Cursor
3. Python 3.10+ installed (Anaconda recommended)
4. Basic familiarity with FastAPI and REST APIs

## Next Steps

1. Open [WALKTHROUGH.md](WALKTHROUGH.md) to begin the step-by-step process
2. Compare your results with [expected-output/](expected-output/) when complete
3. Customize the generated system for your specific API requirements

## Related Examples

- [03 - RAG Chatbot Agent](../03-rag-chatbot-agent/) - If you want to add AI capabilities
- [06 - .NET Enterprise API](../06-dotnet-enterprise-api/) - Similar pattern in C#/.NET
