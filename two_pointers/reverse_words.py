"""
LeetCode #151: Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Problem Statement:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example:
Input: s = "the sky is blue"
Output: "blue is sky the"
"""


def reverse_words(s: str) -> str:
    """
    Two pointers approach to reverse words in string.

    Time Complexity: O(n)
    Space Complexity: O(1) if we modify in-place, O(n) for result string
    """
    s = s.strip()
    result = s.split()
    left, right = 0, len(result) - 1

    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return " ".join(result)


# fast 1 liner option
def reverse_words_fast(s: str) -> str:
    """
    One-liner to reverse words in a string.
    """
    return " ".join(list(s.split())[::-1])


def test_reverse_words():
    """Test cases for reverse words function."""
    # Test case 1
    result1 = reverse_words("the sky is blue")
    print(f"Test 1 - Input: 'the sky is blue', Output: '{result1}'")
    assert result1 == "blue is sky the", "Test case 1 failed"

    # Test case 2
    result2 = reverse_words("  hello world  ")
    print(f"Test 2 - Input: '  hello world  ', Output: '{result2}'")
    assert result2 == "world hello", "Test case 2 failed"

    # Test case 3
    result3 = reverse_words("a good   example")
    print(f"Test 3 - Input: 'a good   example', Output: '{result3}'")
    assert result3 == "example good a", "Test case 3 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_words()
