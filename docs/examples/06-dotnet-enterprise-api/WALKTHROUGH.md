# .NET Enterprise API - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for an enterprise-grade ASP.NET Core API with Clean Architecture.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for an enterprise .NET API with Clean Architecture
```

---

### Pre-Phase: Axiom Selection (Layer 0)

**Factory Prompt:**
> Every agent system needs foundational axioms. Core axioms (A1-A5) are always included.
> Would you like to add optional axioms?

**Your Response:**
```
Yes, add A6 (Minimalism)
```

**Rationale:** Enterprise systems benefit from minimalism to avoid over-engineering and maintain long-term maintainability.

**Selected Axioms:**

| ID | Axiom | Application |
|----|-------|-------------|
| A1 | Verifiability | All code traceable to requirements |
| A2 | User Primacy | API consumers' needs first |
| A3 | Transparency | Clear architecture boundaries |
| A4 | Non-Harm | Secure by design |
| A5 | Consistency | Uniform patterns across layers |
| A6 | Minimalism | No unnecessary complexity |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To accelerate enterprise API development with Clean Architecture patterns, ensuring maintainability and testability
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
.NET developers building enterprise APIs in a team of 4-8 engineers
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Achieve 90% test coverage on business logic while maintaining Clean Architecture compliance
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
Agile Scrum
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
> Sprint length?

**Your Response:**
```
2 weeks
```

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
product-catalog-api
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
Enterprise product catalog API with inventory management, pricing, and search capabilities
```

---

### Phase 2: Technology Stack

**Factory Prompt:**
> What is your primary programming language?

**Your Response:**
```
C#
```

---

**Factory Prompt:**
> What frameworks will you use?

**Your Response:**
```
ASP.NET Core 8, Entity Framework Core, MediatR, FluentValidation
```

---

**Factory Prompt:**
> I found a matching blueprint: csharp-dotnet. Would you like to use it?

**Your Response:**
```
Yes
```

---

**Factory Prompt:**
> What database will you use?

**Your Response:**
```
SQL Server for production, SQLite for development/testing
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
Azure DevOps work items and pull requests
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What patterns should the agent follow?

**Your Response:**
```
Clean Architecture, CQRS with MediatR, Repository pattern, Domain-Driven Design
```

---

### Phase 5: Agent & Skill Selection

**Factory Prompt:**
> Which agents should I include?

**Your Response:**
```
Code reviewer, test generator, documentation agent
```

---

**Factory Prompt:**
> Which skills should be available?

**Your Response:**
```
bugfix-workflow, feature-workflow, tdd, security-audit
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\product-catalog-api
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: product-catalog-api                                   ║
║ Blueprint: csharp-dotnet                                       ║
║ Depth: Standard                                                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: A6 (Minimalism)                                    ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Enterprise API with Clean Architecture              ║
║   Stakeholders: .NET developers (4-8)                          ║
║   Success: 90% test coverage, Clean Architecture compliance    ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Agile Scrum                                     ║
║   Sprint Length: 2 weeks                                       ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: C# 12, ASP.NET Core 8, EF Core, MediatR               ║
║   Agents: code-reviewer, test-generator, documentation-agent   ║
║   Skills: bugfix-workflow, feature-workflow, tdd, security     ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\product-catalog-api                        ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Generated Artifacts

```
product-catalog-api/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── test-generator.md
│   │   └── documentation-agent.md
│   └── skills/
│       ├── bugfix-workflow/
│       ├── feature-workflow/
│       ├── tdd/
│       └── security-audit/
├── knowledge/
│   ├── clean-architecture.json    # Layer patterns
│   ├── csharp-conventions.json    # C# naming
│   ├── efcore-patterns.json       # EF Core patterns
│   └── cqrs-patterns.json         # MediatR patterns
├── src/
│   ├── Api/                       # Presentation layer
│   │   ├── Controllers/
│   │   ├── Middleware/
│   │   └── Program.cs
│   ├── Application/               # Application layer
│   │   ├── Commands/
│   │   ├── Queries/
│   │   ├── DTOs/
│   │   └── Validators/
│   ├── Domain/                    # Domain layer
│   │   ├── Entities/
│   │   ├── ValueObjects/
│   │   └── Interfaces/
│   └── Infrastructure/            # Infrastructure layer
│       ├── Data/
│       ├── Repositories/
│       └── Services/
├── tests/
│   ├── Unit/
│   │   ├── Application/
│   │   └── Domain/
│   └── Integration/
│       └── Api/
├── workflows/
│   └── methodology.yaml
├── Solution.sln
├── .cursorrules
├── PURPOSE.md
└── README.md
```

---

## Clean Architecture Layers

### Domain Layer (Core)
- Entities and Value Objects
- Domain interfaces
- No external dependencies

```csharp
// Domain/Entities/Product.cs
public class Product : BaseEntity
{
    public string Name { get; private set; }
    public Money Price { get; private set; }
    public ProductCategory Category { get; private set; }
    
    public void UpdatePrice(Money newPrice)
    {
        if (newPrice.Amount <= 0)
            throw new DomainException("Price must be positive");
        Price = newPrice;
    }
}
```

### Application Layer
- Commands and Queries (CQRS)
- DTOs and Validators
- Application services

```csharp
// Application/Commands/CreateProductCommand.cs
public record CreateProductCommand(
    string Name,
    decimal Price,
    int CategoryId
) : IRequest<ProductDto>;

public class CreateProductHandler : IRequestHandler<CreateProductCommand, ProductDto>
{
    private readonly IProductRepository _repository;
    
    public async Task<ProductDto> Handle(CreateProductCommand request, CancellationToken ct)
    {
        var product = new Product(request.Name, new Money(request.Price));
        await _repository.AddAsync(product, ct);
        return ProductDto.FromEntity(product);
    }
}
```

### Infrastructure Layer
- EF Core DbContext
- Repository implementations
- External service integrations

### API Layer
- Controllers
- Middleware
- Dependency injection setup

---

## Using the Generated System

### Implementing a Feature

**Example: Add Product Search**
```
Implement a search feature for products by name and category
```

The agent will:
1. Create Query in Application layer
2. Add handler with repository call
3. Create API endpoint
4. Generate xUnit tests

### Security Audit

**Example: Check for Vulnerabilities**
```
Run a security audit on the authentication endpoints
```

The security-audit skill will:
1. Check for common vulnerabilities
2. Verify authorization patterns
3. Review input validation
4. Report findings with remediation

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Clean Architecture rules
2. `PURPOSE.md` - Enterprise API mission
3. Layer structure - Domain → Application → Infrastructure → API

---

## Next Steps

1. Create the .NET solution with the generated structure
2. Add EF Core migrations
3. Use TDD skill for domain logic
4. Apply security-audit before deployment

**Congratulations!** You've generated a complete Cursor agent system for enterprise .NET development.
