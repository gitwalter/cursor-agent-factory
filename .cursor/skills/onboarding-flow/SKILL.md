---
name: onboarding-flow
description: Onboard existing repositories into the Cursor Agent Factory ecosystem
type: skill
knowledge: [skill-catalog.json, stack-capabilities.json]
---

# Onboarding Flow Skill

Integrate Cursor Agent Factory into existing repositories non-destructively, preserving existing artifacts while adding missing components.

## Philosophy

> Existing repositories have value. Our job is to enhance, not replace.

This skill enables seamless integration of the factory's agent system into repositories that already have code, configurations, and potentially some Cursor artifacts.

## When to Use

- User mentions an existing repository they want to enhance with AI agents
- User says "onboard my repo", "integrate into existing project", "add agents to my codebase"
- User provides a path to a local repository
- User wants to upgrade an older factory-generated setup

**For Team Onboarding:** If the user mentions a team (2+ people), consider suggesting the `team-workshop-onboarding` skill instead, which provides a collaborative workshop series with games and discussions.

## Prerequisites

Before starting the onboarding flow, ensure:
1. User has provided the repository path
2. Repository exists and is accessible
3. User has write permissions to the repository

## Process

### Step 1: Gather Repository Information

Ask user for the repository path:

```
"Please provide the path to the repository you want to onboard.
For example: C:\Projects\my-existing-app"
```

Validate the path exists and is a directory.

### Step 2: Analyze Repository

Run the repository analyzer to detect existing artifacts:

```bash
python cli/factory_cli.py --analyze <repo_path>
```

**MCP Tools:** None required (local operation)

Present the analysis results to user:
- Detected scenario (FRESH, MINIMAL, PARTIAL, UPGRADE, COMPLETE)
- Existing Cursor artifacts
- Detected technology stack
- Suggested blueprint

### Step 3: Confirm Blueprint Selection

Based on tech stack detection, suggest a blueprint:

```
"I detected the following:
- Languages: C#, TypeScript
- Frameworks: ASP.NET Core, React
- Suggested Blueprint: csharp-dotnet

Would you like to use this blueprint, or choose a different one?"
```

Available blueprints:
- `python-fastapi` - Python REST API development
- `typescript-react` - TypeScript web applications
- `java-spring` - Java enterprise applications
- `kotlin-spring` - Kotlin Spring applications
- `csharp-dotnet` - C#/.NET applications
- `sap-abap` - SAP ABAP development
- `sap-cpi-pi` - SAP CPI/PI integration

### Step 4: Preview Changes (Dry Run)

Before making any changes, show what will be modified:

```bash
python cli/factory_cli.py --onboard <repo_path> --blueprint <blueprint_id> --dry-run
```

Present the preview:
- Files that will be created
- Files that will be modified
- Conflicts that need resolution

### Step 5: Resolve Conflicts

For each conflict, ask user for resolution:

| Conflict Type | Options |
|---------------|---------|
| Existing agent with same name | Keep existing / Replace / Rename new |
| Existing .cursorrules | Merge / Replace / Keep existing |
| Existing knowledge file | Merge / Replace / Keep existing |
| Existing MCP config | Merge servers / Replace / Keep existing |

Default behavior: **Preserve existing** (ask for each conflict)

### Step 6: Execute Onboarding

With user confirmation, execute the onboarding:

```bash
python cli/factory_cli.py --onboard <repo_path> --blueprint <blueprint_id>
```

The process will:
1. Create backup of existing files
2. Generate missing directories
3. Add missing agents
4. Add missing skills
5. Merge or add .cursorrules sections
6. Add missing knowledge files
7. Report results

### Step 7: Provide Summary and Next Steps

After completion, provide:

```
"Onboarding complete!

Summary:
- Scenario: PARTIAL
- Files created: 8
- Files merged: 2
- Skipped (preserved): 3

A backup was created: .cursor-factory-backup/20260129_143022/

Next steps:
1. Review the merged .cursorrules file
2. Test the new agents by mentioning them
3. Check the knowledge/ folder for new reference files

If anything looks wrong, you can rollback:
python cli/factory_cli.py --rollback <repo_path>
"
```

