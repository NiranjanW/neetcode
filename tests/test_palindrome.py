import pytest
from typing import List
from palindrome_linked_list import solution , ListNode

@pytest.fixture
def palindromes() -> List[str]:
    """Pytest fixture which returns a list of palindromes.
    :return: A list of palindrome strings.
    :rtype: List[str]
    """
    return ["", "a", "aba", "ababa", "racecar"]

def to_linked_list(iterable) -> ListNode:
    head = None
    for val in reversed(iterable):
        head = ListNode(val, head)
    return head

def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def test_is_plaindrome(palindromes: List[str]):
    """Test true cases for ``is_palindrome``.
    :param List[str] palindromes: A list of palindrome strings
    """
    for value in palindromes:
        assert solution.is_palindrome(value)


def test_palindrom():
    node = to_linked_list('racecar')
    actual = 'racecar'
    expected = True
    assert solution.isPalindrome(node) == expected
    # assert.equals(solution.isPalindrom(input),True)