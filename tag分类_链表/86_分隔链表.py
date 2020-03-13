# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/14 4:48

"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""

'''
思考：两个临时头节点
小于就插到第一个后面，大于就插到第二个后面
以类推。最终可以将所有节点划到两个临时节点后面
最终将第一个临时链表插入第二个链表头部
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        # print(listNodeToString(dummy1.next))
        # print(listNodeToString(dummy2.next))
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next

class Solution1:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_h = ListNode(None)
        left = left_h
        right_h = ListNode(None)
        right = right_h
        while head:
            if head.val < x:
                left_h.next = ListNode(head.val)
                left_h = left_h.next
            elif head.val >= x:
                right_h.next = ListNode(head.val)
                right_h = right_h.next
            head = head.next
            continue
        left_h.next = right.next
        return left.next


l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l2 = Solution().partition(l1, 3)