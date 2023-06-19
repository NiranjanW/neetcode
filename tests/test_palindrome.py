import pytest
from typing import List
from palindrome_linked_list import solution

@pytest.fixture
def palindromes() -> List[str]:
    """Pytest fixture which returns a list of palindromes.
    :return: A list of palindrome strings.
    :rtype: List[str]
    """
    return ["", "a", "aba", "ababa", "racecar"]


def test_is_plaindrome(palindromes: List[str]):
    """Test true cases for ``is_palindrome``.
    :param List[str] palindromes: A list of palindrome strings
    """
    for value in palindromes:
        assert solution.is_palindrome(value)

def test_palindrom():
    actual = 'racecar'
    expected = True
    assert solution.isPalindrome(actual) == expected
    # assert.equals(solution.isPalindrom(input),True)