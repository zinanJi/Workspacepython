# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 需要一个哑节点的额外空间用于最后返回头结点
        dummy = ListNode()
        result = dummy
        # 两条链表任意一条没有遍历到尾部
        while list1 or list2:
            # list1为空，则直接把剩余的list2接到result上
            if not list1:
                result.next = list2
                break
            # list2为空，则直接把剩余的list1接到result上
            if not list2:
                result.next = list1
                break
            # list1和list2都不为空，取最小的接到result上
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        return dummy.next

    def mergeTwoListsRecursion(self, list1, list2):
        # 递归思路：
        # list1[0] + merge(list1[1:],list2)  ,  list1[0]<list2[0]
        # list2[0] + merge(list1,list2[1:])  ,  list1[0]≥list2[0]
        # 边界情况，链表为空，则返回另一条非空链表
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val<list2.val:
            list1.next = self.mergeTwoListsRecursion(list1.next,l2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursion(list1,list2.next)
            return list2
