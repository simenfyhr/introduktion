import pytest


@pytest.mark.skip('Not implemented yet.')
def test_find_max():
    from exercises.find_max import find_max

    assert find_max([1, 5, 2]) == 5
    assert find_max([7, 2, 2]) == 7
    assert find_max([-3, -2, -4]) == -2


@pytest.mark.skip('Not implemented yet.')
def test_odd_list():
    from exercises.odd_list import odd_list

    assert odd_list([]) == []
    assert odd_list([1]) == []
    assert odd_list(['a', 'b']) == ['b']
    assert odd_list([1, 2, 3, 4, 5, 6, 7]) == [2, 4, 6]


@pytest.mark.skip('Not implemented yet.')
def test_running_total():
    from exercises.running_total import running_total

    assert running_total([2, 4, 3]) == [2, 6, 9]
    assert running_total([2, 4, -7, 2, -1, 4]) == [2, 6, -1, 1, 0, 4]


@pytest.mark.skip('Not implemented yet.')
def test_merge_sorted_lists():
    from exercises.merge_sorted_lists import merge_sorted_lists

    assert merge_sorted_lists([1, 3, 5, 7], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sorted_lists([], [2, 4, 7]) == [2, 4, 7]
    assert merge_sorted_lists([1, 1, 4, 7], [1, 3]) == [1, 1, 1, 3, 4, 7]
