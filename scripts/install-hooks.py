#!/usr/bin/env python3
"""
Install Git hooks for the Cursor Agent Factory project.

This script sets up pre-commit hooks that automatically maintain
README structure counts, ensuring documentation stays synchronized.

Usage:
    python scripts/install-hooks.py
"""

import os
import stat
import sys
from pathlib import Path


# Shell script hook for Unix systems
PRE_COMMIT_HOOK_UNIX = '''#!/bin/sh
#
# Pre-commit hook: Auto-update README structure counts.
#

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRIPT_PATH="$REPO_ROOT/scripts/validate_readme_structure.py"

if [ ! -f "$SCRIPT_PATH" ]; then
    exit 0
fi

# Find Python
if command -v python3 >/dev/null 2>&1; then
    python3 "$SCRIPT_PATH" --update
elif command -v python >/dev/null 2>&1; then
    python "$SCRIPT_PATH" --update
fi

git add README.md 2>/dev/null || true
exit 0
'''

# PowerShell hook for Windows (Git for Windows runs hooks via sh, but we provide fallback)
PRE_COMMIT_HOOK_WINDOWS = '''#!/bin/sh
#
# Pre-commit hook: Auto-update README structure counts.
# Works with Git for Windows (uses sh from Git bash)
#

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRIPT_PATH="$REPO_ROOT/scripts/validate_readme_structure.py"

if [ ! -f "$SCRIPT_PATH" ]; then
    exit 0
fi

# Try multiple Python locations for Windows compatibility
if [ -x "/c/App/Anaconda/python.exe" ]; then
    /c/App/Anaconda/python.exe "$SCRIPT_PATH" --update
elif command -v python >/dev/null 2>&1; then
    python "$SCRIPT_PATH" --update
elif command -v python3 >/dev/null 2>&1; then
    python3 "$SCRIPT_PATH" --update
fi

git add README.md 2>/dev/null || true
exit 0
'''


def install_hooks():
    """Install Git hooks for the project."""
    # Find .git directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    git_dir = repo_root / ".git"
    
    if not git_dir.exists():
        print("Error: .git directory not found. Are you in a git repository?")
        return 1
    
    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)
    
    # Install pre-commit hook
    pre_commit_path = hooks_dir / "pre-commit"
    
    # Check if hook already exists
    if pre_commit_path.exists():
        print(f"Pre-commit hook already exists at {pre_commit_path}")
        response = input("Overwrite? [y/N]: ").strip().lower()
        if response != 'y':
            print("Skipping pre-commit hook installation")
            return 0
    
    # Write the hook (use Windows version on Windows for Anaconda path)
    hook_content = PRE_COMMIT_HOOK_WINDOWS if os.name == 'nt' else PRE_COMMIT_HOOK_UNIX
    pre_commit_path.write_text(hook_content, newline='\n')  # Unix line endings for Git
    
    # Make it executable (Unix)
    if os.name != 'nt':
        pre_commit_path.chmod(pre_commit_path.stat().st_mode | stat.S_IEXEC)
    
    print(f"Installed pre-commit hook at {pre_commit_path}")
    print("\nThe hook will automatically:")
    print("  - Update README.md structure counts before each commit")
    print("  - Stage the updated README.md")
    print("\nNo more CI failures from outdated counts!")
    
    return 0


if __name__ == "__main__":
    sys.exit(install_hooks())
