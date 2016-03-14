import pytest
from exercises.introduction import area, bouncer, character_frequency, is_of_age, largest_of_four, overlapping, palindrome, repeat, reverse, rovarsprak, to_seconds, travel_price, vowel


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


def test_area():
    assert area(20, 20) == 40
    assert area(23.5, 24.0) == 564


def test_to_seconds():
    assert to_seconds(5) == 18000
    assert to_seconds(1.8) == 6480


def test_is_of_age():
    assert is_of_age(12) == False
    assert is_of_age(20) == True
    assert is_of_age(17.5) == False


def test_vowel():
    assert vowel('a') == True
    assert vowel('Y') == True
    assert vowel('b') == False
    assert vowel('C') == False


def test_reverse():
    assert reverse('Test string') == 'gnirts tseT'
    assert reverse('Hello') == 'olleH'
    assert reverse('a') == 'a'


def test_overlapping():
    assert overlapping([1,2,3], [3,4,5]) == True
    assert overlapping([1.23, 'test', 5], [1.24, 'test1', 'test']) == True
    assert overlapping(['a', 6, 'c'], ['e', 'f', 'g']) == False


def test_travel_price():
    assert travel_price(20, 0.6, 12) == 14.4
    assert travel_price(105.5, 0.8, 14) == 118.16


def test_palindrome():
    assert palindrome('ni talar bra latin') == True
    assert palindrome('A car a man a maraca') == True
    assert palindrome('hello there') == False


def test_character_frequency():
    assert character_frequency('hej janne') == {'h' : 1, 'e' : 2, 'j' : 2, 'a' : 1, 'n' : 2}
    assert character_frequency('bananer') == {'b' : 1, 'a' : 2, 'n' : 2, 'e' : 1, 'r' : 1}
