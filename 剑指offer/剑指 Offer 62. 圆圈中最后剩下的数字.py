# -*- coding: utf-8 -*-
# Time   : 2020/8/6 9:32
# Author : Zhang Xie

"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17
输出: 2
 

限制：
1 <= n <= 10^5
1 <= m <= 10^6
"""
from tag_listnode import ListNode


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if m == 1:
            return n - 1

        head = cur = ListNode(0)
        for i in range(1, n):
            cur.next = ListNode(i)
            cur = cur.next
        cur.next = head

        while head != head.next:
            cur_ = head
            for i in range(m-2):
                cur_ = cur_.next
            cur_.next = cur_.next.next
            head = cur_.next

        return head.val


print(Solution().lastRemaining(70866, 116922))
