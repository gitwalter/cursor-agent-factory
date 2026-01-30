# Getting Set Up

Let's make sure you have everything you need. This takes just a few minutes, and we'll walk you through each step.

> **Tool Paths:** Commands in this document use default Windows paths.
> See [Configuration Guide](CONFIGURATION.md) to customize tool paths for your environment.

---

## What You'll Need

| Tool | Why You Need It | How to Get It |
|------|-----------------|---------------|
| **Cursor IDE** | Where the magic happens - AI-powered code editor | [cursor.com](https://cursor.com) |
| **Python 3.9+** | Runs the factory CLI | See setup below |
| **Git** | Manages your projects | Usually pre-installed |

---

## Quick Setup

### Windows (with Anaconda)

If you have Anaconda installed, you're all set! Just use the full path to Python:

```powershell
# Verify Python is available
C:\App\Anaconda\python.exe --version

# Run the factory
C:\App\Anaconda\python.exe cli\factory_cli.py --help
```

**Don't have Anaconda?** You can also use:
- Standard Python from [python.org](https://www.python.org/downloads/)
- Python from the Microsoft Store
- Any Python 3.9+ installation

### macOS

Most macOS systems have Python 3 available:

```bash
# Verify Python is available
python3 --version

# Run the factory
python3 cli/factory_cli.py --help
```

**Need to install Python?** Use [Homebrew](https://brew.sh/):

```bash
brew install python@3.11
```

### Linux

Python is typically pre-installed:

```bash
# Verify Python is available
python3 --version

# Run the factory
python3 cli/factory_cli.py --help
```

**Need to install Python?** Use your package manager:

```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

---

## Let's Verify Everything Works

Run this command to make sure we're good to go:

```powershell
# Windows
C:\App\Anaconda\python.exe cli\factory_cli.py --list-blueprints

# macOS/Linux
python3 cli/factory_cli.py --list-blueprints
```

**You should see a list of 12+ blueprints** like:
- python-fastapi
- ai-agent-development
- typescript-react
- nextjs-fullstack
- and more...

If you see the list, congratulations - you're ready!

---

## Optional: YAML Support

If you want to use YAML configuration files (instead of JSON), install PyYAML:

```powershell
# Windows (Anaconda)
C:\App\Anaconda\Scripts\pip.exe install pyyaml

# macOS/Linux
pip3 install pyyaml
```

---

## Optional: Development Dependencies

If you plan to run tests or contribute to the factory:

```powershell
# Windows (Anaconda)
C:\App\Anaconda\Scripts\pip.exe install -r requirements-dev.txt

# macOS/Linux
pip3 install -r requirements-dev.txt
```

---

## Quick Test: Generate a Demo Project

Try the quickstart to see everything working:

```powershell
# Windows
C:\App\Anaconda\python.exe cli\factory_cli.py --quickstart

# macOS/Linux
python3 cli/factory_cli.py --quickstart
```

This creates a demo project in `./quickstart-demo/` - open it in Cursor IDE to explore!

---

## Something Not Working?

Don't worry - check our [Troubleshooting Guide](TROUBLESHOOTING.md) for common issues and solutions.

Remember: Every expert was once a beginner. You've got this!

---

*[Back to README](../README.md)*
