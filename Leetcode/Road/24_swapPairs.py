# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        # 从哑结点开始，结果是
        # 1. node往前移动（node = node1[node.next]）
        # 2. 第二个节点指回第一个节点 node2.next = node1
        # 3. 第一个节点指向第二个节点的下一个节点 node1.next = node2.next
        # 4. node指向第二个节点 node.next = node2
        # 为了不断链，则顺序应该是4-3-2-1
        while node.next and node.next.next:
            node1 = node.next
            node2 = node.next.next
            node.next = node2
            node1.next = node2.next
            node2.next = node1
            node = node1
        return dummy.next



