# Sprint Master Agent Reference

## Purpose and Role

The Sprint Master Agent facilitates Agile ceremonies including sprint planning, daily standups, sprint retrospectives, and sprint transitions. It ensures team alignment, removes blockers, and maintains sprint health while adapting to the team's chosen methodology.

**Core Responsibilities:**
- Sprint planning and capacity management
- Daily standup facilitation
- Sprint retrospective coordination
- Blocker identification and resolution
- Sprint health monitoring
- Ceremony adaptation to methodology

**Philosophy:**
> Sprint mastery is about facilitation, not control. The Sprint Master Agent helps teams run effective ceremonies grounded in love for team collaboration and trust in their ability to self-organize.

## Capabilities Table

| Capability | Description | Example Command |
|------------|-------------|-----------------|
| **Plan Sprint** | Create sprint plan with selected stories | "Plan sprint for next 2 weeks" |
| **Run Standup** | Facilitate daily standup meeting | "Run standup" |
| **Sprint Retro** | Conduct sprint retrospective | "Run sprint retro" |
| **Close Sprint** | End sprint and calculate metrics | "Close sprint SPRINT-12" |
| **Sprint Review** | Generate sprint review report | "Sprint review for Sprint 12" |
| **Identify Blockers** | Find and report blockers | "List blockers" |
| **Sprint Health** | Check sprint progress and health | "Sprint health check" |
| **Adjust Sprint** | Modify sprint scope or dates | "Add story PROJ-456 to sprint" |
| **Sprint Metrics** | Show sprint velocity and burndown | "Show sprint metrics" |

## Natural Language Commands

### Sprint Planning

**Basic Sprint Planning:**
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

Fetching prioritized backlog...
Preparing sprint plan...

✅ Sprint Plan Created:
Sprint: Sprint 12 - Authentication
Duration: Feb 1-14, 2026
Goal: Complete authentication features
Capacity: 40 story points

Selected Stories:
1. PROJ-456: User Login (5 pts)
2. PROJ-457: Email Verification (3 pts)
3. PROJ-458: Password Reset (3 pts)
4. PROJ-459: User Profile View (8 pts)
5. PROJ-460: Profile Edit (8 pts)
6. PROJ-461: Session Management (5 pts)
7. PROJ-462: OAuth Integration (8 pts)

Total: 40 story points
```

**Capacity-Based Planning:**
```
User: Plan sprint with 25 point capacity

Agent: Reviewing backlog...
Selecting stories to fit capacity...

✅ Sprint planned:
- Stories: 5 stories
- Points: 25 pts
- Capacity: 25 pts (100% utilization)
```

### Daily Standup

**Standard Standup:**
```
User: Run standup

Agent: Daily Standup - Day 5 of Sprint 12
Date: Feb 5, 2026

Fetching sprint status...
Current Sprint: Sprint 12 - Authentication

Standup Questions:
1. What did you complete yesterday?
2. What are you working on today?
3. Any blockers or impediments?

[Team members respond]

Agent: Standup Summary:
- Alice: Completed User Login, working on Email Verification, no blockers
- Bob: Completed Password Reset, working on Session Management, blocked on OAuth config
- Charlie: Completed User Profile View, working on Profile Edit, no blockers

Blockers Identified:
- Bob: OAuth configuration access needed

Action Items:
- [ ] Unblock Bob: Request OAuth config access
```

**Async Standup:**
```
User: Run async standup

Agent: Async Standup Report - Feb 5, 2026

Sprint: Sprint 12 - Authentication

Team Updates:
- Alice: Completed PROJ-456, working on PROJ-457
- Bob: Completed PROJ-458, blocked on PROJ-461
- Charlie: Completed PROJ-459, working on PROJ-460

Blockers: 1
Action Items: 1

Report saved for team review.
```

### Sprint Retrospective

**Traditional Retro:**
```
User: Run sprint retro

Agent: Sprint 12 Retrospective
Sprint: Authentication Features
Duration: Feb 1-14, 2026

Sprint Results:
- Planned: 40 story points
- Completed: 38 story points
- Velocity: 38 points (95% of plan)

Completed Stories:
✓ User Login
✓ Email Verification
✓ Password Reset
✓ User Profile View
✓ Profile Edit
✓ Session Management
✗ OAuth Integration (carried over)

