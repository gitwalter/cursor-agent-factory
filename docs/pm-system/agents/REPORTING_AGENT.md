# Reporting Agent Reference

## Purpose and Role

The Reporting Agent generates project management reports, calculates team metrics, produces health indicators, and creates visualization dashboards. It provides data-driven insights for team improvement and stakeholder communication.

**Core Responsibilities:**
- Burndown chart generation
- Velocity tracking and reporting
- Team health assessment
- Sprint and release reports
- Dashboard creation
- Metrics interpretation

**Philosophy:**
> Metrics illuminate reality. The Reporting Agent helps teams understand their performance through data, grounded in love for transparency and trust in continuous improvement.

## Capabilities Table

| Capability | Description | Example Command |
|------------|-------------|-----------------|
| **Burndown Chart** | Generate sprint burndown visualization | "Show burndown for Sprint 12" |
| **Velocity Report** | Calculate and report team velocity | "Velocity report" |
| **Team Health** | Assess team health indicators | "Team health check" |
| **Sprint Report** | Generate comprehensive sprint report | "Sprint report for Sprint 12" |
| **Dashboard** | Create metrics dashboard | "Create metrics dashboard" |
| **Forecast** | Predict sprint and release dates | "Forecast next sprint completion" |
| **Cycle Time** | Report cycle time metrics | "Show cycle time" |
| **Throughput** | Report throughput metrics | "Show throughput" |
| **WIP Report** | Report work in progress status | "Show WIP status" |

## Natural Language Commands

### Burndown Charts

**Sprint Burndown:**
```
User: Show burndown for Sprint 12

Agent: Generating burndown chart for Sprint 12...

Fetching sprint data...
Calculating remaining work...

Sprint 12 Burndown Chart
========================

Sprint: Authentication Features
Duration: Feb 1-14, 2026
Total Story Points: 40

Day    Ideal    Actual    Remaining
-----------------------------------
1      40       40        40
2      37       38        38
3      34       36        36
4      31       35        35
5      28       32        32
6      25       30        30
7      22       28        28
8      19       25        25
9      16       22        22
10     13       18        18
11     10       15        15
12     7        12        12
13     4        8         8
14     0        0         0

Status: On track (slightly behind ideal, but manageable)
Risk: Low (team catching up in second week)

Generating chart visualization...
✅ Burndown chart saved to docs/reports/sprint-12-burndown.md
```

**Burndown Analysis:**
```
User: Analyze burndown for Sprint 12

Agent: 📊 Burndown Analysis: Sprint 12

Current Status:
- Remaining Points: 8 pts
- Ideal Remaining: 4 pts
- Variance: +4 pts (+10%)
- On Track: ⚠️ Slightly behind

Progress:
- Completed: 32 pts (80%)
- Completion Rate: 2.3 pts/day
- Required Rate: 2.9 pts/day

Trend Analysis:
- Started on track
- Slowed mid-sprint (Days 4-8)
- Catching up in final week

Recommendations:
- Maintain current pace
- Consider scope adjustment if needed
- Review blockers from Days 4-8
```

### Velocity Reports

**Velocity Report:**
```
User: Velocity report

Agent: Calculating team velocity...

Analyzing last 5 sprints...

Team Velocity Report
====================

Sprint        Points    Status
--------------------------------
Sprint 8      35        Completed
Sprint 9      38        Completed
Sprint 10     32        Completed
Sprint 11     40        Completed
Sprint 12     38        Completed

Average Velocity: 36.6 story points
Velocity Trend: ↗️ Increasing (+3 points average)
Forecast: Next sprint ~37 points

Velocity Chart:
[Visual chart showing velocity over time]

Insights:
- Velocity is stable and slightly increasing
- Team capacity is consistent
- No major velocity drops detected
- Predictability: Good (variance < 15%)

✅ Velocity report saved to docs/reports/velocity.md
```

