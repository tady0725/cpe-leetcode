from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:  # 不為偶數無法除以二
            return False
        dp = set()
        dp.add(0)  # 初始可選可不選 0
        target = sum(nums)//2
        for i in range(0, len(nums)):
            ndp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                ndp.add(t+nums[i])
                ndp.add(t)
            dp = ndp  # 遞迴
        return True if target in dp else False


nums = [1, 5, 4, 8]
print(Solution().canPartition(nums))
