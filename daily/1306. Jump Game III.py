from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        s = {start}  # Queried index
        q = [start]  # wait querry index
        while q:
            cur = q.pop()
            for i in (cur + arr[cur], cur - arr[cur]):  # i + arr[i] or i - arr[i]
                if 0 <= i < n:  # not jump outside of the array
                    if arr[i] == 0:
                        return True
                    if i not in s:  # not found in set
                        q.append(i)
                        s.add(i)
        return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(Solution().canReach(arr, start))
'''
class Solution:
    def canReach(self, A, cur):
        if cur < 0 or cur >= len(A) or A[cur] < 0: return False
        A[cur] *= -1
        return A[cur] == 0 or self.canReach(A, cur + A[cur]) or self.canReach(A, cur - A[cur])
'''
