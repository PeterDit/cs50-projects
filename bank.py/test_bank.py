from bank import value

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    try:
        convert("1/0")
    except ZeroDivisionError:
        pass
    try:
        convert("a/b")
    except ValueError:
        pass

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