**Velocity Forecast:**
```
User: Forecast velocity for next sprint

Agent: Velocity Forecast for Next Sprint

Historical Velocity:
- Last 3 sprints: 38, 40, 38 points
- Average: 38.7 points
- Trend: Stable

Forecast:
- Expected Velocity: 37-40 points
- Confidence: High (low variance)
- Recommendation: Plan for 38 points

Factors Considered:
- Team capacity: Stable
- No major changes expected
- Historical consistency: High
```

### Team Health Indicators

**Health Check:**
```
User: Team health check

Agent: Analyzing team health metrics...

Team Health Report
==================

Sprint Completion Rate: 95% ✅
- Last 5 sprints: 4/5 completed fully
- 1 sprint had 1 story carried over

Blocker Frequency: Low ✅
- Average blockers per sprint: 1.2
- Average blocker resolution time: 4 hours

Cycle Time: 3.2 days ✅
- Average time from In Progress to Done
- Target: < 5 days
- Status: Healthy

Lead Time: 5.8 days ✅
- Average time from creation to completion
- Target: < 7 days
- Status: Healthy

WIP: 4 items ✅
- Current work in progress
- WIP limit: 5
- Status: Within limit

Throughput: 8 items/week ✅
- Average items completed per week
- Trend: Stable

Overall Health: 🟢 Healthy
- All metrics within healthy ranges
- No major concerns identified
- Team performing well

✅ Health report saved to docs/reports/health.md
```

**Health Trends:**
```
User: Show health trends

Agent: Team Health Trends (Last 5 Sprints)

Sprint Completion Rate:
Sprint 8:  100% ✅
Sprint 9:  95%  ✅
Sprint 10: 90%  ⚠️
Sprint 11: 100% ✅
Sprint 12: 95%  ✅
Trend: Stable

Blocker Frequency:
Sprint 8:  1.0  ✅
Sprint 9:  1.5  ✅
Sprint 10: 2.0  ✅
Sprint 11: 0.5  ✅
Sprint 12: 1.2  ✅
Trend: Decreasing

Cycle Time:
Sprint 8:  3.5 days
Sprint 9:  3.2 days
Sprint 10: 3.8 days
Sprint 11: 3.0 days
Sprint 12: 3.2 days
Trend: Improving
```

### Sprint Reports

**Comprehensive Sprint Report:**
```
User: Sprint report for Sprint 12

Agent: Generating sprint report...

Sprint 12 Report: Authentication Features
==========================================

Sprint Overview:
- Duration: Feb 1-14, 2026 (2 weeks)
- Goal: Complete authentication features
- Team: Alice, Bob, Charlie

Completed Work:
- Planned: 40 story points
- Completed: 38 story points (95%)
- Stories Done: 6/7
- Tasks Completed: 24/26

Completed Stories:
✓ PROJ-456: User Login (5 pts)
✓ PROJ-457: Email Verification (3 pts)
✓ PROJ-458: Password Reset (3 pts)
✓ PROJ-459: User Profile View (8 pts)
✓ PROJ-460: Profile Edit (8 pts)
✓ PROJ-461: Session Management (5 pts)
✗ PROJ-462: OAuth Integration (8 pts) - Carried over

Metrics:
- Velocity: 38 points (target: 40)
- Burndown: On track
- Cycle Time: 3.1 days (avg)
- Blocker Count: 2 (resolved quickly)

Blockers Resolved:
- OAuth configuration access (resolved Day 6)
- Session storage issue (resolved Day 9)

Retrospective Highlights:
- What went well: Clear sprint goal, effective standups
- Improvements: Better estimation for integrations
- Action items: Document dependencies upfront

Next Sprint Preview:
- Sprint 13 planning scheduled
- OAuth Integration prioritized
- Estimated capacity: 40 points

✅ Sprint report saved to docs/reports/sprint-12-report.md
```

### Dashboards

**Metrics Dashboard:**
```
User: Create metrics dashboard

Agent: Creating metrics dashboard...

Dashboard Components:
- Velocity trend chart
- Current sprint burndown
- Cycle time distribution
- WIP by column
- Team health indicators
- Recent completions

Generating dashboard page...
✅ Dashboard created at docs/dashboards/metrics.md

Dashboard includes:
- Interactive charts
- Real-time metrics
- Historical trends
- Health indicators
- Actionable insights
```

