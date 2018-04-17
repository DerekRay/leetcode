# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = t = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry, val= divmod(val, 10)
            p.next = ListNode(val)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return t.next

l1 = ListNode(7)
l1.next = ListNode(8)
l1.next.next = ListNode(5)

l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(5)

s = Solution()
l3 = s.addTwoNumbers(l1, l2)
while l3:
    if l3.next:
        print(l3.val, end = ',')
    else:
        print(l3.val)
    l3 = l3.next
