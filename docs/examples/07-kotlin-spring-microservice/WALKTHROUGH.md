# Kotlin Spring Microservice - Complete Walkthrough

This walkthrough guides you through generating a complete Cursor agent system for building a reactive Kotlin Spring Boot microservice.

## Prerequisites

1. Open the `cursor-agent-factory` folder in Cursor IDE
2. Ensure the `.cursorrules` file is active
3. Start a new chat with the AI agent

---

## Phase-by-Phase Process

### Starting the Generation

Open a chat in Cursor and say:

```
Create a new agent system for a Kotlin Spring Boot reactive microservice
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

**Rationale:** Kotlin emphasizes concise, expressive code. A6 aligns with this philosophy.

**Selected Axioms:**

| ID | Axiom | Application |
|----|-------|-------------|
| A1 | Verifiability | All code testable with Kotest |
| A2 | User Primacy | API consumer needs first |
| A3 | Transparency | Clear reactive flows |
| A4 | Non-Harm | Secure endpoints |
| A5 | Consistency | Kotlin conventions throughout |
| A6 | Minimalism | Concise, idiomatic Kotlin |

---

### Phase 0: Purpose Definition (Layer 1)

**Factory Prompt:**
> In ONE sentence, why should this agent system exist?

**Your Response:**
```
To accelerate Kotlin microservice development with idiomatic patterns and reactive programming
```

---

**Factory Prompt:**
> Who are the primary users or beneficiaries?

**Your Response:**
```
Kotlin developers building reactive microservices (team of 2-4)
```

---

**Factory Prompt:**
> What is the single most important outcome?

**Your Response:**
```
Fully reactive, Kotlin-idiomatic microservices with 85% test coverage
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

---

**Factory Prompt:**
> Team size?

**Your Response:**
```
2-4 developers
```

---

**Factory Prompt:**
> WIP limits?

**Your Response:**
```
3 items per developer
```

---

### Phase 1: Project Context (Layer 4)

**Factory Prompt:**
> What is the name of your project?

**Your Response:**
```
inventory-service
```

---

**Factory Prompt:**
> Brief description?

**Your Response:**
```
Reactive product inventory microservice with Kotlin coroutines and R2DBC
```

---

### Phase 2: Technology Stack

**Factory Prompt:**
> What is your primary programming language?

**Your Response:**
```
Kotlin
```

---

**Factory Prompt:**
> What frameworks will you use?

**Your Response:**
```
Spring Boot 3, Spring WebFlux, Kotlin Coroutines
```

---

**Factory Prompt:**
> I found a matching blueprint: kotlin-spring. Would you like to use it?

**Your Response:**
```
Yes
```

---

**Factory Prompt:**
> What database will you use?

**Your Response:**
```
PostgreSQL with R2DBC for reactive access
```

---

### Phase 3: Workflow Integration

**Factory Prompt:**
> What triggers your development workflows?

**Your Response:**
```
GitHub issues and pull requests
```

---

### Phase 4: Knowledge Domain

**Factory Prompt:**
> What Kotlin patterns should the agent follow?

**Your Response:**
```
Coroutines, null safety, data classes, extension functions, sealed classes
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
bugfix-workflow, feature-workflow, tdd
```

---

### Specifying Output Directory

**Factory Prompt:**
> Where should I create the project?

**Your Response:**
```
C:\Projects\inventory-service
```

---

## Review Summary

