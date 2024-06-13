import pytest
from string_utils import StringUtils
utils = StringUtils()

@pytest.mark.parametrize("input_string, expected_output", [
    ("bambino", "Bambino"),
    ("device cups", "Device cups"),
    ("333", "333"),
    ("", ""),
    (" ", " "),
    ("4276tests", "4276tests"),
    ])
def test_capitalize(input_string, expected_output):
    assert utils.capitalize(input_string) == expected_output

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim("4276") == "4276"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim(" selibrate ") == " selibrate "

@pytest.mark.parametrize("string, delimeter, result", [
    ("stage_1,stage_2,stage_3", ",", ["stage_1", "stage_2", "stage_3"]),
    ("1,2,3,4,5,6,7", ",", ["1","2", "3", "4", "5", "6", "7"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("store", "s", True),
    (" charge", "e", True),
    ("handle-bandle", "-", True),
    ("4276", "7", True),
    ("colledge", "#", False),
    ("Containe", "c", False),
    ("", "d", False),
    ("Babe", " ", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("chips", "s", "chip"),
    ("Collect", "l", "Coect"),
    ("Hamble-Bandle", "-", "HambleBandle"),
    ("Rage", "f", "Rage"),
    (" ", " ", ""),
    ("sells ", " ", "sells"),
])
def test_delete_simbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("smash", "s", True),
    (" Crack", " ", True),
    ("Chamber", "h", False),
    ("", " ", False),
])
def test_start_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("smash", "h", True),
    ("Crack ", " ", True),
    ("Chamber", "C", False),
    ("", " ", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("kkl", False),
    ("12345", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize("lst, joiner, result", [
    (["j","o","j"], ", ", "j, o, j"),
    ([1,2,3], None, "1, 2, 3"),
    (["chiken", "carri"], "-", "chiken-carri"),
    (["s", "h", "y"], "", "shy"),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result