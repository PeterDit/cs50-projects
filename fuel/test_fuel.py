from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/4") == 50

def test_gauge():
    assert gauge(convert("1/4")) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"

def test_Verror():
    with pytest.raises(ValueError):
        convert("a/b")

def test_Zerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
