# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val

        while head.next:
            num = num * 2 + head.next.val  # num = num * 2 + x。
            head = head.next  # 向下移指標
        return num


head = [1, 0, 1]

print(Solution().getDecimalValue(head))
