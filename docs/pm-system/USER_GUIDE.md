# PM System User Guide

## Table of Contents

1. [Setup Process](#setup-process)
2. [Daily Usage Patterns](#daily-usage-patterns)
3. [Working with Agents](#working-with-agents)
4. [Common Commands](#common-commands)
5. [Troubleshooting](#troubleshooting)

## Setup Process

### Initial Configuration

The PM system can be configured through two approaches:

#### Approach 1: Questionnaire (Quick Setup)

For fast setup, answer a series of questions:

1. **PM System Interest**
   - Full PM system with backend integration
   - Minimal tracking without external backend
   - Skip PM configuration for now

2. **Backend Selection** (if full system selected)
   - Jira, Linear, GitHub Projects, Azure DevOps, or Local
   - Consider team size, existing tools, complexity tolerance

3. **Methodology Selection**
   - Agile Scrum, Kanban, SAFe, Waterfall, Lean/Six Sigma, XP, or Custom
   - Based on project type, team size, work style

4. **Team Configuration**
   - Team size, work style, PM experience, priority values

5. **Methodology-Specific Settings**
   - Sprint length (Scrum)
   - WIP limits (Kanban)
   - Exploration ratio (R&D)
   - Governance frequency (Enterprise)

#### Approach 2: Workshop (Collaborative Setup)

For team alignment, participate in workshops:

1. **Workshop 1: Vision Quest**
   - Define project vision and values
   - Inform PM methodology selection

2. **Workshop 2: Ethics Arena**
   - Establish team principles
   - Guide PM configuration decisions

3. **Workshop 3: Stack Safari**
   - Select technology stack
   - Configure PM backend and methodology

4. **Workshop 4: Agent Assembly**
   - Design PM agents
   - Configure workflows

5. **Workshop 5: Integration Celebration**
   - Finalize PM configuration
   - Test integrations

### Backend Configuration

#### Jira Setup

1. **Get Credentials**
   ```bash
   # Create API token at:
   # https://id.atlassian.com/manage-profile/security/api-tokens
   ```

2. **Configure Environment**
   ```bash
   # Copy template
   cp .env.pm.example .env.pm
   
   # Add credentials
   JIRA_API_TOKEN=your_token_here
   JIRA_PROJECT_KEY=PROJ
   JIRA_WORKSPACE=your-company.atlassian.net
   ```

3. **Test Connection**
   ```bash
   python cli/factory_cli.py --test-pm-connection
   ```

#### Linear Setup

1. **Get API Key**
   ```bash
   # Create API key at:
   # https://linear.app/settings/api
   ```

2. **Configure Environment**
   ```bash
   LINEAR_API_KEY=your_key_here
   LINEAR_TEAM_ID=your_team_id
   ```

#### GitHub Projects Setup

1. **Configure Repository**
   - PM system uses GitHub Issues and Projects
   - No additional credentials needed if using GitHub MCP

2. **Set Project ID**
   ```json
   {
     "backend": {
       "projectId": "your-project-number"
     }
   }
   ```

#### Local Setup

No external credentials needed. System uses local file storage:

```json
{
  "backend": {
    "type": "local",
    "storage": ".pm/local"
  }
}
```

### Methodology Configuration

#### Agile Scrum Configuration

```json
{
  "methodology": {
    "type": "agile-scrum",
    "configuration": {
      "sprintLength": "2_weeks",
      "dailyStandup": "10:00_AM",
      "sprintPlanning": "4_hours",
      "retrospective": "in_person"
    }
  }
}
```

#### Kanban Configuration

```json
{
  "methodology": {
    "type": "kanban",
    "configuration": {
      "wipLimits": {
        "ready": 5,
        "in_progress": 3,
        "review": 2,
        "testing": 2
      }
    }
  }
}
```

## Daily Usage Patterns

### Morning Routine

1. **Check Sprint Status**
   ```
   "Show burndown for current sprint"
   ```

2. **Review Blockers**
   ```
   "List blockers"
   ```

3. **Update Work Status**
   ```
   "Update PROJ-456 to In Progress"
   ```

### Sprint Planning

1. **Review Backlog**
   ```
   "Show prioritized backlog"
   ```

2. **Plan Sprint**
   ```
   "Plan sprint for next 2 weeks"
   ```

3. **Break Down Stories**
   ```
   "Break down story PROJ-456"
   ```

### Daily Standup

1. **Run Standup**
   ```
   "Run standup"
   ```

2. **Review Updates**
   - Agent fetches sprint status
   - Team members provide updates
   - Agent identifies blockers

3. **Track Action Items**
   - Agent creates action items
   - Links to work items
   - Tracks resolution

### Sprint Review

1. **Generate Sprint Report**
   ```
   "Sprint report for Sprint 12"
   ```

2. **Review Metrics**
   ```
   "Velocity report"
   "Team health check"
   ```

3. **Conduct Retrospective**
   ```
   "Run sprint retro"
   ```

### Backlog Management

1. **Create Stories**
   ```
   "Create story for user login"
   ```

2. **Prioritize Backlog**
   ```
   "Prioritize backlog"
   ```

3. **Refine Stories**
   ```
   "Refine story PROJ-456"
   ```

## Working with Agents

### Product Owner Agent

**Purpose**: Manages product backlog and requirements

**Triggers**:
- "create story", "add user story", "create epic"
- "prioritize backlog", "backlog grooming"
- "accept story", "story done"
- "release notes", "changelog"

**Example Interactions**:

```
User: Create a story for user login

Agent: I'll help you create a user login story. Let me gather the details:
1. What's the story title?
   User: User Login Authentication
2. As a [user type], I want to [action] so that [benefit]
   User: As a registered user, I want to log in with email and password so that I can access my account
3. What are the acceptance criteria?
   User: 
   - User can enter email and password
   - System validates credentials
   - User is redirected to dashboard on success
   - Error message shown on invalid credentials
4. Is this part of an epic?
   User: Yes, Authentication Epic
5. Story points (1-8)?
   User: 5

Agent: Story created: PROJ-456 - User Login Authentication
```

### Sprint Master Agent

**Purpose**: Facilitates Agile ceremonies

**Triggers**:
- "plan sprint", "sprint planning"
- "run standup", "daily standup"
- "retro", "retrospective"
- "close sprint", "end sprint"

**Example Interactions**:

```
User: Plan sprint for next 2 weeks

Agent: I'll facilitate sprint planning. Let me gather the details:
1. Sprint duration?
   User: 2 weeks
2. Team capacity (story points)?
   User: 40 story points
3. Previous sprint velocity?
   User: 38 points
4. Sprint goal?
   User: Complete authentication features

Agent: Sprint Plan Created:
Sprint: Sprint 12 - Authentication
Duration: Feb 1-14, 2026
Goal: Complete authentication features
Capacity: 40 story points

Selected Stories:
1. PROJ-456: User Login (5 pts)
2. PROJ-457: Email Verification (3 pts)
...
Total: 40 story points
```

### Task Manager Agent

**Purpose**: Breaks down work and tracks tasks

**Triggers**:
- "create task", "break down story"
- "update status", "mark done"
- "link items", "create dependency"
- "todo to issue", "extract todos"

**Example Interactions**:

```
User: Break down story PROJ-456

Agent: Breaking down story PROJ-456: User Login Authentication

Proposed Tasks:
1. Create login form component (frontend)
2. Implement login API endpoint (backend)
3. Add credential validation logic (backend)
4. Create session management (backend)
5. Implement redirect logic (frontend)
6. Add error handling and messages (frontend)
7. Write unit tests for login flow (testing)

Create these tasks?
User: Yes

Agent: Tasks created and linked to PROJ-456
```

### Reporting Agent

**Purpose**: Generates metrics and reports

**Triggers**:
- "show burndown", "burndown chart"
- "velocity report", "team velocity"
- "team health", "health check"
- "sprint report", "dashboard"

**Example Interactions**:

```
User: Show burndown for Sprint 12

Agent: Sprint 12 Burndown Chart
========================
Sprint: Authentication Features
Duration: Feb 1-14, 2026
Total Story Points: 40

Day    Ideal    Actual    Remaining
-----------------------------------
1      40       40        40
2      37       38        38
...
14     0        0         0

Status: On track
```

## Common Commands

### Story Management

| Command | Description | Example |
|---------|-------------|---------|
| Create story | Create new user story | "Create story for user login" |
| Create epic | Create epic for grouping | "Create epic for authentication" |
| Prioritize backlog | Reorder backlog items | "Prioritize backlog" |
| Refine story | Add details to story | "Refine story PROJ-456" |
| Accept story | Mark story as done | "Accept story PROJ-456" |

### Sprint Management

| Command | Description | Example |
|---------|-------------|---------|
| Plan sprint | Create new sprint plan | "Plan sprint for next 2 weeks" |
| Run standup | Facilitate daily standup | "Run standup" |
| Sprint retro | Conduct retrospective | "Run sprint retro" |
| Close sprint | End sprint and calculate metrics | "Close sprint SPRINT-12" |

### Task Management

| Command | Description | Example |
|---------|-------------|---------|
| Break down story | Decompose story into tasks | "Break down story PROJ-456" |
| Update status | Change task status | "Update PROJ-501 to In Progress" |
| Link items | Create dependencies | "Link PROJ-502 depends on PROJ-501" |
| Extract TODOs | Create issues from code TODOs | "Extract todos from codebase" |

### Reporting

| Command | Description | Example |
|---------|-------------|---------|
| Show burndown | Display burndown chart | "Show burndown for Sprint 12" |
| Velocity report | Show velocity metrics | "Velocity report" |
| Team health | Health indicators | "Team health check" |
| Sprint report | Comprehensive sprint report | "Sprint report for Sprint 12" |
| Generate dashboard | Create metrics dashboard | "Create metrics dashboard" |

## Troubleshooting

### Backend Connection Issues

**Problem**: Cannot connect to backend (Jira, Linear, etc.)

**Solutions**:
1. Verify credentials in `.env.pm`
2. Test connection:
   ```bash
   python cli/factory_cli.py --test-pm-connection
   ```
3. Check API token expiration
4. Verify project ID/workspace URL
5. Check network connectivity

**Common Errors**:
- `401 Unauthorized`: Invalid API token
- `404 Not Found`: Incorrect project ID or workspace URL
- `403 Forbidden`: Insufficient permissions

### Agent Not Responding

**Problem**: Agent doesn't activate when expected

**Solutions**:
1. Check trigger phrases match exactly
2. Verify agent is enabled in configuration
3. Review agent triggers in agent definition
4. Check methodology compatibility

**Example**:
```
# Sprint Master agent triggers:
- "plan sprint", "sprint planning", "start sprint"
- "run standup", "daily standup"
- "retro", "retrospective"
```

### Metrics Not Calculating

**Problem**: Metrics show zero or incorrect values

**Solutions**:
1. Verify sufficient historical data (minimum sprints/items)
2. Check work item status transitions
3. Verify date fields are populated
4. Review metric calculation requirements

**Minimum Requirements**:
- Velocity: 3+ sprints
- Cycle time: 10+ completed items
- Throughput: 4+ time periods

### Workflow State Issues

**Problem**: Cannot transition work item status

**Solutions**:
1. Verify workflow states match methodology
2. Check state transition rules
3. Review methodology configuration
4. Ensure required fields are populated

**Workflow States by Methodology**:
- Scrum: To Do → In Progress → Done
- Kanban: Backlog → Ready → In Progress → Review → Done
- Waterfall: Draft → Approved → In Progress → Completed → Verified

### Configuration Errors

**Problem**: Configuration file errors

**Solutions**:
1. Validate configuration:
   ```bash
   python cli/factory_cli.py --validate-pm-config pm-config.json
   ```
2. Check JSON syntax
3. Verify required fields
4. Review methodology defaults

### Performance Issues

**Problem**: Slow response times

**Solutions**:
1. Reduce data range for reports
2. Cache frequently accessed data
3. Optimize backend queries
4. Use pagination for large datasets

### Getting Help

If issues persist:

1. Check logs in `.pm/logs/`
2. Review agent output for error messages
3. Verify backend API status
4. Consult methodology-specific documentation
5. Ask in Cursor chat - agents can help troubleshoot!

---

*For methodology details, see [METHODOLOGY_REFERENCE.md](./METHODOLOGY_REFERENCE.md)*  
*For metrics details, see [METRICS_REFERENCE.md](./METRICS_REFERENCE.md)*
