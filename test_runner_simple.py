#!/usr/bin/env python3
"""
Simple test runner for noWeirdUtils
"""
import subprocess
import sys

def main():
    print("🧪 Running tests for noWeirdUtils...")
    print("=" * 60)

    # Simple pytest command
    result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"])

    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("✅ All tests passed!")
        print("📊 Test suite completed successfully!")
    else:
        print("\n" + "=" * 60)
        print("❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
