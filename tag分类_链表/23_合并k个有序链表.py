# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/16 17:47

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[1->4->5,
  1->3->4,
  2->6]
输出: 1->1->2->3->4->4->5->6
"""

'''
思考：
三种方法：暴力、分治、最小堆（优先队列）
暴力解法有两种，一种是12排，然后和3，然后和4，继续下去；
另一种是先放到一个数组中进行排序，然后按照顺序连接

分而治之：两两合并
如果有k个链表，平均每个链表有n个节点
那么，第一轮，k/2次，每次2n个节点
第二轮 k/4次，每次4n数字
......
最后一轮  k/k次，每次kn数字
总共复杂度为Kn*(logk)


我实现的是最小堆：
最小堆：很简单，将每个链表的头节点放到一起，组成最小堆，然后输出最小堆顶进行最终结果链表
然后该节点对应的原始链表后移

'''

import heapq
from tag_listnode import ListNode


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return
        elif len(lists) == 1:
            return lists[0]
        else:
            min_heap = []
            ans = cur = ListNode(-1)
            for i in range(len(lists)):
                if lists[i]:
                    heapq.heappush(min_heap, (lists[i].val, i))
            while min_heap:
                val, index = heapq.heappop(min_heap)
                cur.next = ListNode(val)
                cur = cur.next
                lists[index] = lists[index].next
                if lists[index]:
                    heapq.heappush(min_heap, (lists[index].val, index))
            return ans.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(4)
l3.next = ListNode(6)
l3.next.next = ListNode(7)

Solution().mergeKLists([l1, l2, l3])