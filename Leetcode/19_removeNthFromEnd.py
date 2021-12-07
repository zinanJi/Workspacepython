# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for i in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next