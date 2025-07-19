"""
LeetCode #75: Sort nums
https://leetcode.com/problems/sort-nums/

Problem Statement:
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the nums in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

from typing import List


def sort_nums(nums: List[int]) -> None:
    """
    Dutch National Flag algorithm using three pointers.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Do not return anything, modify nums in-place instead.
    """
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(nums) - 1

    # Iterate through the list until the current pointer exceeds the end pointer
    while current <= end:
        if nums[current] == 0:
            # If the current element is 0 (red), swap it with the element at the start pointer
            # This ensures the red element is placed at the beginning of the array
            nums[start], nums[current] = nums[current], nums[start]
            # Move both the start and current pointers one position forward
            current += 1
            start += 1

        elif nums[current] == 1:
            # If the current element is 1 (white), just move the current pointer one position forward
            current += 1

        else:
            # If the current element is 2 (blue), swap it with the element at the end pointer
            # This pushes the blue element to the end of the array
            nums[current], nums[end] = nums[end], nums[current]
            # Move the end pointer one position backward
            end -= 1


def test_sort_nums():
    """Test cases for sort nums function."""
    # Test case 1
    nums1 = [2, 0, 2, 1, 1, 0]
    sort_nums(nums1)
    print(f"Test 1 - Input: [2,0,2,1,1,0], Output: {nums1}")
    assert nums1 == [0, 0, 1, 1, 2, 2], "Test case 1 failed"

    # Test case 2
    nums2 = [2, 0, 1]
    sort_nums(nums2)
    print(f"Test 2 - Input: [2,0,1], Output: {nums2}")
    assert nums2 == [0, 1, 2], "Test case 2 failed"

    # Test case 3
    nums3 = [1, 2, 1, 1, 0, 2, 0]
    sort_nums(nums3)
    print(f"Test 3 - Input: [1,2,1,1,0,2,0], Output: {nums3}")
    assert nums3 == [0, 0, 1, 1, 1, 2, 2], "Test case 3 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_sort_nums()
