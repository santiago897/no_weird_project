#!/usr/bin/env python3
"""
Test suite for NotWeird mutable object functionality.
"""

import pytest
from noWeirdNumbersPls.format_number import NotWeird


class TestNotWeirdMutable:
    """Test class for NotWeird mutable functionality."""

    def test_initial_state(self):
        """Test initial state of NotWeird object."""
        n = NotWeird(1234567.89)
        assert n.number == 1234567.89
        # The format depends on the default settings, just check it's a string with the number
        formatted = n.default()
        assert isinstance(formatted, str)
        assert "1234567" in formatted.replace(",", "").replace(".", "")

    def test_prefix_storage(self):
        """Test that prefix is stored in the object."""
        n = NotWeird(1234567.89)
        n.add_prefix('€')

        # Check that prefix is applied to all format methods
        assert n.default().startswith('€')
        assert n.percent().startswith('€')
        assert n.scientific().startswith('€')

    def test_suffix_storage(self):
        """Test that suffix is stored in the object."""
        n = NotWeird(1234567.89)
        n.add_suffix(' EUR')

        # Check that suffix is applied
        assert n.default().endswith(' EUR')

    def test_prefix_and_suffix_combination(self):
        """Test combining prefix and suffix."""
        n = NotWeird(1234567.89)
        n.add_prefix('€').add_suffix(' EUR')

        result = n.default()
        assert result.startswith('€')
        assert result.endswith(' EUR')

    def test_format_style_changes(self):
        """Test changing number format style."""
        n = NotWeird(1234567.89)

        # Set to Anglo style first
        n.anglo()
        anglo_format = n.default()

        # Change to European style
        n.notAnglo()
        european_format = n.default()

        # The formats should be different
        assert anglo_format != european_format

    def test_decimal_places_setting(self):
        """Test setting decimal places."""
        n = NotWeird(1234567.89)
        n.with_decimals(3)

        result = n.default()
        # For European format, comma is the decimal separator
        if ',' in result:
            decimal_part = result.split(',')[-1]
        elif '.' in result and not ',' in result:
            # If only dots, the last one might be decimal separator
            decimal_part = result.split('.')[-1]
        else:
            decimal_part = ""

        # The decimal part should have exactly 3 digits
        decimal_digits = ''.join(c for c in decimal_part if c.isdigit())
        assert len(decimal_digits) == 3

    def test_temporary_override(self):
        """Test temporary prefix/suffix override."""
        n = NotWeird(1234567.89)
        n.add_prefix('€').add_suffix(' EUR')

        # Temporary override
        temp_result = n.default(prefix='$', suffix=' USD')
        assert temp_result.startswith('$')
        assert temp_result.endswith(' USD')

        # Original settings should be preserved
        original_result = n.default()
        assert original_result.startswith('€')
        assert original_result.endswith(' EUR')

    def test_method_chaining(self):
        """Test chaining multiple settings."""
        n = NotWeird(9876.543)
        result = n.anglo().add_prefix('$').add_suffix(' USD').with_decimals(2)

        # Should return self for chaining
        assert result is n

        # Check final formatting
        formatted = n.default()
        assert formatted.startswith('$')
        assert formatted.endswith(' USD')

    def test_multiple_objects_independence(self):
        """Test that multiple NotWeird objects are independent."""
        n1 = NotWeird(1234567.89)
        n2 = NotWeird(9876.543)

        n1.add_prefix('€').add_suffix(' EUR')
        n2.add_prefix('$').add_suffix(' USD')

        # Objects should have different formatting
        result1 = n1.default()
        result2 = n2.default()

        assert result1.startswith('€')
        assert result1.endswith(' EUR')
        assert result2.startswith('$')
        assert result2.endswith(' USD')

    def test_property_access(self):
        """Test accessing stored properties."""
        n = NotWeird(255)
        n.add_prefix('Value: ').add_suffix(' units').with_decimals(2)

        assert n.number == 255
        assert hasattr(n, '_prefix')
        assert hasattr(n, '_suffix')
        assert hasattr(n, '_decimals')