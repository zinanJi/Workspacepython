# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 双指针同时走，间隔为n+1,走到底左指针就在导数第n+1个节点
        first = head
        dummy = ListNode(0, head)
        # first先走n步
        for i in range(n):
            first = first.next
        second = dummy.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
