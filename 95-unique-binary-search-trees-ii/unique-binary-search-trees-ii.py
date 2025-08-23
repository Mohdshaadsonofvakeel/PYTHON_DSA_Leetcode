# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional['TreeNode']]:
        if n == 0:
            return []

        def build(start: int, end: int) -> List[Optional['TreeNode']]:
            if start > end:
                return [None]

            all_trees = []
            for root_val in range(start, end + 1):
                # All possible left subtrees
                left_trees = build(start, root_val - 1)
                # All possible right subtrees
                right_trees = build(root_val + 1, end)

                # Combine left and right subtrees with the root
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        all_trees.append(root)

            return all_trees

        return build(1, n)
