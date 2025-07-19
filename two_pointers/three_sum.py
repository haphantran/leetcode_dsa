"""
LeetCode #15: 3Sum
https://leetcode.com/problems/3sum/

Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Two pointers approach after fixing one element.

    Time Complexity: O(n^2)
    Space Complexity: O(1) excluding output array
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # for each item, we will look for pairs that are on the right side of it

        if nums[i] > 0:
            # if the current number is positive, we can break early since we are looking for a sum of zero

            break

        if i == 0 or nums[i] != nums[i - 1]:
            low, high = i + 1, n - 1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]

                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])

                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        # move low pointer to the right to skip duplicates
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        # move high pointer to the left to skip duplicates
                        high -= 1

    return result


def test_three_sum():
    """Test cases for the three sum function."""
    # Test case 1
    result1 = three_sum([-1, 0, 1, 2, -1, -4])
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    print(f"Test 1 - Input: [-1,0,1,2,-1,-4], Output: {result1}")
    assert result1 == expected1, "Test case 1 failed"

    # Test case 2
    result2 = three_sum([0, 1, 1])
    expected2 = []
    print(f"Test 2 - Input: [0,1,1], Output: {result2}")
    assert result2 == expected2, "Test case 2 failed"

    # Test case 3
    result3 = three_sum([0, 0, 0])
    expected3 = [[0, 0, 0]]
    print(f"Test 3 - Input: [0,0,0], Output: {result3}")
    assert result3 == expected3, "Test case 3 failed"

    # Test case 4
    result4 = three_sum([-4, -1, -1, 0, 1, 2, 2])
    expected4 = [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1]]
    print(f"Test 4 - Input: [-4,-1,-1,0,1,2,2], Output: {result4}")
    assert result4 == expected4, "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_three_sum()
