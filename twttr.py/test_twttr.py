from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("CS50") == "CS50"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou.") == "."

if __name__ == "__main__":
    print("All tests passed!")
