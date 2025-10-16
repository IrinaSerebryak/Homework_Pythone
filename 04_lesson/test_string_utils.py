import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("123", "123"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("   тест", "тест"),
    ("   04 апреля 2023", "04 апреля 2023"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("skypro", "skypro"),
    ("123", "123"),
    ("тест ", "тест "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("hello world", " ", True),
    ("тест", "т", True),
    ("123", "1", True),
    ("04 апреля 2023", "а", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("hello", "x", False),
    ("", "a", False),
    ("тест", "ы", False),
    ("123", "4", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.edge_cases
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "", True),
    ("test", "", True),
    ("   ", " ", True),
])
def test_contains_edge_cases(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("hello", "l", "heo"),
    ("banana", "a", "bnn"),
    ("тестирование", "и", "тестроване"),
    ("04 апреля 2023", "апреля", "04  2023"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("hello", "x", "hello"),
    ("", "a", ""),
    ("тест", "ы", "тест"),
    ("123", "4", "123"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.edge_cases
@pytest.mark.parametrize("string, symbol, expected", [
    ("test", "", "test"),
    ("   ", " ", ""),
    ("aaa", "a", ""),
])
def test_delete_symbol_edge_cases(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.boundary
class TestBoundaryCases:

    def test_capitalize_with_special_chars(self):
        assert string_utils.capitalize("!test") == "!test"
        assert string_utils.capitalize(" test") == " test"

    def test_trim_multiple_spaces(self):
        assert string_utils.trim("     test") == "test"
        assert string_utils.trim("  ") == ""

    def test_contains_with_numbers(self):
        assert string_utils.contains("12345", "3") == True
        assert string_utils.contains("12.34", ".") == True

    def test_delete_symbol_all_occurrences(self):
        assert string_utils.delete_symbol("aabbcc", "b") == "aacc"
        assert string_utils.delete_symbol("test test", "t") == "es es"

    def test_trim_with_mixed_whitespace(self):
        # Проверяем, что удаляются только пробелы, а не другие символы
        assert string_utils.trim("  test  ") == "test  "
        assert string_utils.trim("\ttest") == "\ttest"


@pytest.mark.performance
class TestPerformance:

    def test_trim_long_string(self):
        long_string = "   " + "a" * 1000
        result = string_utils.trim(long_string)
        assert result == "a" * 1000
        assert len(result) == 1000

    def test_contains_long_string(self):
        long_string = "a" * 1000 + "b"
        assert string_utils.contains(long_string, "b") == True
        assert string_utils.contains(long_string, "c") == False

    def test_delete_symbol_multiple_occurrences(self):
        string = "a" * 50 + "b" + "a" * 50
        result = string_utils.delete_symbol(string, "b")
        assert result == "a" * 100
        assert len(result) == 100