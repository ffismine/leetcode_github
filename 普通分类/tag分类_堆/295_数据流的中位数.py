# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/9 23:53

"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例：
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
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

from heapq import *


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

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if len(self.max_heap) == 0:
                heappush(self.max_heap, -num)
            elif num >= nsmallest(1, self.min_heap)[0]:
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
        elif len(self.max_heap) > len(self.min_heap):
            if num >= -nsmallest(1, self.max_heap)[0]:
                heappush(self.min_heap, num)
            elif num < -nsmallest(1, self.max_heap)[0]:
                # temp = -nsmallest(1, self.max_heap)[0]
                # heappop(self.max_heap)
                temp = -heappop(self.max_heap)
                heappush(self.min_heap, temp)
                heappush(self.max_heap, -num)
        elif len(self.max_heap) < len(self.min_heap):
            if num <= nsmallest(1, self.min_heap)[0]:
                heappush(self.max_heap, -num)
            elif num > nsmallest(1, self.min_heap)[0]:
                # nsmallest(1, self.min_heap)[0]
                temp = heappop(self.min_heap)
                heappush(self.max_heap, -temp)
                heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (nsmallest(1, self.min_heap)[0] - nsmallest(1, self.max_heap)[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -nsmallest(1, self.max_heap)[0]
        elif len(self.max_heap) < len(self.min_heap):
            return nsmallest(1, self.min_heap)[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

a = MedianFinder()
a.addNum(40)
a.addNum(12)
print(a.findMedian())
a.addNum(16)
print(a.findMedian())
