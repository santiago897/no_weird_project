# 🚀 No Weird Utils

[![PyPI version](https://badge.fury.io/py/noWeirdUtils.svg)](https://badge.fury.io/py/noWeirdUtils)
[![Python Support](https://img.shields.io/pypi/pyversions/noWeirdUtils.svg)](https://pypi.org/project/noWeirdUtils/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> 🎯 **Lightweight, fun-named utilities for number formatting, unit conversions, and Unix time handling - because nobody likes weird numbers!**

**No Weird Utils** is a comprehensive Python package that makes working with numbers, units, and time a breeze. Say goodbye to cryptic variable names and hello to intuitive, powerful tools that just work.

## ✨ Features

### 📊 **noWeirdNumbersPls** - Smart Number Formatting
- 🌍 **Flexible separators**: Use any thousands/decimal separators (European style: `1.234.567,89`)
- 🎨 **Multiple styles**: Default, scientific, percentage, binary, hex, and even Roman numerals!
- 🔄 **Bidirectional**: Format numbers for display and parse them back to numeric types
- 📋 **Batch processing**: Handle individual numbers or entire collections (lists, tuples, sets)
- 🔧 **Precision control**: `set_decimals()` function for precise decimal rounding
- 🚀 **Fluent Interface**: Object-oriented `NotWeird` class with chainable methods
- 🎯 **Smart Locale Support**: Built-in `anglo()` and `notAnglo()` formatting presets
- 🔗 **Method Chaining**: Combine operations like `.notAnglo().add_prefix('€').with_decimals(2)`
- 📝 **Rich Properties**: Access formatted values via properties like `.formatted`, `.raw_default`, etc.

### 🔄 **metricFTW** - Universal Unit Converter
- 📏 **Length**: From picometers to light-years, millimeters to miles
- ⚖️ **Mass**: Picograms to tons, ounces to kilograms
- 📐 **Area**: Square millimeters to square miles, hectares to acres
- 🌊 **Volume**: Milliliters to barrels, gallons to liters
- 🏃 **Speed**: m/s to mph, km/h to knots
- ⚡ **Energy**: Joules to BTU, calories to kilowatt-hours
- 💨 **Pressure**: Pascals to atmospheres, PSI to bars
- 🔋 **Power**: Watts to horsepower, kilowatts to BTU/hour
- 🌡️ **Temperature**: Celsius, Fahrenheit, Kelvin, and Rankine
- 🚀 **Batch conversions**: Convert entire datasets at once

### ⏰ **quanticTime** - Intuitive Unix Time Handling
- 🕐 **Smart parsing**: Auto-detect common date/time formats
- 🌍 **Timezone aware**: Full pytz integration with 400+ timezones
- 🔄 **Format flexibility**: Parse and output in any format you need
- 📅 **Date arithmetic**: Add/subtract time periods effortlessly
- 📊 **Relative formatting**: "2 hours ago", "in 3 days", etc.

## 🚀 Quick Start

### Installation

```bash
pip install noWeirdUtils
```

For enhanced features:
```bash
# With timezone support
pip install noWeirdUtils[timezone]
```

### 🎯 Number Formatting Examples

```python
from noWeirdNumbersPls.format_number import format_number, deformat_number, set_decimals, NotWeird

# ═══════════════════════════════════════════════════════════════
# 🔥 NEW: Object-Oriented Fluent Interface with NotWeird Class
# ═══════════════════════════════════════════════════════════════

# Create a NotWeird instance with chainable methods
nw = NotWeird(1234567.89)

# Chain formatting operations - settings persist on the object
formatted = nw.notAnglo().add_prefix('€').with_decimals(2).default()
print(formatted)  # "€1.234.567,89"

# Use different styles with the same settings
print(nw.percent())     # "€123456789,00%"
print(nw.scientific())  # "€1.234568e+06"
print(nw.binary())      # "€0b100101101011010000111"

# Temporary override without changing object settings
print(nw.default(prefix='$'))  # "$1.234.567,89"
print(nw.default())            # "€1.234.567,89" (back to stored prefix)

# Rich property access for formatted values
print(nw.formatted)           # "€1.234.567,89" (fully formatted with prefix/suffix)
print(nw.raw_default)         # "1.234.567,89" (without prefix/suffix)
print(nw.formatted_percent)   # "€123456789,00%"
print(nw.formatted_scientific) # "€1.234568e+06"

# Parse formatted strings back to NotWeird objects
parsed_nw = NotWeird.parse("€1.234.567,89", thou_sep='.', dec_sep=',', prefix='€')
print(parsed_nw.number)  # 1234567.89

# Apply precise rounding to the underlying number
nw.precise(decimals=1)  # Modifies the internal number
print(nw.number)        # 1234567.9

# Quick locale switching
nw.anglo()              # Switch to US/UK format (, for thousands, . for decimal)
print(nw.default())     # "€1,234,567.9"

nw.notAnglo()           # Switch to European format (. for thousands, , for decimal)
print(nw.default())     # "€1.234.567,9"

# ═══════════════════════════════════════════════════════════════
# 📊 Traditional Function-Based API (Still Available)
# ═══════════════════════════════════════════════════════════════

# European-style formatting
number = 1234567.89
formatted = format_number(number, thou_sep='.', dec_sep=',')
print(formatted)  # "1.234.567,89"

# Multiple styles
print(format_number(0.1234, style='percent'))        # "12.34%"
print(format_number(1000000, style='scientific'))    # "1.000000e+06"
print(format_number(255, style='hex'))               # "0xff"
print(format_number(42, style='roman'))              # "XLII"

# With prefix and suffix
price = format_number(1299.99, prefix='$', suffix=' USD', decimals=2)
print(price)  # "$1,299.99 USD"

# Batch processing
prices = [99.99, 149.50, 1299.99]
formatted_prices = format_number(prices, prefix='€', thou_sep='.', dec_sep=',')
print(formatted_prices)  # ['€99,99', '€149,50', '€1.299,99']

# Parse back to numbers
parsed = deformat_number("1.234.567,89", thou_sep='.', dec_sep=',')
print(parsed)  # 1234567.89

# Parse with type enforcement
parsed_int = deformat_number("1.234", thou_sep='.', enforce_type=int)
print(parsed_int)  # 1234

# Parse special formats
hex_number = deformat_number("0xff", style='hex')
print(hex_number)  # 255

roman_number = deformat_number("XLII", style='roman')
print(roman_number)  # 42

# Precise decimal control
precise = set_decimals(3.14159265359, decimals=3)
print(precise)  # 3.142

# Works with strings too
precise_str = set_decimals("2.71828", decimals=2, force_float=True)
print(precise_str)  # 2.72
```

### 🔄 Unit Conversion Examples

```python
from metricFTW.converter import MetricFTW

converter = MetricFTW()

# Length conversions
print(converter.convert_longitude(100, 'cm', 'm'))     # 1.0
print(converter.convert_longitude(1, 'mile', 'km'))    # 1.609344

# Mass conversions
print(converter.convert_mass(1, 'kg', 'pound'))        # 2.20462
print(converter.convert_mass(16, 'ounce', 'g'))        # 453.592

# Temperature conversions
print(converter.convert_temperature(0, 'C', 'F'))      # 32.0
print(converter.convert_temperature(100, 'C', 'K'))    # 373.15

# Volume conversions
print(converter.convert_volume(1, 'gallon_us', 'l'))   # 3.78541
print(converter.convert_volume(500, 'ml', 'cup'))      # 2.083333

# Batch conversions
distances = [1, 5, 10, 26.2]
km_distances = converter.convert_longitude(distances, 'mile', 'km')
print(km_distances)  # [1.609344, 8.04672, 16.09344, 42.164928]

# See all available conversions
converter.show_available_conversions(detailed=True)
```

### ⏰ Time Handling Examples

```python
from quanticTime.core import QuanticTime

# Create from various sources
qt1 = QuanticTime(1640995200)  # Unix timestamp
qt2 = QuanticTime.now()        # Current time
qt3 = QuanticTime.today()      # Today at midnight
qt4 = QuanticTime.from_string("2024-01-01 10:30:00", fmt="%Y-%m-%d %H:%M:%S")

# Auto-parse common formats
qt5 = QuanticTime("2024-01-01")
qt6 = QuanticTime("2024-01-01 15:30:00")
qt7 = QuanticTime("Jan 1, 2024")

# Format output
print(qt2.to_string("%Y-%m-%d %H:%M:%S"))
print(qt2.to_iso())

# Time arithmetic
future = qt2.add_seconds(3600)    # Add 1 hour
past = qt2.add_days(-7)           # Subtract 7 days

# Get datetime object with timezone
dt_santiago = qt2.to_datetime("America/Santiago")
dt_tokyo = qt2.to_datetime("Asia/Tokyo")

# Check properties
print(qt2.is_weekend())
start_day = qt2.start_of_day()
end_day = qt2.end_of_day()

# List available timezones
QuanticTime.print_timezones(show_common_only=True)
QuanticTime.print_timezones(filter_text="Chile", detailed=True)
```

## 📚 Detailed Documentation

### 🎨 Number Formatting Styles

| Style | Example Input | Example Output | Description |
|-------|---------------|----------------|-------------|
| `default` | `1234.56` | `"1,234.56"` | Standard formatting with separators |
| `scientific` | `1234.56` | `"1.234560e+03"` | Scientific notation |
| `percent` | `0.1234` | `"12.34%"` | Percentage format |
| `binary` | `255` | `"0b11111111"` | Binary representation |
| `hex` | `255` | `"0xff"` | Hexadecimal representation |
| `roman` | `42` | `"XLII"` | Roman numerals (integers only) |

### 🔄 Supported Unit Categories

<details>
<summary><strong>📏 Length Units</strong></summary>

**Metric**: pm, nm, μm, mm, cm, dm, m, dam, hm, km
**Imperial/Other**: inch, foot, yard, mile, nautical_mile, angstrom, mil, furlong, fathom, light_year, parsec, astronomical_unit
</details>

<details>
<summary><strong>⚖️ Mass Units</strong></summary>

**Metric**: pg, ng, μg, mg, cg, dg, g, dag, hg, kg, t
**Imperial/Other**: ounce, pound, stone, ton_us, ton_uk, grain, dram, troy_ounce, carat, slug
</details>

<details>
<summary><strong>📐 Area Units</strong></summary>

**Metric**: mm², cm², dm², m², dam², hm², km²
**Imperial/Other**: sqin, sqft, sqyd, acre, hectare, sqmile, barn, are, rood
</details>

<details>
<summary><strong>🌊 Volume Units</strong></summary>

**Metric**: mm³, cm³, dm³, m³, l, ml, cl, dl, dal, hl, kl
**Imperial/Other**: gallon_us, gallon_uk, quart, pint, cup, fluid_ounce, cubic_inch, tablespoon, teaspoon, barrel_oil, bushel
</details>

<details>
<summary><strong>🏃 Speed Units</strong></summary>

**Metric**: mm/s, cm/s, m/s, km/h
**Imperial/Other**: mph, knot, fps, mach
</details>

<details>
<summary><strong>⚡ Energy Units</strong></summary>

J, kJ, MJ, GJ, TJ, cal, kcal, Btu, kWh, eV, erg, therm, quad
</details>

<details>
<summary><strong>💨 Pressure Units</strong></summary>

Pa, kPa, MPa, bar, mbar, atm, psi, torr, mmHg, inHg
</details>

<details>
<summary><strong>🔋 Power Units</strong></summary>

W, kW, MW, GW, hp, Btu_h, cal_s, erg_s
</details>

### ⏰ Time Zone Support

QuanticTime supports 400+ time zones through pytz integration. Some examples:

- **Americas**: `America/New_York`, `America/Los_Angeles`, `America/Santiago`, `America/Mexico_City`
- **Europe**: `Europe/London`, `Europe/Paris`, `Europe/Berlin`, `Europe/Madrid`
- **Asia**: `Asia/Tokyo`, `Asia/Shanghai`, `Asia/Dubai`, `Asia/Kolkata`
- **Oceania**: `Australia/Sydney`, `Australia/Melbourne`, `Pacific/Auckland`
- **Special**: `UTC`, `GMT`, `US/Eastern`, `US/Pacific`

## 🛠️ Advanced Usage

### Custom Number Formatting Functions

```python
from noWeirdNumbersPls.format_number import format_number, set_decimals, NotWeird

# ═══════════════════════════════════════════════════════════════
# 🔥 NEW: Advanced NotWeird Class Usage
# ═══════════════════════════════════════════════════════════════

def create_currency_formatter(currency="USD", european_style=False):
    """Factory function to create currency formatters with consistent settings."""
    if european_style:
        return NotWeird(0).notAnglo().add_prefix(f'{currency} ')
    else:
        return NotWeird(0).anglo().add_prefix(f'{currency}')

# Create reusable formatters
eur_formatter = create_currency_formatter("EUR", european_style=True)
usd_formatter = create_currency_formatter("USD", european_style=False)

# Use the formatters with different amounts
amounts = [1234.56, 9876.54, 15000.00]

for amount in amounts:
    eur_formatter._number = amount  # Update the number
    usd_formatter._number = amount

    print(f"EUR: {eur_formatter.with_decimals(2).default()}")  # "EUR 1.234,56"
    print(f"USD: {usd_formatter.with_decimals(2).default()}")  # "USD1,234.56"

# Complex chaining example
nw = NotWeird(3.14159265359)
result = (nw.precise(decimals=3)          # First apply precision
           .notAnglo()                    # Then set European format
           .add_prefix('π ≈ ')           # Add mathematical prefix
           .add_suffix(' (rounded)'))     # Add descriptive suffix

print(result.default())  # "π ≈ 3,142 (rounded)"

# Working with collections using NotWeird
prices = [99.99, 149.50, 1299.99]
formatter = NotWeird(prices).notAnglo().add_prefix('€').with_decimals(2)
formatted_list = formatter.default()
print(formatted_list)  # ['€99,99', '€149,50', '€1.299,99']

# Property-based access for different formats
sales_data = NotWeird(1234567.89).notAnglo().add_prefix('€')
print(f"Default: {sales_data.formatted}")
print(f"Percentage: {sales_data.formatted_percent}")
print(f"Scientific: {sales_data.formatted_scientific}")
print(f"Raw (no prefix): {sales_data.raw_default}")

# ═══════════════════════════════════════════════════════════════
# 📊 Traditional Function-Based Approach
# ═══════════════════════════════════════════════════════════════

def format_currency(amount, currency="USD", european_style=False):
    """Format currency with locale-specific rules."""
    if european_style:
        return format_number(amount, thou_sep='.', dec_sep=',',
                           prefix=f'{currency} ', decimals=2)
    else:
        return format_number(amount, thou_sep=',', dec_sep='.',
                           prefix=f'{currency}', decimals=2)

# European format
print(format_currency(1234.56, "EUR", european_style=True))   # "EUR 1.234,56"
# US format
print(format_currency(1234.56, "USD", european_style=False))  # "USD1,234.56"

# Use set_decimals for precise rounding
precise_number = set_decimals(3.14159265359, decimals=3)
print(precise_number)  # 3.142
```

### Chained Unit Conversions

```python
from metricFTW.converter import MetricFTW

converter = MetricFTW()

# Convert a recipe from US to metric
ingredients = {
    'flour': (2, 'cup'),      # cups to grams (approximately)
    'milk': (1, 'cup'),       # cups to ml
    'temperature': (350, 'F')    # Fahrenheit to Celsius
}

# Note: For cooking conversions, you might want to use density conversions
flour_ml = converter.convert_volume(ingredients['flour'][0], 'cup', 'ml')
milk_ml = converter.convert_volume(ingredients['milk'][0], 'cup', 'ml')
temp_c = converter.convert_temperature(ingredients['temperature'][0], 'F', 'C')

print(f"Flour: {flour_ml} ml")     # Flour: 480.0 ml
print(f"Milk: {milk_ml} ml")       # Milk: 240.0 ml
print(f"Temperature: {temp_c}°C")  # Temperature: 176.66666666666666°C
```

### Complex Time Operations

```python
from quanticTime.core import QuanticTime

# Create a meeting scheduler
meeting_utc = QuanticTime.from_string("2024-03-15 14:00:00", tz="UTC")

# Show meeting time in different time zones
timezones = ["America/New_York", "Europe/London", "Asia/Tokyo", "America/Santiago"]

for tz in timezones:
    local_time = meeting_utc.to_datetime(tz)
    formatted_time = meeting_utc.to_string('%Y-%m-%d %H:%M %Z', tz)
    print(f"{tz}: {formatted_time}")

# Calculate time until meeting
now = QuanticTime.now()
time_diff = meeting_utc.difference(now)
hours_until = time_diff / 3600

if hours_until > 0:
    print(f"Meeting in {hours_until:.1f} hours")
else:
    print(f"Meeting was {abs(hours_until):.1f} hours ago")

# Working with time ranges
start_day = meeting_utc.start_of_day()
end_day = meeting_utc.end_of_day()
is_weekend = meeting_utc.is_weekend("America/Santiago")
```

## 🧪 Testing

The package includes comprehensive tests to ensure reliability and accuracy. For detailed testing information, see [TESTING.md](TESTING.md).

### Quick Test Commands

```bash
# Install development dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=metricFTW --cov=noWeirdNumbersPls --cov=quanticTime --cov-report=html

# Use the convenient test runner
python run_tests.py --coverage --verbose
```

### Test Coverage

Current test coverage:
- **metricFTW**: 75% coverage
- **noWeirdNumbersPls**: 58% coverage
- **quanticTime**: 89% coverage
- **Overall**: 73% coverage

### Test Categories

- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test component interactions
- **Verification Tests**: Test against known accurate values
- **Property Tests**: Test object properties and formatting

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests (`python run_tests.py`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please ensure:
- All tests pass
- New features include tests
- Code follows the existing style
- Documentation is updated as needed

### Development Setup

```bash
# Clone the repository
git clone https://github.com/santiago897/no-weird-utils.git
cd no-weird-utils

# Install in development mode with all dependencies
poetry install --with test

# Or with pip
pip install -e .[test]

# Run tests
python run_tests.py

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Run the test suite**: `pytest tests/`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Setup

```bash
# Clone the repo
git clone https://github.com/santiago897/no-weird-utils.git
cd no-weird-utils

# Install with development dependencies
pip install -e .[timezone]
pip install pytest pytest-cov black flake8

# Run tests
pytest tests/

# Format code
black .
```

## 📋 Requirements

- **Python 3.8+**
- **Optional dependencies**:
  - `pytz ^2025.2`: For timezone support in quanticTime

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[pytz](https://pythonhosted.org/pytz/)** - Special thanks to Stuart Bishop and the pytz team for creating and maintaining this incredible timezone library. pytz provides accurate and up-to-date timezone calculations for Python, making QuanticTime's timezone conversions possible across 400+ timezones worldwide. Without pytz, handling timezone-aware datetime operations would be significantly more complex and error-prone.
- **Poetry** for elegant dependency management and packaging
- The Python community for inspiration, feedback, and continuous innovation

## 🔗 Links

- **PyPI**: https://pypi.org/project/no-weird-utils/
- **GitHub**: https://github.com/santiago897/noWeirdUtils
- **Documentation**: Coming soon!
- **Issues**: https://github.com/santiago897/noWeirdUtils/issues

---

<div align="center">

**Made with ❤️ by [Santiago Matta](https://github.com/santiago897)**

*"Because life's too short for weird numbers!"* 🎯

</div>
