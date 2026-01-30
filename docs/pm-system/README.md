# PM System Documentation

## What is the PM System?

The PM (Project Management) System is an integrated project management solution for Cursor Agent Factory that enhances development workflows without burdening teams. It provides:

- **Multi-backend support**: Integrate with Jira, Linear, GitHub Projects, Azure DevOps, or use local tracking
- **Methodology flexibility**: Support for Agile Scrum, Kanban, SAFe, Waterfall, Lean/Six Sigma, XP, and custom methodologies
- **AI-powered agents**: Specialized agents for backlog management, sprint facilitation, task tracking, and reporting
- **Automated metrics**: Track velocity, burndown, cycle time, throughput, and team health indicators
- **Workflow integration**: Seamlessly connect PM activities with your development workflows

The system is grounded in **Axiom 0: Love and Trust** - project management should enhance development, not burden it.

## Quick Start Guide

### Step 1: Choose Your Setup Approach

You can configure the PM system in two ways:

**Option A: Questionnaire** (Quick setup)
- Answer a series of questions about your team and preferences
- System generates configuration automatically
- Best for: Teams wanting fast setup

**Option B: Workshop** (Collaborative setup)
- Participate in team workshops to design your PM system
- Aligns with team values and vision
- Best for: Teams wanting deep alignment

### Step 2: Select Backend

Choose your PM backend:

- **Jira**: Enterprise-grade, powerful, extensive integrations
- **Linear**: Fast, developer-friendly, beautiful UI
- **GitHub Projects**: Native GitHub integration, simple, free
- **Azure DevOps**: Full Microsoft ecosystem integration
- **Local**: No external dependencies, full control

### Step 3: Choose Methodology

Select your development methodology:

- **Agile Scrum**: Sprint-based iterations with defined ceremonies
- **Kanban**: Continuous flow with WIP limits
- **SAFe**: Scaled Agile Framework for large organizations
- **Waterfall**: Sequential phases with formal gates
- **Lean/Six Sigma**: Process improvement focus
- **XP**: Extreme Programming practices
- **Custom**: Mix elements from multiple methodologies

### Step 4: Configure Team Settings

Provide team-specific information:

- Team size (1-3, 4-6, 7-10, 10+)
- Work style (remote, hybrid, in-office)
- PM experience level
- Priority values (speed, quality, visibility, flexibility, etc.)

### Step 5: Start Using

Once configured, you can:

- Create stories and epics
- Plan sprints
- Run daily standups
- Track metrics and generate reports
- Use AI agents for PM tasks

## Feature Overview

### Agents

| Agent | Purpose | Key Capabilities |
|-------|---------|-----------------|
| **Product Owner** | Backlog management | Create stories, prioritize backlog, accept work, generate release notes |
| **Sprint Master** | Ceremony facilitation | Sprint planning, daily standups, retrospectives, sprint transitions |
| **Task Manager** | Work decomposition | Break down stories, extract TODOs, update status, link items |
| **Reporting Agent** | Metrics and insights | Burndown charts, velocity reports, health indicators, dashboards |

### Backends

| Backend | Best For | Key Features |
|---------|----------|--------------|
| **Jira** | Enterprise teams, complex projects | Custom workflows, extensive integrations, powerful reporting |
| **Linear** | Software teams, startups | Fast UI, developer-friendly, great keyboard shortcuts |
| **GitHub Projects** | Open source, GitHub-heavy teams | Native integration, simple, free for public repos |
| **Azure DevOps** | Microsoft shops | Full ALM features, Azure integration |
| **Local** | Small teams, early projects | No dependencies, full control, simple |

### Methodologies

| Methodology | Structure | Key Metrics |
|-------------|-----------|-------------|
| **Agile Scrum** | Sprint-based (1-4 weeks) | Velocity, burndown, sprint completion |
| **Kanban** | Continuous flow | Lead time, cycle time, throughput, WIP |
| **SAFe** | Scaled sprints, program increments | PI objectives, velocity, predictability |
| **Waterfall** | Sequential phases | Milestone completion, gate reviews |
| **Lean/Six Sigma** | Process improvement | Defect rate, cycle time, waste reduction |
| **XP** | Engineering practices | Velocity, test coverage, pair programming |

### Metrics

The system tracks comprehensive metrics across five categories:

- **Velocity**: Story points, velocity trend, completion rate
- **Flow**: Lead time, cycle time, throughput, WIP
- **Quality**: Bug ratio, rework rate, escaped defects
- **Predictive**: Sprint forecast, release prediction, risk score
- **Health**: Blocker frequency, stale items, assignment balance

See [METRICS_REFERENCE.md](./METRICS_REFERENCE.md) for detailed formulas and interpretation guides.

## Documentation Structure

- **[USER_GUIDE.md](./USER_GUIDE.md)**: Comprehensive user guide with setup, daily usage, and troubleshooting
- **[METHODOLOGY_REFERENCE.md](./METHODOLOGY_REFERENCE.md)**: Detailed methodology guide with official links and selection guide
- **[METRICS_REFERENCE.md](./METRICS_REFERENCE.md)**: Complete metrics documentation with formulas and best practices

## Common Commands

### Configuration
```bash
# Configure PM system interactively
python cli/factory_cli.py --configure-pm

# Test backend connection
python cli/factory_cli.py --test-pm-connection

# Validate configuration
python cli/factory_cli.py --validate-pm-config pm-config.json
```

### Daily Usage
```
# Create a story
"Create story for user login"

# Plan sprint
"Plan sprint for next 2 weeks"

# Run standup
"Run standup"

# Show metrics
"Show burndown for Sprint 12"
"Velocity report"
"Team health check"
```

## Philosophy

> Project management should enhance development, not burden it.

The PM system is designed with these principles:

1. **Love for the team**: PM configuration flows from care for team members and their process
2. **Trust in process**: Trust teams to choose what works for them
3. **Enhance, don't burden**: If PM feels like overhead, simplify it
4. **Methodology-aware**: Adapt to team's chosen methodology
5. **Data-driven**: Provide metrics for informed decisions
6. **Reversible**: Teams can change their mind and reconfigure

## Getting Help

- Review the [USER_GUIDE.md](./USER_GUIDE.md) for detailed usage instructions
- Check [METHODOLOGY_REFERENCE.md](./METHODOLOGY_REFERENCE.md) for methodology selection guidance
- See [METRICS_REFERENCE.md](./METRICS_REFERENCE.md) for metrics interpretation
- Ask questions in your Cursor chat - the PM agents are ready to help!

## Next Steps

1. Read the [USER_GUIDE.md](./USER_GUIDE.md) for comprehensive setup instructions
2. Review [METHODOLOGY_REFERENCE.md](./METHODOLOGY_REFERENCE.md) to choose your methodology
3. Configure your PM system using the quick start steps above
4. Start using PM agents for daily project management tasks

---

*PM System v1.0.0 | Grounded in Axiom 0: Love and Trust*
