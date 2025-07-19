"""
LeetCode #125: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


def is_palindrome(s: str) -> bool:
    """
    Two pointers approach to check if string is a palindrome.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def test_is_palindrome():
    """Test cases for the palindrome function."""
    # Test case 1
    assert is_palindrome("A man, a plan, a canal: Panama") == True

    # Test case 2
    assert is_palindrome("race a car") == False

    # Test case 3
    assert is_palindrome(" ") == True

    # Test case 4
    assert is_palindrome("No 'x' in Nixon") == True

    # Test case 5
    assert is_palindrome("1A@2!3 23!2@a1") == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_is_palindrome()
