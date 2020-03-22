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

以下两种，第二种更简单
'''
from tag_listnode import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head = ListNode(-1)
        right_head = ListNode(-1)
        left = left_head
        right = right_head
        while head:
            if head.val < x:
                left.next = head  # p1.next并没有对p1操作，因此dummy和p1地址不变。等于head相当于把p1内部存储了东西
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = right_head.next
        right.next = None
        return left_head.next


class Solution1:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head = ListNode(-1)
        left = left_head
        right_head = ListNode(-1)
        right = right_head
        while head:
            if head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            elif head.val >= x:
                right.next = ListNode(head.val)
                right = right.next
            head = head.next
        left.next = right_head.next
        return left_head.next


l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l2 = Solution1().partition(l1, 3)