from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode()
        evens = ListNode()  # 建立linklist
        oddsHead = odds  # 實體
        evensHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd  # boolean轉換 判斷基數偶數
            head = head.next  # 向下一個節點
        evens.next = None
        odds.next = evensHead.next
        return oddsHead.next


head = [1, 2, 3, 4, 5]
print(Solution().oddEvenList(head))
'''
odd_node  = ListNode()
        even_node = ListNode()  # 建立linklist
        if head is not None:
            odd_node = odd_head = head
            head = head.next
        else:
            return None
        if head is not None:
            even_node = even_head = head
            head = head.next
        else:
            return odd_head
        count = 3
        while head is not None:
            if count % 2 == 1:
                odd_node.next = head
                odd_node = odd_node.next
            else:
                even_node.next = head
                even_node = even_node.next
            head = head.next
            count = count + 1
        odd_node.next = even_head
        even_node.next = None
        return odd_head
'''
