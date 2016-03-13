import pytest
from exercises.introduction import bouncer, largest_of_four, repeat, rovarsprak


def test_repeat():
    assert repeat("hej", 2) == "hejhej"
    assert repeat("då", -1) == ""
    assert repeat("abc", 8) == "abcabcabcabcabcabcabcabc"


def test_bouncer():
    assert bouncer([7, "ate", "", False, 9]) == [7, "ate", 9]
    assert bouncer(["a", "b", "c"]) == ["a", "b", "c"]
    assert bouncer([0, 0.0, 0j, {}, (), [], "hello"]) == ["hello"]


def test_largest_of_four():
    assert largest_of_four([[13, 27, 18, 26],
                              [4, 5, 1, 3],
                              [32, 35, 37, 39],
                              [1000, 1001, 857, 1]]) == [27,5,39,1001]
    assert largest_of_four([[4, 9, 1, 3],
                              [13, 35, 18, 26],
                              [32, 35, 97, 39],
                              [10000, 1001, 857, 1]]) == [9, 35, 97, 10000]


def test_rovarsprak():
    assert rovarsprak("hej") == "hohejoj"
    assert rovarsprak("Hej") == "Hohejoj"
    assert rovarsprak("TE13 är bäst.") == "TOTE13 äror bobäsostot."
