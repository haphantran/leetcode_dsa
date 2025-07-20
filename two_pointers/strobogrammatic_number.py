"""
LeetCode #246: Strobogrammatic Number (Premium)
https://leetcode.com/problems/strobogrammatic-number/


Problem Statement:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.
Example:
Input: num = "609"
Output: true

Example:
Input: num = "88"
Output: true

Input: num = "962"
Output: false
"""


# Function to check if a number is strobogrammatic
def is_strobogrammatic(num):
    """
    Using two pointers to check if a number is strobogrammatic.
    Time Complexity: O(n), This is because we iterate through the string once, comparing each digit pair from both ends toward the center.
    Space Complexity: O(1) because the solution uses a fixed-size map to store the strobogrammatic digit mappings, regardless of the input size.
    """
    mapping = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in mapping or mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    return True


# Driver code
def test_is_strobogrammatic():
    nums = ["609", "88", "962", "101", "123"]
    expected_results = [True, True, False, True, False]
    for i, num in enumerate(nums):
        result = is_strobogrammatic(num)
        print(f"Test {i + 1} - Input: '{num}', Output: {result}")
        assert result == expected_results[i], f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_is_strobogrammatic()
