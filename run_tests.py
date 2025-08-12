#!/usr/bin/env python3
"""
Test runner script for the no-weird-utils project.
This script can be used to run tests easily with Poetry.
"""

import subprocess
import sys
import os

def run_tests(with_coverage=False, verbose=False):
    """Run the test suite."""
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    # Build the pytest command
    cmd = ["python", "-m", "pytest", "tests/"]

    if verbose:
        cmd.append("-v")

    if with_coverage:
        # Check if pytest-cov is available
        try:
            import pytest_cov
            cmd.extend([
                "--cov=metricFTW",
                "--cov=noWeirdNumbersPls",
                "--cov=quanticTime",
                "--cov-report=term",
                "--cov-report=html"
            ])
        except ImportError:
            print("⚠️  pytest-cov not installed. Running tests without coverage.")
            print("   Install with: pip install pytest-cov")
            with_coverage = False

    print("Running tests...")
    print("Command:", " ".join(cmd))
    print("-" * 60)

    # Run the tests
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("✅ All tests passed!")
        if with_coverage:
            print("📊 Coverage report generated in htmlcov/")
    else:
        print("\n" + "=" * 60)
        print("❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run tests for no-weird-utils")
    parser.add_argument("--coverage", "-c", action="store_true",
                      help="Run tests with coverage report")
    parser.add_argument("--verbose", "-v", action="store_true",
                      help="Run tests in verbose mode")

    args = parser.parse_args()

    run_tests(with_coverage=args.coverage, verbose=args.verbose)