```
╔════════════════════════════════════════════════════════════════╗
║                    GENERATION SUMMARY                          ║
╠════════════════════════════════════════════════════════════════╣
║ Project: inventory-service                                     ║
║ Blueprint: kotlin-spring                                       ║
║ Depth: Standard                                                ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 0 - AXIOMS                                               ║
║   Core: A1-A5                                                  ║
║   Optional: A6 (Minimalism)                                    ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 1 - PURPOSE                                              ║
║   Mission: Kotlin-idiomatic reactive microservices             ║
║   Stakeholders: Kotlin developers (2-4)                        ║
║   Success: 85% test coverage, fully reactive                   ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 3 - METHODOLOGY                                          ║
║   Methodology: Kanban                                          ║
║   WIP Limit: 3 per developer                                   ║
╠════════════════════════════════════════════════════════════════╣
║ LAYER 4 - TECHNICAL                                            ║
║   Stack: Kotlin 1.9, Spring Boot 3, WebFlux, R2DBC             ║
║   Agents: code-reviewer, test-generator                        ║
║   Skills: bugfix-workflow, feature-workflow, tdd               ║
╠════════════════════════════════════════════════════════════════╣
║ Output: C:\Projects\inventory-service                          ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Generated Artifacts

```
inventory-service/
├── .cursor/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   └── test-generator.md
│   └── skills/
│       ├── bugfix-workflow/
│       ├── feature-workflow/
│       └── tdd/
├── knowledge/
│   ├── kotlin-idioms.json        # Kotlin patterns
│   ├── spring-kotlin-patterns.json
│   ├── coroutines-patterns.json
│   └── kotest-patterns.json
├── src/
│   ├── main/
│   │   ├── kotlin/
│   │   │   ├── controller/       # REST controllers
│   │   │   ├── service/          # Business logic
│   │   │   ├── repository/       # R2DBC repositories
│   │   │   ├── model/            # Domain models
│   │   │   ├── dto/              # Data transfer objects
│   │   │   └── config/           # Configuration
│   │   └── resources/
│   │       └── application.yml
│   └── test/
│       └── kotlin/               # Kotest specs
├── workflows/
│   └── methodology.yaml
├── build.gradle.kts              # Gradle Kotlin DSL
├── settings.gradle.kts
├── .cursorrules
├── PURPOSE.md
└── README.md
```

---

## Key Kotlin Patterns

### Suspend Service

```kotlin
@Service
class ProductService(
    private val repository: ProductRepository
) {
    suspend fun findById(id: Long): Product? =
        repository.findById(id)
    
    suspend fun findAll(): Flow<Product> =
        repository.findAll()
    
    suspend fun create(dto: CreateProductDto): Product =
        repository.save(dto.toEntity())
}
```

### Flow Controller

```kotlin
@RestController
@RequestMapping("/api/products")
class ProductController(
    private val service: ProductService
) {
    @GetMapping
    fun getAll(): Flow<ProductDto> =
        service.findAll().map { it.toDto() }
    
    @GetMapping("/{id}")
    suspend fun getById(@PathVariable id: Long): ResponseEntity<ProductDto> =
        service.findById(id)
            ?.let { ResponseEntity.ok(it.toDto()) }
            ?: ResponseEntity.notFound().build()
    
    @PostMapping
    suspend fun create(@RequestBody dto: CreateProductDto): ProductDto =
        service.create(dto).toDto()
}
```

### Data Class DTO

```kotlin
data class ProductDto(
    val id: Long,
    val name: String,
    val price: BigDecimal,
    val quantity: Int
)

data class CreateProductDto(
    val name: String,
    val price: BigDecimal,
    val quantity: Int = 0
) {
    fun toEntity() = Product(
        name = name,
        price = price,
        quantity = quantity
    )
}
```

### Kotest Spec

```kotlin
class ProductServiceSpec : FunSpec({
    val repository = mockk<ProductRepository>()
    val service = ProductService(repository)
    
    test("findById returns product when exists") {
        val product = Product(1, "Widget", BigDecimal("9.99"), 100)
        coEvery { repository.findById(1) } returns product
        
        val result = service.findById(1)
        
        result shouldBe product
    }
    
    test("findById returns null when not found") {
        coEvery { repository.findById(999) } returns null
        
        val result = service.findById(999)
        
        result.shouldBeNull()
    }
})
```

---

## Verification

Compare your generated files with [expected-output/](expected-output/).

> **Note**: Reference files use `.example` extension to prevent interference with the factory.

1. `.cursorrules` - Should have Kotlin-specific rules
2. `PURPOSE.md` - Should reflect Kotlin-idiomatic mission
3. `build.gradle.kts` - Should use Kotlin DSL
4. Code patterns - Should use coroutines and Flow

---

## Next Steps

1. Initialize the Gradle project
2. Add Spring Boot starters for WebFlux and R2DBC
3. Implement domain models and repositories
4. Use TDD skill with Kotest

**Congratulations!** You've generated a complete Cursor agent system for Kotlin Spring Boot development.
