# Your First Week with Cursor Agent Factory

Congratulations on creating your agent system! This guide will help you get the most out of it during your first week.

---

## Day 1: Meet Your Agents

Your first day is about getting comfortable with your new AI teammates.

### Step 1: Open Your Project

Open your generated project folder in Cursor IDE. The `.cursorrules` file will automatically configure agent behavior.

### Step 2: Say Hello

Start a chat and introduce yourself:

```
Hi! I just set up this agent system. Can you tell me what agents 
and skills are available?
```

Your agent will respond with an overview of your configured agents and their capabilities.

### Step 3: Try a Simple Request

Ask for something simple to see how your agents respond:

```
Review this README file and suggest improvements.
```

Or:

```
Explain the purpose of this project based on PURPOSE.md.
```

### Step 4: Explore PURPOSE.md

Open `PURPOSE.md` and read through it. This document captures:
- Your mission statement
- Who you're serving
- How success is measured

Everything your agents do should align with this purpose.

### Checkpoint

By end of Day 1, you should be able to:
- [ ] Open the project in Cursor
- [ ] Have a basic conversation with your agents
- [ ] Understand what's in PURPOSE.md

---

## Day 2: Try a Workflow

Today you'll use your first skill-based workflow.

### If You Have a Bug to Fix

Try the bugfix workflow:

```
I need to fix a bug: [describe the bug or paste the ticket ID]
```

Your agent will follow the bugfix-workflow skill:
1. Understand the issue
2. Investigate the code
3. Propose a fix
4. Generate tests

### If You Have a Feature to Build

Try the feature workflow:

```
I need to implement a new feature: [describe the feature]
```

Your agent will guide you through the feature-workflow skill.

### If You Just Want to Explore

Try the grounding skill:

```
Help me understand how [component] works in this codebase.
```

### Pro Tip: Mention Skills Explicitly

You can invoke skills directly:

```
Using the tdd skill, help me write tests for the user service.
```

### Checkpoint

By end of Day 2, you should be able to:
- [ ] Complete one workflow (bugfix, feature, or exploration)
- [ ] Understand how skills structure the agent's work

---

## Day 3: Add Domain Knowledge

Your agents become smarter when you give them domain knowledge.

### Step 1: Check Your Knowledge Files

Look in the `knowledge/` folder. You might see:
- `team-wisdom.json` - Lessons learned during onboarding
- `{language}-patterns.json` - Language-specific patterns
- Other domain files

### Step 2: Add Something New

Think about knowledge your agents should have:
- **Terminology**: Domain-specific terms and definitions
- **Patterns**: Code patterns your team uses
- **Rules**: Business rules not obvious from code

Create or edit a knowledge file:

```json
// knowledge/domain-terms.json
{
  "glossary": {
    "ACH": "Automated Clearing House - bank transfer system",
    "Settlement": "When funds actually move between accounts"
  }
}
```

### Step 3: Test It

Ask your agent about the new knowledge:

```
What does ACH mean in our system?
```

If you've added it correctly, the agent should know.

### Step 4: Add Wisdom

Did something happen today worth remembering? Add it:

```json
// knowledge/team-wisdom.json
{
  "lessonsLearned": [
    {
      "insight": "Always check rate limits before calling external APIs",
      "date": "2026-01-31",
      "source": "Production incident"
    }
  ]
}
```

### Checkpoint

By end of Day 3, you should have:
- [ ] Explored the existing knowledge files
- [ ] Added at least one new piece of knowledge
- [ ] Verified the agent can use it

---

## Day 4: Customize an Agent

Today you'll make an agent more useful for your specific needs.

### Step 1: Open an Agent Definition

Look in `.cursor/agents/`. Open one, like `code-reviewer.md`.

### Step 2: Understand the Structure

Agent files have:
- **Frontmatter**: Name, skills, knowledge references
- **Purpose**: What this agent does
- **When Activated**: Trigger phrases
- **Workflow**: How it operates

### Step 3: Add a Custom Behavior

Add something specific to your project. For example, in code-reviewer:

```markdown
## Additional Checks

For this project specifically:
- Always check for proper error handling in API endpoints
- Ensure database queries use parameterized statements
- Verify logging includes correlation IDs
```

### Step 4: Test Your Customization

```
Review this code, paying special attention to our project-specific standards.
```

### Pro Tip: Create a New Agent

If you need a specialized agent, copy an existing one and modify:

```bash
cp .cursor/agents/code-reviewer.md .cursor/agents/security-reviewer.md
```

Then edit to focus on security concerns.

