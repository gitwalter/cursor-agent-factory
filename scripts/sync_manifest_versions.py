#!/usr/bin/env python3
"""
Sync manifest.json versions from actual source files.

Source of Truth:
- File versions → Read from each knowledge/*.json file's "version" field
- Factory version → Read from CHANGELOG.md's latest version header

Usage:
    python scripts/sync_manifest_versions.py          # Check only
    python scripts/sync_manifest_versions.py --sync   # Auto-fix
"""

import json
import re
import sys
from pathlib import Path

def get_changelog_version() -> str:
    """Extract latest version from CHANGELOG.md (source of truth for factory version)."""
    changelog = Path('CHANGELOG.md').read_text(encoding='utf-8')
    match = re.search(r'^## \[(\d+\.\d+\.\d+)\]', changelog, re.MULTILINE)
    if match:
        return match.group(1)
    return "0.0.0"

def get_file_version(filepath: Path) -> str | None:
    """Extract version from a knowledge JSON file."""
    try:
        data = json.loads(filepath.read_text(encoding='utf-8'))
        return data.get('version')
    except (json.JSONDecodeError, FileNotFoundError):
        return None

def sync_manifest(dry_run: bool = True) -> tuple[bool, list[str]]:
    """
    Sync manifest versions from source files.
    
    Returns:
        (all_synced, list of changes)
    """
    manifest_path = Path('knowledge/manifest.json')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    
    changes = []
    
    # 1. Sync factory_version from CHANGELOG
    changelog_version = get_changelog_version()
    if manifest.get('factory_version') != changelog_version:
        changes.append(f"factory_version: {manifest.get('factory_version')} -> {changelog_version}")
        if not dry_run:
            manifest['factory_version'] = changelog_version
    
    # 2. Sync each file's version from actual file
    knowledge_dir = Path('knowledge')
    for filename, entry in manifest.get('files', {}).items():
        filepath = knowledge_dir / filename
        if filepath.exists():
            actual_version = get_file_version(filepath)
            manifest_version = entry.get('version')
            
            if actual_version and actual_version != manifest_version:
                changes.append(f"{filename}: {manifest_version} -> {actual_version}")
                if not dry_run:
                    entry['version'] = actual_version
    
    # 3. Write updated manifest
    if not dry_run and changes:
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + '\n',
            encoding='utf-8'
        )
    
    return len(changes) == 0, changes

def main():
    sync = '--sync' in sys.argv
    
    all_synced, changes = sync_manifest(dry_run=not sync)
    
    if all_synced:
        print("[OK] All versions are in sync")
        return 0
    
    if sync:
        print(f"[SYNCED] {len(changes)} version(s):")
        for change in changes:
            print(f"  - {change}")
        return 0
    else:
        print(f"[OUT OF SYNC] {len(changes)} version(s):")
        for change in changes:
            print(f"  - {change}")
        print("\nRun with --sync to fix")
        return 1

if __name__ == '__main__':
    sys.exit(main())
