#!/usr/bin/env python3
"""
Cursor Agent Factory - Command Line Interface

CLI for generating Cursor agent development systems.

Usage:
    python factory_cli.py --config project.yaml --output C:\\Projects\\my-project
    python factory_cli.py --blueprint python-fastapi --output C:\\Projects\\my-project
    python factory_cli.py --interactive --output C:\\Projects\\my-project
    python factory_cli.py --list-blueprints

Author: Cursor Agent Factory
Version: 1.0.0
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.generate_project import ProjectConfig, ProjectGenerator


def get_factory_root() -> Path:
    """Get the factory root directory.
    
    Returns:
        Path to factory root.
    """
    return Path(__file__).parent.parent


def list_blueprints() -> None:
    """List all available blueprints."""
    blueprints_dir = get_factory_root() / 'blueprints'
    
    print("\n[*] Available Blueprints\n")
    print("-" * 60)
    
    for blueprint_dir in sorted(blueprints_dir.iterdir()):
        if blueprint_dir.is_dir():
            blueprint_file = blueprint_dir / 'blueprint.json'
            if blueprint_file.exists():
                with open(blueprint_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    metadata = data.get('metadata', {})
                    name = metadata.get('blueprintName', blueprint_dir.name)
                    desc = metadata.get('description', 'No description')
                    tags = metadata.get('tags', [])
                    
                    print(f"\n  {blueprint_dir.name}")
                    print(f"    Name: {name}")
                    print(f"    Description: {desc}")
                    print(f"    Tags: {', '.join(tags)}")
            else:
                print(f"\n  {blueprint_dir.name} (no blueprint.json)")
    
    print("\n" + "-" * 60)
    print("\nUsage: python factory_cli.py --blueprint <blueprint-id> --output <path>\n")


def list_patterns() -> None:
    """List all available patterns."""
    patterns_dir = get_factory_root() / 'patterns'
    
    print("\n[*] Available Patterns\n")
    print("-" * 60)
    
    for pattern_type in ['agents', 'skills', 'workflows']:
        type_dir = patterns_dir / pattern_type
        if type_dir.exists():
            print(f"\n  {pattern_type.upper()}:")
            for pattern_file in sorted(type_dir.glob('*.json')):
                with open(pattern_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    metadata = data.get('metadata', {})
                    desc = metadata.get('description', '')
                    print(f"    - {pattern_file.stem}: {desc}")
    
    print("\n" + "-" * 60 + "\n")


def interactive_mode(output_dir: str) -> None:
    """Run interactive requirements gathering.
    
    Args:
        output_dir: Target output directory.
    """
    print("\n=== Cursor Agent Factory - Interactive Mode ===\n")
    print("=" * 60)
    print("Let's gather requirements for your new agent system.\n")
    
    # Phase 1: Project Context
    print("[PHASE 1] Project Context\n")
    
    project_name = input("1. Project name: ").strip()
    if not project_name:
        project_name = "new-agent-project"
    
    project_description = input("2. Project description: ").strip()
    
    print("\n   Available domains: web, mobile, data-science, sap, devops, general")
    domain = input("3. Domain/Industry [general]: ").strip() or "general"
    
    team_context = input("4. Team size and experience (optional): ").strip()
    
    # Phase 2: Technology Stack
    print("\n[PHASE 2] Technology Stack\n")
    
    print("   Available languages: python, typescript, java, csharp, go, rust, abap")
    primary_language = input("1. Primary programming language [python]: ").strip() or "python"
    
    frameworks_input = input("2. Frameworks (comma-separated, e.g., fastapi,sqlalchemy): ").strip()
    frameworks = [f.strip() for f in frameworks_input.split(',')] if frameworks_input else []
    
    # Check for matching blueprint
    blueprint_id = None
    if primary_language == 'python' and 'fastapi' in [f.lower() for f in frameworks]:
        blueprint_id = 'python-fastapi'
        print(f"\n   [OK] Matched blueprint: {blueprint_id}")
    elif primary_language == 'typescript' and 'react' in [f.lower() for f in frameworks]:
        blueprint_id = 'typescript-react'
        print(f"\n   [OK] Matched blueprint: {blueprint_id}")
    elif primary_language == 'java' and 'spring' in [f.lower() for f in frameworks]:
        blueprint_id = 'java-spring'
        print(f"\n   [OK] Matched blueprint: {blueprint_id}")
    elif primary_language == 'abap':
        blueprint_id = 'sap-abap'
        print(f"\n   [OK] Matched blueprint: {blueprint_id}")
    
    # Phase 3: Workflow
    print("\n[PHASE 3] Workflow Methodology\n")
    
    print("   Available triggers: jira, confluence, github, gitlab, manual")
    triggers_input = input("1. Workflow triggers (comma-separated) [manual]: ").strip() or "manual"
    triggers = [t.strip() for t in triggers_input.split(',')]
    
    # Phase 4: Agents & Skills
    print("\n[PHASE 4] Agent Capabilities\n")
    
    print("   Available agents: code-reviewer, test-generator, explorer")
    agents_input = input("1. Agents to include (comma-separated) [code-reviewer]: ").strip() or "code-reviewer"
    agents = [a.strip() for a in agents_input.split(',')]
    
    print("   Available skills: bugfix-workflow, feature-workflow, grounding, tdd, code-templates")
    skills_input = input("2. Skills to include (comma-separated) [bugfix-workflow,tdd]: ").strip() or "bugfix-workflow,tdd"
    skills = [s.strip() for s in skills_input.split(',')]
    
    # Phase 5: MCP Servers
    print("\n[PHASE 5] Integrations\n")
    
    mcp_servers = []
    if 'jira' in triggers or 'confluence' in triggers:
        print("   [OK] Adding Atlassian MCP server for Jira/Confluence")
        mcp_servers.append({
            'name': 'atlassian',
            'url': 'https://mcp.atlassian.com/v1/sse',
            'purpose': 'Jira/Confluence integration'
        })
    
    add_deepwiki = input("Add DeepWiki for GitHub repo analysis? [y/N]: ").strip().lower()
    if add_deepwiki == 'y':
        mcp_servers.append({
            'name': 'deepwiki',
            'url': 'https://mcp.deepwiki.com/mcp',
            'purpose': 'GitHub repository analysis'
        })
    
    # Summary
    print("\n" + "=" * 60)
    print("[SUMMARY] REQUIREMENTS\n")
    print(f"  Project: {project_name}")
    print(f"  Description: {project_description}")
    print(f"  Domain: {domain}")
    print(f"  Language: {primary_language}")
    print(f"  Frameworks: {', '.join(frameworks) if frameworks else 'None'}")
    print(f"  Blueprint: {blueprint_id or 'None (custom)'}")
    print(f"  Triggers: {', '.join(triggers)}")
    print(f"  Agents: {', '.join(agents)}")
    print(f"  Skills: {', '.join(skills)}")
    print(f"  MCP Servers: {len(mcp_servers)}")
    print(f"  Output: {output_dir}")
    print("=" * 60)
    
    confirm = input("\nGenerate project? [Y/n]: ").strip().lower()
    if confirm == 'n':
        print("Cancelled.")
        return
    
    # Generate
    config = ProjectConfig(
        project_name=project_name,
        project_description=project_description,
        domain=domain,
        primary_language=primary_language,
        frameworks=frameworks,
        triggers=triggers,
        agents=agents,
        skills=skills,
        mcp_servers=mcp_servers,
        blueprint_id=blueprint_id,
        team_context=team_context
    )
    
    generator = ProjectGenerator(config, output_dir)
    result = generator.generate()
    
    if result['success']:
        print("\n[SUCCESS] Project generated successfully!")
        print(f"   Location: {result['target_dir']}")
        print(f"   Files created: {len(result['files_created'])}")
        print("\n   Next steps:")
        print("   1. Open the project in Cursor IDE")
        print("   2. The .cursorrules will configure agent behavior")
        print("   3. Start developing with AI assistance!")
    else:
        print("\n[ERROR] Generation failed:")
        for error in result['errors']:
            print(f"   - {error}")


def generate_from_blueprint(blueprint_id: str, output_dir: str, project_name: str = None) -> None:
    """Generate project from a blueprint.
    
    Args:
        blueprint_id: Blueprint identifier.
        output_dir: Target output directory.
        project_name: Optional project name override.
    """
    blueprint_path = get_factory_root() / 'blueprints' / blueprint_id / 'blueprint.json'
    
    if not blueprint_path.exists():
        print(f"[ERROR] Blueprint not found: {blueprint_id}")
        print("   Use --list-blueprints to see available blueprints")
        sys.exit(1)
    
    with open(blueprint_path, 'r', encoding='utf-8') as f:
        blueprint = json.load(f)
    
    metadata = blueprint.get('metadata', {})
    stack = blueprint.get('stack', {})
    
    # Extract configuration from blueprint
    config = ProjectConfig(
        project_name=project_name or blueprint_id + '-project',
        project_description=metadata.get('description', ''),
        domain=', '.join(metadata.get('tags', [])),
        primary_language=stack.get('primaryLanguage', 'python'),
        frameworks=[f['name'] for f in stack.get('frameworks', [])],
        triggers=['jira', 'confluence'],  # Default triggers
        agents=[a['patternId'] for a in blueprint.get('agents', [])],
        skills=[s['patternId'] for s in blueprint.get('skills', [])],
        mcp_servers=blueprint.get('mcpServers', []),
        blueprint_id=blueprint_id
    )
    
    print(f"\n[*] Generating from blueprint: {blueprint_id}")
    print(f"   Output: {output_dir}\n")
    
    generator = ProjectGenerator(config, output_dir)
    result = generator.generate()
    
    if result['success']:
        print("\n[SUCCESS] Project generated successfully!")
        print(f"   Location: {result['target_dir']}")
        print(f"   Files created: {len(result['files_created'])}")
    else:
        print("\n[ERROR] Generation failed:")
        for error in result['errors']:
            print(f"   - {error}")
        sys.exit(1)


def generate_from_config_file(config_path: str, output_dir: str) -> None:
    """Generate project from configuration file.
    
    Args:
        config_path: Path to configuration file.
        output_dir: Target output directory.
    """
    if not os.path.exists(config_path):
        print(f"[ERROR] Configuration file not found: {config_path}")
        sys.exit(1)
    
    try:
        if config_path.endswith('.yaml') or config_path.endswith('.yml'):
            import yaml
            with open(config_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        else:
            with open(config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        
        config = ProjectConfig.from_dict(data)
        
        print(f"\n[*] Generating from config: {config_path}")
        print(f"   Project: {config.project_name}")
        print(f"   Output: {output_dir}\n")
        
        generator = ProjectGenerator(config, output_dir)
        result = generator.generate()
        
        if result['success']:
            print("\n[SUCCESS] Project generated successfully!")
            print(f"   Location: {result['target_dir']}")
            print(f"   Files created: {len(result['files_created'])}")
        else:
            print("\n[ERROR] Generation failed:")
            for error in result['errors']:
                print(f"   - {error}")
            sys.exit(1)
            
    except Exception as e:
        print(f"[ERROR] Error loading configuration: {e}")
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Cursor Agent Factory - Generate Cursor agent development systems',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --list-blueprints
  %(prog)s --list-patterns
  %(prog)s --blueprint python-fastapi --output C:\\Projects\\my-api
  %(prog)s --config project.yaml --output C:\\Projects\\my-project
  %(prog)s --interactive --output C:\\Projects\\my-project
        '''
    )
    
    parser.add_argument(
        '--list-blueprints',
        action='store_true',
        help='List all available blueprints'
    )
    
    parser.add_argument(
        '--list-patterns',
        action='store_true',
        help='List all available patterns'
    )
    
    parser.add_argument(
        '--blueprint',
        type=str,
        metavar='ID',
        help='Generate from a blueprint (e.g., python-fastapi)'
    )
    
    parser.add_argument(
        '--config',
        type=str,
        metavar='FILE',
        help='Generate from a configuration file (YAML or JSON)'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run interactive requirements gathering'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        metavar='DIR',
        help='Output directory for generated project'
    )
    
    parser.add_argument(
        '--name',
        type=str,
        metavar='NAME',
        help='Project name (overrides blueprint/config name)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Cursor Agent Factory 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Handle list commands
    if args.list_blueprints:
        list_blueprints()
        return
    
    if args.list_patterns:
        list_patterns()
        return
    
    # Validate output directory for generation commands
    if args.blueprint or args.config or args.interactive:
        if not args.output:
            print("[ERROR] --output is required for generation")
            parser.print_help()
            sys.exit(1)
    
    # Handle generation commands
    if args.interactive:
        interactive_mode(args.output)
    elif args.blueprint:
        generate_from_blueprint(args.blueprint, args.output, args.name)
    elif args.config:
        generate_from_config_file(args.config, args.output)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
