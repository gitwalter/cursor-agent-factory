# Task Manager Agent Reference

## Purpose and Role

The Task Manager Agent breaks down user stories into actionable tasks, creates PM issues from code TODOs, updates work item status, and links related items. It ensures work is properly decomposed and tracked throughout the development lifecycle.

**Core Responsibilities:**
- Story decomposition into tasks
- TODO extraction from codebase
- Task status management
- Work item linking and dependencies
- Task assignment
- Workflow state transitions

**Philosophy:**
> Task management makes work actionable. The Task Manager Agent helps teams break down complex work into manageable pieces, grounded in love for clarity and trust in systematic execution.

## Capabilities Table

| Capability | Description | Example Command |
|------------|-------------|-----------------|
| **Break Down Story** | Decompose story into tasks | "Break down story PROJ-456" |
| **Extract TODOs** | Create issues from code TODOs | "Extract todos from codebase" |
| **Update Status** | Change task status | "Update PROJ-501 to In Progress" |
| **Link Items** | Create dependencies | "Link PROJ-502 depends on PROJ-501" |
| **Assign Task** | Assign task to team member | "Assign PROJ-501 to Alice" |
| **Create Task** | Create standalone task | "Create task for API testing" |
| **Update Progress** | Update task progress | "Update PROJ-501 progress to 80%" |
| **List Tasks** | Show tasks for story | "List tasks for PROJ-456" |
| **Task Details** | Show task information | "Show task PROJ-501" |

## Natural Language Commands

### Story Breakdown

**Basic Breakdown:**
```
User: Break down story PROJ-456

Agent: Breaking down story PROJ-456: User Login Authentication

Story Details:
- Title: User Login Authentication
- Acceptance Criteria:
  1. User can enter email and password
  2. System validates credentials
  3. User is redirected to dashboard on success
  4. Error message shown on invalid credentials

Proposed Tasks:
1. Create login form component (frontend)
2. Implement login API endpoint (backend)
3. Add credential validation logic (backend)
4. Create session management (backend)
5. Implement redirect logic (frontend)
6. Add error handling and messages (frontend)
7. Write unit tests for login flow (testing)

Create these tasks?
User: Yes, but combine 1 and 5 into "Create login UI"

Agent: Creating tasks...
✅ Tasks Created for PROJ-456:
1. PROJ-501: Create login UI
2. PROJ-502: Implement login API endpoint
3. PROJ-503: Add credential validation logic
4. PROJ-504: Create session management
5. PROJ-505: Add error handling
6. PROJ-506: Write unit tests

All tasks linked to story PROJ-456
```

**Guided Breakdown:**
```
User: Help me break down PROJ-456

Agent: Let's break down User Login Authentication step by step:

1. What's the first task needed?
   User: Create the login form

2. What's the next task?
   User: Implement the API endpoint

3. Continue?
   User: Yes, add validation, session management, error handling, and tests

Agent: Creating tasks...
✅ 6 tasks created
```

### TODO Extraction

**Extract from Codebase:**
```
User: Extract todos from codebase

Agent: Scanning codebase for TODO comments...

Found TODOs:
1. src/auth/login.ts:42 - TODO: Add rate limiting
2. src/auth/session.ts:15 - FIXME: Handle token expiration
3. src/components/LoginForm.tsx:28 - TODO: Add password strength indicator
4. tests/auth.test.ts:10 - TODO: Add integration tests

Creating issues...
✅ TODO Issues Created:
1. PROJ-507: TODO: Add rate limiting
   Location: src/auth/login.ts:42

2. PROJ-508: FIXME: Handle token expiration
   Location: src/auth/session.ts:15

3. PROJ-509: TODO: Add password strength indicator
   Location: src/components/LoginForm.tsx:28

4. PROJ-510: TODO: Add integration tests
   Location: tests/auth.test.ts:10
```

**Extract from Specific File:**
```
User: Extract todos from src/auth/login.ts

Agent: Scanning src/auth/login.ts...

Found TODOs:
1. Line 42: TODO: Add rate limiting
2. Line 78: FIXME: Handle concurrent login attempts

Creating issues...
✅ 2 issues created
```

### Status Updates

**Update Task Status:**
```
User: Update status of PROJ-501 to In Progress

Agent: Updating PROJ-501: Create login UI

Current Status: To Do
New Status: In Progress

Updating...
✅ Status updated successfully.

PROJ-501 is now In Progress
```

