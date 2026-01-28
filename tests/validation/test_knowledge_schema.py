"""
Schema validation tests for knowledge files.

Tests validate that knowledge JSON files conform to expected structure.
"""

import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft7Validator

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


# Define skill catalog schema
SKILL_CATALOG_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["skills"],
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "version": {"type": "string"},
        "categories": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "description": {"type": "string"},
                    "implementedInFactory": {"type": "boolean"},
                    "note": {"type": "string"}
                }
            }
        },
        "skills": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["id", "name", "category"],
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "category": {"type": "string"},
                    "stackAgnostic": {"type": "boolean"},
                    "description": {"type": "string"},
                    "factoryPattern": {"type": ["string", "null"]},
                    "implementationRepo": {"type": "string"},
                    "whenToUse": {"type": "array", "items": {"type": "string"}}
                }
            }
        },
        "skillsByStack": {
            "type": "object",
            "additionalProperties": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "usage": {"type": "object"}
    }
}

# Define MCP servers catalog schema
MCP_CATALOG_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "version": {"type": "string"},
        "servers": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["name"],
                "properties": {
                    "name": {"type": "string"},
                    "url": {"type": "string"},
                    "description": {"type": "string"},
                    "authentication": {"type": "string"},
                    "tools": {"type": "array"}
                }
            }
        }
    }
}


class TestKnowledgeFilesStructure:
    """Tests for knowledge file structure."""
    
    def test_all_knowledge_files_valid_json(self, knowledge_dir):
        """Test that all knowledge files are valid JSON."""
        for knowledge_file in knowledge_dir.glob("*.json"):
            try:
                with open(knowledge_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                assert isinstance(data, dict), f"{knowledge_file} should be a JSON object"
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in {knowledge_file}: {e}")
    
    def test_knowledge_files_have_content(self, knowledge_dir):
        """Test that knowledge files are not empty."""
        for knowledge_file in knowledge_dir.glob("*.json"):
            with open(knowledge_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            assert len(data) > 0, f"{knowledge_file} should not be empty"


class TestSkillCatalogSchema:
    """Tests for skill catalog schema validation."""
    
    @pytest.fixture
    def validator(self):
        """Create a JSON schema validator."""
        return Draft7Validator(SKILL_CATALOG_SCHEMA)
    
    def test_skill_catalog_exists(self, knowledge_dir):
        """Test that skill-catalog.json exists."""
        catalog_path = knowledge_dir / "skill-catalog.json"
        assert catalog_path.exists(), "skill-catalog.json should exist"
    
    def test_skill_catalog_valid(self, knowledge_dir, validator):
        """Test that skill catalog is valid against schema."""
        catalog_path = knowledge_dir / "skill-catalog.json"
        
        with open(catalog_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        errors = list(validator.iter_errors(data))
        assert len(errors) == 0, f"Validation errors: {[e.message for e in errors]}"
    
    def test_skill_catalog_has_skills(self, knowledge_dir):
        """Test that skill catalog has skills defined."""
        catalog_path = knowledge_dir / "skill-catalog.json"
        
        with open(catalog_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        skills = data.get("skills", {})
        assert len(skills) > 0, "Skill catalog should have at least one skill"
    
    def test_skill_ids_match_keys(self, knowledge_dir):
        """Test that skill IDs match their dictionary keys."""
        catalog_path = knowledge_dir / "skill-catalog.json"
        
        with open(catalog_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for key, skill in data.get("skills", {}).items():
            skill_id = skill.get("id")
            assert skill_id == key, f"Skill ID '{skill_id}' should match key '{key}'"
    
    def test_skills_have_categories(self, knowledge_dir):
        """Test that all skills have valid categories."""
        catalog_path = knowledge_dir / "skill-catalog.json"
        
        with open(catalog_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        categories = set(data.get("categories", {}).keys())
        
        for skill_id, skill in data.get("skills", {}).items():
            category = skill.get("category")
            assert category in categories, \
                f"Skill '{skill_id}' has invalid category '{category}'"


class TestStackCapabilitiesSchema:
    """Tests for stack capabilities file."""
    
    def test_stack_capabilities_exists(self, knowledge_dir):
        """Test that stack-capabilities.json exists."""
        capabilities_path = knowledge_dir / "stack-capabilities.json"
        assert capabilities_path.exists(), "stack-capabilities.json should exist"
    
    def test_stack_capabilities_valid_json(self, knowledge_dir):
        """Test that stack capabilities is valid JSON."""
        capabilities_path = knowledge_dir / "stack-capabilities.json"
        
        with open(capabilities_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, dict), "Stack capabilities should be a JSON object"


class TestWorkflowPatternsSchema:
    """Tests for workflow patterns file."""
    
    def test_workflow_patterns_exists(self, knowledge_dir):
        """Test that workflow-patterns.json exists."""
        patterns_path = knowledge_dir / "workflow-patterns.json"
        assert patterns_path.exists(), "workflow-patterns.json should exist"
    
    def test_workflow_patterns_valid_json(self, knowledge_dir):
        """Test that workflow patterns is valid JSON."""
        patterns_path = knowledge_dir / "workflow-patterns.json"
        
        with open(patterns_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, dict), "Workflow patterns should be a JSON object"


class TestBestPracticesSchema:
    """Tests for best practices file."""
    
    def test_best_practices_exists(self, knowledge_dir):
        """Test that best-practices.json exists."""
        practices_path = knowledge_dir / "best-practices.json"
        assert practices_path.exists(), "best-practices.json should exist"
    
    def test_best_practices_valid_json(self, knowledge_dir):
        """Test that best practices is valid JSON."""
        practices_path = knowledge_dir / "best-practices.json"
        
        with open(practices_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, dict), "Best practices should be a JSON object"


class TestKnowledgeFileNaming:
    """Tests for knowledge file naming conventions."""
    
    def test_knowledge_files_use_kebab_case(self, knowledge_dir):
        """Test that knowledge files use kebab-case naming."""
        for knowledge_file in knowledge_dir.glob("*.json"):
            filename = knowledge_file.stem
            
            # Check for kebab-case (lowercase with hyphens)
            assert filename == filename.lower(), \
                f"Knowledge file '{filename}' should be lowercase"
            assert "_" not in filename, \
                f"Knowledge file '{filename}' should use hyphens, not underscores"
    
    def test_knowledge_files_have_json_extension(self, knowledge_dir):
        """Test that knowledge files have .json extension."""
        # This is implicit from the glob, but good to document
        json_files = list(knowledge_dir.glob("*.json"))
        all_files = list(knowledge_dir.iterdir())
        
        # Filter to only files (not directories)
        all_files = [f for f in all_files if f.is_file()]
        
        assert len(json_files) == len(all_files), \
            "All knowledge files should have .json extension"
