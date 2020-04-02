# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/3 2:41

"""
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 
限制：最多会对 addNum、findMedia进行 50000 次调用。
"""
'''
思考：由于是中位数，所以自然而然想到堆
两个堆，最大堆和最小堆，各储存一半数据
最大堆堆顶 < 最小堆堆顶
这样中位数要么是其中一个，要么是平均数，由总数字个数决定

新元素进入时的各种情况：
(1) 最大堆与最小堆个数相等：直接与最小堆堆顶和最大堆堆顶进行比较
(2) 最大堆比最小堆多一个元素：两种情况，如果新元素小于最大堆堆顶，还需要更新两个堆堆顶；另外一种情况简单
(3) 最大堆比最小堆少一个元素：两种情况，如果新元素大于最小堆堆顶，也需要更新两个堆堆顶；另外一种情况简单
'''

import heapq
# 在这里复习python堆的用法

# heappush(heap, x) 将x压入堆中
# heappop(heap) 从堆中弹出最小的元素
# heapify(heap) 让列表具备堆特征
# heapreplace(heap, x) 弹出最小的元素，并将x压入堆中，返回弹出的元素
# nlargest(n, iter) 返回iter中n个最大的元素
# nsmallest(n, iter) 返回iter中n个最小的元素
# 默认为最小堆，如果需要使用最大堆，一般需要取相反数


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if len(self.max_heap) == 0:
                heapq.heappush(self.max_heap, -num)
            elif num >= heapq.nsmallest(1, self.min_heap)[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif len(self.max_heap) > len(self.min_heap):
            if num >= -heapq.nsmallest(1, self.max_heap)[0]:
                heapq.heappush(self.min_heap, num)
            elif num < -heapq.nsmallest(1, self.max_heap)[0]:
                temp = -heapq.nsmallest(1, self.max_heap)[0]
                heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, temp)
                heapq.heappush(self.max_heap, -num)
        elif len(self.max_heap) < len(self.min_heap):
            if num <= heapq.nsmallest(1, self.min_heap)[0]:
                heapq.heappush(self.max_heap, -num)
            elif num > heapq.nsmallest(1, self.min_heap)[0]:
                temp = heapq.nsmallest(1, self.min_heap)[0]
                heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (heapq.nsmallest(1, self.min_heap)[0]-heapq.nsmallest(1, self.max_heap)[0])/2
        elif len(self.max_heap) > len(self.min_heap):
            return -heapq.nsmallest(1, self.max_heap)[0]
        elif len(self.max_heap) < len(self.min_heap):
            return heapq.nsmallest(1, self.min_heap)[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

a = MedianFinder()
a.addNum(1)
print(a.findMedian())
a.addNum(16)
print(a.findMedian())