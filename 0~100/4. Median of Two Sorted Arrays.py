'''
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            s = (len(nums1))//2
            # print(s)
            sums = (nums1[s-1]+nums1[s])/2
            # r = ('{:06.5f}'.format(sums))

            return sums
        else:
            y = ((len(nums1))//2)+1
            ss = nums1[y-1]
            # r = ('{:06.5f}'.format(ss))
            return ss


nums1 = [11, 12, 13, 14, 15, 16, 17, 18]
nums2 = [19, 20]
print(Solution().findMedianSortedArrays(nums1, nums2))
# 降低複雜度 https://atharayil.medium.com/median-of-two-sorted-arrays-day-36-python-fcbd2dbbb668
