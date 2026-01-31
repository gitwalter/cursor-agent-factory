# Getting Started with Cursor Agent Factory

Welcome! This guide will help you find the perfect onboarding path for your needs.

---

## Choose Your Path

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    WELCOME TO CURSOR AGENT FACTORY                            ║
║                                                                              ║
║  "Every great agent system begins with understanding who you are             ║
║   and what you're trying to achieve."                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### How many people will use this system?

| Path | Team Size | Duration | Best For |
|------|-----------|----------|----------|
| [Express Lane](#express-lane) | Just me | 10-15 min | Quick personal setup |
| [Team Huddle](#team-huddle) | 2-5 people | 1-2 hours | Small team alignment |
| [Workshop Series](#workshop-series) | 6+ people | 11-15 hours | Enterprise transformation |
| [Existing Repo](#existing-repository) | Any | 15-30 min | Enhance existing projects |
| [Quick Demo](#quick-demo) | Any | 30 seconds | See it in action first |

---

## Quick Demo

Want to see what the factory creates before committing? Run the quickstart:

```powershell
python cli/factory_cli.py --quickstart
```

In 30 seconds, you'll have a complete demo project. See [QUICKSTART.md](QUICKSTART.md) for details.

---

## Express Lane

**Duration:** 10-15 minutes  
**Team Size:** Individual  
**Best For:** Developers who know what they want and want to get started quickly

### What You'll Do

1. **Welcome & Intent** (2 min) - Share your dream for this project
2. **Values Check** (2 min) - Pick 3 values that matter most
3. **Stack Discovery** (3 min) - Choose your technology with smart suggestions
4. **Agent Design** (3 min) - Meet your AI team
5. **Wisdom Capture** (2 min) - Share one lesson learned
6. **Magic Preview** (2 min) - See what you'll get before confirming
7. **Celebration & Launch** (1 min) - Generate with fanfare!

### How to Start

In Cursor, open a chat and say:

```
I want to create a new agent system using Express Lane onboarding
```

Or use the skill directly:

```
/skill express-onboarding
```

### What You'll Get

- Personalized `.cursorrules` with your values embedded
- `PURPOSE.md` capturing your mission
- Custom agents and skills for your stack
- `knowledge/team-wisdom.json` with your captured insights

---

## Team Huddle

**Duration:** 1-2 hours  
**Team Size:** 2-5 people  
**Best For:** Small teams who want alignment without a multi-day workshop

### What You'll Do Together

| Time | Activity | Purpose |
|------|----------|---------|
| 0:00 | Lightning Hopes (5 min) | Each person shares one hope |
| 0:05 | Future Headlines (15 min) | Align on vision through imagination |
| 0:20 | Values Speed Round (10 min) | Rank 3 team values by vote |
| 0:30 | Stack Consensus (15 min) | Decide technology together |
| 0:45 | Agent Character Design (20 min) | Create your AI team creatively |
| 1:05 | Wisdom Harvest (10 min) | Capture the team's best practices |
| 1:15 | Preview & Launch (15 min) | Review and generate |
| 1:30 | Gratitude Close (5 min) | End with appreciation |

### How to Start

Gather your team (in-person or video call), open Cursor, and say:

```
We want to run a Team Huddle for our project
```

Or use the skill directly:

```
/skill team-huddle-onboarding
```

### What You'll Get

- `TEAM_CHARTER.md` - Your shared vision
- `PURPOSE.md` - Mission and success criteria
- `knowledge/team-wisdom.json` - Collective knowledge
- Custom agents reflecting team personality
- Shared values embedded in `.cursorrules`

---

## Workshop Series

**Duration:** 11-15 hours (across 5 sessions)  
**Team Size:** 6+ people  
**Best For:** Enterprise teams, major projects, organizational transformation

### The 5 Workshops

| # | Workshop | Duration | What Happens |
|---|----------|----------|--------------|
| 1 | Vision Quest | 2-3 hours | Define mission through Future Headlines & Stakeholder Safari |
| 2 | Ethics Arena | 2 hours | Establish values through Dilemma Duel & Value Auction |
| 3 | Stack Safari | 2-3 hours | Choose technology through Trade-Off Tetris & Architecture Pictionary |
| 4 | Agent Assembly | 3-4 hours | Design agents through Trading Cards & Skill Bingo |
| 5 | Integration Celebration | 1.5-2 hours | Generate system with Demo Derby & Gratitude Circle |

### How to Start

In Cursor, say:

```
We want to run the full Team Workshop series for our project
```

Or see the complete facilitator's guide: [TEAM_WORKSHOP_GUIDE.md](TEAM_WORKSHOP_GUIDE.md)

### What You'll Get

Everything from Team Huddle, plus:
- Deep ethical framework
- Full methodology configuration
- Comprehensive agent roster
- Complete skill library
- Team practices and enforcement patterns

---

## Existing Repository

**Duration:** 15-30 minutes  
**Team Size:** Any  
**Best For:** Adding AI agents to projects that already have code

### What Happens

1. **Analysis** - Factory detects your tech stack and existing artifacts
2. **Blueprint Matching** - Suggests the best blueprint for your stack
3. **Conflict Resolution** - Handles any overlapping configurations
4. **Enhancement** - Adds missing agents, skills, and knowledge
5. **Backup** - Creates rollback point for safety

### How to Start

```powershell
# Analyze your repo first
python cli/factory_cli.py --analyze C:\Projects\my-existing-repo

# Preview changes
python cli/factory_cli.py --onboard C:\Projects\my-existing-repo --dry-run

# Execute onboarding
python cli/factory_cli.py --onboard C:\Projects\my-existing-repo
```

Or in Cursor chat:

```
Please onboard my existing repository at C:\Projects\my-existing-repo
```

See [ONBOARDING_GUIDE.md](ONBOARDING_GUIDE.md) for full details.

---

## After Onboarding: Your First Week

No matter which path you chose, see the [FIRST_WEEK_GUIDE.md](FIRST_WEEK_GUIDE.md) to make the most of your new agent system:

- **Day 1:** Meet your agents
- **Day 2:** Try a workflow
- **Day 3:** Add domain knowledge
- **Day 4:** Customize an agent
- **Day 5:** Team retrospective

---

## Path Comparison

| Feature | Express Lane | Team Huddle | Workshop Series |
|---------|--------------|-------------|-----------------|
| Duration | 10-15 min | 1-2 hours | 11-15 hours |
| Values capture | 3 values | Team vote | Deep exploration |
| Vision alignment | Individual | Quick consensus | Multi-session |
| Wisdom harvest | 1 question | 3 questions | Full sessions |
| Agent design | Template-based | Creative naming | Trading cards |
| Methodology | Default | Selected | Fully configured |
| Games | None | 3 mini-games | 10+ games |
| Celebration | Inline | Group moment | Full ceremony |

---

## Need Help?

| Question | Where to Look |
|----------|---------------|
| Installation issues | [PREREQUISITES.md](PREREQUISITES.md) |
| Errors during generation | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| Understanding the architecture | [LAYERED_ARCHITECTURE.md](LAYERED_ARCHITECTURE.md) |
| Complete reference | [FACTORY_REFERENCE.md](FACTORY_REFERENCE.md) |
| Example walkthroughs | [examples/](examples/) |

---

## Philosophy

> "All being and doing is grounded in love and trust." — Axiom 0

Every onboarding path is designed to capture not just *what* you're building, but *why* it matters and *who* you are as a team. The technical artifacts are important, but the spirit you bring to the work is what makes the difference.

---

*Cursor Agent Factory v2.0*  
*Start with purpose. Build with excellence. Serve with love.*
