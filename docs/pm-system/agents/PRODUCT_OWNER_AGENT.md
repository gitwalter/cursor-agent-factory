# Product Owner Agent Reference

## Purpose and Role

The Product Owner Agent manages the product backlog, creates and refines user stories, prioritizes work, accepts completed stories, and generates release notes. It ensures the product vision aligns with stakeholder needs and development capacity.

**Core Responsibilities:**
- Backlog management and prioritization
- User story creation and refinement
- Epic organization
- Story acceptance and quality gates
- Release documentation
- Stakeholder communication

**Philosophy:**
> Product ownership bridges vision and execution. The Product Owner Agent helps teams maintain clarity on what to build and why, grounded in love for the product mission and trust in the team's ability to deliver value.

## Capabilities Table

| Capability | Description | Example Command |
|------------|-------------|-----------------|
| **Create Story** | Create new user story with acceptance criteria | "Create story for user login" |
| **Create Epic** | Create epic for grouping related stories | "Create epic for authentication features" |
| **Prioritize Backlog** | Reorder backlog items by priority | "Prioritize backlog" |
| **Refine Story** | Add details and acceptance criteria to existing story | "Refine story PROJ-456" |
| **Accept Story** | Review and accept completed stories | "Accept story PROJ-456" |
| **Backlog Grooming** | Review and organize backlog items | "Groom backlog" |
| **Generate Release Notes** | Create release documentation from completed stories | "Generate release notes for v1.2.0" |
| **Link Stories to Epic** | Organize stories under epics | "Link PROJ-456 to Authentication epic" |
| **Estimate Stories** | Add story point estimates | "Estimate story PROJ-456" |

## Natural Language Commands

### Story Creation

**Basic Story Creation:**
```
User: Create story for user login

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

**Quick Story Creation:**
```
User: Add story "User can reset password" with 3 points to Authentication epic

Agent: Creating story...
✅ Story PROJ-457 created: User can reset password (3 pts)
Linked to Authentication epic
```

### Backlog Prioritization

**Prioritize Backlog:**
```
User: Prioritize the backlog

Agent: I'll help you prioritize the backlog. Let me fetch current items:

Current Backlog:
1. User Login (5 pts) - Medium priority
2. Password Reset (3 pts) - Low priority
3. User Profile (8 pts) - High priority
4. Email Verification (3 pts) - Medium priority

What's the priority order? Consider:
- Business value
- Dependencies (e.g., Login must come before Profile)
- Risk and complexity
- Stakeholder requests

User: 
1. User Login (foundation)
2. Email Verification (depends on Login)
3. User Profile (depends on Login)
4. Password Reset (can wait)

Agent: Updating priorities...
✅ Backlog prioritized successfully
```

**Priority Adjustment:**
```
User: Move User Profile to top priority

Agent: Updating priority...
✅ User Profile (PROJ-459) moved to highest priority
```

### Story Refinement

**Add Acceptance Criteria:**
```
User: Refine story PROJ-456

Agent: Current story: PROJ-456 - User Login Authentication

Current acceptance criteria:
- User can enter email and password
- System validates credentials

What would you like to add?
User: Add criteria for session timeout and remember me feature

Agent: Adding acceptance criteria...
✅ Story refined with additional criteria
```

### Story Acceptance

**Accept Completed Story:**
```
User: Accept story PROJ-456

Agent: Reviewing story PROJ-456: User Login Authentication

Acceptance Criteria Check:
✓ User can enter email and password
✓ System validates credentials
✓ User is redirected to dashboard on success
✓ Error message shown on invalid credentials

All criteria met! Accepting story...

✅ Story PROJ-456 accepted and moved to Done.
```

**Accept with Notes:**
```
User: Accept PROJ-456 with note "Minor UI improvements needed"

Agent: Accepting story with notes...
✅ Story PROJ-456 accepted
Note added: Minor UI improvements needed
```

### Release Notes Generation

**Generate Release Notes:**
```
User: Generate release notes for v1.2.0

Agent: Generating release notes for v1.2.0...

Fetching completed stories since v1.1.0...
Organizing by epic...

Release Notes v1.2.0
====================

