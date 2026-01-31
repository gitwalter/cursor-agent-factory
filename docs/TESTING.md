# Testing Documentation

This document describes the test suite for the Cursor Agent Factory project.

> **Tool Paths:** Commands in this document use the `cursor-factory` conda environment.
> See [Configuration Guide](CONFIGURATION.md) to customize for your environment.

## Overview

The test suite uses **pytest** and consists of **458 tests** organized into three categories:

| Category | Tests | Purpose |
|----------|-------|---------|
| Unit Tests | ~200 | Test individual components in isolation |
| Integration Tests | ~50 | Test component interactions and CLI |
| Validation Tests | ~208 | Validate JSON schemas and file structure |

**Code Coverage: 77%** (as of latest update)

| Module | Coverage |
|--------|----------|
| `cli/factory_cli.py` | 75% |
| `scripts/install-hooks.py` | 94% |
| `scripts/backup_manager.py` | 73% |
| `scripts/repo_analyzer.py` | 82% |
| `scripts/merge_strategy.py` | 85% |
| `scripts/validate_readme_structure.py` | 96% |
| `scripts/generate_project.py` | 66% |

## Quick Start

### Install Dependencies

```powershell
# Create and activate conda environment
conda create -n cursor-factory python=3.11 -y
conda activate cursor-factory
pip install -r requirements-dev.txt
```

### Run All Tests

```powershell
# With cursor-factory environment
python -m pytest tests/ -v

# With coverage report
python -m pytest tests/ --cov=scripts --cov=cli --cov-report=term-missing
```

## Test Structure

```
tests/
├── __init__.py
├── conftest.py                     # Shared fixtures
├── unit/                           # Unit tests (~200 tests)
│   ├── __init__.py
│   ├── test_project_config.py      # ProjectConfig dataclass
│   ├── test_project_generator.py   # ProjectGenerator class
│   ├── test_pattern_loading.py     # Pattern/blueprint loading
│   ├── test_factory_cli.py         # CLI function tests
│   ├── test_install_hooks.py       # Git hooks installation
│   ├── test_backup_manager.py      # Backup/rollback system
│   ├── test_repo_analyzer.py       # Repository analysis
│   ├── test_merge_strategy.py      # Merge conflict handling
│   ├── test_validate_readme.py     # README validation
│   ├── test_pm_adapters.py         # PM backend adapters
│   └── test_pm_config.py           # PM configuration
├── integration/                    # Integration tests (~50 tests)
│   ├── __init__.py
│   ├── test_cli.py                 # CLI commands
│   ├── test_cli_pm.py              # PM CLI integration
│   └── test_generation.py          # End-to-end generation
├── validation/                     # Schema validation (~208 tests)
│   ├── __init__.py
│   ├── test_blueprint_schema.py    # Blueprint JSON schema
│   ├── test_pattern_schema.py      # Pattern JSON schemas
│   ├── test_knowledge_schema.py    # Knowledge file schemas
│   ├── test_pm_schema.py           # PM configuration schema
│   └── test_readme_structure.py    # README structure validation
└── fixtures/                       # Test data files
    ├── README.md
    ├── sample_config.yaml
    ├── sample_config.json
    ├── minimal_blueprint.json
    ├── empty_config.json
    ├── invalid_config.json
    ├── pm/                          # PM test fixtures
    │   ├── sample_pm_config.json
    │   └── sample_pm_config.yaml
    └── existing_repo_*/            # Onboarding test fixtures
```

## Unit Tests

### test_project_config.py (19 tests)

Tests for the `ProjectConfig` dataclass in `scripts/generate_project.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestProjectConfigInstantiation` | 3 | Direct instantiation with various parameters |
| `TestProjectConfigFromDict` | 5 | `from_dict()` factory method |
| `TestProjectConfigFromYaml` | 4 | `from_yaml_file()` factory method |
| `TestProjectConfigFromJson` | 5 | `from_json_file()` factory method |
| `TestProjectConfigDefaults` | 2 | Default value handling |

### test_project_generator.py (28 tests)

Tests for the `ProjectGenerator` class in `scripts/generate_project.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestProjectGeneratorInit` | 2 | Initialization and factory root detection |
| `TestDirectoryCreation` | 2 | Directory structure creation |
| `TestBlueprintLoading` | 3 | Blueprint loading (valid/missing/none) |
| `TestPatternLoading` | 4 | Pattern loading from files |
| `TestAgentRendering` | 3 | Agent markdown generation |
| `TestSkillRendering` | 3 | Skill markdown generation |
| `TestFileWriting` | 4 | File creation and tracking |
| `TestCursorrulesGeneration` | 2 | Variable substitution in .cursorrules |
| `TestMcpServerSection` | 2 | MCP server configuration |
| `TestFullGeneration` | 3 | Complete generation workflow |

