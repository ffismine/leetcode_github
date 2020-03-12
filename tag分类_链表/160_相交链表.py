# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/12 1:45


"""
编写一个程序，找到两个单链表相交的起始节点。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""

'''
思考：
方法1：哈希：用集合可以轻易求出交点
方法2：
较长链表长度减去较短链表长度，然后同时移动指针，指向同一节点即找到了交点
方法3：太优美了，双指针，当自己链表遍历完了，让尾节点续上另一个链表的头。由于m+n = n+m 因此如果有相交最后会殊途同归。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# set
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s:
                return headB
            headB = headB.next


# length
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.getLen(headA)
        len_b = self.getLen(headB)
        if len_a > len_b:
            while len_a - len_b:
                headA = headA.next
                len_a -= 1
        if len_b > len_a:
            while len_b - len_a:
                headB = headB.next
                len_b -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

    def getLen(self, head):
        le = 1
        while head:
            head = head.next
            le += 1
        return le


# 双指针
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha


