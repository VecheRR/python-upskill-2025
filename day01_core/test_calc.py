from calc import string_calc

def test_simple():
    assert string_calc("2 + 2") == 4.0
    assert string_calc("3 * 3") == 9.0
    assert string_calc("10 - 5") == 5.0
    assert string_calc("6 / 2") == 3.0

def test_with_spaces():
    assert string_calc("  4 + 5  ") == 9.0
    assert string_calc(" 8 *    2 ") == 16.0
    assert string_calc("10 -3") == 7.0
    assert string_calc("12/4") == 3.0

def test_error():
    import pytest
    with pytest.raises(ValueError):
        string_calc("2++*2")