import pytest

from fib import fib


@pytest.mark.parametrize('n, expected_nth', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
])
def test_fib_calculates_correctly(n, expected_nth):
    nth = fib(n)
    assert nth == expected_nth


@pytest.mark.parametrize('bad_input', [
    -1,
    'string',
    None,
    123.456,
    False,
    True
])
def test_fib_handles_bad_input(bad_input):
    assert fib(bad_input) is None
