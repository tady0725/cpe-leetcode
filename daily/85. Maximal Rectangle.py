from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:  # 判斷矩形存在
            return 0
        # print(len(matrix))
        height = [0] * (len(matrix[0])+1)
        # print(height)
        print(matrix)
        ans = 0
        for row in matrix:
            for i in range(len(matrix[0])):
                # height[0] = height[0]+1
                height[i] = height[i]+1 if row[i] == '1' else 0
                # print(height)
            stack = [-1]
            # print(stack)
            print(height)

            for i in range(len(matrix[0])+1):
                while height[i] < height[stack[-1]]:
                    print(height[stack[-1]])

                    h = height[stack.pop()]
                    w = i-stack[-1]-1
                    ans = max(ans, h*w)
                stack.append(i)
        return ans


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalRectangle(matrix))
