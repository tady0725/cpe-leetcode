from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        pre = dummy
        node = head  # 輸入的表
        while node:  # 當還有節點存在
            cur = node
            node = node.next
            if cur.val < pre.val:  # 值小於當前值標位置
                pre = dummy  # 指標位置移到最前
            while pre.next and cur.val > pre.next.val:
                pre = pre.next  # 向後移
            cur.next = pre.next
            pre.next = cur

        return dummy.next


head = [4, 2, 1, 3]
print(Solution().insertionSortList(head))
