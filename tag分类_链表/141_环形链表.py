# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/13 3:42

"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。
"""

'''
思考：
法1_快慢指针
假设慢指针速度1，快指针速度2
那么在环的某位置快能追上慢

假设环之前距离为a，而环被相遇点分割，由两部分 x1 x2构成
那么 a+x1 = n(x1+x2)  所以 a = (n-1)x1+nx2 = (n-1)(x1+x2)+x2
所以如果分别以相遇点和最初起点两个点为起点，两个速度相同的指针，再走a距离
又会相遇，此时相遇点便是环起点
  
法2_哈希

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if not fast:
                return
            fast = fast.next
            slow = slow.next
            if fast == slow:
                break
        if not fast:
            return
        else:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
