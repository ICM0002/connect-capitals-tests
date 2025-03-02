from connect_capitals import connect_capitals

def test_connect_capitals():
    assert connect_capitals("Kes on Mart?", "Mart on mingi LOLL Tartust") == "KM-MLOLLT"
    assert connect_capitals("HELLO World", "Python IS Fun") == "HELLOW-PISF"
    assert connect_capitals("abc", "def") == "-"  # No capital letters, just a hyphen
    assert connect_capitals("CAPS LOCK", "MODE") == "CAPSLOCK-MODE"
    assert connect_capitals("", "NO CAPITALS") == "-NOCAPITALS"
    assert connect_capitals("Only FIRST", "") == "OFIRST-"  # Only first has capitals
    assert connect_capitals("", "") == "-"  # Both empty