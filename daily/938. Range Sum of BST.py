# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Init
        ans = root.val if root.val >= low and root.val <= high else 0

        # Iter
        if root.left and root.val > low:
            ans += self.rangeSumBST(root.left, low, high)

        if root.right and root.val < high:
            ans += self.rangeSumBST(root.right, low, high)

        return ans
