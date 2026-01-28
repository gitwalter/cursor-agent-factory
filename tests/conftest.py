"""
Shared pytest fixtures for Cursor Agent Factory tests.

This module provides common fixtures used across unit, integration,
and validation tests.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict

import pytest

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.generate_project import ProjectConfig, ProjectGenerator


@pytest.fixture
def factory_root() -> Path:
    """Get the factory root directory.
    
    Returns:
        Path to the factory root directory.
    """
    return PROJECT_ROOT


@pytest.fixture
def temp_output_dir(tmp_path: Path) -> Path:
    """Provide a temporary directory for generation output.
    
    Args:
        tmp_path: Pytest's built-in temporary path fixture.
        
    Returns:
        Path to temporary output directory.
    """
    output_dir = tmp_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


@pytest.fixture
def sample_config() -> ProjectConfig:
    """Create a minimal valid ProjectConfig for testing.
    
    Returns:
        ProjectConfig instance with minimal valid configuration.
    """
    return ProjectConfig(
        project_name="test-project",
        project_description="Test project description",
        domain="testing",
        primary_language="python",
        frameworks=["pytest"],
        triggers=["manual"],
        agents=["code-reviewer"],
        skills=["bugfix-workflow"],
        mcp_servers=[],
        style_guide="pep8"
    )


@pytest.fixture
def sample_config_dict() -> Dict[str, Any]:
    """Create a sample configuration dictionary.
    
    Returns:
        Dictionary with valid project configuration.
    """
    return {
        "project_name": "dict-test-project",
        "project_description": "Project from dictionary",
        "domain": "web-development",
        "primary_language": "python",
        "frameworks": ["fastapi", "sqlalchemy"],
        "triggers": ["jira", "confluence"],
        "agents": ["code-reviewer", "test-generator"],
        "skills": ["bugfix-workflow", "tdd"],
        "mcp_servers": [
            {
                "name": "atlassian",
                "url": "https://mcp.atlassian.com/v1/sse",
                "purpose": "Jira/Confluence integration"
            }
        ],
        "style_guide": "google"
    }


@pytest.fixture
def sample_generator(sample_config: ProjectConfig, temp_output_dir: Path) -> ProjectGenerator:
    """Create a ProjectGenerator instance for testing.
    
    Args:
        sample_config: Sample ProjectConfig fixture.
        temp_output_dir: Temporary output directory fixture.
        
    Returns:
        ProjectGenerator instance ready for testing.
    """
    return ProjectGenerator(sample_config, str(temp_output_dir))


@pytest.fixture
def blueprints_dir(factory_root: Path) -> Path:
    """Get the blueprints directory.
    
    Args:
        factory_root: Factory root directory fixture.
        
    Returns:
        Path to blueprints directory.
    """
    return factory_root / "blueprints"


@pytest.fixture
def patterns_dir(factory_root: Path) -> Path:
    """Get the patterns directory.
    
    Args:
        factory_root: Factory root directory fixture.
        
    Returns:
        Path to patterns directory.
    """
    return factory_root / "patterns"


@pytest.fixture
def knowledge_dir(factory_root: Path) -> Path:
    """Get the knowledge directory.
    
    Args:
        factory_root: Factory root directory fixture.
        
    Returns:
        Path to knowledge directory.
    """
    return factory_root / "knowledge"


@pytest.fixture
def sample_yaml_config(tmp_path: Path, sample_config_dict: Dict[str, Any]) -> Path:
    """Create a sample YAML configuration file.
    
    Args:
        tmp_path: Pytest's built-in temporary path fixture.
        sample_config_dict: Sample configuration dictionary fixture.
        
    Returns:
        Path to the created YAML file.
    """
    import yaml
    
    yaml_path = tmp_path / "test_config.yaml"
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(sample_config_dict, f)
    return yaml_path


@pytest.fixture
def sample_json_config(tmp_path: Path, sample_config_dict: Dict[str, Any]) -> Path:
    """Create a sample JSON configuration file.
    
    Args:
        tmp_path: Pytest's built-in temporary path fixture.
        sample_config_dict: Sample configuration dictionary fixture.
        
    Returns:
        Path to the created JSON file.
    """
    json_path = tmp_path / "test_config.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sample_config_dict, f, indent=2)
    return json_path


@pytest.fixture
def python_executable() -> str:
    """Get the Python executable path for CLI tests.
    
    Returns:
        Path to Python executable.
    """
    return r"C:\App\Anaconda\python.exe"


@pytest.fixture
def cli_path(factory_root: Path) -> Path:
    """Get the CLI script path.
    
    Args:
        factory_root: Factory root directory fixture.
        
    Returns:
        Path to factory_cli.py.
    """
    return factory_root / "cli" / "factory_cli.py"
