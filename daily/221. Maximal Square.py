from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= rows or c >= cols:  # out of range
                return 0
            if (r, c) not in cache:
                down = helper(r+1, c)  # 下
                right = helper(r, c+1)  # 右
                diag = helper(r+1, c+1)  # 對角
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            return cache[(r, c)]
        helper(0, 0)
        return max(cache.values()) ** 2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalSquare(matrix))
