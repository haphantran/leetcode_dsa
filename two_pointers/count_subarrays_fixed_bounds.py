"""
LeetCode #2444: Count Subarrays With Fixed Bounds
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

Problem Statement:
You are given an integer array nums and two integers minK and maxK.
A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
- The minimum value in the subarray is equal to minK.
- The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
"""


def count_subarrays_with_fixed_bounds(nums, minK, maxK):
    """
    Count subarrays with fixed bounds.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Replace this placeholder return statement with your code
    return 0


def test_count_subarrays_with_fixed_bounds():
    """Test cases for count subarrays with fixed bounds function."""
    test_inputs = [
        ([1, 3, 5, 2, 7, 5], 1, 5, 2),
        ([1, 1, 1, 1], 1, 1, 10),
        ([1, 2, 3], 1, 3, 1),
        ([1, 4, 2, 2, 3], 2, 3, 3),
        ([1, 5, 2, 5, 3, 5, 4], 2, 5, 12),
    ]

    for i, (nums, minK, maxK, expected_output) in enumerate(test_inputs):
        result = count_subarrays_with_fixed_bounds(nums, minK, maxK)
        print(f"Test {i + 1} - Input: nums={nums}, minK={minK}, maxK={maxK}, Output: {result}")
        assert result == expected_output, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_count_subarrays_with_fixed_bounds()
