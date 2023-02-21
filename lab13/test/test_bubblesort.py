import pytest
from bubblesort import bubblesort

@pytest.mark.parametrize('list',[
    ([1, 5, 3, 6, 2, 4]),
    ([-1, -4, -5, -2, -3, -6]),
    ([1.05, 1.03, 1.06, 1.02, 1.01, 1.04])
])
def test_bubblesort(list):
    assert bubblesort(list) == sorted(list)


def test_bubblesort_empty():
    assert bubblesort([]) == []

@pytest.mark.parametrize('invalid_list', [
    (['a', 'b', 'c']),
    (1),
    ({'a': 5})
])
def test_bubblesort_invalid_value(invalid_list):
    with pytest.raises(TypeError) as exc_info:
        bubblesort(invalid_list)
    assert exc_info.value.args[0] == "Invalid value type"