Authentication Epic:
- ✅ User Login Authentication (PROJ-456)
- ✅ Email Verification (PROJ-457)
- ✅ Password Reset (PROJ-458)

User Profile Epic:
- ✅ User Profile View (PROJ-459)
- ✅ Profile Edit (PROJ-460)

Creating release notes page...
✅ Release notes created at docs/releases/v1.2.0.md
```

## Workflow Examples

### Story Creation Workflow

**Complete Story Creation Process:**

1. **Identify Need**
   ```
   User: We need user authentication
   ```

2. **Create Epic**
   ```
   Agent: Creating epic for user authentication...
   ✅ Epic EPIC-123 created: User Authentication System
   ```

3. **Create Stories**
   ```
   Agent: Let's break this down into stories:
   - User Login
   - Email Verification
   - Password Reset
   - Session Management
   
   Creating stories...
   ✅ 4 stories created and linked to epic
   ```

4. **Estimate Stories**
   ```
   Agent: Estimating stories...
   - User Login: 5 pts
   - Email Verification: 3 pts
   - Password Reset: 3 pts
   - Session Management: 5 pts
   ```

5. **Prioritize**
   ```
   Agent: Prioritizing stories...
   ✅ Stories prioritized by dependencies
   ```

### Backlog Grooming Workflow

**Regular Backlog Maintenance:**

1. **Review Backlog**
   ```
   User: Show backlog
   Agent: Current backlog has 15 stories across 3 epics...
   ```

2. **Identify Unrefined Stories**
   ```
   Agent: Found 3 stories without acceptance criteria:
   - PROJ-501: User Dashboard
   - PROJ-502: Settings Page
   - PROJ-503: Notifications
   ```

3. **Refine Stories**
   ```
   User: Refine PROJ-501
   Agent: Adding acceptance criteria...
   ✅ Story refined
   ```

4. **Remove Obsolete Items**
   ```
   User: Remove PROJ-504, it's no longer needed
   Agent: Removing story...
   ✅ Story removed from backlog
   ```

5. **Re-prioritize**
   ```
   User: Prioritize backlog
   Agent: Reordering based on current priorities...
   ✅ Backlog updated
   ```

### Release Planning Workflow

**Preparing for Release:**

1. **Review Completed Work**
   ```
   User: What's completed since v1.1.0?
   Agent: 12 stories completed across 2 epics...
   ```

2. **Organize by Epic**
   ```
   Agent: Organizing by epic:
   - Authentication Epic: 4 stories
   - User Profile Epic: 8 stories
   ```

3. **Generate Release Notes**
   ```
   User: Generate release notes
   Agent: Creating release documentation...
   ✅ Release notes generated
   ```

4. **Review and Publish**
   ```
   Agent: Release notes ready for review at docs/releases/v1.2.0.md
   ```

## Configuration Options

### Backend Configuration

**Jira Configuration:**
```json
{
  "backend": {
    "type": "jira",
    "workspace": "company.atlassian.net",
    "projectKey": "PROJ",
    "epicField": "customfield_10011"
  }
}
```

**Linear Configuration:**
```json
{
  "backend": {
    "type": "linear",
    "teamId": "team-123",
    "projectId": "project-456"
  }
}
```

**GitHub Projects Configuration:**
```json
{
  "backend": {
    "type": "github",
    "projectId": "project-v2_123",
    "organization": "company"
  }
}
```

### Story Template Configuration

**Custom Story Template:**
```json
{
  "storyTemplate": {
    "format": "as-a-i-want-so-that",
    "requiredFields": ["title", "description", "acceptanceCriteria"],
    "optionalFields": ["epic", "labels", "storyPoints"],
    "defaultPoints": null
  }
}
```

### Acceptance Criteria Template

**Structured Acceptance Criteria:**
```json
{
  "acceptanceCriteria": {
    "format": "bullet-list",
    "required": true,
    "minCriteria": 3,
    "template": "Given [context], When [action], Then [outcome]"
  }
}
```

## Backend-Specific Behaviors

### Jira

**Story Creation:**
- Creates issue type "Story"
- Links to Epic via Epic Link field
- Sets Story Points custom field
- Adds acceptance criteria to Description

**Epic Creation:**
- Creates issue type "Epic"
- Sets Epic Name field
- Links stories via Epic Link

**Release Notes:**
- Creates Confluence page
- Links to completed stories
- Includes Jira links

### Linear

**Story Creation:**
- Creates issue with type "Story"
- Links to Epic via parent relationship
- Sets estimate field
- Adds acceptance criteria as description

**Epic Creation:**
- Creates issue with type "Epic"
- Groups stories under epic
- Sets epic status

**Release Notes:**
- Creates Linear document
- Links to completed issues
- Includes Linear links

### GitHub Projects

**Story Creation:**
- Creates GitHub Issue
- Links to Epic via project relationship
- Adds story points as label
- Adds acceptance criteria to issue body

**Epic Creation:**
- Creates GitHub Issue with "Epic" label
- Links stories via project relationships
- Uses project board for organization

**Release Notes:**
- Creates GitHub Release
- Links to closed issues
- Generates changelog automatically

### Local Backend

**Story Creation:**
- Creates JSON file in `.pm/local/stories/`
- Links to epic via epicId field
- Stores all metadata locally

**Epic Creation:**
- Creates JSON file in `.pm/local/epics/`
- Links stories via file references

**Release Notes:**
- Creates Markdown file in `docs/releases/`
- Links to story files
- Includes all story details

## Methodology-Specific Behaviors

### Agile Scrum

**Story Format:**
- Uses "As a... I want... So that..." format
- Story points required (1-8 scale)
- Acceptance criteria mandatory
- Stories linked to sprints

**Backlog Management:**
- Prioritized by business value
- Estimated before sprint planning
- Refined during backlog grooming

**Release Notes:**
- Sprint-based releases
- Organized by sprint completion
- Includes velocity metrics

### Kanban

**Story Format:**
- Focus on flow and cycle time
- Optional story points
- Acceptance criteria required
- Stories flow through board columns

**Backlog Management:**
- Prioritized by classes of service
- WIP limits considered
- Flow metrics tracked

**Release Notes:**
- Time-based releases
- Organized by completion date
- Includes cycle time metrics

### Research & Development

**Story Format:**
- Framed as experiments
- Learning outcomes instead of acceptance criteria
- Research questions instead of user stories

**Backlog Management:**
- Prioritized by research value
- Exploration ratio tracked
- Learning velocity measured

**Release Notes:**
- Research summaries
- Learning outcomes documented
- Experiment results included

### Enterprise Integration

**Story Format:**
- Formal requirements format
- Compliance criteria included
- Traceability required

**Backlog Management:**
- Prioritized by milestones
- Gate reviews tracked
- Compliance status monitored

**Release Notes:**
- Milestone reports
- Compliance documentation
- Formal release notes

## Integration with Other Agents

### Sprint Master Agent

**Integration Points:**
- Provides prioritized backlog for sprint planning
- Receives sprint completion data for release notes
- Coordinates story refinement before planning

**Example Flow:**
```
Product Owner: Prioritize backlog
Sprint Master: Plan sprint using prioritized backlog
Product Owner: Review sprint plan
Sprint Master: Execute sprint
Product Owner: Accept completed stories
Product Owner: Generate release notes
```

### Task Manager Agent

**Integration Points:**
- Stories broken down into tasks
- Task completion tracked for story acceptance
- Dependencies identified during breakdown

**Example Flow:**
```
Product Owner: Create story PROJ-456
Task Manager: Break down story into tasks
Product Owner: Review task breakdown
Task Manager: Complete tasks
Product Owner: Accept story when all tasks done
```

### Reporting Agent

**Integration Points:**
- Provides backlog metrics
- Receives velocity data for capacity planning
- Uses completion data for release notes

**Example Flow:**
```
Product Owner: Review backlog
Reporting Agent: Show backlog metrics
Product Owner: Prioritize based on metrics
Reporting Agent: Track velocity trends
Product Owner: Plan releases based on velocity
```

## Best Practices

### Story Creation

1. **User-Centric Format**
   - Always use "As a... I want... So that..." format
   - Focus on user value, not implementation
   - Keep stories independent and negotiable

2. **Clear Acceptance Criteria**
   - Minimum 3 acceptance criteria per story
   - Use Given/When/Then format when appropriate
   - Make criteria testable and specific

3. **Proper Sizing**
   - Stories should be completable in one sprint
   - Break down large stories (8+ points)
   - Keep stories small enough to estimate accurately

### Backlog Management

1. **Regular Grooming**
   - Groom backlog weekly
   - Refine stories before sprint planning
   - Remove obsolete items regularly

2. **Prioritization Principles**
   - Prioritize by business value
   - Consider dependencies
   - Balance risk and complexity
   - Involve stakeholders

3. **Backlog Health**
   - Maintain 2-3 sprints of ready work
   - Keep stories refined and estimated
   - Document dependencies clearly

### Story Acceptance

1. **Rigorous Review**
   - Verify all acceptance criteria met
   - Check for quality standards
   - Ensure stakeholder approval

2. **Documentation**
   - Add acceptance notes
   - Document deviations if any
   - Link to related work

3. **Feedback Loop**
   - Provide feedback to team
   - Update story templates based on learnings
   - Improve acceptance process

### Release Notes

1. **Regular Releases**
   - Generate notes after each release
   - Include all completed stories
   - Organize by epic or feature area

2. **Stakeholder-Friendly**
   - Use clear, non-technical language
   - Highlight user-facing changes
   - Include screenshots or demos when possible

3. **Comprehensive**
   - Include all completed work
   - Note breaking changes
   - Provide migration guides if needed

## Common Use Cases

### Use Case 1: New Feature Request

**Scenario:** Stakeholder requests new feature

**Workflow:**
1. Create epic for feature area
2. Break down into user stories
3. Estimate stories
4. Prioritize in backlog
5. Refine stories before sprint planning

**Commands:**
```
"Create epic for payment processing"
"Create story for adding payment method"
"Prioritize backlog"
```

### Use Case 2: Sprint Preparation

**Scenario:** Preparing backlog for next sprint

**Workflow:**
1. Review current backlog
2. Refine unrefined stories
3. Re-estimate if needed
4. Re-prioritize based on current priorities
5. Ensure 2-3 sprints of ready work

**Commands:**
```
"Show backlog"
"Refine story PROJ-456"
"Prioritize backlog"
```

### Use Case 3: Release Preparation

**Scenario:** Preparing release documentation

**Workflow:**
1. Review completed stories since last release
2. Organize by epic or feature
3. Generate release notes
4. Review and publish

**Commands:**
```
"What's completed since v1.1.0?"
"Generate release notes for v1.2.0"
```

### Use Case 4: Story Refinement Session

**Scenario:** Backlog grooming meeting

**Workflow:**
1. List unrefined stories
2. Refine each story with team
3. Add acceptance criteria
4. Estimate stories
5. Update priorities

**Commands:**
```
"Show unrefined stories"
"Refine story PROJ-456"
"Estimate story PROJ-456"
```

## Troubleshooting

### Story Creation Issues

**Problem:** Story not created in backend

**Solutions:**
- Verify backend connection
- Check project ID is correct
- Ensure required fields provided
- Review backend logs

### Prioritization Issues

**Problem:** Priorities not saving

**Solutions:**
- Verify backend supports priority updates
- Check user permissions
- Ensure story IDs are valid
- Try updating one story at a time

### Release Notes Issues

**Problem:** Release notes missing stories

**Solutions:**
- Verify story status is "Done"
- Check date range includes all stories
- Ensure stories are linked to project
- Review backend query filters

## References

- [PM System User Guide](../USER_GUIDE.md)
- [Methodology Reference](../METHODOLOGY_REFERENCE.md)
- [Metrics Reference](../METRICS_REFERENCE.md)
- [Sprint Master Agent](./SPRINT_MASTER_AGENT.md)
- [Task Manager Agent](./TASK_MANAGER_AGENT.md)
- [Reporting Agent](./REPORTING_AGENT.md)

---

*Product Owner Agent Reference v1.0.0*  
*Grounded in Axiom 0: Love and Trust*