### Checkpoint

By end of Day 4, you should have:
- [ ] Read and understood an agent definition
- [ ] Made at least one customization
- [ ] Tested that the customization works

---

## Day 5: Team Retrospective

End your first week by reflecting and improving.

### For Solo Developers

Take 15 minutes to reflect:

1. **What worked well?**
   - Which agents were most helpful?
   - Which workflows saved time?

2. **What was frustrating?**
   - Any gaps in knowledge files?
   - Any missing skills?

3. **What should change?**
   - Add notes to `knowledge/team-wisdom.json`
   - Create issues for improvements

### For Teams

Hold a brief retrospective (30 min):

#### Agenda

| Time | Activity |
|------|----------|
| 0:00 | Check-in: One word for your week with the agents (5 min) |
| 0:05 | What worked well? (10 min) |
| 0:15 | What was frustrating? (10 min) |
| 0:25 | Action items (5 min) |

#### Discussion Questions

1. Which agents did you use most?
2. Did the agents understand our codebase?
3. What knowledge should we add?
4. What skills are we missing?

#### Capture Actions

Add to `knowledge/team-wisdom.json`:

```json
{
  "retrospectives": [
    {
      "date": "2026-01-31",
      "week": 1,
      "whatWorked": ["Code reviews were faster", "TDD skill helped"],
      "improvements": ["Need more domain terminology", "Add deployment skill"],
      "actions": ["Add payment-terms.json", "Create deploy-workflow skill"]
    }
  ]
}
```

### Checkpoint

By end of Day 5:
- [ ] Reflected on your first week
- [ ] Identified at least one improvement
- [ ] Captured learnings in team-wisdom.json

---

## Quick Reference

### Common Commands

| What You Want | What to Say |
|---------------|-------------|
| Code review | "Review this code for issues" |
| Write tests | "Generate tests for [component]" |
| Fix a bug | "Help me fix [bug description]" |
| Understand code | "Explain how [component] works" |
| Start a feature | "I need to implement [feature]" |

### Invoking Skills Directly

```
Using the [skill-name] skill, help me [task].
```

Examples:
- "Using the tdd skill, create tests for the user service"
- "Using the grounding skill, verify the data model"
- "Using the bugfix-workflow skill, fix issue #123"

### Updating Knowledge

1. Edit JSON files in `knowledge/`
2. Add new files for new domains
3. Update `team-wisdom.json` with lessons learned

### Adding Agents

1. Create new `.md` file in `.cursor/agents/`
2. Follow the existing agent template format
3. Reference skills the agent should use

---

## Common Questions

### "My agent doesn't know about our codebase"

Agents learn through:
1. Reading the files you reference
2. Knowledge files you create
3. Patterns they discover

Add domain knowledge explicitly in `knowledge/` files.

### "The agent gave incorrect information"

1. Correct it in the chat: "Actually, that's not right. [correct info]"
2. Add the correct information to a knowledge file
3. The agent will learn from the correction

### "I want a skill that doesn't exist"

Create it! Add a new folder in `.cursor/skills/`:

```
.cursor/skills/my-new-skill/
└── SKILL.md
```

Follow the structure of existing skills.

### "Can I change the agent's personality?"

Yes! Edit the agent file and adjust:
- The tone in the Purpose section
- The approach in the Workflow section
- Add personality notes in a new section

---

## Beyond Week 1

### Week 2-4: Build Habits

- Use agents for all code reviews
- Follow skills for workflows
- Update knowledge files regularly

### Month 2: Optimize

- Review which agents you use most
- Enhance those agents further
- Archive or remove unused agents

### Ongoing: Evolve

- After major projects, update knowledge
- After incidents, capture lessons
- After retrospectives, improve skills

---

## Getting Help

| Question | Where to Look |
|----------|---------------|
| How skills work | [USAGE_GUIDE.md](USAGE_GUIDE.md) |
| Blueprint details | [FACTORY_REFERENCE.md](FACTORY_REFERENCE.md) |
| Architecture concepts | [LAYERED_ARCHITECTURE.md](LAYERED_ARCHITECTURE.md) |
| Troubleshooting | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |

---

## You're Ready!

After this first week, you're no longer a beginner. You understand:
- How to talk to your agents
- How workflows and skills structure work
- How to add domain knowledge
- How to customize agents
- How to reflect and improve

The agent system is now truly yours. It knows your values, your purpose, and increasingly, your domain knowledge.

Go build something amazing!

---

*Cursor Agent Factory v2.0*  
*Your first week is just the beginning.*
