"""
LeetCode #1842: Next Palindrome Using Same Digits
https://leetcode.com/problems/next-palindrome-using-same-digits/description/

Problem Statement:
Given a numeric string, num_str, representing a palindrome (composed only of digits). Return the smallest palindrome larger than num_str that can be created by rearranging its digits. If no such palindrome exists, return an empty string "".

Consider the following example to understand the expected output for a given numeric string:

    input string = "123321"

    The valid palindromes made from the exact digits are "213312", "231132", "312213", "132231", "321123".

    We return the palindrome "132231" because it is the smallest palindrome larger than the input string "123321".

Constraints:

    1 <= num_str.length <= 10^5
    num_str is a palindrome.
"""


def find_next_permutation(digits: list[int]) -> bool:
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1 :] = reversed(digits[i + 1 :])
    return True


def next_palindrome_using_same_digits(num_str):
    """
    Find the closest palindrome to the given number.
    Time Complexity:
    Space Complexity:
    """
    # Replace this placeholder return statement with your code
    n = len(num_str)

    if n == 1:
        return ""

    half_length = n // 2
    left_half = list(num_str[:half_length])

    if not find_next_permutation(left_half):
        return ""

    if n % 2 == 0:
        next_palindrome = "".join(left_half + left_half[::-1])
    else:
        middle_digit = num_str[half_length]
        next_palindrome = "".join(left_half + [middle_digit] + left_half[::-1])

    if next_palindrome > num_str:
        return next_palindrome
    return ""


def test_next_palindrome_using_same_digits():
    """Test cases for next palindrome using same digits function."""
    test_inputs = [
        ("123321", "132231"),
        ("1234321", "1324231"),
        ("999", ""),
        ("89798", "98789"),
    ]

    for i, (input_str, expected_output) in enumerate(test_inputs):
        result = next_palindrome_using_same_digits(input_str)
        print(f"Test {i + 1} - Input: '{input_str}', Output: '{result}', expected: '{expected_output}'")
        assert result == expected_output, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_next_palindrome_using_same_digits()