**Bulk Status Update:**
```
User: Mark all tasks for PROJ-456 as In Progress

Agent: Updating tasks for story PROJ-456...

Tasks:
- PROJ-501: Create login UI → In Progress ✅
- PROJ-502: Implement login API endpoint → In Progress ✅
- PROJ-503: Add credential validation logic → In Progress ✅
- PROJ-504: Create session management → In Progress ✅
- PROJ-505: Add error handling → In Progress ✅
- PROJ-506: Write unit tests → In Progress ✅

✅ All tasks updated
```

### Linking Items

**Create Dependency:**
```
User: Link PROJ-502 depends on PROJ-501

Agent: Creating dependency link...

PROJ-502: Implement login API endpoint
depends on
PROJ-501: Create login UI

✅ Link created. PROJ-502 will be blocked until PROJ-501 is done.
```

**Link Multiple Dependencies:**
```
User: Link PROJ-503 depends on PROJ-501 and PROJ-502

Agent: Creating dependencies...
✅ PROJ-503 depends on:
   - PROJ-501: Create login UI
   - PROJ-502: Implement login API endpoint
```

**Link to Story:**
```
User: Link PROJ-501 to story PROJ-456

Agent: Linking task to story...
✅ PROJ-501 linked to PROJ-456: User Login Authentication
```

### Task Assignment

**Assign to Team Member:**
```
User: Assign PROJ-501 to Alice

Agent: Assigning PROJ-501: Create login UI to Alice...

✅ Task assigned successfully.
Alice is now assigned to PROJ-501.
```

**Assign Based on Skills:**
```
User: Assign tasks for PROJ-456 based on skills

Agent: Analyzing tasks and team skills...

Task Assignments:
- PROJ-501: Create login UI → Alice (frontend specialist)
- PROJ-502: Implement login API endpoint → Bob (backend specialist)
- PROJ-503: Add credential validation logic → Bob (backend specialist)
- PROJ-504: Create session management → Bob (backend specialist)
- PROJ-505: Add error handling → Alice (frontend specialist)
- PROJ-506: Write unit tests → Charlie (QA specialist)

Assign these tasks?
User: Yes

Agent: ✅ All tasks assigned
```

## Workflow Examples

### Story Breakdown Workflow

**Complete Breakdown Process:**

1. **Analyze Story**
   ```
   Agent: Analyzing story PROJ-456...
   - Acceptance criteria: 4 items
   - Story points: 5
   - Complexity: Medium
   ```

2. **Identify Tasks**
   ```
   Agent: Identifying tasks from acceptance criteria...
   Proposed tasks: 7 tasks
   ```

3. **Review and Adjust**
   ```
   User: Combine tasks 1 and 5
   Agent: Adjusting tasks...
   ✅ Tasks updated
   ```

4. **Create Tasks**
   ```
   Agent: Creating tasks in backend...
   ✅ 6 tasks created
   ```

5. **Link to Story**
   ```
   Agent: Linking tasks to story...
   ✅ All tasks linked to PROJ-456
   ```

### TODO Extraction Workflow

**Complete Extraction Process:**

1. **Scan Codebase**
   ```
   Agent: Scanning codebase for TODO comments...
   Found: 4 TODOs in 4 files
   ```

2. **Extract Context**
   ```
   Agent: Extracting context for each TODO...
   - File location
   - Line number
   - Code context
   ```

3. **Create Issues**
   ```
   Agent: Creating issues from TODOs...
   ✅ 4 issues created
   ```

4. **Link to Related Work**
   ```
   Agent: Linking to related stories if found...
   ✅ 2 issues linked to stories
   ```

### Status Management Workflow

**Complete Status Update Process:**

1. **Check Current Status**
   ```
   Agent: Current status: To Do
   ```

2. **Validate Transition**
   ```
   Agent: Validating status transition...
   To Do → In Progress: ✅ Valid
   ```

3. **Update Status**
   ```
   Agent: Updating status...
   ✅ Status updated
   ```

4. **Update Timestamps**
   ```
   Agent: Updating timestamps...
   - Started: 2026-01-30 10:30 AM
   ```

5. **Notify Team**
   ```
   Agent: Notifying team...
   ✅ Team notified
   ```

## Configuration Options

### Task Template Configuration

**Task Template:**
```json
{
  "taskTemplate": {
    "requiredFields": ["title", "storyId"],
    "optionalFields": ["description", "assignee", "estimate", "labels"],
    "defaultEstimate": null,
    "autoLinkToStory": true
  }
}
```

