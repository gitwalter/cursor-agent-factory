# Metrics Reference Guide

## Table of Contents

1. [Velocity Metrics](#velocity-metrics)
2. [Flow Metrics](#flow-metrics)
3. [Quality Metrics](#quality-metrics)
4. [Predictive Metrics](#predictive-metrics)
5. [Health Metrics](#health-metrics)
6. [Best Practices](#best-practices)
7. [Sources and References](#sources-and-references)

## Velocity Metrics

### Velocity

**Definition**: Average story points completed per sprint

**Formula**: `SUM(completed_story_points) / number_of_sprints`

**Unit**: Points

**Interpretation**:
- ✅ **Good**: Consistent velocity indicates predictable delivery
- ⚠️ **Warning**: High variance (> 25%) suggests estimation issues or external factors

**Thresholds**:
- Excellent: Variance < 15%
- Good: Variance < 25%
- Warning: Variance > 25%

**Minimum Requirements**: 3+ sprints of historical data

**Use Cases**:
- Sprint planning capacity estimation
- Release date prediction
- Team capacity assessment

**Sources**: Sprint completion data

---

### Velocity Trend

**Definition**: Directional change in velocity over time

**Formula**: `linear_regression_slope(velocity_values)`

**Unit**: Points per sprint

**Interpretation**:
- ✅ **Good**: Positive trend indicates improving capacity
- ⚠️ **Warning**: Negative trend (< -2 points/sprint) suggests declining capacity

**Thresholds**:
- Excellent: Trend > +2 points/sprint
- Good: Trend > 0
- Warning: Trend < -2 points/sprint

**Minimum Requirements**: 5+ sprints of historical data

**Use Cases**:
- Identify capacity trends
- Assess team improvement
- Predict future velocity

**Sources**: Historical velocity data

---

### Sprint Completion Rate

**Definition**: Percentage of committed work completed per sprint

**Formula**: `(completed_story_points / committed_story_points) * 100`

**Unit**: Percentage

**Interpretation**:
- ✅ **Good**: 85-100% indicates realistic commitment
- ⚠️ **Warning**: < 70% suggests overcommitment, > 120% suggests undercommitment

**Thresholds**:
- Excellent: 85-100%
- Good: 75-110%
- Warning: < 70% or > 120%

**Use Cases**:
- Assess sprint planning accuracy
- Identify commitment issues
- Improve estimation

**Sources**: Sprint commitment and completion data

---

### Carry Over Rate

**Definition**: Percentage of sprint work carried to next sprint

**Formula**: `(carried_over_story_points / sprint_total_story_points) * 100`

**Unit**: Percentage

**Interpretation**:
- ✅ **Good**: < 10% indicates good sprint closure
- ⚠️ **Warning**: > 20% suggests planning or execution issues

**Thresholds**:
- Excellent: < 5%
- Good: < 10%
- Warning: > 20%

**Use Cases**:
- Assess sprint closure quality
- Identify planning issues
- Improve sprint execution

**Sources**: Sprint carry-over data

## Flow Metrics

### Lead Time

**Definition**: Time from work item creation to completion

**Formula**: `AVG(completion_date - creation_date)`

**Unit**: Days

**Interpretation**:
- ✅ **Good**: Lower lead time indicates faster delivery
- ⚠️ **Warning**: Increasing lead time suggests bottlenecks

**Thresholds**:
- Excellent: < 7 days
- Good: < 14 days
- Warning: > 21 days

**Minimum Requirements**: 10+ completed items

**Use Cases**:
- Customer delivery time assessment
- Process efficiency measurement
- Bottleneck identification

**Sources**: Work item cycle data (creation to completion)

**References**: 
- [DORA Metrics](https://www.devops-research.com/research.html)
- [Kanban Guide](https://kanban.university/kanban-guide/)

---

### Cycle Time

**Definition**: Time from work start to completion (in progress to done)

**Formula**: `AVG(completion_date - start_date)`

**Unit**: Days

**Interpretation**:
- ✅ **Good**: Lower cycle time indicates efficient execution
- ⚠️ **Warning**: Increasing cycle time suggests process inefficiencies

**Thresholds**:
- Excellent: < 3 days
- Good: < 7 days
- Warning: > 14 days

**Minimum Requirements**: 10+ completed items

**Use Cases**:
- Execution efficiency measurement
- Process optimization
- WIP limit validation

**Sources**: Work item cycle data (start to completion)

**References**:
- [DORA Metrics](https://www.devops-research.com/research.html)
- [Kanban Guide](https://kanban.university/kanban-guide/)

---

### Throughput

**Definition**: Number of work items completed per unit time

**Formula**: `COUNT(completed_items) / time_period`

**Unit**: Count (items per week/month)

**Interpretation**:
- ✅ **Good**: Consistent or increasing throughput indicates stable capacity
- ⚠️ **Warning**: Decreasing throughput (> -10%) suggests capacity constraints

**Thresholds**:
- Excellent: Trend > 0
- Good: Stable
- Warning: Trend < -10%

**Minimum Requirements**: 4+ time periods

**Use Cases**:
- Capacity assessment
- Process stability measurement
- Delivery predictability

**Sources**: Work item completion data

**References**:
- [Kanban Guide](https://kanban.university/kanban-guide/)
- [Little's Law](https://en.wikipedia.org/wiki/Little%27s_law)

---

### Work In Progress (WIP)

**Definition**: Number of work items currently in progress

**Formula**: `COUNT(items WHERE status = 'in_progress')`

**Unit**: Count

**Interpretation**:
- ✅ **Good**: WIP within team capacity indicates good flow
- ⚠️ **Warning**: High WIP (> team_size * 2) suggests context switching

**Thresholds**:
- Excellent: WIP <= team_size
- Good: WIP <= team_size * 1.5
- Warning: WIP > team_size * 2

**Use Cases**:
- Flow management
- Context switching assessment
- WIP limit enforcement

**Sources**: Current work item status

**References**:
- [Kanban Guide](https://kanban.university/kanban-guide/)
- [Little's Law](https://en.wikipedia.org/wiki/Little%27s_law)

## Quality Metrics

### Bug Ratio

**Definition**: Percentage of work items that are bugs

**Formula**: `(bug_count / total_work_items) * 100`

**Unit**: Percentage

**Interpretation**:
- ✅ **Good**: < 20% indicates good quality
- ⚠️ **Warning**: > 30% suggests quality issues

**Thresholds**:
- Excellent: < 10%
- Good: < 20%
- Warning: > 30%

**Use Cases**:
- Quality assessment
- Process improvement focus
- Testing effectiveness

**Sources**: Work item type distribution

**References**:
- [Agile Alliance](https://www.agilealliance.org/)
- [Six Sigma](https://asq.org/quality-resources/six-sigma)

---

### Rework Rate

**Definition**: Percentage of work items requiring rework

**Formula**: `(reworked_items / total_completed_items) * 100`

**Unit**: Percentage

**Interpretation**:
- ✅ **Good**: < 10% indicates good first-time quality
- ⚠️ **Warning**: > 20% suggests requirements or quality issues

**Thresholds**:
- Excellent: < 5%
- Good: < 10%
- Warning: > 20%

**Minimum Requirements**: 3+ sprints of data

**Use Cases**:
- First-time quality assessment
- Requirements clarity measurement
- Process improvement

**Sources**: Work item rework tracking

**References**:
- [Six Sigma](https://asq.org/quality-resources/six-sigma)
- [Lean Principles](https://www.lean.org/)

---

### Escaped Defects

**Definition**: Number of defects found in production

**Formula**: `COUNT(defects WHERE found_in = 'production')`

**Unit**: Count

**Interpretation**:
- ✅ **Good**: 0-1 per sprint indicates good quality gates
- ⚠️ **Warning**: > 3 per sprint suggests testing gaps

**Thresholds**:
- Excellent: 0
- Good: <= 1
- Warning: > 3

**Use Cases**:
- Quality gate effectiveness
- Testing coverage assessment
- Production stability

**Sources**: Defect tracking

**References**:
- [DORA Metrics](https://www.devops-research.com/research.html)
- [Agile Testing](https://www.agilealliance.org/agile101/)

## Predictive Metrics

### Sprint Forecast

**Definition**: Predicted story points for next sprint based on historical velocity

**Formula**: `AVG(historical_velocity) * confidence_factor`

**Unit**: Points

**Interpretation**:
- ✅ **Good**: Forecast within 15% of actual indicates good predictability
- ⚠️ **Warning**: Forecast variance > 25% suggests estimation issues

**Thresholds**:
- Excellent: Variance < 10%
- Good: Variance < 15%
- Warning: Variance > 25%

**Minimum Requirements**: 3+ sprints of historical data

**Use Cases**:
- Sprint planning
- Capacity estimation
- Predictability assessment

**Sources**: Velocity forecasting

**References**:
- [Scrum Guide](https://scrumguides.org/)
- [Agile Estimation](https://www.agilealliance.org/agile101/)

---

### Release Prediction

**Definition**: Predicted release date based on velocity and remaining work

**Formula**: `current_date + (remaining_story_points / average_velocity) * sprint_duration`

**Unit**: Date

**Interpretation**:
- ✅ **Good**: Prediction within 1 sprint indicates good planning
- ⚠️ **Warning**: Prediction variance > 2 sprints suggests scope or velocity issues

**Thresholds**:
- Excellent: Variance < 0.5 sprints
- Good: Variance < 1 sprint
- Warning: Variance > 2 sprints

**Minimum Requirements**: 5+ sprints of historical data

**Use Cases**:
- Release planning
- Stakeholder communication
- Risk assessment

**Sources**: Release planning data

**References**:
- [Scrum Guide](https://scrumguides.org/)
- [Release Planning](https://www.agilealliance.org/agile101/)

---

### Risk Score

**Definition**: Composite risk score based on multiple factors

**Formula**: `weighted_sum(blocker_frequency, stale_items, velocity_variance, bug_ratio)`

**Unit**: Score (0-100)

**Interpretation**:
- ✅ **Good**: Score < 30 indicates low risk
- ⚠️ **Warning**: Score > 60 suggests high risk

**Thresholds**:
- Excellent: < 20
- Good: < 30
- Warning: > 60

**Minimum Requirements**: 3+ sprints of data

**Use Cases**:
- Risk assessment
- Early warning system
- Stakeholder reporting

**Sources**: Composite risk calculation

**References**:
- [PMI Risk Management](https://www.pmi.org/learning/library/risk-management-overview-7090)
- [Agile Risk Management](https://www.agilealliance.org/agile101/)

## Health Metrics

### Blocker Frequency

**Definition**: Average number of blockers per sprint

**Formula**: `AVG(blocker_count_per_sprint)`

**Unit**: Count

**Interpretation**:
- ✅ **Good**: < 2 blockers per sprint indicates good flow
- ⚠️ **Warning**: > 4 blockers per sprint suggests dependency or resource issues

**Thresholds**:
- Excellent: < 1
- Good: < 2
- Warning: > 4

**Minimum Requirements**: 3+ sprints of data

**Use Cases**:
- Process health assessment
- Dependency management
- Resource allocation

**Sources**: Blocker tracking

**References**:
- [Scrum Guide](https://scrumguides.org/)
- [Agile Practices](https://www.agilealliance.org/agile101/)

---

### Stale Items

**Definition**: Number of work items without activity for threshold period

**Formula**: `COUNT(items WHERE last_updated < current_date - stale_threshold)`

**Unit**: Count

**Interpretation**:
- ✅ **Good**: < 2 stale items indicates active work
- ⚠️ **Warning**: > 5 stale items suggests abandonment or bottlenecks

**Thresholds**:
- Excellent: 0
- Good: < 2
- Warning: > 5

**Stale Threshold**: 7 days (configurable)

**Use Cases**:
- Work health monitoring
- Bottleneck identification
- Process improvement

**Sources**: Work item activity tracking

**References**:
- [Kanban Guide](https://kanban.university/kanban-guide/)
- [Flow Management](https://www.agilealliance.org/agile101/)

---

### Assignment Balance

**Definition**: Distribution of work across team members

**Formula**: `standard_deviation(work_items_per_person) / mean(work_items_per_person)`

**Unit**: Coefficient of Variation

**Interpretation**:
- ✅ **Good**: CV < 0.3 indicates balanced workload
- ⚠️ **Warning**: CV > 0.5 suggests imbalanced distribution

**Thresholds**:
- Excellent: < 0.2
- Good: < 0.3
- Warning: > 0.5

**Use Cases**:
- Workload balance assessment
- Resource allocation
- Team health monitoring

**Sources**: Work item assignment data

**References**:
- [Team Dynamics](https://www.agilealliance.org/agile101/)
- [Scrum Guide](https://scrumguides.org/)

## Best Practices

### Metric Collection

1. **Consistency**: Collect metrics at the same time and frequency
2. **Automation**: Use automated data collection when possible
3. **Validation**: Validate data quality before calculation
4. **Documentation**: Document data sources and assumptions

### Metric Interpretation

1. **Context**: Consider context when interpreting metrics
2. **Trends**: Look for trends rather than single data points
3. **Combination**: Combine multiple metrics for better insights
4. **Avoid Gaming**: Don't optimize metrics at the expense of value

### Metric Reporting

1. **Regularity**: Report metrics regularly (sprint-end, monthly)
2. **Visualization**: Use charts and graphs for clarity
3. **Context**: Include explanations and context
4. **Actionable**: Focus on actionable insights, not just numbers

### Common Pitfalls

1. **Vanity Metrics**: Avoid metrics that don't drive improvement
2. **Over-Measurement**: Don't track too many metrics
3. **Misinterpretation**: Understand what metrics actually measure
4. **Gaming**: Don't optimize metrics instead of improving process

## Sources and References

### Official Methodology Sources

- **Scrum Guide**: [scrumguides.org](https://scrumguides.org/)
- **Kanban Guide**: [kanban.university/kanban-guide](https://kanban.university/kanban-guide/)
- **SAFe Framework**: [scaledagileframework.com](https://scaledagileframework.com/)
- **PMI**: [pmi.org](https://www.pmi.org/)
- **Lean Enterprise**: [lean.org](https://www.lean.org/)
- **ASQ**: [asq.org](https://asq.org/)

### Research and Standards

- **DORA Metrics**: [devops-research.com](https://www.devops-research.com/research.html)
- **Agile Alliance**: [agilealliance.org](https://www.agilealliance.org/)
- **IEEE Software Engineering**: [ieee.org](https://www.ieee.org/)

### Key Concepts

- **Little's Law**: [wikipedia.org/wiki/Little's_law](https://en.wikipedia.org/wiki/Little%27s_law)
- **Cumulative Flow Diagram**: [kanban.university](https://kanban.university/)
- **Burndown Charts**: [scrumguides.org](https://scrumguides.org/)
- **Velocity Tracking**: [scrum.org](https://www.scrum.org/)

### Additional Reading

- **Accelerate** (Forsgren, Humble, Kim) - DORA metrics research
- **The Scrum Guide** - Official Scrum framework
- **Kanban: Successful Evolutionary Change** (Anderson) - Kanban methodology
- **The Lean Startup** (Ries) - Lean principles

---

*For methodology details, see [METHODOLOGY_REFERENCE.md](./METHODOLOGY_REFERENCE.md)*  
*For usage details, see [USER_GUIDE.md](./USER_GUIDE.md)*
