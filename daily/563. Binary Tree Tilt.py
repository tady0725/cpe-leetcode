# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:  # 判斷節點存在
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left - right)  # 取差值
            return left + right + root.val

        self.res = 0
        dfs(root)
        return self.res


root = [1, 2, 3]
print(Solution().findTilt(root))
