"""
LeetCode #19: Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Two pointers approach - right and left pointers with a gap of n nodes.

    Time Complexity: O(L), where L is the length of the linked list.
    Space Complexity: O(1).
    starting from the head of the list, we use two pointers: right and left.
    The right pointer is moved n steps ahead first.
    Then, both pointers are moved together until the right pointer reaches the end of the list.
    At this point, the left pointer will be just before the node that needs to be removed.

    """
    right = head
    left = head

    for i in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return head


def create_linked_list(values):
    """Helper function to create linked list from list of values."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to list for testing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_remove_nth_from_end():
    """Test cases for remove nth from end function."""
    # Test case 1: Remove 2nd from end
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = remove_nth_from_end(head1, 2)
    print(f"Test 1 - Remove 2nd from end of [1,2,3,4,5]: {linked_list_to_list(result1)}")
    assert linked_list_to_list(result1) == [1, 2, 3, 5], "Test case 1 failed"

    # Test case 2: Remove only node
    head2 = create_linked_list([1])
    result2 = remove_nth_from_end(head2, 1)
    print(f"Test 2 - Remove 1st from end of [1]: {linked_list_to_list(result2)}")
    assert linked_list_to_list(result2) == [], "Test case 2 failed"

    # Test case 3: Remove first node
    head3 = create_linked_list([1, 2])
    result3 = remove_nth_from_end(head3, 2)
    print(f"Test 3 - Remove 2nd from end of [1,2]: {linked_list_to_list(result3)}")
    assert linked_list_to_list(result3) == [2], "Test case 3 failed"

    # Test case 4: Remove middle node
    head4 = create_linked_list([1, 2, 3, 4, 5, 6])
    result4 = remove_nth_from_end(head4, 3)
    print(f"Test 4 - Remove 3rd from end of [1,2,3,4,5,6]: {linked_list_to_list(result4)}")
    assert linked_list_to_list(result4) == [1, 2, 3, 5, 6], "Test case 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_remove_nth_from_end()