## Scenario Handling

### FRESH Scenario (No Cursor artifacts)
- Full generation with all factory components
- Detect tech stack and suggest blueprint
- Create complete .cursor/ structure

### MINIMAL Scenario (Only .cursorrules)
- Augment with agents, skills, knowledge
- Merge new sections into existing .cursorrules
- Preserve user's custom rules

### PARTIAL Scenario (Some artifacts missing)
- Add only missing components
- Never overwrite existing agents/skills
- Offer to merge knowledge files

### UPGRADE Scenario (Old factory version)
- Show diff between old and new format
- Offer section-by-section upgrade
- Preserve user customizations

### COMPLETE Scenario (Fully configured)
- Report status
- Offer enhancements or updates
- No changes unless explicitly requested

## Fallback Procedures

| Condition | Action |
|-----------|--------|
| Path not found | Ask user to verify path |
| No write permission | Suggest running with admin rights |
| Unknown tech stack | Ask user to specify blueprint |
| Backup fails | Abort and report error |
| Conflict with no resolution | Skip artifact, report to user |

## Integration with Other Skills

| Skill | Integration Point |
|-------|-------------------|
| `requirements-gathering` | Use if user wants to customize before onboarding |
| `stack-configuration` | Use if detected stack needs adjustment |
| `agent-generation` | Used for generating missing agents |
| `skill-generation` | Used for generating missing skills |
| `team-workshop-onboarding` | Alternative for team onboarding with collaborative workshops |

## Team Onboarding Alternative

If a team (2+ people) is onboarding together, suggest the Team Workshop Onboarding:

```
"I notice you mentioned a team. Would you like to:

A) Individual Onboarding - I'll analyze and enhance your repo now
B) Team Workshop Series - Collaborative 5-workshop journey with games 
   and discussions that builds shared vision, ethics, and custom agents

The workshop series takes more time but creates deeper team alignment
and more customized results. It's grounded in Axiom 0: Love and Trust."
```

If they choose team workshops, hand off to `team-workshop-onboarding` skill.

## Important Rules

1. **Never overwrite without backup** - Always create backup before any modification
2. **Preserve user customizations** - Default to keeping existing content
3. **Ask for conflicts** - Don't make assumptions, ask user for each conflict
4. **Provide rollback path** - Always inform user how to undo changes
5. **Validate before acting** - Run dry-run first to preview changes
6. **Report completely** - Show summary of all actions taken
7. **Update CHANGELOG** - After any feature addition or modification, update CHANGELOG.md before committing

## CLI Quick Reference

```bash
# Analyze repository (no changes)
python cli/factory_cli.py --analyze C:\Projects\my-repo

# Preview onboarding (dry run)
python cli/factory_cli.py --onboard C:\Projects\my-repo --dry-run

# Onboard with auto-detected blueprint
python cli/factory_cli.py --onboard C:\Projects\my-repo

# Onboard with specific blueprint
python cli/factory_cli.py --onboard C:\Projects\my-repo --blueprint csharp-dotnet

# Rollback last onboarding
python cli/factory_cli.py --rollback C:\Projects\my-repo
```

## Example Conversation

**User:** "I have an existing C# project at C:\Projects\PaymentService that I want to enhance with Cursor agents"

**Agent:** "I'll analyze your repository to understand what's already configured.

*Running analysis...*

**Analysis Results:**
- Scenario: PARTIAL
- Existing: .cursorrules, 2 agents (code-reviewer, explorer)
- Missing: skills, knowledge files, templates
- Tech Stack: C# (.NET 8), ASP.NET Core
- Suggested Blueprint: csharp-dotnet

Would you like me to:
1. Show a preview of what will be added (dry run)
2. Proceed with onboarding using the csharp-dotnet blueprint
3. Choose a different blueprint

What would you prefer?"

**User:** "Show me the preview first"

**Agent:** *Runs dry run and shows preview...*

---

*Generated by Cursor Agent Factory*
*Skill: onboarding-flow v1.0.0*