### TODO Detection Configuration

**TODO Patterns:**
```json
{
  "todoDetection": {
    "patterns": ["TODO", "FIXME", "HACK", "XXX"],
    "fileTypes": [".ts", ".tsx", ".js", ".jsx", ".py", ".java", ".cs", ".go", ".rs"],
    "includeContext": true,
    "linkToRelated": true
  }
}
```

### Workflow States Configuration

**Scrum Workflow:**
```json
{
  "workflow": {
    "type": "scrum",
    "states": ["To Do", "In Progress", "Review", "Done"],
    "transitions": {
      "To Do": ["In Progress"],
      "In Progress": ["Review", "Done"],
      "Review": ["Done", "In Progress"],
      "Done": []
    }
  }
}
```

**Kanban Workflow:**
```json
{
  "workflow": {
    "type": "kanban",
    "states": ["Backlog", "Ready", "In Progress", "Review", "Testing", "Done"],
    "wipLimits": {
      "Ready": 5,
      "In Progress": 3,
      "Review": 2,
      "Testing": 2
    }
  }
}
```

## Backend-Specific Behaviors

### Jira

**Task Creation:**
- Creates issue type "Task" or "Sub-task"
- Links to parent story via "Parent Link"
- Sets assignee field
- Adds description

**Status Updates:**
- Uses Jira workflow states
- Updates status via transitions
- Tracks status change history

**Linking:**
- Creates "depends on" links
- Uses Jira link types
- Supports blocking links

### Linear

**Task Creation:**
- Creates issue with type "Task"
- Links to parent via parent relationship
- Sets assignee
- Adds description

**Status Updates:**
- Uses Linear workflow states
- Updates via state transitions
- Tracks state history

**Linking:**
- Creates dependency links
- Uses Linear relationships
- Supports blocking

### GitHub Projects

**Task Creation:**
- Creates GitHub Issue
- Links to parent via project relationships
- Sets assignee
- Adds description

**Status Updates:**
- Uses project column states
- Updates via project board
- Tracks state changes

**Linking:**
- Creates issue references
- Uses GitHub relationships
- Supports dependencies

### Local Backend

**Task Creation:**
- Creates JSON file in `.pm/local/tasks/`
- Links to story via storyId field
- Stores all metadata locally

**Status Updates:**
- Updates status field
- Tracks status history
- Updates timestamps

**Linking:**
- Creates link references in JSON
- Stores dependencies locally
- Supports all link types

## Methodology-Specific Behaviors

### Agile Scrum

**Task Structure:**
- Tasks linked to stories
- Estimated in hours (optional)
- Assigned during sprint planning
- Status: To Do → In Progress → Done

**Breakdown:**
- Story decomposed during planning
- Tasks created before sprint start
- All tasks linked to story

**Status Management:**
- Status updated daily
- Progress tracked in standups
- Completion verified before story acceptance

### Kanban

**Task Structure:**
- Tasks flow through board columns
- Focus on cycle time
- Self-assigned (pull-based)
- Status: Backlog → Ready → In Progress → Review → Done

**Breakdown:**
- Tasks created as needed
- WIP limits enforced
- Flow metrics tracked

**Status Management:**
- Status updated when moving columns
- WIP monitored
- Cycle time measured

### Research & Development

**Task Structure:**
- Tasks framed as experiments
- Learning outcomes tracked
- Assigned by research area
- Status: Proposed → Running → Analyzed → Documented

**Breakdown:**
- Experiments broken into steps
- Learning goals defined
- Research questions tracked

**Status Management:**
- Status reflects experiment phase
- Learning outcomes documented
- Research insights captured

### Enterprise Integration

**Task Structure:**
- Tasks linked to requirements
- Assigned by role
- Compliance tracked
- Status: Draft → Approved → In Progress → Completed → Verified

**Breakdown:**
- Requirements decomposed into tasks
- Formal approval required
- Traceability maintained

**Status Management:**
- Status requires approvals
- Compliance checks at each stage
- Formal documentation required

## Integration with Other Agents

### Product Owner Agent

**Integration Points:**
- Receives stories to break down
- Provides task completion for story acceptance
- Coordinates story refinement

**Example Flow:**
```
Product Owner: Create story PROJ-456
Task Manager: Break down story into tasks
Product Owner: Review task breakdown
Task Manager: Complete tasks
Product Owner: Accept story when all tasks done
```

### Sprint Master Agent

**Integration Points:**
- Tasks used in sprint planning
- Task progress tracked in standups
- Dependencies identified

