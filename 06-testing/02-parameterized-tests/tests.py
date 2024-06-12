import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize('string', [
    '',
    '()',
    '(())',
    '()()()',
    '(())()',
])
def test_matching_parentheses_in_given_string(string):
    actual = matching_parentheses(string)
    assert actual == True, f'{string} has matching parentheses'


@pytest.mark.parametrize('string', [
    '(',
    ')',
    ')(',
    '(()))(()',
])
def test_non_matching_parentheses_in_given_string(string):
    actual = matching_parentheses(string)
    assert actual == False, f'{string} has unmatching parentheses'