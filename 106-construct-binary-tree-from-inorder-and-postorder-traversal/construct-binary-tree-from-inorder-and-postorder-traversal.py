class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index for O(1) lookups in inorder
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Pick root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Split inorder into left and right subtrees
            index = idx_map[root_val]

            # Build right subtree first
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)
