#!/usr/bin/env python3
"""
Verification test suite for MetricFTW converter accuracy.
"""

import pytest
from metricFTW.converter import MetricFTW


class TestMetricFTWVerification:
    """Test class for verifying MetricFTW conversion accuracy."""

    @pytest.fixture
    def converter(self):
        """Fixture providing a MetricFTW converter instance."""
        return MetricFTW()

    def test_known_length_conversions(self, converter):
        """Test known accurate length conversions."""
        # Test inch to cm
        result = converter.convert_longitude(1, "inch", "cm")
        assert abs(result - 2.54) < 0.01

        # Test foot to cm
        result = converter.convert_longitude(1, "foot", "cm")
        assert abs(result - 30.48) < 0.01

        # Test meter to cm
        result = converter.convert_longitude(1, "m", "cm")
        assert abs(result - 100) < 0.01

        # Test km to m
        result = converter.convert_longitude(1, "km", "m")
        assert abs(result - 1000) < 0.01

    def test_known_mass_conversions(self, converter):
        """Test known accurate mass conversions."""
        # Test pound to kg
        result = converter.convert_mass(1, "pound", "kg")
        assert abs(result - 0.453592) < 0.000001

        # Test kg to g
        result = converter.convert_mass(1, "kg", "g")
        assert abs(result - 1000) < 0.01

        # Test gram to kg
        result = converter.convert_mass(1, "g", "kg")
        assert abs(result - 0.001) < 0.000001

        # Test 1000g to kg
        result = converter.convert_mass(1000, "g", "kg")
        assert abs(result - 1) < 0.01

    def test_known_temperature_conversions(self, converter):
        """Test known accurate temperature conversions."""
        # Test 0°C to °F
        result = converter.convert_temperature(0, "C", "F")
        assert abs(result - 32) < 0.01

        # Test 100°C to °F
        result = converter.convert_temperature(100, "C", "F")
        assert abs(result - 212) < 0.01

    def test_known_area_conversions(self, converter):
        """Test known accurate area conversions."""
        # Test m² to cm²
        result = converter.convert_area(1, "m2", "cm2")
        assert abs(result - 10000) < 1

    def test_volume_conversions(self, converter):
        """Test volume conversions."""
        # Test liter to ml
        result = converter.convert_volume(1, "l", "ml")
        assert abs(result - 1000) < 0.01

        # Test 1000 ml to l
        result = converter.convert_volume(1000, "ml", "l")
        assert abs(result - 1) < 0.01

    def test_metric_unit_progression(self, converter):
        """Test metric unit progression for consistency."""
        # Test mm to cm
        result = converter.convert_longitude(1, "mm", "cm")
        assert abs(result - 0.1) < 0.01

        # Test 10 mm to cm
        result = converter.convert_longitude(10, "mm", "cm")
        assert abs(result - 1) < 0.01

        # Test 1 cm to mm
        result = converter.convert_longitude(1, "cm", "mm")
        assert abs(result - 10) < 0.01

    def test_specialized_conversions(self, converter):
        """Test specialized unit conversions."""
        # Test nautical mile to cm (should be large number)
        result = converter.convert_longitude(1, 'nautical_mile', 'cm')
        assert result > 180000  # Should be around 185200

        # Test parsec to km (should be very large)
        result = converter.convert_longitude(1, 'parsec', 'km')
        assert result > 1e13  # Should be around 3.086e13

        # Test troy ounce to kg
        result = converter.convert_mass(1, 'troy_ounce', 'kg')
        assert 0.03 < result < 0.04  # Should be around 0.0311

        # Test acre to m²
        result = converter.convert_area(1, 'acre', 'm2')
        assert 4000 < result < 5000  # Should be around 4047

    def test_conversion_symmetry(self, converter):
        """Test that conversions are symmetric (A->B->A = A)."""
        original_value = 100

        # Test length symmetry (using 'foot' instead of 'ft')
        converted = converter.convert_longitude(original_value, "m", "foot")
        back_converted = converter.convert_longitude(converted, "foot", "m")
        assert abs(back_converted - original_value) < 0.01

        # Test mass symmetry
        converted = converter.convert_mass(original_value, "kg", "pound")
        back_converted = converter.convert_mass(converted, "pound", "kg")
        assert abs(back_converted - original_value) < 0.01

        # Test temperature symmetry
        converted = converter.convert_temperature(original_value, "C", "F")
        back_converted = converter.convert_temperature(converted, "F", "C")
        assert abs(back_converted - original_value) < 0.01

    def test_show_available_conversions(self, converter):
        """Test that show_available_conversions method works."""
        # This method prints to console, so we just test it doesn't raise errors
        try:
            converter.show_available_conversions(detailed=True)
        except Exception as e:
            pytest.fail(f"show_available_conversions failed: {e}")

    def test_error_handling_for_invalid_units(self, converter):
        """Test proper error handling for invalid units."""
        with pytest.raises(ValueError):
            converter.convert_longitude(100, "invalid_unit", "m")

        with pytest.raises(ValueError):
            converter.convert_mass(100, "kg", "invalid_unit")
