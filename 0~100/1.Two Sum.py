class Solution:
    def two_sum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                # 找到key: 值 對應的value: 索引 回傳
                return hash_map.get(target - nums[i]), i

            # 在hash table中增加數據(key: 值, value: 索引)
            hash_map[nums[i]] = i   # 添加進dict

            # print(hash_map)
nums = [1, 2, 3, 4, 5, 6]
target = 10
print(Solution().two_sum(nums, target))


'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

時間複雜度 :O(n) n元素只有一次迴圈
空間複雜度 :O(n) 最多存儲n 元素(key =>value)
HashTable，
需要先建立一張表 (此處建立 dict)，
利用 「key -> value」 的特性保存 「剩餘值 對應 index」
因此當後續的計算，發現剩餘值存在 dict 的 key 中，
就能快速反查表得到 index。
'''