### test_factory_cli.py (44 tests)

Tests for the CLI interface functions in `cli/factory_cli.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestGetFactoryRoot` | 3 | Factory root path detection |
| `TestDisplayWelcome` | 1 | Welcome message display |
| `TestDisplayTour` | 1 | Post-generation tour display |
| `TestDisplayErrorWithHelp` | 1 | Error message formatting |
| `TestListBlueprints` | 2 | Blueprint listing |
| `TestListPatterns` | 2 | Pattern listing |
| `TestRunQuickstart` | 4 | Quickstart functionality |
| `TestInteractiveMode` | 3 | Interactive requirements gathering |
| `TestGenerateFromBlueprint` | 4 | Blueprint-based generation |
| `TestGenerateFromConfigFile` | 2 | Config file generation |
| `TestAnalyzeRepository` | 2 | Repository analysis |
| `TestOnboardRepository` | 3 | Onboarding workflow |
| `TestRollbackSession` | 2 | Session rollback |
| `TestCreateDefaultConfig` | 1 | Default config creation |
| `TestInteractiveConflictResolver` | 2 | Conflict resolution UI |
| `TestMain` | 11 | Main CLI entry point |

### test_install_hooks.py (11 tests)

Tests for Git hook installation in `scripts/install-hooks.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestPreCommitHookContent` | 8 | Hook script content validation |
| `TestInstallHooks` | 3 | Hook installation logic |

### test_backup_manager.py (30 tests)

Tests for backup and rollback in `scripts/backup_manager.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestBackupEntry` | 2 | Backup entry dataclass |
| `TestBackupManifest` | 4 | Manifest serialization |
| `TestBackupSession` | 6 | Session management |
| `TestBackupManager` | 12 | Manager operations |
| `TestEnsureGitignoreExcludesBackup` | 3 | Gitignore handling |
| `TestMainEntry` | 3 | CLI interface |

### test_repo_analyzer.py (27 tests)

Tests for repository analysis in `scripts/repo_analyzer.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestOnboardingScenario` | 1 | Scenario enum values |
| `TestCursorruleAnalysis` | 1 | Cursorrules dataclass |
| `TestMcpAnalysis` | 1 | MCP analysis dataclass |
| `TestTechStackDetection` | 1 | Tech stack dataclass |
| `TestRepoInventory` | 2 | Inventory summary |
| `TestRepoAnalyzer` | 19 | Full analysis workflow |
| `TestGetFileHash` | 4 | File hashing utility |
| `TestMainEntry` | 2 | CLI interface |

### test_merge_strategy.py (41 tests)

Tests for merge conflict handling in `scripts/merge_strategy.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestConflictResolution` | 1 | Resolution enum values |
| `TestArtifactType` | 1 | Artifact type enum |
| `TestMergeStrategy` | 1 | Strategy enum |
| `TestDefaultStrategies` | 4 | Default strategy mappings |
| `TestConflict` | 3 | Conflict dataclass |
| `TestConflictPrompt` | 1 | Prompt formatting |
| `TestMergeResult` | 2 | Result dataclass |
| `TestMergeEngine` | 14 | Engine operations |
| `TestMergeJsonFiles` | 6 | JSON merge logic |
| `TestDeepMerge` | 4 | Deep merge helper |

### test_validate_readme.py (43 tests)

Tests for README validation in `scripts/validate_readme_structure.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestStructureValidatorInit` | 2 | Initialization |
| `TestShouldIgnore` | 5 | Path ignore logic |
| `TestCountFilesByExtension` | 3 | File counting |
| `TestScanAgents` | 2 | Agent scanning |
| `TestScanSkills` | 2 | Skill scanning |
| `TestScanBlueprints` | 2 | Blueprint scanning |
| `TestScanPatterns` | 2 | Pattern scanning |
| `TestScanKnowledge` | 2 | Knowledge scanning |
| `TestScanTemplates` | 2 | Template scanning |
| `TestScanAll` | 1 | Full scan |
| `TestRoundToThreshold` | 3 | Threshold rounding |
| `TestGenerateCountsSummary` | 1 | Summary generation |
| `TestExtractReadmeCounts` | 3 | README parsing |
| `TestValidate` | 2 | Validation logic |
| `TestUpdateReadme` | 3 | README update |
| `TestGenerateStructureMarkdown` | 2 | Markdown generation |
| `TestMain` | 6 | CLI interface |

### test_pattern_loading.py (13 tests)

