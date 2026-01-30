# Methodology Reference Guide

## Table of Contents

1. [Agile Scrum](#agile-scrum)
2. [Kanban](#kanban)
3. [SAFe (Scaled Agile Framework)](#safe-scaled-agile-framework)
4. [Waterfall](#waterfall)
5. [Lean/Six Sigma](#leansix-sigma)
6. [Extreme Programming (XP)](#extreme-programming-xp)
7. [Methodology Selection Guide](#methodology-selection-guide)

## Agile Scrum

### Overview

Scrum is an Agile framework for managing complex product development. It emphasizes iterative development, cross-functional teams, and regular inspection and adaptation.

### Key Concepts

- **Sprints**: Time-boxed iterations (typically 1-4 weeks)
- **Product Backlog**: Prioritized list of work items
- **Sprint Backlog**: Work selected for current sprint
- **Increment**: Potentially shippable product increment
- **Roles**: Product Owner, Scrum Master, Developers
- **Ceremonies**: Sprint Planning, Daily Standup, Sprint Review, Retrospective
- **Artifacts**: Product Backlog, Sprint Backlog, Increment

### Roles

| Role | Responsibilities |
|------|------------------|
| **Product Owner** | Backlog prioritization, stakeholder communication, value maximization |
| **Scrum Master** | Process facilitation, impediment removal, team coaching |
| **Developers** | Story implementation, estimation, quality assurance |

### Ceremonies

| Ceremony | Frequency | Duration | Purpose |
|----------|-----------|----------|---------|
| **Sprint Planning** | Sprint start | 2-4 hours | Select work, create sprint goal, plan tasks |
| **Daily Standup** | Daily | 15 minutes | Synchronize work, identify blockers |
| **Sprint Review** | Sprint end | 1-2 hours | Demo work, gather feedback |
| **Retrospective** | Sprint end | 1 hour | Reflect, identify improvements |

### Metrics

- **Velocity**: Story points completed per sprint
- **Burndown**: Sprint progress tracking
- **Sprint Goal Achievement**: Percentage of sprint goal met

### Official Resources

- **Scrum Guide**: [scrumguides.org](https://scrumguides.org/)
- **Scrum.org**: [scrum.org](https://www.scrum.org/)
- **Scrum Alliance**: [scrumalliance.org](https://www.scrumalliance.org/)

### When to Use Scrum

✅ **Good fit for**:
- Product development teams
- Teams needing structure and predictability
- Projects with changing requirements
- Teams of 3-9 developers

❌ **Not ideal for**:
- Very small teams (1-2 people)
- Support/maintenance work
- Highly regulated environments requiring formal gates
- Teams preferring continuous flow

## Kanban

### Overview

Kanban is a flow-based methodology focused on visualizing work, limiting work-in-progress (WIP), and managing flow. It emphasizes continuous delivery and evolutionary change.

### Key Concepts

- **Visual Board**: Columns representing workflow stages
- **WIP Limits**: Maximum items in each column
- **Pull System**: Work pulled when capacity available
- **Flow Metrics**: Lead time, cycle time, throughput
- **Classes of Service**: Different work types with SLAs
- **Continuous Improvement**: Evolutionary process changes

### Board Structure

| Column | Purpose | WIP Limit |
|--------|---------|-----------|
| **Backlog** | Unprioritized work | None |
| **Ready** | Ready to start | 5 |
| **In Progress** | Active work | 3 |
| **Review** | Code review/QA | 2 |
| **Done** | Completed work | None |

### Classes of Service

| Class | SLA | Priority | Use Case |
|-------|-----|----------|----------|
| **Expedite** | 1 day | Highest | Critical bugs, urgent requests |
| **Standard** | 5 days | Normal | Regular features, normal priority |
| **Fixed Date** | By date | Medium | Date-committed deliverables |
| **Intangible** | None | Low | Research, improvements |

### Ceremonies

| Ceremony | Frequency | Duration | Purpose |
|----------|-----------|----------|---------|
| **Daily Standup** | Daily | 15 minutes | Walk board, identify blockers |
| **Replenishment** | As needed | 30 minutes | Select new work for Ready |
| **Service Delivery Review** | Bi-weekly | 1 hour | Review flow metrics, SLA performance |
| **Operations Review** | Monthly | 2 hours | Analyze bottlenecks, improve process |

### Metrics

- **Lead Time**: Time from commitment to delivery
- **Cycle Time**: Time from start to completion
- **Throughput**: Items completed per time period
- **WIP**: Work in progress at any time

### Official Resources

- **Kanban University**: [kanban.university](https://kanban.university/)
- **Kanban Guide**: [kanban.university/kanban-guide](https://kanban.university/kanban-guide/)
- **David J. Anderson**: [djaa.com](https://djaa.com/)

### When to Use Kanban

✅ **Good fit for**:
- Support and maintenance teams
- Operations teams
- Teams preferring continuous flow
- Work with unpredictable arrival patterns
- Teams wanting minimal process overhead

❌ **Not ideal for**:
- Teams needing sprint structure
- Projects requiring formal planning cycles
- Teams new to Agile (may need more structure)

## SAFe (Scaled Agile Framework)

### Overview

SAFe is a framework for scaling Agile practices across large organizations. It provides structure for coordinating multiple Agile teams while maintaining alignment and quality.

### Key Concepts

- **Agile Release Train (ART)**: 5-12 teams working together
- **Program Increment (PI)**: 8-12 week planning cycle
- **PI Planning**: 2-day planning event for entire ART
- **System Demo**: Integrated demo of all teams' work
- **Inspect & Adapt**: PI retrospective and problem-solving workshop
- **Roles**: Product Management, System Architect, Release Train Engineer

### Levels

| Level | Focus | Duration |
|-------|-------|----------|
| **Team** | Sprint execution | 1-4 weeks |
| **Program** | ART coordination | 8-12 weeks (PI) |
| **Large Solution** | Multiple ARTs | 8-12 weeks |
| **Portfolio** | Strategic themes | Quarterly/Annually |

### Ceremonies

| Ceremony | Frequency | Duration | Participants |
|----------|-----------|----------|-------------|
| **PI Planning** | PI start | 2 days | Entire ART |
| **System Demo** | End of sprint | 1-2 hours | ART + stakeholders |
| **Inspect & Adapt** | PI end | 4 hours | Entire ART |
| **Scrum of Scrums** | Daily | 15 minutes | Team representatives |

### Metrics

- **PI Objectives**: Business value delivered
- **Velocity**: Team and ART velocity
- **Predictability**: Planned vs. actual delivery
- **Quality**: Defect rate, test coverage

### Official Resources

- **SAFe Website**: [scaledagileframework.com](https://scaledagileframework.com/)
- **SAFe Community**: [scaledagile.com](https://scaledagile.com/)
- **SAFe Knowledge Base**: [scaledagileframework.com/knowledge-base](https://scaledagileframework.com/knowledge-base/)

### When to Use SAFe

✅ **Good fit for**:
- Large organizations (100+ people)
- Multiple teams needing coordination
- Complex products requiring integration
- Organizations wanting structured scaling
- Enterprise environments

❌ **Not ideal for**:
- Small teams (< 20 people)
- Simple products
- Teams preferring lightweight frameworks
- Organizations new to Agile

## Waterfall

### Overview

Waterfall is a sequential project management methodology with distinct phases. Each phase must be completed before moving to the next, with formal gates and approvals.

### Key Concepts

- **Sequential Phases**: Requirements → Design → Implementation → Testing → Deployment
- **Formal Gates**: Approval required to proceed
- **Documentation**: Comprehensive documentation at each phase
- **Change Control**: Formal change management process
- **Milestones**: Major deliverables marking phase completion

### Phases

| Phase | Activities | Deliverables |
|-------|-----------|-------------|
| **Requirements** | Gather and document requirements | Requirements specification |
| **Design** | System and detailed design | Design documents |
| **Implementation** | Code development | Working software |
| **Testing** | System and user acceptance testing | Test reports, bug fixes |
| **Deployment** | Release to production | Deployed system |
| **Maintenance** | Ongoing support | Updates, patches |

### Ceremonies

| Ceremony | Frequency | Purpose |
|----------|-----------|---------|
| **Requirements Review** | Phase gate | Approve requirements |
| **Design Review** | Phase gate | Approve design |
| **Code Review** | During implementation | Quality assurance |
| **Test Review** | Phase gate | Approve for deployment |
| **Go/No-Go Meeting** | Before deployment | Final approval |

### Metrics

- **Milestone Completion**: On-time delivery percentage
- **Gate Reviews**: Approval rate
- **Defect Rate**: Defects found per phase
- **Schedule Variance**: Planned vs. actual timeline

### Official Resources

- **PMI (Project Management Institute)**: [pmi.org](https://www.pmi.org/)
- **PMBOK Guide**: [pmi.org/pmbok-guide-standards](https://www.pmi.org/pmbok-guide-standards)
- **IEEE Software Engineering**: [ieee.org](https://www.ieee.org/)

### When to Use Waterfall

✅ **Good fit for**:
- Projects with fixed, well-understood requirements
- Regulated industries (healthcare, finance, aerospace)
- Projects requiring formal documentation
- Teams with clear phase expertise
- Projects with fixed deadlines and budgets

❌ **Not ideal for**:
- Projects with changing requirements
- Software products needing rapid iteration
- Teams preferring Agile approaches
- Uncertain or exploratory projects

## Lean/Six Sigma

### Overview

Lean focuses on eliminating waste and maximizing value, while Six Sigma focuses on reducing variation and defects. Combined, they provide a data-driven approach to process improvement.

### Key Concepts

- **Waste Elimination**: Remove non-value-adding activities
- **Value Stream Mapping**: Visualize end-to-end process
- **Continuous Improvement**: Kaizen mindset
- **Defect Reduction**: Target < 3.4 defects per million
- **Process Metrics**: Measure and improve systematically
- **DMAIC**: Define, Measure, Analyze, Improve, Control

### DMAIC Process

| Phase | Activities | Tools |
|-------|-----------|-------|
| **Define** | Problem statement, scope, goals | SIPOC, stakeholder analysis |
| **Measure** | Baseline metrics, data collection | Process mapping, data collection |
| **Analyze** | Root cause analysis | Fishbone, Pareto, statistical analysis |
| **Improve** | Solution design and testing | Brainstorming, pilot testing |
| **Control** | Standardize, monitor | Control charts, documentation |

### Types of Waste (7 Wastes)

1. **Overproduction**: Producing more than needed
2. **Waiting**: Idle time between steps
3. **Transport**: Unnecessary movement
4. **Over-processing**: More work than necessary
5. **Inventory**: Excess work in progress
6. **Motion**: Unnecessary movement of people
7. **Defects**: Rework and corrections

### Metrics

- **Defect Rate**: Defects per million opportunities (DPMO)
- **Cycle Time**: Time to complete process
- **First Pass Yield**: Percentage completed correctly first time
- **Process Capability**: Process performance vs. requirements

### Official Resources

- **Lean Enterprise Institute**: [lean.org](https://www.lean.org/)
- **ASQ (American Society for Quality)**: [asq.org](https://asq.org/)
- **Six Sigma Institute**: [sixsigma-institute.org](https://www.sixsigma-institute.org/)

### When to Use Lean/Six Sigma

✅ **Good fit for**:
- Process improvement initiatives
- Manufacturing and operations
- Quality-focused organizations
- Teams wanting data-driven improvement
- Reducing defects and waste

❌ **Not ideal for**:
- Rapid product development
- Teams preferring Agile approaches
- Projects needing flexibility
- Early-stage products

## Extreme Programming (XP)

### Overview

Extreme Programming (XP) is an Agile methodology emphasizing engineering practices, technical excellence, and rapid feedback. It focuses on high-quality code and frequent releases.

### Key Concepts

- **Engineering Practices**: Test-driven development, pair programming, continuous integration
- **Short Iterations**: 1-2 week iterations
- **Customer Collaboration**: On-site customer or proxy
- **Simple Design**: YAGNI (You Aren't Gonna Need It)
- **Refactoring**: Continuous code improvement
- **Collective Ownership**: Anyone can modify any code

### Core Practices

| Practice | Description |
|----------|-------------|
| **Test-Driven Development (TDD)** | Write tests before code |
| **Pair Programming** | Two developers work together |
| **Continuous Integration** | Integrate code frequently |
| **Refactoring** | Improve code structure |
| **Simple Design** | Simplest solution that works |
| **Collective Code Ownership** | Anyone can change any code |
| **Coding Standards** | Consistent style |
| **Sustainable Pace** | 40-hour weeks |

### Roles

| Role | Responsibilities |
|------|------------------|
| **Customer** | Defines requirements, prioritizes features |
| **Developer** | Implements features, writes tests |
| **Coach** | Facilitates process, removes impediments |
| **Tracker** | Monitors progress, identifies risks |

### Ceremonies

| Ceremony | Frequency | Duration | Purpose |
|----------|-----------|----------|---------|
| **Planning Game** | Iteration start | 1-2 hours | Select features, estimate |
| **Standup** | Daily | 15 minutes | Synchronize, identify blockers |
| **Iteration Demo** | Iteration end | 1 hour | Show completed work |
| **Retrospective** | Iteration end | 1 hour | Reflect and improve |

### Metrics

- **Velocity**: Story points per iteration
- **Test Coverage**: Percentage of code covered by tests
- **Build Success Rate**: Percentage of successful builds
- **Defect Rate**: Defects found per iteration

### Official Resources

- **Extreme Programming**: [extremeprogramming.org](https://extremeprogramming.org/)
- **Ron Jeffries**: [ronjeffries.com](https://ronjeffries.com/)
- **XP Community**: [xprogramming.com](https://xprogramming.com/)

### When to Use XP

✅ **Good fit for**:
- Teams emphasizing technical excellence
- Projects requiring high quality
- Small, co-located teams
- Projects with changing requirements
- Teams comfortable with pair programming

❌ **Not ideal for**:
- Teams uncomfortable with pair programming
- Distributed teams (though possible)
- Projects requiring extensive documentation
- Teams preferring less intensive practices

## Methodology Selection Guide

### Decision Matrix

| Factor | Scrum | Kanban | SAFe | Waterfall | Lean/Six Sigma | XP |
|--------|-------|--------|------|-----------|----------------|-----|
| **Team Size** | 3-9 | Any | 50+ | Any | Any | 2-10 |
| **Requirements Stability** | Changing | Changing | Changing | Fixed | Varies | Changing |
| **Delivery Frequency** | Sprint-based | Continuous | PI-based | Phase-based | Continuous | Iteration-based |
| **Documentation** | Minimal | Minimal | Moderate | Extensive | Moderate | Minimal |
| **Structure** | High | Low | Very High | Very High | Moderate | Moderate |
| **Best For** | Product dev | Support/Ops | Large orgs | Regulated | Process improvement | Technical excellence |

### Selection Questions

1. **What is your team size?**
   - 1-3: Kanban or XP
   - 4-9: Scrum or XP
   - 10-50: Scrum or SAFe (Team level)
   - 50+: SAFe

2. **How stable are your requirements?**
   - Changing frequently: Scrum, Kanban, XP
   - Mostly stable: Waterfall, Lean/Six Sigma
   - Mix: Hybrid approach

3. **What is your primary focus?**
   - Product development: Scrum
   - Support/maintenance: Kanban
   - Process improvement: Lean/Six Sigma
   - Technical excellence: XP
   - Large-scale coordination: SAFe
   - Compliance/regulation: Waterfall

4. **What is your delivery cadence?**
   - Weekly: Kanban, XP
   - Bi-weekly: Scrum
   - Monthly: SAFe
   - Per phase: Waterfall

5. **What is your organizational context?**
   - Startup: Scrum, Kanban, XP
   - Enterprise: SAFe, Waterfall
   - Operations: Kanban, Lean/Six Sigma

### Hybrid Approaches

Many teams combine methodologies:

- **Scrumban**: Scrum structure with Kanban flow
- **SAFe + Scrum**: SAFe framework with Scrum teams
- **Lean + Agile**: Lean principles with Agile practices
- **XP + Scrum**: XP practices within Scrum framework

### Migration Paths

**From Waterfall to Agile**:
1. Start with Scrum (more structure)
2. Gradually adopt XP practices
3. Consider Kanban for support work

**From Scrum to Kanban**:
1. Remove sprint boundaries
2. Implement WIP limits
3. Focus on flow metrics

**Scaling Scrum**:
1. Start with Scrum
2. Add SAFe elements as needed
3. Coordinate multiple Scrum teams

---

*For implementation details, see [USER_GUIDE.md](./USER_GUIDE.md)*  
*For metrics details, see [METRICS_REFERENCE.md](./METRICS_REFERENCE.md)*
