"""
LeetCode #408: Valid Word Abbreviation (Premium)
https://leetcode.com/problems/valid-word-abbreviation/

Problem Statement:
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings
with their lengths. The lengths should not have leading zeros.

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Example:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n"
("i nternational iz atio n").
"""


def valid_word_abbreviation(word: str, abbr: str) -> bool:
    """
    Two pointers approach to validate word abbreviation.

    Time Complexity: O(n + m) where n is length of word and m is length of abbr
    Space Complexity: O(1)
    """
    word_index, abbr_index = 0, 0

    while abbr_index < len(abbr):
        if abbr[abbr_index].isdigit():
            if abbr[abbr_index] == "0":
                return False
            num = 0

            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])
                abbr_index += 1
            word_index += num
        else:
            if word_index >= len(word) or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1

    return word_index == len(word) and abbr_index == len(abbr)


def test_valid_word_abbreviation():
    """Test cases for valid word abbreviation function."""
    # Test case 1
    result1 = valid_word_abbreviation("internationalization", "i12iz4n")
    print(f"Test 1 - word: 'internationalization', abbr: 'i12iz4n', Output: {result1}")
    assert result1 == True, "Test case 1 failed"

    # Test case 2
    result2 = valid_word_abbreviation("apple", "a3e")
    print(f"Test 2 - word: 'apple', abbr: 'a3e', Output: {result2}")
    assert result2 == True, "Test case 2 failed"

    # Test case 3
    result3 = valid_word_abbreviation("internationalization", "i5a11o1")
    print(f"Test 3 - word: 'internationalization', abbr: 'i5a11o1', Output: {result3}")
    assert result3 == True, "Test case 3 failed"

    # Test case 4: Leading zeros should be invalid
    result4 = valid_word_abbreviation("hi", "h01")
    print(f"Test 4 - word: 'hi', abbr: 'h01', Output: {result4}")
    assert result4 == False, "Test case 4 failed"

    # Test case 5
    result5 = valid_word_abbreviation("word", "w2rd")
    print(f"Test 5 - word: 'word', abbr: 'w2rd', Output: {result5}")
    assert result5 == False, "Test case 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_word_abbreviation()
