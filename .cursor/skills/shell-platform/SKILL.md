---
name: shell-platform
description: Platform-specific shell command considerations for Windows PowerShell and Unix shells
type: skill
scope: local
---

# Shell Platform Skill

Handle platform-specific shell syntax differences when executing commands.

## Scope

**This skill is LOCAL to this machine only.** Do not apply automatically - always ask the user before applying platform-specific command adjustments.

## When to Use

- Before executing shell commands that may have platform-specific syntax
- When writing git commit messages with multi-line content
- When using heredoc, pipes, or other shell-specific constructs

## Activation

**First-time activation only:** If this skill has not been confirmed yet, ask the user:

> "I notice you're on Windows/PowerShell. Should I enable PowerShell-compatible syntax for shell commands? This setting will persist in your Cursor configuration."

Once the user confirms:
1. The skill remains **permanently active** in Cursor settings
2. No need to ask again in future sessions
3. Apply PowerShell-compatible syntax automatically from then on

**Status:** ✅ ACTIVE (confirmed by user)

## Platform Detection

Check the user's OS from `user_info`:
- `win32` → Windows (PowerShell)
- `darwin` → macOS (zsh/bash)
- `linux` → Linux (bash)

## Critical: PowerShell Limitations

### Heredoc Syntax NOT Supported

PowerShell does NOT support bash-style heredoc syntax:

```bash
# THIS DOES NOT WORK IN POWERSHELL:
git commit -m "$(cat <<'EOF'
Multi-line
commit message
EOF
)"
```

### PowerShell Alternatives

**Option 1: Multiple -m flags (recommended for git commits)**
```powershell
git commit -m "Title line" -m "Body paragraph 1" -m "Body paragraph 2"
```

**Option 2: Backtick for line continuation**
```powershell
git commit -m "Title line`n`nBody with newlines"
```

**Option 3: Here-string (PowerShell native)**
```powershell
$message = @"
Title line

Body paragraph
"@
git commit -m $message
```

### Command Chaining

PowerShell uses different operators:

| Bash | PowerShell | Purpose |
|------|------------|---------|
| `&&` | `;` or `-and` | Run if previous succeeds |
| `||` | `-or` | Run if previous fails |
| `\|` | `\|` | Pipe (same) |

**Note:** `&&` and `||` work in PowerShell 7+ but NOT in Windows PowerShell 5.x.

## Git Commit Message Best Practices

For cross-platform compatibility, use multiple `-m` flags:

```powershell
git commit -m "feat: Short title" -m "Longer description of the change." -m "Additional details if needed."
```

This works on all platforms and produces proper multi-paragraph commit messages.

## Tool Paths Configuration

Tool paths are **configurable** via `.cursor/config/tools.json` with environment variable fallbacks.

See [Configuration Guide](../../docs/CONFIGURATION.md) for full details.

### Configuration Priority

1. **Environment Variable** (e.g., `$env:PYTHON_PATH`) - Highest priority
2. **Config File** (`.cursor/config/tools.json`) - Project defaults
3. **Hardcoded Fallback** - Ultimate default

### Default Tool Paths (Windows)

| Tool | Default Path | Env Variable |
|------|--------------|--------------|
| **Python** | `C:\App\Anaconda\python.exe` | `PYTHON_PATH` |
| **Pip** | `C:\App\Anaconda\Scripts\pip.exe` | `PIP_PATH` |
| **Conda** | `C:\App\Anaconda\Scripts\conda.exe` | `CONDA_PATH` |
| **GitHub CLI** | `C:\App\gh\bin\gh.exe` | `GH_CLI_PATH` |
| **Pytest** | `C:\App\Anaconda\Scripts\pytest.exe` | `PYTEST_PATH` |

### Resolving Tool Paths

When using tools, resolve the path in this order:

```powershell
# Example: Resolve Python path
$pythonPath = if ($env:PYTHON_PATH) { 
    $env:PYTHON_PATH 
} else { 
    "C:\App\Anaconda\python.exe"  # Default from config
}
```

### GitHub CLI Examples

```powershell
# Using environment variable (recommended)
& $env:GH_CLI_PATH run list --limit 5

# Or with default path
C:\App\gh\bin\gh.exe run list --limit 5

# View specific run details
C:\App\gh\bin\gh.exe run view <run-id> --json jobs

# Check job status
C:\App\gh\bin\gh.exe run view <run-id> --json jobs --jq ".jobs[] | {name, conclusion}"

# Create a pull request
C:\App\gh\bin\gh.exe pr create --title "Title" --body "Description"

# List open issues
C:\App\gh\bin\gh.exe issue list
```

### Cross-Platform Paths

For Linux/macOS, paths typically use forward slashes and may be simpler:

| Tool | Linux/macOS Path |
|------|------------------|
| **Python** | `python3` or `/usr/bin/python3` |
| **Pip** | `pip3` or `/usr/bin/pip3` |
| **GitHub CLI** | `gh` or `/usr/local/bin/gh` |

## Important Rules

1. **Always check platform** before using shell-specific syntax
2. **Avoid heredoc** in Windows environments
3. **Use multiple -m flags** for multi-line git commits
4. **Test command syntax** matches the target shell
5. **Prefer simple commands** that work across platforms
6. **Use full tool paths** on Windows to avoid PATH issues
