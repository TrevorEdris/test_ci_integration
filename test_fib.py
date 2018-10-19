import pytest

from fib import (
    fib,
    is_valid_input
)


@pytest.mark.parametrize('bad_input', [
    -1,
    'string',
    None,
    123.456,
    False,
    True
])
def test_is_valid_input_handles_bad_input(bad_input):
    assert is_valid_input(bad_input) is False


@pytest.mark.parametrize('good_input', [
])
def test_is_valid_input_handles_good_input(good_input):
    assert is_valid_input(good_input) is True
    

@pytest.mark.parametrize('bad_input', [
    -1,
    'string',
    None,
    123.456,
    False,
    True
])
def test_fib_checks_valid_input(bad_input):
    assert fib(bad_input) is None


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

