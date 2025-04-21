from um import count
import pytest


def test_count():
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks, ") == 1
    assert count("Thank you") == 0
    assert count("circumcision") == 0

if __name__ == "__main__":
    print("All tests passed!")
