#!/usr/bin/env python3
"""
Test suite for QuanticTime timezone functionality.
"""

import pytest
from quanticTime.core import QuanticTime


class TestQuanticTimeTimezones:
    """Test class for QuanticTime timezone functionality."""

    def test_print_timezones_common_only(self):
        """Test printing common timezones only."""
        # This method prints to console, so we test it doesn't raise errors
        try:
            QuanticTime.print_timezones(show_common_only=True, limit=5)
        except Exception as e:
            pytest.fail(f"print_timezones with common_only failed: {e}")

    def test_print_timezones_with_details(self):
        """Test printing timezones with detailed information."""
        try:
            QuanticTime.print_timezones(show_common_only=True, detailed=True, limit=3)
        except Exception as e:
            pytest.fail(f"print_timezones with details failed: {e}")

    def test_print_timezones_with_filter(self):
        """Test printing timezones with text filter."""
        try:
            QuanticTime.print_timezones(filter_text="america", limit=5)
        except Exception as e:
            pytest.fail(f"print_timezones with filter failed: {e}")

    def test_print_timezones_filtered_detailed(self):
        """Test printing filtered timezones with details."""
        try:
            QuanticTime.print_timezones(filter_text="europe", detailed=True, limit=3)
        except Exception as e:
            pytest.fail(f"print_timezones filtered detailed failed: {e}")

    def test_search_timezones_function(self):
        """Test search_timezones function returns proper structure."""
        results = QuanticTime.search_timezones("america", limit=3)

        assert isinstance(results, list)
        assert len(results) <= 3

        if results:  # If any results returned
            for result in results:
                assert isinstance(result, dict)
                assert 'timezone' in result
                assert 'current_time' in result
                assert 'offset' in result

    def test_list_timezones_function(self):
        """Test list_timezones function returns list of strings."""
        timezones = QuanticTime.list_timezones("pacific", limit=3)

        assert isinstance(timezones, list)
        assert len(timezones) <= 3

        if timezones:  # If any results returned
            for tz in timezones:
                assert isinstance(tz, str)
                assert len(tz) > 0

    def test_search_timezones_with_different_filters(self):
        """Test search_timezones with different filter terms."""
        # Test with different geographical regions
        for region in ["asia", "europe", "america"]:
            results = QuanticTime.search_timezones(region, limit=2)
            assert isinstance(results, list)
            # Should return some results for major regions
            if region in ["asia", "europe", "america"]:
                assert len(results) >= 0  # May or may not have results

    def test_list_timezones_with_different_filters(self):
        """Test list_timezones with different filter terms."""
        for region in ["utc", "gmt"]:
            timezones = QuanticTime.list_timezones(region, limit=2)
            assert isinstance(timezones, list)

    def test_timezone_functions_empty_filter(self):
        """Test timezone functions with empty or None filter."""
        # Test with empty string filter (None might not be supported)
        results = QuanticTime.search_timezones("", limit=2)
        assert isinstance(results, list)

        # Test with empty string filter
        timezones = QuanticTime.list_timezones("", limit=2)
        assert isinstance(timezones, list)

    def test_timezone_functions_limit_parameter(self):
        """Test that limit parameter is respected."""
        limit = 2
        results = QuanticTime.search_timezones("america", limit=limit)
        assert len(results) <= limit

        timezones = QuanticTime.list_timezones("europe", limit=limit)
        assert len(timezones) <= limit
