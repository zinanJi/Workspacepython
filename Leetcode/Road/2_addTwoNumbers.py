# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 生成链表节点对象
        head = tail = ListNode()
        # 设置初始进位
        carry = 0
        # 只要两个链表非空
        while l1 or l2:
            # 取当前节点值，其中一条链表遍历到最后则填充0
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry
            
            tail.next = ListNode(val=sum % 10)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            carry = sum // 10
        if carry:
            tail.next = ListNode(carry)
        return head.next
