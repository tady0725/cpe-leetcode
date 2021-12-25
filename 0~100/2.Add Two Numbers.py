# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0  # 紀錄進位值
        record = ListNode()
        curr = record
        while l1 != None or l2 != None:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)  # 新增node
            carry = 1 if carry >= 10 else 0
            curr = curr.next  # 移到下一個
        if carry != 0:
            curr.next = ListNode(carry)  # 假設有進位
        return record.next


'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
