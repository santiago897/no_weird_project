#!/usr/bin/env python3
"""
Test suite for the MetricFTW converter with iterable support.
"""

import pytest
from metricFTW.converter import MetricFTW


class TestMetricFTWConverter:
    """Test class for MetricFTW converter functionality."""

    @pytest.fixture
    def converter(self):
        """Fixture providing a MetricFTW converter instance."""
        return MetricFTW()

    def test_length_conversions(self, converter):
        """Test length conversions with individual values."""
        # Basic metric conversions
        assert converter.convert_longitude(100, 'cm', 'm') == 1.0
        assert converter.convert_longitude(1000, 'm', 'km') == 1.0

        # Imperial conversions
        result = converter.convert_longitude(1, 'km', 'mile')
        assert abs(result - 0.621371) < 0.001  # Approximate equality

    def test_mass_conversions(self, converter):
        """Test mass conversions with individual values."""
        assert converter.convert_mass(1000, 'g', 'kg') == 1.0

        # Imperial conversion
        result = converter.convert_mass(1, 'pound', 'kg')
        assert abs(result - 0.453592) < 0.001

    def test_temperature_conversions(self, converter):
        """Test temperature conversions."""
        assert converter.convert_temperature(0, 'C', 'F') == 32.0
        assert converter.convert_temperature(100, 'C', 'F') == 212.0
        assert converter.convert_temperature(100, 'C', 'K') == 373.15

    def test_volume_conversions(self, converter):
        """Test volume conversions."""
        assert converter.convert_volume(1, 'l', 'ml') == 1000.0

        # US gallon to liter
        result = converter.convert_volume(1, 'gallon_us', 'l')
        assert abs(result - 3.78541) < 0.001

    def test_iterable_conversions(self, converter):
        """Test conversions with iterables (lists, tuples)."""
        # Test with lists
        result = converter.convert_longitude([1, 2, 3], 'm', 'cm')
        expected = [100.0, 200.0, 300.0]
        assert result == expected

        # Test temperature with lists
        result = converter.convert_temperature([32, 100, 212], 'F', 'C')
        expected = [0.0, 37.777777777777786, 100.0]
        for i, val in enumerate(result):
            assert abs(val - expected[i]) < 0.001

        # Test mass with lists
        result = converter.convert_mass([1, 2, 5], 'kg', 'pound')
        for val in result:
            assert val > 0  # All should be positive

        # Test with tuples
        result = converter.convert_speed((60, 120), 'mph', 'km/h')
        assert len(result) == 2
        assert all(val > 0 for val in result)

        # Test with ranges
        result = converter.convert_power(range(1, 4), 'kW', 'W')
        expected = [1000.0, 2000.0, 3000.0]
        assert result == expected

    def test_mixed_scenarios(self, converter):
        """Test various edge cases and mixed scenarios."""
        # Empty list
        result = converter.convert_longitude([], 'm', 'cm')
        assert result == []

        # Single element list
        result = converter.convert_longitude([100], 'cm', 'm')
        assert result == [1.0]

        # Large list
        large_list = list(range(1, 11))
        result = converter.convert_mass(large_list, 'kg', 'pound')
        assert len(result) == 10
        assert all(val > 0 for val in result)

    def test_error_handling(self, converter):
        """Test error handling with invalid units."""
        with pytest.raises(ValueError):
            converter.convert_longitude(100, 'invalid_unit', 'm')

        with pytest.raises(ValueError):
            converter.convert_longitude([1, 2, 3], 'm', 'invalid_unit')

    def test_all_conversion_categories(self, converter):
        """Test that all conversion categories work with iterables."""
        values = [1, 2, 3]

        # Length
        result = converter.convert_longitude(values, 'm', 'foot')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Mass
        result = converter.convert_mass(values, 'kg', 'pound')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Area
        result = converter.convert_area(values, 'm2', 'sqft')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Volume
        result = converter.convert_volume(values, 'l', 'gallon_us')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Speed
        result = converter.convert_speed(values, 'm/s', 'mph')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Energy
        result = converter.convert_energy(values, 'kJ', 'cal')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Pressure
        result = converter.convert_pressure(values, 'bar', 'psi')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Power
        result = converter.convert_power(values, 'kW', 'hp')
        assert len(result) == 3
        assert all(val > 0 for val in result)

        # Temperature
        result = converter.convert_temperature(values, 'C', 'F')
        assert len(result) == 3
