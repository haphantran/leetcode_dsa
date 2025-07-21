"""
LeetCode #2824: Count Pairs Whose Sum is Less than Target
https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

Problem Statement:
Given a 0-indexed integer array nums of length n and an integer target,
return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

Example 1:
Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions:
- (0, 1) since 0 <= 0 < 1 < 5 and nums[0] + nums[1] = 0 < 2
- (0, 2) since 0 <= 0 < 2 < 5 and nums[0] + nums[2] = 1 < 2
- (0, 4) since 0 <= 0 < 4 < 5 and nums[0] + nums[4] = 0 < 2

Example 2:
Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
Output: 10
Explanation: There are 10 pairs of indices that satisfy the conditions:
- (0, 1), (0, 3), (0, 4), (0, 5), (0, 6)
- (1, 4), (3, 4), (3, 5), (4, 5), (4, 6)

Constraints:
1 <= nums.length <= 50
-50 <= nums[i], target <= 50
"""


def count_pairs_sum_less_than_target(nums, target):
    """
    Count pairs whose sum is less than target.
    Time Complexity: O(n^2) brute force or O(n log n) with sorting + two pointers
    Space Complexity: O(1)
    """
    # Replace this placeholder return statement with your code
    return 0


def test_count_pairs_sum_less_than_target():
    """Test cases for count pairs whose sum is less than target function."""
    test_inputs = [
        ([-1, 1, 2, 3, 1], 2, 3),
        ([-6, 2, 5, -2, -7, -1, 3], -2, 10),
        ([1, 2, 3, 4], 5, 2),
        ([1], 1, 0),
        ([1, 1, 1, 1], 3, 6),
    ]

    for i, (nums, target, expected_output) in enumerate(test_inputs):
        result = count_pairs_sum_less_than_target(nums, target)
        print(f"Test {i + 1} - Input: nums={nums}, target={target}, Output: {result}")
        assert result == expected_output, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_count_pairs_sum_less_than_target()
