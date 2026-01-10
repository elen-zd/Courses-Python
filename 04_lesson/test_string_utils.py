import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("str_value, result", [
    ("   skypro", "skypro"),
    (" Sky", "Sky"),
    ("  Sky Pro", "Sky Pro"),
    ("Skypro   ", "Skypro   "),
    (" 125677", "125677"),
    (" ", "")
])
def test_trim_positive(str_value, result):
    string_utils = StringUtils()
    expected = string_utils.trim(str_value)
    assert expected == result


@pytest.mark.negative
@pytest.mark.parametrize("str_value, result", [
    ("", ""),
    ("\n  небо", "\n  небо"),
    (" \n sky", "\n sky")
])
def test_trim_negative(str_value, result):
    string_utils = StringUtils()
    expected = string_utils.trim(str_value)
    assert expected == result


@pytest.mark.negative
def test_trim_with_None_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize("str_name, symbol, result", [
    ("Skypro", "y", True),
    ("My name", "a", True),
    ("Привет", "", True),
    ("", "", True),
    ("Test1", "1", True)
])
def test_contains_positive(str_name, symbol, result):
    string_utils = StringUtils()
    expected = string_utils.contains(str_name, symbol)
    assert expected == result


@pytest.mark.negative
@pytest.mark.parametrize("str_name, symbol, result", [
    ("", "S", False),
    ("Hello", "f", False),
    ("HELLO", "h", False)
])
def test_contains_negative(str_name, symbol, result):
    string_utils = StringUtils()
    expected = string_utils.contains(str_name, symbol)
    assert expected == result


@pytest.mark.negative
def test_contains_with_None_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains(None, "x")

 
@pytest.mark.positive
@pytest.mark.parametrize("string, del_symbol, result", [
    ("SkyPro", "P", "Skyro"),
    ("^&123!", "&", "^123!"),
    (" ", " ", ""),
    ("Test test", "", "Test test"),
    ("skyprosky", "sky", "pro")
])
def test_delete_symbol_positive(string, del_symbol, result):
    string_utils = StringUtils()
    expected = string_utils.delete_symbol(string, del_symbol)
    assert expected == result


@pytest.mark.negative
@pytest.mark.parametrize("string, del_symbol, result", [
    ("skypro", "P", "skypro"),
    ("", "0", ""),
    ("test", "", "test")
])
def test_delete_symbol_negative(string, del_symbol, result):
    string_utils = StringUtils()
    expected = string_utils.delete_symbol(string, del_symbol)
    assert expected == result


@pytest.mark.negative
def test_delete_symbol_with_None_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "x")
