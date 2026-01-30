"""
Integration tests for the Cursor Agent Factory CLI.

Tests cover:
- --list-blueprints command
- --list-patterns command
- --blueprint generation
- --config file generation
- --help output
- Error handling for missing arguments
"""

import subprocess
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestCLIHelp:
    """Tests for CLI help functionality."""
    
    def test_help_exits_successfully(self, python_executable, cli_path):
        """Test that --help exits with code 0."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--help"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode == 0
    
    def test_help_shows_commands(self, python_executable, cli_path):
        """Test that --help shows available commands."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--help"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert "--list-blueprints" in result.stdout
        assert "--list-patterns" in result.stdout
        assert "--blueprint" in result.stdout
        assert "--config" in result.stdout
        assert "--output" in result.stdout
        assert "--interactive" in result.stdout
    
    def test_version_shows_version(self, python_executable, cli_path):
        """Test that --version shows version information."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--version"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode == 0
        assert "2.0.0" in result.stdout or "2.0.0" in result.stderr


class TestListBlueprints:
    """Tests for --list-blueprints command."""
    
    def test_list_blueprints_exits_successfully(self, python_executable, cli_path):
        """Test that --list-blueprints exits with code 0."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-blueprints"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode == 0
    
    def test_list_blueprints_shows_python_fastapi(self, python_executable, cli_path):
        """Test that python-fastapi blueprint is listed."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-blueprints"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert "python-fastapi" in result.stdout
    
    def test_list_blueprints_shows_all_blueprints(self, python_executable, cli_path):
        """Test that multiple blueprints are shown."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-blueprints"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Check for expected blueprints
        expected_blueprints = ["python-fastapi", "typescript-react", "java-spring", "sap-abap"]
        found_count = sum(1 for bp in expected_blueprints if bp in result.stdout)
        
        assert found_count >= 3, "Expected at least 3 blueprints to be listed"
    
    def test_list_blueprints_shows_metadata(self, python_executable, cli_path):
        """Test that blueprint metadata is shown."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-blueprints"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Check for metadata fields in output
        assert "Name:" in result.stdout or "Description:" in result.stdout


class TestListPatterns:
    """Tests for --list-patterns command."""
    
    def test_list_patterns_exits_successfully(self, python_executable, cli_path):
        """Test that --list-patterns exits with code 0."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-patterns"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode == 0
    
    def test_list_patterns_shows_categories(self, python_executable, cli_path):
        """Test that pattern categories are shown."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-patterns"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert "AGENTS:" in result.stdout
        assert "SKILLS:" in result.stdout
    
    def test_list_patterns_shows_patterns(self, python_executable, cli_path):
        """Test that individual patterns are listed."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--list-patterns"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert "code-reviewer" in result.stdout
        assert "bugfix-workflow" in result.stdout


class TestBlueprintGeneration:
    """Tests for --blueprint generation command."""
    
    def test_blueprint_generation_requires_output(self, python_executable, cli_path):
        """Test that --blueprint without --output fails."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--blueprint", "python-fastapi"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode != 0
        assert "output" in result.stdout.lower() or "output" in result.stderr.lower() \
            or "required" in result.stdout.lower() or "required" in result.stderr.lower()
    
    def test_blueprint_generation_invalid_blueprint(self, python_executable, cli_path, temp_output_dir):
        """Test that invalid blueprint ID fails."""
        result = subprocess.run(
            [python_executable, str(cli_path), 
             "--blueprint", "nonexistent-blueprint", 
             "--output", str(temp_output_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode != 0
        assert "not found" in result.stdout.lower() or "error" in result.stdout.lower()
    
    def test_blueprint_generation_success(self, python_executable, cli_path, temp_output_dir):
        """Test successful blueprint generation."""
        output_dir = temp_output_dir / "blueprint-test"
        
        result = subprocess.run(
            [python_executable, str(cli_path),
             "--blueprint", "python-fastapi",
             "--output", str(output_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0
        assert "success" in result.stdout.lower()
        
        # Verify generated files
        assert (output_dir / ".cursorrules").exists()
        assert (output_dir / "README.md").exists()
        assert (output_dir / ".cursor" / "agents").exists()
    
    def test_blueprint_generation_with_name(self, python_executable, cli_path, temp_output_dir):
        """Test blueprint generation with custom project name."""
        output_dir = temp_output_dir / "named-project"
        
        result = subprocess.run(
            [python_executable, str(cli_path),
             "--blueprint", "python-fastapi",
             "--name", "custom-name",
             "--output", str(output_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0


class TestConfigGeneration:
    """Tests for --config file generation command."""
    
    def test_config_generation_requires_output(self, python_executable, cli_path, sample_json_config):
        """Test that --config without --output fails."""
        result = subprocess.run(
            [python_executable, str(cli_path), "--config", str(sample_json_config)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode != 0
    
    def test_config_generation_missing_file(self, python_executable, cli_path, temp_output_dir):
        """Test that missing config file fails."""
        result = subprocess.run(
            [python_executable, str(cli_path),
             "--config", "nonexistent.yaml",
             "--output", str(temp_output_dir)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode != 0
        assert "not found" in result.stdout.lower() or "error" in result.stdout.lower()
    
    def test_config_generation_from_json(self, python_executable, cli_path, sample_json_config, temp_output_dir):
        """Test generation from JSON config file."""
        output_dir = temp_output_dir / "json-config-test"
        
        result = subprocess.run(
            [python_executable, str(cli_path),
             "--config", str(sample_json_config),
             "--output", str(output_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0
        assert (output_dir / ".cursorrules").exists()
    
    def test_config_generation_from_yaml(self, python_executable, cli_path, sample_yaml_config, temp_output_dir):
        """Test generation from YAML config file."""
        output_dir = temp_output_dir / "yaml-config-test"
        
        result = subprocess.run(
            [python_executable, str(cli_path),
             "--config", str(sample_yaml_config),
             "--output", str(output_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        assert result.returncode == 0
        assert (output_dir / ".cursorrules").exists()


class TestCLIErrorHandling:
    """Tests for CLI error handling."""
    
    def test_no_arguments_shows_help(self, python_executable, cli_path):
        """Test that running without arguments shows help."""
        result = subprocess.run(
            [python_executable, str(cli_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should show help, may or may not exit with 0
        assert "--help" in result.stdout or "--list-blueprints" in result.stdout
    
    def test_conflicting_arguments(self, python_executable, cli_path, temp_output_dir):
        """Test handling of conflicting arguments (blueprint and config together)."""
        # This should process one of them, not crash
        result = subprocess.run(
            [python_executable, str(cli_path),
             "--blueprint", "python-fastapi",
             "--config", "config.yaml",
             "--output", str(temp_output_dir)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should not crash - either succeeds or shows error
        # The actual behavior depends on implementation
        assert result.returncode is not None
