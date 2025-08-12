# Testing Guide

This document describes how to run and work with tests in the noWeirdUtils project.

## Overview

The project uses **pytest** as the testing framework. All tests are located in the `tests/` directory and follow pytest conventions.

## Test Structure

```
tests/
├── __init__.py                    # Makes tests a Python package
├── test_improved_converter.py     # Tests for MetricFTW converter
├── test_notweird_mutable.py      # Tests for NotWeird mutable functionality
├── test_properties.py            # Tests for NotWeird properties
├── test_quantic_time.py          # Tests for QuanticTime core functionality
├── test_timezones.py             # Tests for QuanticTime timezone features
└── test_verification.py          # Verification tests for accuracy
```

## Running Tests

### Prerequisites

Make sure you have the development dependencies installed:

```bash
poetry install --with test
```

Or if using pip in a virtual environment:

```bash
pip install pytest pytest-cov
```

### Basic Test Execution

```bash
# Run all tests
poetry run pytest

# Or using the test runner script
python run_tests.py

# Run tests with verbose output
python run_tests.py --verbose
```

### With Coverage

```bash
# Run tests with coverage report
python run_tests.py --coverage

# Or manually with pytest
poetry run pytest --cov=metricFTW --cov=noWeirdNumbersPls --cov=quanticTime --cov-report=html --cov-report=term
```

### Running Specific Tests

```bash
# Run tests for a specific module
poetry run pytest tests/test_improved_converter.py

# Run a specific test class
poetry run pytest tests/test_notweird_mutable.py::TestNotWeirdMutable

# Run a specific test method
poetry run pytest tests/test_notweird_mutable.py::TestNotWeirdMutable::test_initial_state
```

## Test Categories

### Unit Tests
- **MetricFTW Converter Tests**: Test individual conversion functions and iterable support
- **NotWeird Tests**: Test number formatting, mutable state, and properties
- **QuanticTime Tests**: Test time manipulation and timezone functions

### Integration Tests
- **Verification Tests**: Test conversion accuracy against known values
- **End-to-End Tests**: Test complete workflows

### Property Tests
- **Format Properties**: Test all formatting properties and combinations
- **Symmetry Tests**: Test that A->B->A conversions return to original values

## Writing New Tests

### Test File Naming
- Test files should start with `test_`
- Test classes should start with `Test`
- Test methods should start with `test_`

### Test Structure Example

```python
import pytest
from mymodule import MyClass

class TestMyClass:
    """Test class for MyClass functionality."""

    @pytest.fixture
    def instance(self):
        """Fixture providing a MyClass instance."""
        return MyClass()

    def test_basic_functionality(self, instance):
        """Test basic functionality."""
        result = instance.some_method()
        assert result == expected_value

    def test_error_handling(self, instance):
        """Test error handling."""
        with pytest.raises(ValueError):
            instance.some_method(invalid_input)
```

### Assertions
Use descriptive assertions:
```python
# Good
assert abs(result - expected) < 0.001  # For floating-point comparisons
assert isinstance(result, list)
assert len(result) == 3

# Avoid
assert result  # Too vague
```

## Configuration

### pytest.ini
The project includes a `pytest.ini` file with standard configuration:
- Test discovery patterns
- Markers for categorizing tests
- Output formatting

### Coverage Configuration
Coverage settings are in `pyproject.toml`:
- Source code directories to measure
- Files to omit from coverage
- Report formatting options

## Continuous Integration

The tests are designed to be run in CI/CD environments. Key considerations:
- All tests should be deterministic
- No external dependencies required
- Tests should complete quickly (< 10 seconds total)

## Current Test Coverage

As of the last run:
- **metricFTW**: 75% coverage
- **noWeirdNumbersPls**: 58% coverage
- **quanticTime**: 89% coverage
- **Overall**: 73% coverage

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure the project is installed in development mode:
   ```bash
   poetry install
   ```

2. **Missing Dependencies**: Install test dependencies:
   ```bash
   poetry install --with test
   ```

3. **Path Issues**: Run tests from the project root directory

### Getting Help

If you encounter issues with tests:
1. Check this guide first
2. Look at existing test examples
3. Run tests with `-v` flag for verbose output
4. Check the pytest documentation: https://docs.pytest.org/
