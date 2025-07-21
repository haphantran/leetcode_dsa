"""
LeetCode #564: Find the Closest Palindrome
https://leetcode.com/problems/find-the-closest-palindrome/

Problem Statement:
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome.
The "closest" is defined as the absolute difference minimized between two integers.

Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"

Example 3:
Input: n = "99"
Output: "101"

Constraints:
1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 10^18 - 1].
"""


def next_palindrome_using_same_digits(n):
    """
    Find the closest palindrome to the given number.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Replace this placeholder return statement with your code
    return ""


def test_next_palindrome_using_same_digits():
    """Test cases for next palindrome using same digits function."""
    test_inputs = [
        ("123", "121"),
        ("1", "0"),
        ("99", "101"),
        ("9", "11"),
        ("1991", "2002"),
        ("12321", "12221"),
    ]

    for i, (input_str, expected_output) in enumerate(test_inputs):
        result = next_palindrome_using_same_digits(input_str)
        print(f"Test {i + 1} - Input: '{input_str}', Output: '{result}'")
        assert result == expected_output, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_next_palindrome_using_same_digits()
