"""
LeetCode #2193: Minimum Number of Moves to Make Palindrome
https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
Problem Statement:
You are given a string s consisting only of lowercase English letters.
In one move, you can select any two adjacent characters of s and swap them.
Return the minimum number of moves needed to make s a palindrome.
Note that the input will be generated such that s can always be converted to a palindrome.

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab".
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.


Constraints:

1 <= s.length <= 2000
s consists only of lowercase English letters.
s can be converted to a palindrome using a finite number of moves."""


def min_moves_to_make_palindrome(s):
    """
    Two pointers approach to find minimum moves to make a palindrome.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    print(f"Input string: {s}")
    s = list(s)

    moves = 0

    i, j = 0, len(s) - 1
    while i < j:
        k = j
        while k > i:
            if s[i] == s[k]:
                for m in range(k, j):
                    s[m], s[m + 1] = s[m + 1], s[m]
                    moves += 1
                j -= 1
                break
            k -= 1
        if k == i:
            moves += len(s) // 2 - i
        i += 1

    return moves


def test_min_moves_to_make_palindrome():
    """Test cases for minimum moves to make palindrome function."""
    test_inputs = [
        ("w", 0),
        ("ccxx", 2),
        ("arcacer", 4),
        ("eggeekgbbeg", 7),
        ("ooooooo", 0),
    ]

    for i, (input_str, expected_output) in enumerate(test_inputs):
        result = min_moves_to_make_palindrome(input_str)
        print(f"Test {i + 1} - Input: '{input_str}', Output: {result}")
        assert result == expected_output, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_min_moves_to_make_palindrome()
