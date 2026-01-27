#!/usr/bin/env python3
"""
Cursor Agent Factory - Project Generation Engine

This module generates complete Cursor agent development systems based on
requirements configuration and blueprint templates.

Usage:
    from scripts.generate_project import ProjectGenerator
    
    generator = ProjectGenerator(config, target_dir)
    generator.generate()

Author: Cursor Agent Factory
Version: 1.0.0
"""

import json
import os
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class ProjectConfig:
    """Configuration for project generation.
    
    Attributes:
        project_name: Name of the project (used for directory and documentation).
        project_description: Brief description of the project.
        domain: Industry/domain context.
        primary_language: Main programming language.
        frameworks: List of frameworks to use.
        triggers: Workflow trigger sources (jira, confluence, github, etc.).
        agents: List of agent pattern IDs to include.
        skills: List of skill pattern IDs to include.
        mcp_servers: List of MCP server configurations.
        style_guide: Coding style guide preference.
        blueprint_id: Optional blueprint to use as base.
    """
    project_name: str
    project_description: str = ""
    domain: str = "general"
    primary_language: str = "python"
    frameworks: List[str] = field(default_factory=list)
    triggers: List[str] = field(default_factory=list)
    agents: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    mcp_servers: List[Dict[str, Any]] = field(default_factory=list)
    style_guide: str = "default"
    blueprint_id: Optional[str] = None
    team_context: str = ""
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ProjectConfig':
        """Create ProjectConfig from dictionary.
        
        Args:
            data: Dictionary containing configuration values.
            
        Returns:
            ProjectConfig instance.
        """
        return cls(
            project_name=data.get('project_name', 'new-project'),
            project_description=data.get('project_description', ''),
            domain=data.get('domain', 'general'),
            primary_language=data.get('primary_language', 'python'),
            frameworks=data.get('frameworks', []),
            triggers=data.get('triggers', []),
            agents=data.get('agents', []),
            skills=data.get('skills', []),
            mcp_servers=data.get('mcp_servers', []),
            style_guide=data.get('style_guide', 'default'),
            blueprint_id=data.get('blueprint_id'),
            team_context=data.get('team_context', '')
        )
    
    @classmethod
    def from_yaml_file(cls, filepath: str) -> 'ProjectConfig':
        """Load configuration from YAML file.
        
        Args:
            filepath: Path to YAML configuration file.
            
        Returns:
            ProjectConfig instance.
        """
        import yaml
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls.from_dict(data)
    
    @classmethod
    def from_json_file(cls, filepath: str) -> 'ProjectConfig':
        """Load configuration from JSON file.
        
        Args:
            filepath: Path to JSON configuration file.
            
        Returns:
            ProjectConfig instance.
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)


class ProjectGenerator:
    """Generates complete Cursor agent projects.
    
    This class orchestrates the generation of a complete Cursor agent
    development system based on configuration and patterns.
    
    Attributes:
        config: Project configuration.
        target_dir: Target directory for generated project.
        factory_root: Root directory of the factory.
    """
    
    def __init__(self, config: ProjectConfig, target_dir: str):
        """Initialize the generator.
        
        Args:
            config: Project configuration.
            target_dir: Target directory for generated project.
        """
        self.config = config
        self.target_dir = Path(target_dir)
        self.factory_root = Path(__file__).parent.parent
        self.generated_files: List[str] = []
        self.errors: List[str] = []
        
    def generate(self) -> Dict[str, Any]:
        """Generate the complete project.
        
        Returns:
            Dictionary with generation results including:
            - success: Boolean indicating success.
            - target_dir: Path to generated project.
            - files_created: List of created files.
            - errors: List of any errors encountered.
        """
        print(f"Generating project: {self.config.project_name}")
        print(f"Target directory: {self.target_dir}")
        
        try:
            # Create directory structure
            self._create_directories()
            
            # Load blueprint if specified
            blueprint = self._load_blueprint()
            
            # Generate .cursorrules
            self._generate_cursorrules(blueprint)
            
            # Generate agents
            self._generate_agents(blueprint)
            
            # Generate skills
            self._generate_skills(blueprint)
            
            # Generate knowledge files
            self._generate_knowledge(blueprint)
            
            # Generate templates
            self._generate_templates(blueprint)
            
            # Generate workflows
            self._generate_workflows(blueprint)
            
            # Generate README
            self._generate_readme()
            
            # Generate diagrams folder with README
            self._generate_diagrams()
            
            return {
                'success': len(self.errors) == 0,
                'target_dir': str(self.target_dir),
                'files_created': self.generated_files,
                'errors': self.errors
            }
            
        except Exception as e:
            self.errors.append(f"Generation failed: {str(e)}")
            return {
                'success': False,
                'target_dir': str(self.target_dir),
                'files_created': self.generated_files,
                'errors': self.errors
            }
    
    def _create_directories(self) -> None:
        """Create the project directory structure."""
        directories = [
            '.cursor/agents',
            '.cursor/skills',
            'knowledge',
            'templates',
            'workflows',
            'scripts',
            'diagrams',
            'docs',
            'src'
        ]
        
        for dir_path in directories:
            full_path = self.target_dir / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            
        print(f"Created directory structure in {self.target_dir}")
    
    def _load_blueprint(self) -> Optional[Dict[str, Any]]:
        """Load blueprint configuration if specified.
        
        Returns:
            Blueprint configuration dictionary or None.
        """
        if not self.config.blueprint_id:
            return None
            
        blueprint_path = self.factory_root / 'blueprints' / self.config.blueprint_id / 'blueprint.json'
        
        if not blueprint_path.exists():
            print(f"Warning: Blueprint {self.config.blueprint_id} not found")
            return None
            
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _load_pattern(self, pattern_type: str, pattern_id: str) -> Optional[Dict[str, Any]]:
        """Load a pattern file.
        
        Args:
            pattern_type: Type of pattern (agents, skills, etc.).
            pattern_id: Pattern identifier.
            
        Returns:
            Pattern dictionary or None.
        """
        pattern_path = self.factory_root / 'patterns' / pattern_type / f'{pattern_id}.json'
        
        if not pattern_path.exists():
            return None
            
        with open(pattern_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _generate_cursorrules(self, blueprint: Optional[Dict[str, Any]]) -> None:
        """Generate the .cursorrules file.
        
        Args:
            blueprint: Optional blueprint configuration.
        """
        template = self._load_cursorrules_template()
        
        # Replace variables
        content = template.replace('{PROJECT_NAME}', self.config.project_name)
        content = content.replace('{PROJECT_DESCRIPTION}', self.config.project_description)
        content = content.replace('{PRIMARY_LANGUAGE}', self.config.primary_language)
        content = content.replace('{STYLE_GUIDE}', self.config.style_guide)
        content = content.replace('{DOMAIN}', self.config.domain)
        content = content.replace('{GENERATED_DATE}', datetime.now().strftime('%Y-%m-%d'))
        
        # Add MCP server configuration
        if self.config.mcp_servers:
            mcp_section = self._generate_mcp_section()
            content = content.replace('{MCP_SERVERS}', mcp_section)
        else:
            content = content.replace('{MCP_SERVERS}', '')
        
        # Add agents list
        agents_section = self._generate_agents_list_section()
        content = content.replace('{AGENTS_LIST}', agents_section)
        
        # Add skills list
        skills_section = self._generate_skills_list_section()
        content = content.replace('{SKILLS_LIST}', skills_section)
        
        output_path = self.target_dir / '.cursorrules'
        self._write_file(output_path, content)
    
    def _load_cursorrules_template(self) -> str:
        """Load the cursorrules template.
        
        Returns:
            Template content string.
        """
        template_path = self.factory_root / 'templates' / 'factory' / 'cursorrules-template.md'
        
        if template_path.exists():
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        # Default template
        return '''# {PROJECT_NAME} - LLM Agent Instructions

## Project Context

{PROJECT_DESCRIPTION}

**Domain:** {DOMAIN}
**Primary Language:** {PRIMARY_LANGUAGE}
**Style Guide:** {STYLE_GUIDE}

## Configuration Variables

```
PYTHON_PATH = C:\\App\\Anaconda\\python.exe
```

## Available Agents

{AGENTS_LIST}

## Available Skills

{SKILLS_LIST}

## MCP Server Integration

{MCP_SERVERS}

## Autonomous Behavior Rules

### Rule 1: Ticket Handling
When user mentions a ticket ID:
- Fetch ticket details using MCP tools
- Summarize and extract relevant information
- Proceed with appropriate workflow

### Rule 2: Code Review
After implementation:
- Invoke code reviewer agent
- Apply style guide rules
- Generate review report

### Rule 3: Data Verification
Before implementation:
- Verify data structures and assumptions
- Use grounding skill if available
- Ask user for confirmation if uncertain

## Response Behavior

- Be proactive with tool usage
- Provide specific references and line numbers
- Create actionable checklists
- Document all assumptions

---

*Generated by Cursor Agent Factory on {GENERATED_DATE}*
'''
    
    def _generate_mcp_section(self) -> str:
        """Generate MCP servers configuration section.
        
        Returns:
            Formatted MCP section string.
        """
        lines = ['| Server | Purpose | URL |', '|--------|---------|-----|']
        for server in self.config.mcp_servers:
            name = server.get('name', 'unknown')
            purpose = server.get('purpose', '')
            url = server.get('url', '')
            lines.append(f"| `{name}` | {purpose} | {url} |")
        return '\n'.join(lines)
    
    def _generate_agents_list_section(self) -> str:
        """Generate agents list section.
        
        Returns:
            Formatted agents section string.
        """
        lines = ['| Agent | Purpose |', '|-------|---------|']
        for agent_id in self.config.agents:
            pattern = self._load_pattern('agents', agent_id)
            if pattern:
                name = pattern.get('frontmatter', {}).get('name', agent_id)
                desc = pattern.get('metadata', {}).get('description', '')
                lines.append(f"| `{name}` | {desc} |")
            else:
                lines.append(f"| `{agent_id}` | Custom agent |")
        return '\n'.join(lines)
    
    def _generate_skills_list_section(self) -> str:
        """Generate skills list section.
        
        Returns:
            Formatted skills section string.
        """
        lines = ['| Skill | Description |', '|-------|-------------|']
        for skill_id in self.config.skills:
            pattern = self._load_pattern('skills', skill_id)
            if pattern:
                name = pattern.get('frontmatter', {}).get('name', skill_id)
                desc = pattern.get('metadata', {}).get('description', '')
                lines.append(f"| `{name}` | {desc} |")
            else:
                lines.append(f"| `{skill_id}` | Custom skill |")
        return '\n'.join(lines)
    
    def _generate_agents(self, blueprint: Optional[Dict[str, Any]]) -> None:
        """Generate agent files.
        
        Args:
            blueprint: Optional blueprint configuration.
        """
        agents_dir = self.target_dir / '.cursor' / 'agents'
        
        for agent_id in self.config.agents:
            pattern = self._load_pattern('agents', agent_id)
            if pattern:
                content = self._render_agent_from_pattern(pattern)
                name = pattern.get('frontmatter', {}).get('name', agent_id)
                output_path = agents_dir / f'{name}.md'
                self._write_file(output_path, content)
            else:
                print(f"Warning: Agent pattern {agent_id} not found")
    
    def _render_agent_from_pattern(self, pattern: Dict[str, Any]) -> str:
        """Render agent markdown from pattern.
        
        Args:
            pattern: Agent pattern dictionary.
            
        Returns:
            Rendered markdown content.
        """
        frontmatter = pattern.get('frontmatter', {})
        sections = pattern.get('sections', {})
        
        lines = ['---']
        for key, value in frontmatter.items():
            if isinstance(value, list):
                lines.append(f"{key}: {json.dumps(value)}")
            else:
                lines.append(f"{key}: {value}")
        lines.append('---')
        lines.append('')
        
        # Title
        title = sections.get('title', frontmatter.get('name', 'Agent'))
        lines.append(f"# {title}")
        lines.append('')
        
        # Purpose
        if 'purpose' in sections:
            lines.append('## Purpose')
            lines.append('')
            lines.append(sections['purpose'])
            lines.append('')
        
        # When Activated
        if 'whenActivated' in sections:
            lines.append('## When Activated')
            lines.append('')
            for item in sections['whenActivated']:
                lines.append(f"- {item}")
            lines.append('')
        
        # Workflow
        if 'workflow' in sections:
            lines.append('## Workflow')
            lines.append('')
            for step in sections['workflow']:
                lines.append(f"### Step {step.get('step', '')}: {step.get('name', '')}")
                lines.append('')
                lines.append(step.get('description', ''))
                if 'actions' in step:
                    lines.append('')
                    for action in step['actions']:
                        lines.append(f"- {action}")
                lines.append('')
        
        # Skills Used
        if 'skillsUsed' in sections:
            lines.append('## Skills Used')
            lines.append('')
            lines.append('| Skill | Purpose |')
            lines.append('|-------|---------|')
            for skill in sections['skillsUsed']:
                lines.append(f"| `{skill.get('skill', '')}` | {skill.get('purpose', '')} |")
            lines.append('')
        
        # Important Rules
        if 'importantRules' in sections:
            lines.append('## Important Rules')
            lines.append('')
            for i, rule in enumerate(sections['importantRules'], 1):
                lines.append(f"{i}. {rule}")
            lines.append('')
        
        return '\n'.join(lines)
    
    def _generate_skills(self, blueprint: Optional[Dict[str, Any]]) -> None:
        """Generate skill files.
        
        Args:
            blueprint: Optional blueprint configuration.
        """
        for skill_id in self.config.skills:
            pattern = self._load_pattern('skills', skill_id)
            if pattern:
                content = self._render_skill_from_pattern(pattern)
                name = pattern.get('frontmatter', {}).get('name', skill_id)
                skill_dir = self.target_dir / '.cursor' / 'skills' / name
                skill_dir.mkdir(parents=True, exist_ok=True)
                output_path = skill_dir / 'SKILL.md'
                self._write_file(output_path, content)
            else:
                print(f"Warning: Skill pattern {skill_id} not found")
    
    def _render_skill_from_pattern(self, pattern: Dict[str, Any]) -> str:
        """Render skill markdown from pattern.
        
        Args:
            pattern: Skill pattern dictionary.
            
        Returns:
            Rendered markdown content.
        """
        frontmatter = pattern.get('frontmatter', {})
        sections = pattern.get('sections', {})
        
        lines = ['---']
        for key, value in frontmatter.items():
            if isinstance(value, list):
                lines.append(f"{key}: {json.dumps(value)}")
            else:
                lines.append(f"{key}: {value}")
        lines.append('---')
        lines.append('')
        
        # Title
        title = sections.get('title', frontmatter.get('name', 'Skill'))
        lines.append(f"# {title}")
        lines.append('')
        
        # Introduction
        if 'introduction' in sections:
            lines.append(sections['introduction'])
            lines.append('')
        
        # When to Use
        if 'whenToUse' in sections:
            lines.append('## When to Use')
            lines.append('')
            for item in sections['whenToUse']:
                lines.append(f"- {item}")
            lines.append('')
        
        # Process
        if 'process' in sections:
            lines.append('## Process')
            lines.append('')
            for step in sections['process']:
                lines.append(f"### Step {step.get('step', '')}: {step.get('name', '')}")
                lines.append('')
                lines.append(step.get('description', ''))
                if 'actions' in step:
                    lines.append('')
                    for action in step['actions']:
                        lines.append(f"- {action}")
                if 'mcpTools' in step:
                    lines.append('')
                    lines.append('**MCP Tools:** ' + ', '.join(f"`{t}`" for t in step['mcpTools']))
                lines.append('')
        
        # Fallback Procedures
        if 'fallbackProcedures' in sections:
            lines.append('## Fallback Procedures')
            lines.append('')
            for proc in sections['fallbackProcedures']:
                lines.append(f"- **{proc.get('condition', '')}**: {proc.get('action', '')}")
            lines.append('')
        
        # Important Rules
        if 'importantRules' in sections:
            lines.append('## Important Rules')
            lines.append('')
            for i, rule in enumerate(sections['importantRules'], 1):
                lines.append(f"{i}. {rule}")
            lines.append('')
        
        return '\n'.join(lines)
    
    def _generate_knowledge(self, blueprint: Optional[Dict[str, Any]]) -> None:
        """Generate knowledge files.
        
        Args:
            blueprint: Optional blueprint configuration.
        """
        knowledge_dir = self.target_dir / 'knowledge'
        
        # Copy relevant knowledge files from factory
        source_knowledge = self.factory_root / 'knowledge'
        
        if source_knowledge.exists():
            for file in source_knowledge.glob('*.json'):
                dest = knowledge_dir / file.name
                shutil.copy2(file, dest)
                self.generated_files.append(str(dest))
    
    def _generate_templates(self, blueprint: Optional[Dict[str, Any]]) -> None:
        """Generate template files.
        
        Args:
            blueprint: Optional blueprint configuration.
        """
        templates_dir = self.target_dir / 'templates'
        
        # Create document templates
        docs_templates = [
            ('implementation_plan.md', self._get_implementation_plan_template()),
            ('technical_spec.md', self._get_technical_spec_template()),
            ('test_plan.md', self._get_test_plan_template())
        ]
        
        for filename, content in docs_templates:
            output_path = templates_dir / filename
            self._write_file(output_path, content)
    
    def _get_implementation_plan_template(self) -> str:
        """Get implementation plan template content.
        
        Returns:
            Template content string.
        """
        return '''# Implementation Plan: {TICKET_ID}

## References

| Type | Link |
|------|------|
| Ticket | [{TICKET_ID}]({TICKET_URL}) |
| Specification | [{SPEC_NAME}]({SPEC_URL}) |

## Problem Summary

{PROBLEM_DESCRIPTION}

## Solution Approach

{SOLUTION_DESCRIPTION}

## Data Model Verification

| Structure | Field | Verified? | Source |
|-----------|-------|-----------|--------|
| {STRUCTURE} | {FIELD} | Yes/No | {SOURCE} |

## Files to Modify

| File | Change Type | Description |
|------|-------------|-------------|
| {FILE_PATH} | Modify/Create | {DESCRIPTION} |

## Implementation Steps

### Phase 1: Preparation
- [ ] Review requirements
- [ ] Verify data model
- [ ] Create backup

### Phase 2: Implementation
- [ ] {STEP_1}
- [ ] {STEP_2}
- [ ] {STEP_3}

### Phase 3: Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Regression tests

## Code Changes

### {FILE_NAME}

**Before:**
```{LANGUAGE}
{ORIGINAL_CODE}
```

**After:**
```{LANGUAGE}
{MODIFIED_CODE}
```

---
*Generated by Cursor Agent System*
'''
    
    def _get_technical_spec_template(self) -> str:
        """Get technical specification template content.
        
        Returns:
            Template content string.
        """
        return '''# Technical Specification: {FEATURE_NAME}

## Overview

{FEATURE_DESCRIPTION}

## Requirements Reference

- Specification: [{SPEC_NAME}]({SPEC_URL})

## Architecture

### Component Diagram

```
{COMPONENT_DIAGRAM}
```

### Data Model

| Entity | Fields | Description |
|--------|--------|-------------|
| {ENTITY} | {FIELDS} | {DESCRIPTION} |

## Interface Design

### API Endpoints / Methods

| Endpoint/Method | Parameters | Returns | Description |
|-----------------|------------|---------|-------------|
| {NAME} | {PARAMS} | {RETURNS} | {DESCRIPTION} |

## Implementation Details

### {COMPONENT_NAME}

{IMPLEMENTATION_DETAILS}

## Error Handling

| Error Condition | Handling |
|-----------------|----------|
| {CONDITION} | {HANDLING} |

## Testing Strategy

{TESTING_APPROACH}

---
*Generated by Cursor Agent System*
'''
    
    def _get_test_plan_template(self) -> str:
        """Get test plan template content.
        
        Returns:
            Template content string.
        """
        return '''# Test Plan: {FEATURE_NAME}

## Overview

{TEST_SCOPE}

## Test Cases

### Unit Tests

| ID | Description | Input | Expected Output | Status |
|----|-------------|-------|-----------------|--------|
| UT-001 | {DESCRIPTION} | {INPUT} | {OUTPUT} | ⬜ |

### Integration Tests

| ID | Scenario | Steps | Expected Result | Status |
|----|----------|-------|-----------------|--------|
| IT-001 | {SCENARIO} | {STEPS} | {RESULT} | ⬜ |

### Regression Tests

- [ ] {EXISTING_FUNCTION_1} still works
- [ ] {EXISTING_FUNCTION_2} still works

## Test Data

{TEST_DATA_REQUIREMENTS}

## Environment

{TEST_ENVIRONMENT}

---
*Generated by Cursor Agent System*
'''
    
    def _generate_workflows(self, blueprint: Optional[Dict[str, Any]]) -> None:
        """Generate workflow documentation.
        
        Args:
            blueprint: Optional blueprint configuration.
        """
        workflows_dir = self.target_dir / 'workflows'
        
        # Create README
        readme_content = self._get_workflows_readme()
        self._write_file(workflows_dir / 'README.md', readme_content)
        
        # Create basic workflow files based on triggers
        if 'jira' in self.config.triggers:
            self._write_file(workflows_dir / 'bugfix_workflow.md', 
                           self._get_bugfix_workflow_template())
        
        if 'confluence' in self.config.triggers:
            self._write_file(workflows_dir / 'feature_workflow.md',
                           self._get_feature_workflow_template())
    
    def _get_workflows_readme(self) -> str:
        """Get workflows README content.
        
        Returns:
            README content string.
        """
        return f'''# Workflows

## Overview

This directory contains workflow documentation for {self.config.project_name}.

## Available Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| Bugfix | Ticket mention | Fix bugs from issue tracker |
| Feature | Specification | Implement new features |

## Quick Start

1. Mention a ticket ID to start bugfix workflow
2. Reference a specification page for feature workflow

---
*Generated by Cursor Agent Factory*
'''
    
    def _get_bugfix_workflow_template(self) -> str:
        """Get bugfix workflow template.
        
        Returns:
            Workflow template string.
        """
        return '''# Bugfix Workflow

## Trigger

Ticket ID mentioned (e.g., {PROJECT}-123)

## Steps

1. **Read Ticket** - Fetch ticket details
2. **Fetch Source** - Get relevant source code
3. **Analyze** - Find root cause
4. **Plan** - Create implementation plan
5. **Implement** - Make code changes
6. **Update** - Update ticket status

## Artifacts

- `docs/{TICKET_ID}_plan.md` - Implementation plan
- Code changes

---
*Generated by Cursor Agent Factory*
'''
    
    def _get_feature_workflow_template(self) -> str:
        """Get feature workflow template.
        
        Returns:
            Workflow template string.
        """
        return '''# Feature Workflow

## Trigger

Specification page referenced

## Steps

1. **Read Requirements** - Analyze specification
2. **Design** - Create technical design
3. **Plan** - Create implementation plan
4. **Implement** - Write code
5. **Test** - Run tests
6. **Document** - Update documentation

## Artifacts

- Technical specification
- Implementation plan
- Test plan
- Code

---
*Generated by Cursor Agent Factory*
'''
    
    def _generate_readme(self) -> None:
        """Generate project README."""
        content = f'''# {self.config.project_name}

{self.config.project_description}

## Overview

This is a Cursor agent development system generated by the Cursor Agent Factory.

**Domain:** {self.config.domain}  
**Primary Language:** {self.config.primary_language}  
**Style Guide:** {self.config.style_guide}

## Project Structure

```
{self.config.project_name}/
├── .cursor/
│   ├── agents/           # AI agent definitions
│   └── skills/           # Reusable skill definitions
├── knowledge/            # Structured reference data
├── templates/            # Code and document templates
├── workflows/            # Workflow documentation
├── scripts/              # Utility scripts
├── diagrams/             # Architecture diagrams
├── docs/                 # Documentation
├── src/                  # Source code
├── .cursorrules          # LLM agent behavior rules
└── README.md             # This file
```

## Quick Start

1. Open this project in Cursor IDE
2. The `.cursorrules` file will configure agent behavior
3. Start by mentioning a ticket or requesting a workflow

## Available Agents

{self._generate_agents_list_section()}

## Available Skills

{self._generate_skills_list_section()}

## Workflows

See `workflows/README.md` for available workflows.

---

*Generated by Cursor Agent Factory on {datetime.now().strftime('%Y-%m-%d')}*
'''
        
        self._write_file(self.target_dir / 'README.md', content)
    
    def _generate_diagrams(self) -> None:
        """Generate diagrams folder with README."""
        diagrams_dir = self.target_dir / 'diagrams'
        
        readme_content = '''# Diagrams

This directory contains architecture and workflow diagrams.

## Creating Diagrams

Use Mermaid syntax in `.mmd` files:

```mermaid
flowchart LR
    A[Start] --> B[Process] --> C[End]
```

## Rendering

To render diagrams to PNG, use a Mermaid CLI tool or the diagram rendering script.
'''
        
        self._write_file(diagrams_dir / 'README.md', readme_content)
    
    def _write_file(self, path: Path, content: str) -> None:
        """Write content to file.
        
        Args:
            path: File path.
            content: File content.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.generated_files.append(str(path))
        print(f"Created: {path}")


def generate_from_config(config_path: str, target_dir: str) -> Dict[str, Any]:
    """Generate project from configuration file.
    
    Args:
        config_path: Path to configuration file (YAML or JSON).
        target_dir: Target directory for generated project.
        
    Returns:
        Generation result dictionary.
    """
    if config_path.endswith('.yaml') or config_path.endswith('.yml'):
        config = ProjectConfig.from_yaml_file(config_path)
    else:
        config = ProjectConfig.from_json_file(config_path)
    
    generator = ProjectGenerator(config, target_dir)
    return generator.generate()


if __name__ == '__main__':
    # Example usage
    config = ProjectConfig(
        project_name='example-project',
        project_description='An example Cursor agent project',
        primary_language='python',
        agents=['code-reviewer', 'test-generator'],
        skills=['bugfix-workflow', 'feature-workflow', 'tdd'],
        triggers=['jira', 'confluence']
    )
    
    generator = ProjectGenerator(config, './example-output')
    result = generator.generate()
    print(f"Generation result: {result}")
