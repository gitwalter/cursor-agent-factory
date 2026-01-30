# Configuration Guide

This document describes how to configure the Cursor Agent Factory for your development environment.

## Overview

The factory uses a **layered configuration system** that allows customization at multiple levels:

1. **Config File** (`.cursor/config/tools.json`) - Project-specific tool paths
2. **Environment Variables** - Machine-wide overrides
3. **Hardcoded Defaults** - Fallback values

```mermaid
flowchart LR
    A[".cursor/config/tools.json"] -->|not found| B["Environment Variables"]
    B -->|not set| C["Hardcoded Defaults"]
```

## Tool Paths Configuration

### Configuration File

The primary configuration file is located at:

```
.cursor/config/tools.json
```

This file defines paths to development tools used by the factory and its generated projects.

### Current Default Values

| Tool | Path | Environment Variable |
|------|------|---------------------|
| **Python** | `C:\App\Anaconda\python.exe` | `PYTHON_PATH` |
| **Pip** | `C:\App\Anaconda\Scripts\pip.exe` | `PIP_PATH` |
| **Conda** | `C:\App\Anaconda\Scripts\conda.exe` | `CONDA_PATH` |
| **GitHub CLI** | `C:\App\gh\bin\gh.exe` | `GH_CLI_PATH` |
| **Pytest** | `C:\App\Anaconda\Scripts\pytest.exe` | `PYTEST_PATH` |

### How to Customize

#### Option 1: Edit the Config File

Modify `.cursor/config/tools.json` directly:

```json
{
  "tools": {
    "python": {
      "path": "C:\\Python311\\python.exe",
      "env_var": "PYTHON_PATH",
      "description": "Python interpreter"
    }
  }
}
```

#### Option 2: Use Environment Variables

Set environment variables to override paths without modifying files:

**Windows (PowerShell):**
```powershell
$env:PYTHON_PATH = "C:\Python311\python.exe"
$env:GH_CLI_PATH = "C:\Program Files\GitHub CLI\gh.exe"
```

**Windows (Permanent):**
```powershell
[Environment]::SetEnvironmentVariable("PYTHON_PATH", "C:\Python311\python.exe", "User")
```

**Linux/macOS:**
```bash
export PYTHON_PATH="/usr/bin/python3"
export GH_CLI_PATH="/usr/local/bin/gh"
```

Add to `~/.bashrc` or `~/.zshrc` for persistence.

#### Option 3: CI/CD Configuration

For CI/CD environments, set environment variables in your workflow:

**GitHub Actions:**
```yaml
env:
  PYTHON_PATH: python3
  GH_CLI_PATH: gh
```

**Azure DevOps:**
```yaml
variables:
  PYTHON_PATH: python3
  GH_CLI_PATH: gh
```

## Platform-Specific Configuration

### Windows

The default configuration uses Windows paths with backslashes:

```json
{
  "path": "C:\\App\\Anaconda\\python.exe"
}
```

### Linux

Use forward slashes and standard paths:

```json
{
  "path": "/usr/bin/python3"
}
```

Or rely on PATH resolution:

```json
{
  "path": "python3"
}
```

### macOS

Similar to Linux, with Homebrew paths if applicable:

```json
{
  "path": "/usr/local/bin/python3"
}
```

## Configuration Priority

The factory resolves tool paths in this order:

1. **Environment Variable** - If set, takes highest priority
2. **Config File** - Read from `.cursor/config/tools.json`
3. **Hardcoded Default** - Built-in fallback value

### Example Resolution

For the Python interpreter:

```
1. Check: Is $PYTHON_PATH set? → Use it
2. Check: Does tools.json have python.path? → Use it
3. Fallback: Use "C:\App\Anaconda\python.exe"
```

## Validation

### Schema Validation

The config file includes a JSON Schema reference for validation:

```json
{
  "$schema": "./tools-schema.json",
  ...
}
```

Your IDE should provide autocomplete and validation based on this schema.

### Verify Configuration

To verify your configuration is correct:

```powershell
# Check Python path
$pythonPath = if ($env:PYTHON_PATH) { $env:PYTHON_PATH } else { "C:\App\Anaconda\python.exe" }
& $pythonPath --version

# Check GitHub CLI
$ghPath = if ($env:GH_CLI_PATH) { $env:GH_CLI_PATH } else { "C:\App\gh\bin\gh.exe" }
& $ghPath --version
```

## Common Configurations

### Standard Python Installation

```json
{
  "tools": {
    "python": { "path": "python" },
    "pip": { "path": "pip" },
    "pytest": { "path": "pytest" }
  }
}
```

### Anaconda Installation (Windows)

```json
{
  "tools": {
    "python": { "path": "C:\\App\\Anaconda\\python.exe" },
    "pip": { "path": "C:\\App\\Anaconda\\Scripts\\pip.exe" },
    "conda": { "path": "C:\\App\\Anaconda\\Scripts\\conda.exe" }
  }
}
```

### Virtual Environment

```json
{
  "tools": {
    "python": { "path": ".venv\\Scripts\\python.exe" },
    "pip": { "path": ".venv\\Scripts\\pip.exe" }
  }
}
```

### Docker/Container

```json
{
  "tools": {
    "python": { "path": "/usr/local/bin/python" },
    "pip": { "path": "/usr/local/bin/pip" }
  }
}
```

## Troubleshooting

### Tool Not Found

If you see "command not found" or "executable not found":

1. Verify the path exists: `Test-Path "C:\App\Anaconda\python.exe"`
2. Check environment variable: `$env:PYTHON_PATH`
3. Verify config file syntax: Validate JSON

### Permission Denied

On Linux/macOS, ensure the tool is executable:

```bash
chmod +x /path/to/tool
```

### Path Contains Spaces

Wrap paths with spaces in quotes:

```json
{
  "path": "C:\\Program Files\\Python311\\python.exe"
}
```

## Related Documentation

- [Shell Platform Skill](.cursor/skills/shell-platform/SKILL.md) - Platform-specific command syntax
- [Prerequisites](PREREQUISITES.md) - Initial setup requirements
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions

## Contributing

When adding new tools to the configuration:

1. Add to `.cursor/config/tools.json`
2. Update the schema in `.cursor/config/tools-schema.json`
3. Document in this file
4. Update shell-platform skill if needed
