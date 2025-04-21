import pytest
from working import convert  # Import the convert function from your working.py file

def test_convert():
    # Valid cases
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:00 AM to 8:50 PM") == "10:00 to 20:50"

    # Invalid cases
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

if __name__ == "__main__":
    print("All tests passed!")
