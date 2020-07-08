# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/15 3:51

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

'''
思考：这题还是挺简单的，比较之前链表元素大小，小的插入新链表，并且当前链表后移

第二种解法递归，递归需要考虑两个因素：
递归函数必须要有终止条件，否则会出错；
递归函数先不断调用自身，直到遇到终止条件后进行回溯，最终返回答案。
因此本题递归函数的终止条件就是有一个链表空了，那么可以直接返回另外一个当前链表
要不然就需要调用递归函数，遍历下去

递归有一个技巧给思路：
正确答案是112344，那么拆解子问题，最大的子问题的12344，这样拆解下去，思路就清晰了

0708更新：新增一种便于理解的递归思路
'''

# Definition for singly-linked list.
from tag_listnode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(-1)
        head = new_head
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    head.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    head.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                head.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next
        return new_head.next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution2:

    def __init__(self):
        self.res = self.cur = ListNode(-1)

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            while l2:
                self.cur.next = ListNode(l2.val)
                self.cur = self.cur.next
                l2 = l2.next
        if not l2:
            while l1:
                self.cur.next = ListNode(l1.val)
                self.cur = self.cur.next
                l1 = l1.next
        if l1 and l2:
            if l1.val <= l2.val:
                self.cur.next = ListNode(l1.val)
                self.cur = self.cur.next
                self.mergeTwoLists2(l1.next, l2)
            else:
                self.cur.next = ListNode(l2.val)
                self.cur = self.cur.next
                self.mergeTwoLists2(l1, l2.next)
        return self.res.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
Solution1().mergeTwoLists(l1, l2)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(Solution2().mergeTwoLists2(l1, l2))
