__author__: str = 730667045

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# Tests for invert
def test_invert_edge() -> None:
    """Edge Case for duplicate keys"""
    assert invert({"A": "10", "B": "12", "B": "14"}) == "Duplicate key detected"

def test_invert_use1() -> None:
    """Normal use case"""
    assert invert({"A": "10", "B": "12"}) == {"10": "A", "12": "B"}

def test_invert_use2() -> None:
    """use case but key=value"""
    assert invert({"A": "A", "B": "12"}) == {"A": "A", "12": "B"}

# Tests for count
def test_count_edge() -> None:
    """Caps sensitive edge case"""
    assert count(["A", "a"]) == {"A": 1, "a": 1}
    
def test_count_use1() -> None:
    """All ones use case"""
    assert count(["A", "B", "C", "D"]) == {"A":1"B":1,"C":1,"D":1} 

def test_count_use2() -> None:
    """Kinda like favorite_color"""
    assert count(["blue", "green", "blue", "black"]) == {"blue":2, "green":1, "black":1}

# Tests for favorite_color
def test_favorite_color_edge() -> None:
    """Not colors"""
    assert favorite_color({"Jack": "Jack", "Jill": "Jack"}) == "Jack"

def test_favorite_color_use1() -> None:
    """Ties?"""
    assert favorite_color({"Jack": "Blue", "Jill": "Green"}) == "Blue"

def test_favorite_color_use2() -> None:
    """Normal usage"""
    assert favorite_color({"Jack": "Blue", "Jill": "Green", "Jesse": "Green"}) == "Green"

# Tests for bin_length
def test_bin_len_edge() -> None:
    """Weird characters?"""
    assert bin_len(["#", "$", "^"]) == {1:{"#", "$", "^"}}

def test_bin_len_use1() -> None:
    """With punctuation"""
    assert bin_len(["This", "dog."]) == {4:{"This", "dog."}} 

def test_bin_len_use2() -> None:
    """normal words"""
    assert bin_len(["three", "blind", "mice"]) == {5:{"three", "blind"}, 4:{"mice"}}
