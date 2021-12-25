from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        ''' ex:[2, 2, 2, 3, 3] => 放在 index [0] 2移到0為偶數零成本  3需2成本
                                    index [1] 2移到1為偶奇數成本3  3移到1為偶數零成本
            選擇最低成本 final index(odd or even)
        '''

        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)      # 最後有可能在奇數上或偶數上 最少花費


position = [2, 2, 2, 3, 3]
print(Solution().minCostToMoveChips(position))