**Example Flow:**
```
Sprint Master: Plan sprint
Task Manager: Break down stories into tasks
Sprint Master: Track task progress in standups
Task Manager: Update task status
Sprint Master: Close sprint when tasks done
```

### Reporting Agent

**Integration Points:**
- Provides task completion metrics
- Receives task status data
- Uses task data for reports

**Example Flow:**
```
Task Manager: Complete tasks
Reporting Agent: Track task completion rate
Task Manager: Update status
Reporting Agent: Generate task metrics
```

## Best Practices

### Story Breakdown

1. **Actionable Tasks**
   - Each task should be completable independently
   - Clear, specific descriptions
   - Appropriate size (1-2 days)

2. **Complete Coverage**
   - All acceptance criteria covered
   - Include testing tasks
   - Include documentation tasks

3. **Proper Linking**
   - Link all tasks to parent story
   - Identify dependencies
   - Maintain relationships

### TODO Extraction

1. **Regular Scanning**
   - Extract TODOs weekly
   - Don't let them accumulate
   - Prioritize critical TODOs

2. **Context Preservation**
   - Include file location
   - Preserve code context
   - Link to related work

3. **Prioritization**
   - Prioritize TODOs by impact
   - Link to stories if related
   - Track resolution

### Status Management

1. **Timely Updates**
   - Update status daily
   - Reflect actual progress
   - Keep status current

2. **Valid Transitions**
   - Follow workflow rules
   - Don't skip states
   - Maintain state history

3. **Progress Tracking**
   - Update progress percentage
   - Add progress notes
   - Track blockers

### Task Assignment

1. **Skill-Based**
   - Assign based on skills
   - Consider workload
   - Balance assignments

2. **Capacity Awareness**
   - Don't over-assign
   - Consider availability
   - Respect WIP limits

3. **Clear Ownership**
   - One owner per task
   - Clear responsibilities
   - Support collaboration

## Common Use Cases

### Use Case 1: Story Breakdown

**Scenario:** Breaking down a story for sprint planning

**Workflow:**
1. Analyze story acceptance criteria
2. Identify tasks needed
3. Create tasks
4. Link to story
5. Assign tasks

**Commands:**
```
"Break down story PROJ-456"
"List tasks for PROJ-456"
"Assign tasks for PROJ-456"
```

### Use Case 2: TODO Extraction

**Scenario:** Converting code TODOs to tracked issues

**Workflow:**
1. Scan codebase for TODOs
2. Extract context
3. Create issues
4. Link to related work
5. Prioritize

**Commands:**
```
"Extract todos from codebase"
"Extract todos from src/auth/"
"Link PROJ-507 to story PROJ-456"
```

### Use Case 3: Status Updates

**Scenario:** Updating task progress

**Workflow:**
1. Check current status
2. Validate transition
3. Update status
4. Update progress
5. Notify team

**Commands:**
```
"Update PROJ-501 to In Progress"
"Update PROJ-501 progress to 80%"
"Mark PROJ-501 as Done"
```

### Use Case 4: Dependency Management

**Scenario:** Managing task dependencies

**Workflow:**
1. Identify dependencies
2. Create links
3. Track blockers
4. Resolve dependencies
5. Update status

**Commands:**
```
"Link PROJ-502 depends on PROJ-501"
"List dependencies for PROJ-502"
"Show blocked tasks"
```

## Troubleshooting

### Breakdown Issues

**Problem:** Tasks not created

**Solutions:**
- Verify story exists
- Check backend connection
- Ensure required fields provided
- Review backend permissions

### TODO Extraction Issues

**Problem:** TODOs not found

**Solutions:**
- Check file types configured
- Verify TODO patterns
- Ensure codebase accessible
- Review scan paths

### Status Update Issues

**Problem:** Status not updating

**Solutions:**
- Verify workflow states
- Check transition rules
- Ensure task exists
- Review backend permissions

## References

- [PM System User Guide](../USER_GUIDE.md)
- [Methodology Reference](../METHODOLOGY_REFERENCE.md)
- [Metrics Reference](../METRICS_REFERENCE.md)
- [Product Owner Agent](./PRODUCT_OWNER_AGENT.md)
- [Sprint Master Agent](./SPRINT_MASTER_AGENT.md)
- [Reporting Agent](./REPORTING_AGENT.md)

---

*Task Manager Agent Reference v1.0.0*  
*Grounded in Axiom 0: Love and Trust*
