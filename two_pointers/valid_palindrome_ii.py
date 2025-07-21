"""
LeetCode #680: Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Problem Statement:
Given a string s, return true if the s can be a palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


def valid_palindrome_ii(s):
    """
    Check if string can be a palindrome after deleting at most one character.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Replace this placeholder return statement with your code
    return False


def test_valid_palindrome_ii():
    """Test cases for valid palindrome II function."""
    test_inputs = [
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("raceacar", True),
        ("race a car", True),
        ("abcddcba", True),
        ("abcdefg", False),
        ("deeee", True),
        ("a", True),
        ("ab", True),
    ]

    for i, (input_str, expected_output) in enumerate(test_inputs):
        result = valid_palindrome_ii(input_str)
        print(f"Test {i + 1} - Input: '{input_str}', Output: {result}")
        assert result == expected_output, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_palindrome_ii()