**Custom Dashboard:**
```
User: Create dashboard for stakeholders

Agent: Creating stakeholder dashboard...

Including:
- High-level metrics
- Release progress
- Team velocity
- Health summary
- Upcoming milestones

✅ Dashboard created at docs/dashboards/stakeholder.md
```

## Report Types

### Burndown Reports

**Sprint Burndown:**
- Daily remaining work
- Ideal vs. actual comparison
- Trend analysis
- Risk assessment

**Release Burndown:**
- Remaining work across sprints
- Release date prediction
- Scope adjustment recommendations

### Velocity Reports

**Historical Velocity:**
- Sprint-by-sprint velocity
- Average and trends
- Predictability metrics
- Capacity analysis

**Velocity Forecast:**
- Next sprint prediction
- Release date estimation
- Capacity planning

### Health Reports

**Team Health:**
- Sprint completion rate
- Blocker frequency
- Cycle time
- Lead time
- WIP status
- Throughput

**Health Trends:**
- Historical health metrics
- Trend analysis
- Improvement areas
- Risk indicators

### Sprint Reports

**Sprint Summary:**
- Completed work
- Metrics and trends
- Blockers and resolutions
- Retrospective insights

**Sprint Comparison:**
- Compare multiple sprints
- Identify patterns
- Track improvements
- Benchmark performance

### Forecast Reports

**Sprint Forecast:**
- Predicted completion
- Risk assessment
- Scope recommendations

**Release Forecast:**
- Release date prediction
- Scope completion estimate
- Risk factors

## Configuration Options

### Report Configuration

**Report Formats:**
```json
{
  "reports": {
    "formats": ["markdown", "html", "json", "csv"],
    "defaultFormat": "markdown",
    "includeCharts": true,
    "chartFormat": "ascii"
  }
}
```

**Dashboard Configuration:**
```json
{
  "dashboard": {
    "components": [
      "velocity",
      "burndown",
      "cycleTime",
      "wip",
      "health"
    ],
    "refreshInterval": "daily",
    "autoGenerate": true
  }
}
```

### Metrics Configuration

**Velocity Settings:**
```json
{
  "velocity": {
    "sprintCount": 5,
    "includeForecast": true,
    "confidenceLevel": 0.8
  }
}
```

**Health Settings:**
```json
{
  "health": {
    "metrics": [
      "sprintCompletionRate",
      "blockerFrequency",
      "cycleTime",
      "leadTime",
      "wip",
      "throughput"
    ],
    "thresholds": {
      "sprintCompletionRate": 0.85,
      "blockerFrequency": 2.0,
      "cycleTime": 5.0,
      "leadTime": 7.0
    }
  }
}
```

## Metrics Interpretation

### Velocity Metrics

**Good Velocity:**
- Consistent across sprints
- Variance < 15%
- Slight upward trend
- Predictable

**Warning Signs:**
- High variance (> 25%)
- Declining trend
- Unpredictable
- Capacity issues

### Burndown Metrics

**On Track:**
- Actual close to ideal
- Variance < 10%
- Steady progress
- No major spikes

**At Risk:**
- Actual above ideal
- Variance > 15%
- Slowing progress
- Blockers present

### Health Metrics

**Healthy Team:**
- Sprint completion > 85%
- Low blocker frequency (< 2/sprint)
- Cycle time < 5 days
- WIP within limits

**Concerning Signs:**
- Sprint completion < 70%
- High blocker frequency (> 4/sprint)
- Cycle time > 7 days
- WIP over limits

## Dashboard Generation

### Dashboard Components

**Velocity Dashboard:**
- Velocity trend chart
- Historical velocity table
- Forecast visualization
- Predictability metrics

**Burndown Dashboard:**
- Current sprint burndown
- Historical burndowns
- Trend comparison
- Risk indicators

**Health Dashboard:**
- Health score
- Metric breakdown
- Trend analysis
- Improvement areas

