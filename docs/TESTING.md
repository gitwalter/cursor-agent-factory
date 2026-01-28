# Testing Documentation

This document describes the test suite for the Cursor Agent Factory project.

## Overview

The test suite uses **pytest** and consists of **131 tests** organized into three categories:

| Category | Tests | Purpose |
|----------|-------|---------|
| Unit Tests | 60 | Test individual components in isolation |
| Integration Tests | 38 | Test component interactions and CLI |
| Validation Tests | 33 | Validate JSON schemas and file structure |

## Quick Start

### Install Dependencies

```powershell
# Windows (Anaconda)
C:\App\Anaconda\Scripts\pip.exe install -r requirements-dev.txt

# Linux/macOS
pip install -r requirements-dev.txt
```

### Run All Tests

```powershell
# Windows
C:\App\Anaconda\python.exe -m pytest tests/ -v

# Linux/macOS
python -m pytest tests/ -v
```

## Test Structure

```
tests/
├── __init__.py
├── conftest.py                     # Shared fixtures
├── unit/                           # Unit tests
│   ├── __init__.py
│   ├── test_project_config.py      # ProjectConfig dataclass
│   ├── test_project_generator.py   # ProjectGenerator class
│   └── test_pattern_loading.py     # Pattern/blueprint loading
├── integration/                    # Integration tests
│   ├── __init__.py
│   ├── test_cli.py                 # CLI commands
│   └── test_generation.py          # End-to-end generation
├── validation/                     # Schema validation
│   ├── __init__.py
│   ├── test_blueprint_schema.py    # Blueprint JSON schema
│   ├── test_pattern_schema.py      # Pattern JSON schemas
│   └── test_knowledge_schema.py    # Knowledge file schemas
└── fixtures/                       # Test data files
    ├── README.md
    ├── sample_config.yaml
    ├── sample_config.json
    ├── minimal_blueprint.json
    ├── empty_config.json
    └── invalid_config.json
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

**Key scenarios tested:**
- Minimal vs full configuration
- Default value consistency
- Error handling for missing/invalid files
- Mutable default isolation

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

**Key scenarios tested:**
- All expected directories created
- Correct markdown structure with frontmatter
- UTF-8 encoding for generated files
- File tracking for all created files

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

**Key scenarios tested:**
- CLI exits with correct codes
- Output contains expected content
- Error messages for invalid inputs
- Generation creates expected files

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

## Validation Tests

### test_blueprint_schema.py (6 tests)

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
```

## Code Coverage

```powershell
# Generate coverage report
python -m pytest tests/ --cov=scripts --cov=cli --cov-report=html

# View HTML report
start htmlcov/index.html
```

Coverage reports show which lines of code are exercised by tests.

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
```

### Adding Integration Tests

1. Create test file in `tests/integration/`
2. Use `subprocess` for CLI tests
3. Use `temp_output_dir` fixture for file generation tests

### Adding Validation Tests

1. Create test file in `tests/validation/`
2. Define JSON schema using `jsonschema`
3. Iterate over files in target directories

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

## Best Practices

1. **Test isolation**: Each test should be independent
2. **Descriptive names**: Test names should describe what's being tested
3. **Use fixtures**: Avoid duplicating setup code
4. **Test edge cases**: Include error conditions and boundary cases
5. **Keep tests fast**: Mock external dependencies when possible
6. **Document tests**: Use docstrings to explain complex tests