Retrospective Format:
1. What went well?
2. What didn't go well?
3. What should we improve?

[Team responds]

Agent: Retro Summary:

What Went Well:
- Clear sprint goal kept team focused
- Daily standups were effective
- Pair programming helped with complex stories

What Didn't Go Well:
- OAuth integration took longer than estimated
- Some dependencies weren't clear upfront
- Standup timing conflicted with some team members

Action Items:
- [ ] Improve story estimation (add buffer for integrations)
- [ ] Document dependencies during planning
- [ ] Adjust standup time to accommodate all time zones
```

**Start/Stop/Continue Retro:**
```
User: Run retro with start/stop/continue format

Agent: Sprint Retrospective - Start/Stop/Continue Format

Start Doing:
- Better dependency documentation
- Buffer time for integrations

Stop Doing:
- Overcommitting on sprint capacity
- Late standup starts

Continue Doing:
- Clear sprint goals
- Effective standups
- Pair programming
```

### Sprint Closure

**Close Sprint:**
```
User: Close sprint SPRINT-12

Agent: Closing Sprint 12 - Authentication

Final Status:
- Completed: 38/40 story points (95%)
- Stories Done: 6/7
- OAuth Integration carried over

Closing sprint...
Moving incomplete items to backlog...
Calculating velocity...

✅ Sprint Closed:
- Velocity: 38 points
- Burndown chart saved
- Retrospective notes saved
- Sprint report generated