Tests for pattern and blueprint file loading.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestBlueprintFiles` | 3 | Blueprint JSON validation |
| `TestAgentPatternFiles` | 3 | Agent pattern structure |
| `TestSkillPatternFiles` | 3 | Skill pattern structure |
| `TestKnowledgeFiles` | 2 | Knowledge file validation |
| `TestPatternConsistency` | 2 | Cross-reference validation |

## Integration Tests

### test_cli.py (20 tests)

Tests for the CLI interface in `cli/factory_cli.py`.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestCLIHelp` | 3 | `--help` and `--version` |
| `TestListBlueprints` | 4 | `--list-blueprints` command |
| `TestListPatterns` | 3 | `--list-patterns` command |
| `TestBlueprintGeneration` | 4 | `--blueprint` generation |
| `TestConfigGeneration` | 4 | `--config` generation |
| `TestCLIErrorHandling` | 2 | Error cases |

### test_generation.py (18 tests)

End-to-end tests for project generation.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestFullProjectGeneration` | 5 | Complete structure creation |
| `TestBlueprintGeneration` | 2 | Blueprint-based generation |
| `TestGeneratedContentValidation` | 4 | Content correctness |
| `TestWorkflowGeneration` | 3 | Workflow file creation |
| `TestGenerationErrors` | 2 | Error handling |
| `TestFileTracking` | 2 | File tracking accuracy |

### test_cli_pm.py

Tests for Project Management CLI integration.

| Test | Description |
|------|-------------|
| PM backend configuration | GitHub, Jira, Azure DevOps, Linear |
| PM workflow integration | Sprint planning, task creation |
| PM artifact generation | PM-specific agents and skills |

## Validation Tests

### test_blueprint_schema.py (7 tests)

JSON schema validation for blueprint files.

| Test | Description |
|------|-------------|
| `test_schema_is_valid` | Schema definition is valid |
| `test_all_blueprints_valid` | All blueprints pass schema validation |
| `test_python_fastapi_blueprint_valid` | Specific blueprint validation |
| `test_blueprint_ids_match_directory_names` | ID/directory consistency |
| `test_blueprint_has_valid_language` | Valid primary language |
| `test_blueprint_agent_references_format` | Agent reference format |

### test_pattern_schema.py (12 tests)

JSON schema validation for pattern files.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestAgentPatternSchema` | 5 | Agent pattern schema validation |
| `TestSkillPatternSchema` | 5 | Skill pattern schema validation |
| `TestPatternConsistency` | 2 | ID/filename/name consistency |

### test_knowledge_schema.py (15 tests)

Validation for knowledge files.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestKnowledgeFilesStructure` | 2 | JSON validity and content |
| `TestSkillCatalogSchema` | 5 | skill-catalog.json validation |
| `TestStackCapabilitiesSchema` | 2 | stack-capabilities.json |
| `TestWorkflowPatternsSchema` | 2 | workflow-patterns.json |
| `TestBestPracticesSchema` | 2 | best-practices.json |
| `TestKnowledgeFileNaming` | 2 | Naming conventions |

### test_readme_structure.py (29 tests)

README structure validation against actual filesystem.

| Test Class | Tests | Description |
|------------|-------|-------------|
| `TestReadmeStructureCounts` | 6 | Component count validation |
| `TestStructureValidatorFunctionality` | 10 | Validator methods |
| `TestProjectComponentsExist` | 9 | Directory existence |

## Fixtures

### conftest.py

Shared fixtures available to all tests:

| Fixture | Description |
|---------|-------------|
| `factory_root` | Path to factory root directory |
| `temp_output_dir` | Temporary directory for generation output |
| `sample_config` | Minimal valid `ProjectConfig` instance |
| `sample_config_dict` | Sample configuration dictionary |
| `sample_generator` | Pre-configured `ProjectGenerator` instance |
| `blueprints_dir` | Path to blueprints directory |
| `patterns_dir` | Path to patterns directory |
| `knowledge_dir` | Path to knowledge directory |
| `sample_yaml_config` | Path to temp YAML config file |
| `sample_json_config` | Path to temp JSON config file |
| `python_executable` | Python executable path for CLI tests |
| `cli_path` | Path to factory_cli.py |

### Test Fixture Files

| File | Purpose |
|------|---------|
| `sample_config.yaml` | Valid YAML configuration |
| `sample_config.json` | Valid JSON configuration |
| `minimal_blueprint.json` | Minimal valid blueprint |
| `empty_config.json` | Empty config for default testing |
| `invalid_config.json` | Invalid JSON for error testing |
| `pm/sample_pm_config.json` | PM configuration sample |
| `pm/sample_pm_config.yaml` | PM YAML configuration |
| `existing_repo_fresh/` | Fresh repo for onboarding tests |
| `existing_repo_minimal/` | Minimal repo for onboarding tests |
| `existing_repo_partial/` | Partial repo for onboarding tests |

## Running Specific Tests

```powershell
# Run a specific test file
python -m pytest tests/unit/test_project_config.py -v

