import pytest
from typing import List
from binarysearch import Solution 

@pytest.fixture
def input() -> List[int]:
    """Pytest fixture which returns a list of palindromes.
    :return: A list of palindrome strings.
    :rtype: List[str]
    """
    return [[-1,0,3,5,9,12]]


def test_binarysearch(input: List[int]):
    """Test true cases for ``is_palindrome``.
    :param List[str] palindromes: A list of palindrome strings
    """
    for value in input:
        assert( Solution.search(value, 9) ) == 4