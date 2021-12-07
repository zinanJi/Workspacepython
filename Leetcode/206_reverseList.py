# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 双指针
        pre = None
        cur = head
        while cur:
            # 存储下一个结点
            tmp = cur.next
            # 反转
            cur.next = pre
            # pre后移
            pre = cur
            # cur后移
            cur = tmp
        return pre

        """
        if not head or not head.next:
            return head
        cur = self.reverseList(head.next)
        # 递归到最后然后相当于从右往左把结点接到更右
        head.next.next = head
        head.next = None
        return cur
        """