**Combined Dashboard:**
- All key metrics
- Interactive charts
- Real-time updates
- Actionable insights

### Dashboard Formats

**Markdown Dashboard:**
- Text-based charts
- Tables and metrics
- Easy to read
- Version controlled

**HTML Dashboard:**
- Interactive charts
- Visualizations
- Real-time updates
- Web accessible

**JSON Dashboard:**
- Raw data format
- API accessible
- Programmatic access
- Integration friendly

## Best Practices

### Report Generation

1. **Regular Reporting**
   - Generate reports weekly
   - Sprint-end reports
   - Monthly summaries
   - Quarterly reviews

2. **Consistent Format**
   - Use standard templates
   - Maintain format consistency
   - Include context
   - Provide explanations

3. **Actionable Insights**
   - Highlight trends
   - Identify risks
   - Provide recommendations
   - Focus on improvement

### Metrics Interpretation

1. **Context Matters**
   - Consider team context
   - Account for external factors
   - Look at trends, not single points
   - Combine multiple metrics

2. **Avoid Gaming**
   - Don't optimize metrics
   - Focus on value delivery
   - Use metrics for improvement
   - Trust the process

3. **Stakeholder Communication**
   - Use clear language
   - Provide context
   - Explain trends
   - Focus on value

### Dashboard Design

1. **Key Metrics First**
   - Show most important metrics
   - Limit dashboard size
   - Focus on actionable data
   - Update regularly

2. **Visual Clarity**
   - Use clear charts
   - Consistent formatting
   - Color coding
   - Easy to scan

3. **Accessibility**
   - Multiple formats
   - Easy to share
   - Mobile friendly
   - Export options

## Common Use Cases

### Use Case 1: Sprint Review

**Scenario:** Preparing sprint review presentation

**Workflow:**
1. Generate sprint report
2. Create burndown chart
3. Calculate velocity
4. Assess health metrics
5. Create presentation

**Commands:**
```
"Sprint report for Sprint 12"
"Show burndown for Sprint 12"
"Velocity report"
"Team health check"
```

### Use Case 2: Release Planning

**Scenario:** Planning release timeline

**Workflow:**
1. Review velocity trends
2. Calculate remaining work
3. Forecast release date
4. Assess risks
5. Create release plan

**Commands:**
```
"Velocity report"
"Forecast release date"
"Show release burndown"
```

### Use Case 3: Team Health Assessment

**Scenario:** Assessing team performance

**Workflow:**
1. Generate health report
2. Review trends
3. Identify issues
4. Create improvement plan
5. Track progress

**Commands:**
```
"Team health check"
"Show health trends"
"Health dashboard"
```

### Use Case 4: Stakeholder Reporting

**Scenario:** Reporting to stakeholders

**Workflow:**
1. Create stakeholder dashboard
2. Generate summary report
3. Highlight key metrics
4. Provide context
5. Share dashboard

**Commands:**
```
"Create stakeholder dashboard"
"Generate summary report"
"Show key metrics"
```

## Troubleshooting

### Report Generation Issues

**Problem:** Reports incomplete

**Solutions:**
- Verify data availability
- Check date ranges
- Ensure sprint data complete
- Review backend queries

### Metrics Calculation Issues

**Problem:** Metrics incorrect

**Solutions:**
- Verify data quality
- Check calculation formulas
- Review date fields
- Validate status transitions

### Dashboard Issues

**Problem:** Dashboard not updating

**Solutions:**
- Check refresh interval
- Verify data sources
- Review dashboard configuration
- Check backend connection

## References

- [PM System User Guide](../USER_GUIDE.md)
- [Methodology Reference](../METHODOLOGY_REFERENCE.md)
- [Metrics Reference](../METRICS_REFERENCE.md)
- [Product Owner Agent](./PRODUCT_OWNER_AGENT.md)
- [Sprint Master Agent](./SPRINT_MASTER_AGENT.md)
- [Task Manager Agent](./TASK_MANAGER_AGENT.md)

---

*Reporting Agent Reference v1.0.0*  
*Grounded in Axiom 0: Love and Trust*
