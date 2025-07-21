"""
LeetCode #1650: Lowest Common Ancestor of a Binary Tree III
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

Problem Statement:
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q
in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be
a descendant of itself)."

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q exist in the tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lowest_common_ancestor_iii(p, q):
    """
    Find the lowest common ancestor of two nodes with parent pointers.
    Time Complexity: O(h) where h is the height of the tree
    Space Complexity: O(1)
    """
    # Replace this placeholder return statement with your code
    return None


def test_lowest_common_ancestor_iii():
    """Test cases for lowest common ancestor with parent pointers."""
    # Create test tree: [3,5,1,6,2,0,8,null,null,7,4]
    root = Node(3)
    node5 = Node(5)
    node1 = Node(1)
    node6 = Node(6)
    node2 = Node(2)
    node0 = Node(0)
    node8 = Node(8)
    node7 = Node(7)
    node4 = Node(4)

    # Build tree structure with parent pointers
    root.left = node5
    root.right = node1

    node5.parent = root
    node1.parent = root

    node5.left = node6
    node5.right = node2

    node6.parent = node5
    node2.parent = node5

    node1.left = node0
    node1.right = node8

    node0.parent = node1
    node8.parent = node1

    node2.left = node7
    node2.right = node4

    node7.parent = node2
    node4.parent = node2

    test_cases = [
        (node5, node1, root),  # LCA of 5 and 1 is 3
        (node5, node4, node5),  # LCA of 5 and 4 is 5
        (node6, node2, node5),  # LCA of 6 and 2 is 5
        (node7, node4, node2),  # LCA of 7 and 4 is 2
    ]

    for i, (p, q, expected) in enumerate(test_cases):
        result = lowest_common_ancestor_iii(p, q)
        print(f"Test {i + 1} - p: {p.val}, q: {q.val}, Expected: {expected.val}")
        if result:
            print(f"Result: {result.val}")
        assert result == expected, f"Test case {i + 1} failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_lowest_common_ancestor_iii()