Next Steps:
- Sprint 13 planning scheduled for Feb 15
- OAuth Integration added to backlog (priority: High)
```

## Workflow Examples

### Sprint Planning Workflow

**Complete Planning Process:**

1. **Review Previous Sprint**
   ```
   Agent: Previous sprint velocity: 38 points
   ```

2. **Check Team Capacity**
   ```
   Agent: Team capacity: 40 points
   - Alice: 13 pts (available 10 days)
   - Bob: 13 pts (available 10 days)
   - Charlie: 14 pts (available 10 days)
   ```

3. **Review Backlog**
   ```
   Agent: Prioritized backlog:
   - PROJ-456: User Login (5 pts) - High
   - PROJ-457: Email Verification (3 pts) - High
   ...
   ```

4. **Select Stories**
   ```
   Agent: Selecting stories to fit capacity...
   ✅ 7 stories selected (40 pts)
   ```

5. **Set Sprint Goal**
   ```
   Agent: Sprint goal: Complete authentication features
   ```

6. **Create Sprint**
   ```
   Agent: Sprint SPRINT-12 created
   ```

### Daily Standup Workflow

**Daily Standup Process:**

1. **Fetch Sprint Status**
   ```
   Agent: Fetching sprint status...
   Current sprint: Sprint 12 (Day 5)
   ```

2. **Query In-Progress Items**
   ```
   Agent: In-progress items:
   - PROJ-457: Email Verification (Alice)
   - PROJ-461: Session Management (Bob)
   - PROJ-460: Profile Edit (Charlie)
   ```

3. **Identify Blockers**
   ```
   Agent: Blockers found:
   - PROJ-461: OAuth config access needed
   ```

4. **Format Standup Report**
   ```
   Agent: Generating standup report...
   ✅ Standup report ready
   ```

5. **Track Action Items**
   ```
   Agent: Action items created:
   - Unblock Bob: Request OAuth config access
   ```

### Retrospective Workflow

**Complete Retro Process:**

1. **Gather Sprint Data**
   ```
   Agent: Gathering sprint metrics...
   - Velocity: 38 points
   - Completion rate: 95%
   - Blocker count: 2
   ```

2. **Present Sprint Results**
   ```
   Agent: Sprint results:
   - Completed: 6/7 stories
   - Velocity: 38/40 points
   ```

3. **Facilitate Discussion**
   ```
   Agent: Retrospective questions:
   1. What went well?
   2. What didn't go well?
   3. What should we improve?
   ```

4. **Capture Action Items**
   ```
   Agent: Action items identified:
   - Improve estimation
   - Document dependencies
   ```

5. **Save Retro Notes**
   ```
   Agent: Retrospective notes saved
   ```

## Configuration Options

### Sprint Configuration

**Sprint Length:**
```json
{
  "sprint": {
    "defaultLength": "2_weeks",
    "options": ["1_week", "2_weeks", "3_weeks", "4_weeks"],
    "customLength": true
  }
}
```

**Standup Configuration:**
```json
{
  "standup": {
    "time": "10:00_AM",
    "duration": "15_minutes",
    "format": "traditional",
    "async": false,
    "timezone": "America/New_York"
  }
}
```

**Retrospective Configuration:**
```json
{
  "retrospective": {
    "format": "traditional",
    "duration": "1_hour",
    "frequency": "end_of_sprint",
    "formats": ["traditional", "start_stop_continue", "4ls", "mad_sad_glad"]
  }
}
```

### Ceremony Automation

**Automated Standups:**
```json
{
  "automation": {
    "standup": {
      "enabled": true,
      "schedule": "daily",
      "time": "10:00_AM",
      "async": false,
      "notify": true
    }
  }
}
```

**Sprint Transitions:**
```json
{
  "transitions": {
    "autoClose": false,
    "autoCreate": false,
    "carryOver": true,
    "notifyTeam": true
  }
}
```

## Methodology-Specific Behaviors

### Agile Scrum

**Sprint Planning:**
- Story point estimation required
- Capacity-based selection
- Sprint goal mandatory
- 2-4 hour planning meeting

**Standup Format:**
- 3 questions: What did I do? What will I do? Any blockers?
- 15 minutes maximum
- Time-boxed
- Focus on coordination

**Retrospective:**
- Traditional format: What went well? What didn't? What to improve?
- 1 hour duration
- Action items tracked
- Held at sprint end

**Sprint Length:**
- Typically 1-4 weeks
- Most common: 2 weeks
- Fixed length per team

### Kanban

**Planning:**
- Flow-based selection
- WIP limits considered
- No fixed sprint length
- Continuous flow

**Standup Format:**
- Focus on flow and blockers
- Walk the board
- WIP status check
- Blocker identification

**Retrospective:**
- Flow metrics focus
- Cycle time analysis
- WIP limit review
- Weekly or bi-weekly

**Sprint Length:**
- No sprints (continuous flow)
- Optional iterations for planning

### Research & Development

**Planning:**
- Experiment selection
- Learning goals set
- Exploration ratio tracked
- Variable sprint length

**Standup Format:**
- Progress on experiments
- Insights shared
- Learning outcomes
- Research questions

**Retrospective:**
- Learning outcomes review
- Experiment results
- Research insights
- Knowledge sharing

**Sprint Length:**
- Variable based on experiments
- Typically 2-4 weeks
- Flexible based on research needs

### Enterprise Integration

**Planning:**
- Milestone-based planning
- Gate reviews scheduled
- Compliance checks
- Formal approval process

**Standup Format:**
- Status updates
- Compliance checks
- Risk assessment
- Formal reporting

**Retrospective:**
- Process compliance review
- Risk assessment
- Gate review outcomes
- Compliance metrics

**Sprint Length:**
- Aligned with milestones
- Typically 4-8 weeks
- Fixed by governance

## Integration with Other Agents

### Product Owner Agent

**Integration Points:**
- Receives prioritized backlog for planning
- Provides sprint completion data
- Coordinates story refinement

**Example Flow:**
```
Product Owner: Prioritize backlog
Sprint Master: Plan sprint using prioritized backlog
Product Owner: Review sprint plan
Sprint Master: Execute sprint
Product Owner: Accept completed stories
```

### Task Manager Agent

**Integration Points:**
- Stories broken down during planning
- Task completion tracked in standups
- Dependencies identified

**Example Flow:**
```
Sprint Master: Plan sprint
Task Manager: Break down stories into tasks
Sprint Master: Track task progress in standups
Task Manager: Complete tasks
Sprint Master: Close sprint when stories done
```

### Reporting Agent

**Integration Points:**
- Provides sprint metrics
- Receives burndown data
- Uses velocity for planning

**Example Flow:**
```
Sprint Master: Plan sprint
Reporting Agent: Provide velocity data
Sprint Master: Use velocity for capacity
Reporting Agent: Generate burndown during sprint
Sprint Master: Review burndown in standups
Reporting Agent: Calculate final metrics
Sprint Master: Use metrics in retrospective
```

## Best Practices

### Sprint Planning

1. **Use Historical Velocity**
   - Average last 3 sprints
   - Account for team changes
   - Consider context changes

2. **Set Realistic Capacity**
   - Account for time off
   - Include buffer (10-20%)
   - Consider other commitments

3. **Clear Sprint Goal**
   - Single, focused goal
   - Measurable success criteria
   - Aligned with product vision

4. **Balance Story Sizes**
   - Mix of small, medium, large
   - Avoid all large stories
   - Include quick wins

### Daily Standups

1. **Keep It Brief**
   - 15 minutes maximum
   - Focus on coordination
   - Not status reporting

2. **Identify Blockers Early**
   - Surface blockers immediately
   - Assign owners
   - Set resolution deadlines

3. **Update Items**
   - Update status after standup
   - Track progress
   - Link blockers to items

4. **Respect Time**
   - Start on time
   - Stay focused
   - End on time

### Retrospectives

1. **Safe Environment**
   - Psychological safety
   - No blame
   - Focus on process

2. **Actionable Items**
   - Specific action items
   - Assigned owners
   - Tracked in next sprint

3. **Follow Up**
   - Review previous action items
   - Track progress
   - Celebrate improvements

4. **Variety**
   - Try different formats
   - Keep it engaging
   - Adapt to team needs

### Sprint Health

1. **Monitor Progress**
   - Daily burndown check
   - Velocity tracking
   - Blocker monitoring

2. **Early Intervention**
   - Identify risks early
   - Adjust scope if needed
   - Communicate changes

3. **Team Support**
   - Remove impediments
   - Support team members
   - Facilitate collaboration

## Common Use Cases

### Use Case 1: New Sprint Planning

**Scenario:** Starting a new sprint

**Workflow:**
1. Review previous sprint velocity
2. Check team capacity
3. Review prioritized backlog
4. Select stories
5. Set sprint goal
6. Create sprint

**Commands:**
```
"Plan sprint for next 2 weeks"
"What's our velocity?"
"Show prioritized backlog"
```

### Use Case 2: Daily Standup

**Scenario:** Running daily standup

**Workflow:**
1. Fetch sprint status
2. Query in-progress items
3. Identify blockers
4. Format standup report
5. Track action items

**Commands:**
```
"Run standup"
"List blockers"
"Show sprint status"
```

### Use Case 3: Sprint Retrospective

**Scenario:** End of sprint retrospective

**Workflow:**
1. Gather sprint metrics
2. Present sprint results
3. Facilitate discussion
4. Capture action items
5. Save retro notes

**Commands:**
```
"Run sprint retro"
"Show sprint metrics"
"Generate sprint report"
```

### Use Case 4: Sprint Adjustment

**Scenario:** Need to adjust sprint scope

**Workflow:**
1. Check current sprint capacity
2. Review story priorities
3. Add or remove stories
4. Update sprint plan

**Commands:**
```
"Add story PROJ-456 to sprint"
"Remove story PROJ-457 from sprint"
"Show sprint capacity"
```

## Troubleshooting

### Sprint Planning Issues

**Problem:** Cannot create sprint

**Solutions:**
- Verify backend connection
- Check project ID
- Ensure dates are valid
- Review backend permissions

### Standup Issues

**Problem:** Standup data incomplete

**Solutions:**
- Verify sprint ID
- Check item statuses
- Ensure team members assigned
- Review backend queries

### Retrospective Issues

**Problem:** Retro format not working

**Solutions:**
- Try different format
- Check methodology configuration
- Verify team preferences
- Adapt to team needs

## References

- [PM System User Guide](../USER_GUIDE.md)
- [Methodology Reference](../METHODOLOGY_REFERENCE.md)
- [Metrics Reference](../METRICS_REFERENCE.md)
- [Product Owner Agent](./PRODUCT_OWNER_AGENT.md)
- [Task Manager Agent](./TASK_MANAGER_AGENT.md)
- [Reporting Agent](./REPORTING_AGENT.md)

---

*Sprint Master Agent Reference v1.0.0*  
*Grounded in Axiom 0: Love and Trust*