# Run tests matching a pattern
python -m pytest tests/ -k "blueprint" -v

# Run a specific test class
python -m pytest tests/unit/test_project_generator.py::TestFileWriting -v

# Run a specific test method
python -m pytest tests/unit/test_project_config.py::TestProjectConfigFromDict::test_from_dict_valid_full -v

# Run with parallel execution
python -m pytest tests/ -n auto -v
```

## Code Coverage

```powershell
# Generate coverage report (terminal)
python -m pytest tests/ --cov=scripts --cov=cli --cov-report=term-missing

# Generate HTML coverage report
python -m pytest tests/ --cov=scripts --cov=cli --cov-report=html

# View HTML report (Windows)
start htmlcov/index.html

# View HTML report (macOS/Linux)
open htmlcov/index.html
```

### Coverage Goals

| Target | Goal | Current |
|--------|------|---------|
| Overall | 80% | 77% |
| Critical paths | 90% | ~85% |
| New code | 100% | - |

## CI/CD Integration

The test suite runs automatically on GitHub Actions:

- **Triggers**: Push to `main`/`develop`, pull requests
- **Matrix**: Python 3.10, 3.11, 3.12 on Ubuntu and Windows
- **Jobs**:
  - `test`: Run all tests with coverage
  - `lint`: Code quality with Ruff
  - `validate-json`: JSON syntax validation
  - `generate-test`: End-to-end generation verification

See `.github/workflows/ci.yml` for the full configuration.

## Writing New Tests

### Adding Unit Tests

1. Create test file in `tests/unit/` following naming convention `test_*.py`
2. Import the module under test
3. Use pytest fixtures from `conftest.py`
4. Follow existing test structure with test classes

```python
import pytest
from scripts.generate_project import ProjectConfig

class TestMyFeature:
    def test_feature_works(self, sample_config):
        """Test description."""
        result = sample_config.some_method()
        assert result == expected
    
    def test_edge_case(self):
        """Test edge case handling."""
        with pytest.raises(ValueError):
            some_function(invalid_input)
```

### Adding Integration Tests

1. Create test file in `tests/integration/`
2. Use `subprocess` for CLI tests
3. Use `temp_output_dir` fixture for file generation tests

```python
import subprocess

class TestCLIIntegration:
    def test_cli_command(self, cli_path, python_executable, temp_output_dir):
        result = subprocess.run(
            [python_executable, cli_path, "--blueprint", "python-fastapi", "--output", str(temp_output_dir)],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
```

### Adding Validation Tests

1. Create test file in `tests/validation/`
2. Define JSON schema using `jsonschema`
3. Iterate over files in target directories

```python
import json
from jsonschema import validate, ValidationError

class TestMySchema:
    def test_all_files_valid(self, target_dir):
        for file_path in target_dir.glob("*.json"):
            with open(file_path) as f:
                data = json.load(f)
            validate(data, MY_SCHEMA)
```

## Troubleshooting

### Common Issues

**Import errors:**
- Ensure `conftest.py` adds project root to `sys.path`
- Check that `__init__.py` exists in test directories

**Fixture not found:**
- Fixtures must be in `conftest.py` or imported
- Check fixture scope (function/class/module/session)

**Tests fail on Windows:**
- Use `pathlib.Path` for cross-platform paths
- Use `encoding='utf-8'` for file operations

**Slow tests:**
- Use `pytest-xdist` for parallel execution: `pytest -n auto`
- Mark slow tests with `@pytest.mark.slow`

**Timeout errors:**
- Default timeout is 120 seconds (configured in `pytest.ini`)
- Use `@pytest.mark.timeout(300)` for longer tests

## Best Practices

1. **Test isolation**: Each test should be independent
2. **Descriptive names**: Test names should describe what's being tested
3. **Use fixtures**: Avoid duplicating setup code
4. **Test edge cases**: Include error conditions and boundary cases
5. **Keep tests fast**: Mock external dependencies when possible
6. **Document tests**: Use docstrings to explain complex tests
7. **Use temporary directories**: Always use `tempfile.TemporaryDirectory()` for file operations
8. **Verify cleanup**: Ensure tests clean up after themselves
9. **Test both success and failure paths**: Cover happy path and error handling
10. **Use parametrize**: For testing multiple inputs, use `@pytest.mark.parametrize`