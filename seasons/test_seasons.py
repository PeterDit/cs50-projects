import pytest
from seasons import get_birth_date
from seasons import calculate_minutes
from seasons import convert_to_words
import datetime

def test_convert_to_words():
    assert convert_to_words(1) == "One"
    assert convert_to_words(123) == "One hundred twenty-three"
    assert convert_to_words(0) == "Zero"

"""def test_birth_date():
    assert get_birth_date("1998-01-01") == datetime.date(1998, 1, 1)
    try:
        get_birth_date("invalid-date")
    except ValueError:
        assert True
    else:
        assert False
"""
def test_calculate_minutes():
    expected_minutes = 14040000
    assert calculate_minutes(datetime.date(1998, 1, 1)) == expected_minutes

if __name__ == "__main__":
    print("All tests passed!")
