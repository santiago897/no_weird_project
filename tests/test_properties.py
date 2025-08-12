#!/usr/bin/env python3
"""
Test suite for NotWeird formatted properties functionality.
"""

import pytest
from noWeirdNumbersPls.format_number import NotWeird


class TestNotWeirdProperties:
    """Test class for NotWeird formatted properties."""

    def test_basic_formatted_properties(self):
        """Test basic formatted properties without prefix/suffix."""
        n = NotWeird(255)

        # Test basic properties exist and return strings
        assert isinstance(n.formatted, str)
        assert isinstance(n.formatted_percent, str)
        assert isinstance(n.formatted_scientific, str)
        assert isinstance(n.formatted_binary, str)
        assert isinstance(n.formatted_hex, str)
        assert isinstance(n.formatted_roman, str)

    def test_formatted_properties_with_prefix_suffix(self):
        """Test formatted properties with prefix and suffix."""
        n = NotWeird(255)
        n.add_prefix('Value: ').add_suffix(' units')

        # All formatted properties should include prefix and suffix
        assert n.formatted.startswith('Value: ')
        assert n.formatted.endswith(' units')
        assert n.formatted_percent.startswith('Value: ')
        assert n.formatted_percent.endswith(' units')
        assert n.formatted_scientific.startswith('Value: ')
        assert n.formatted_scientific.endswith(' units')

    def test_binary_and_hex_formatting(self):
        """Test binary and hex formatting."""
        n = NotWeird(255)

        # Binary of 255 should be 11111111
        assert '11111111' in n.formatted_binary

        # Hex of 255 should be ff or FF
        hex_result = n.formatted_hex.lower()
        assert 'ff' in hex_result

    def test_roman_numerals(self):
        """Test Roman numeral formatting."""
        n = NotWeird(1984)
        n.add_prefix('Year: ').add_suffix(' AD')

        roman_result = n.formatted_roman
        assert roman_result.startswith('Year: ')
        assert roman_result.endswith(' AD')
        # 1984 in Roman numerals should contain M, CM, L, XXX, IV
        assert 'M' in roman_result

    def test_decimal_number_formatting(self):
        """Test formatting with decimal numbers."""
        n = NotWeird(123.456)
        n.notAnglo().add_prefix('€').add_suffix(' EUR')

        # Test that all properties work with decimals
        assert n.formatted.startswith('€')
        assert n.formatted.endswith(' EUR')
        assert n.formatted_percent.startswith('€')
        assert n.formatted_scientific.startswith('€')

    def test_raw_properties(self):
        """Test raw properties (without prefix/suffix)."""
        n = NotWeird(123.456)
        n.notAnglo().add_prefix('€').add_suffix(' EUR')

        # Raw properties should not include prefix/suffix
        assert not n.raw_default.startswith('€')
        assert not n.raw_default.endswith(' EUR')
        assert not n.raw_percent.startswith('€')
        assert not n.raw_scientific.startswith('€')
        assert not n.raw_binary.startswith('€')
        assert not n.raw_hex.startswith('€')
        assert not n.raw_roman.startswith('€')

    def test_percentage_formatting(self):
        """Test percentage formatting."""
        n = NotWeird(0.25)  # 25%

        percent_result = n.formatted_percent
        # Should contain 25 and % symbol
        assert '%' in percent_result

    def test_scientific_notation(self):
        """Test scientific notation formatting."""
        n = NotWeird(1234567)

        scientific_result = n.formatted_scientific
        # Should contain 'e' or 'E' for scientific notation
        assert 'e' in scientific_result.lower()

    def test_property_consistency(self):
        """Test that properties are consistent with method calls."""
        n = NotWeird(123)
        n.add_prefix('$').add_suffix(' USD')

        # Formatted property should match default() method
        assert n.formatted == n.default()

        # Other formatted properties should match their respective methods
        assert n.formatted_percent == n.percent()
        assert n.formatted_scientific == n.scientific()
        assert n.formatted_binary == n.binary()
        assert n.formatted_hex == n.hex()
        assert n.formatted_roman == n.roman()
