# Troubleshooting Guide

Having trouble? Don't worry - we've got you covered. Here are solutions to the most common issues, and we're here to help you succeed.

---

## Python Not Found

### "python: command not found" or "'python' is not recognized"

This usually means your system can't find Python. No problem - here's how to fix it:

**On Windows (with Anaconda):**

Use the full path to your Anaconda installation:

```powershell
C:\App\Anaconda\python.exe cli\factory_cli.py --quickstart
```

**On Windows (without Anaconda):**

Try using `python` or `py`:

```powershell
py cli\factory_cli.py --quickstart
```

Or find where Python is installed and use the full path.

**On macOS/Linux:**

Try `python3` instead of `python`:

```bash
python3 cli/factory_cli.py --quickstart
```

**Still stuck?** See [Prerequisites](PREREQUISITES.md) for installation instructions.

---

## Blueprint Not Found

### "Blueprint 'xyz' not found"

The blueprint name might have a typo - easy to do!

**To see all available blueprints:**

```powershell
python cli/factory_cli.py --list-blueprints
```

You'll see options like:
- `python-fastapi`
- `ai-agent-development`
- `multi-agent-systems`
- `typescript-react`
- `nextjs-fullstack`
- `java-spring`
- `kotlin-spring`
- `csharp-dotnet`
- `sap-abap`
- `sap-cap`
- `sap-rap`
- `sap-cpi-pi`

**Make sure to use the exact ID** (e.g., `python-fastapi`, not `Python FastAPI`).

---

## Permission Denied

### "Permission denied" when writing files

Your system is protecting that folder. Here's how to fix it:

**Option 1: Choose a different output location**

```powershell
# Use a folder in your user directory
python cli/factory_cli.py --quickstart --quickstart-output ./my-project

# Or specify a full path you have access to
python cli/factory_cli.py --quickstart --quickstart-output C:\Users\YourName\Projects\demo
```

**Option 2: Run with elevated permissions**

On Windows, try running PowerShell or Command Prompt as Administrator.

On macOS/Linux, check folder permissions:

```bash
ls -la ./
chmod 755 ./my-project
```

---

## Template Not Found

### "Template 'xyz.tmpl' not found"

This usually means you're not running from the factory root directory.

**Make sure you're in the cursor-agent-factory folder:**

```powershell
# Check your current directory
pwd

# Navigate to the factory root
cd C:\Users\YourName\path\to\cursor-agent-factory

# Now run the command
python cli/factory_cli.py --quickstart
```

---

## Import Errors

### "ModuleNotFoundError: No module named 'yaml'"

You need to install PyYAML:

```powershell
# Windows (Anaconda)
C:\App\Anaconda\Scripts\pip.exe install pyyaml

# macOS/Linux
pip3 install pyyaml
```

### "ModuleNotFoundError: No module named 'scripts'"

Make sure you're running from the factory root directory (see "Template Not Found" above).

---

## Output Directory Issues

### "Output directory already exists"

The factory won't overwrite existing projects to protect your work.

**Options:**
1. Choose a different output directory
2. Delete or rename the existing directory
3. Use the `--onboard` flag to integrate into an existing repo

```powershell
# Option 1: Different directory
python cli/factory_cli.py --quickstart --quickstart-output ./new-demo

# Option 3: Onboard existing repo
python cli/factory_cli.py --onboard ./existing-project
```

---

## JSON/YAML Syntax Errors

### "Error loading configuration"

There might be a syntax error in your config file.

**Common issues:**
- Missing commas between items
- Unbalanced quotes or brackets
- Tabs instead of spaces (in YAML)
- Trailing commas (not allowed in JSON)

**Use a validator:**
- JSON: [jsonlint.com](https://jsonlint.com/)
- YAML: [yamllint.com](http://www.yamllint.com/)

---

## Slow or Hanging

### Generation seems stuck

Large projects may take a moment to generate. If it's been more than a minute:

1. Check if your antivirus is scanning the files
2. Try a simpler blueprint first (e.g., `python-fastapi`)
3. Make sure you have enough disk space

---

## Windows-Specific Issues

### Long Path Errors

Windows has path length limits. If you see path-related errors:

1. Use a shorter output path:
   ```powershell
   python cli/factory_cli.py --quickstart --quickstart-output C:\P\demo
   ```

2. Enable long paths in Windows (requires admin):
   - Run `regedit`
   - Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
   - Set `LongPathsEnabled` to `1`

### PowerShell Execution Policy

If you see "running scripts is disabled":

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## macOS/Linux-Specific Issues

### Zsh Syntax Issues

If you use zsh and see weird errors with brackets:

```bash
# Quote the pattern
python3 cli/factory_cli.py --blueprint 'python-fastapi' --output './my-project'
```

---

## Still Stuck?

We want to help! Here's what to do:

1. **Check the logs** - Look for error messages that explain what went wrong
2. **Try the simplest case** - Run `--quickstart` with no options to verify basic functionality
3. **Check prerequisites** - Make sure everything in [Prerequisites](PREREQUISITES.md) is set up
4. **Open an issue** - [GitHub Issues](https://github.com/your-repo/cursor-agent-factory/issues)

When reporting an issue, please include:
- Your operating system and version
- Python version (`python --version`)
- The exact command you ran
- The complete error message

---

## Common Success Patterns

Here are commands that work reliably:

```powershell
# Quickstart - always works from factory root
python cli/factory_cli.py --quickstart

# List blueprints - verify factory is working
python cli/factory_cli.py --list-blueprints

# Interactive mode - guided experience
python cli/factory_cli.py --interactive --output ./my-project
```

---

Remember: Every expert was once a beginner. You've got this!

---

*[Back to README](../README.md) | [Prerequisites](PREREQUISITES.md)*
