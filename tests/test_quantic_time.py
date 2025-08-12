import pytest
from datetime import datetime, date, timezone, timedelta
from quanticTime.core import QuanticTime

class TestQuanticTime:

    def test_init_with_datetime(self):
        dt = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        qt = QuanticTime(dt)
        assert qt.timestamp == int(dt.timestamp())

    def test_init_with_date(self):
        d = date(2023, 1, 1)
        qt = QuanticTime(d)
        expected_dt = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        assert qt.timestamp == int(expected_dt.timestamp())

    def test_init_with_timestamp(self):
        ts = 1672574400  # 2023-01-01 12:00:00 UTC
        qt = QuanticTime(ts)
        assert qt.timestamp == ts

    def test_init_with_string_iso(self):
        qt = QuanticTime("2023-01-01T12:00:00")
        expected = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        assert qt.timestamp == int(expected.timestamp())

    def test_init_with_string_simple(self):
        qt = QuanticTime("2023-01-01 12:00:00")
        expected = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        assert qt.timestamp == int(expected.timestamp())

    def test_from_string_with_format(self):
        qt = QuanticTime.from_string("01/01/2023 12:00:00", "%m/%d/%Y %H:%M:%S")
        expected = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        assert qt.timestamp == int(expected.timestamp())

    def test_now(self):
        qt = QuanticTime.now()
        now = datetime.now(timezone.utc)
        # Should be very close (within 2 seconds)
        assert abs(qt.timestamp - int(now.timestamp())) < 2

    def test_today(self):
        qt = QuanticTime.today()
        today = datetime.now(timezone.utc).date()
        expected = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc)
        assert qt.timestamp == int(expected.timestamp())

    def test_to_datetime(self):
        ts = 1672574400  # 2023-01-01 12:00:00 UTC
        qt = QuanticTime(ts)
        dt = qt.to_datetime()
        assert dt.year == 2023
        assert dt.month == 1
        assert dt.day == 1
        assert dt.hour == 12

    def test_to_string(self):
        ts = 1672574400  # 2023-01-01 12:00:00 UTC
        qt = QuanticTime(ts)
        assert qt.to_string() == "2023-01-01 12:00:00"

    def test_to_iso(self):
        ts = 1672574400  # 2023-01-01 12:00:00 UTC
        qt = QuanticTime(ts)
        iso_str = qt.to_iso()
        assert iso_str.startswith("2023-01-01T12:00:00")

    def test_add_seconds(self):
        qt = QuanticTime(1672574400)
        qt2 = qt.add_seconds(3600)  # Add 1 hour
        assert qt2.timestamp == 1672578000

    def test_add_minutes(self):
        qt = QuanticTime(1672574400)
        qt2 = qt.add_minutes(60)  # Add 1 hour
        assert qt2.timestamp == 1672578000

    def test_add_hours(self):
        qt = QuanticTime(1672574400)
        qt2 = qt.add_hours(1)
        assert qt2.timestamp == 1672578000

    def test_add_days(self):
        qt = QuanticTime(1672574400)
        qt2 = qt.add_days(1)
        assert qt2.timestamp == 1672660800

    def test_difference(self):
        qt1 = QuanticTime(1672574400)
        qt2 = QuanticTime(1672578000)  # 1 hour later
        assert qt2.difference(qt1) == 3600
        assert qt1.difference(qt2) == -3600

    def test_is_weekend(self):
        # 2023-01-01 was a Sunday
        qt = QuanticTime("2023-01-01")
        assert qt.is_weekend() == True

        # 2023-01-02 was a Monday
        qt2 = QuanticTime("2023-01-02")
        assert qt2.is_weekend() == False

    def test_start_of_day(self):
        qt = QuanticTime("2023-01-01 15:30:45")
        start = qt.start_of_day()
        assert start.to_string() == "2023-01-01 00:00:00"

    def test_end_of_day(self):
        qt = QuanticTime("2023-01-01 15:30:45")
        end = qt.end_of_day()
        end_str = end.to_string("%Y-%m-%d %H:%M:%S")
        assert end_str == "2023-01-01 23:59:59"

    def test_comparisons(self):
        qt1 = QuanticTime(1672574400)
        qt2 = QuanticTime(1672578000)

        assert qt1 < qt2
        assert qt1 <= qt2
        assert qt2 > qt1
        assert qt2 >= qt1
        assert qt1 == qt1
        assert qt1 != qt2

    def test_arithmetic_operators(self):
        qt = QuanticTime(1672574400)

        # Add seconds
        qt2 = qt + 3600
        assert qt2.timestamp == 1672578000

        # Add timedelta
        qt3 = qt + timedelta(hours=1)
        assert qt3.timestamp == 1672578000

        # Subtract seconds
        qt4 = qt - 3600
        assert qt4.timestamp == 1672570800

        # Subtract QuanticTime (returns difference)
        diff = qt2 - qt
        assert diff == 3600

    def test_hash(self):
        qt1 = QuanticTime(1672574400)
        qt2 = QuanticTime(1672574400)
        qt3 = QuanticTime(1672578000)

        # Same timestamps should have same hash
        assert hash(qt1) == hash(qt2)
        # Different timestamps should have different hash
        assert hash(qt1) != hash(qt3)

        # Should be usable in sets
        time_set = {qt1, qt2, qt3}
        assert len(time_set) == 2  # qt1 and qt2 are the same

    def test_error_handling(self):
        with pytest.raises(ValueError):
            QuanticTime("invalid date string")

        with pytest.raises(TypeError):
            QuanticTime([1, 2, 3])  # Invalid type

        qt = QuanticTime(1672574400)
        with pytest.raises(TypeError):
            qt < "not a QuanticTime"
