# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/10 2:05

"""
优先队列做了一个动态的变化：

如果总个数为偶数，那么插入新元素经历 最大堆 → 最小堆 → 最大堆
如果总个数为奇数，那么插入新元素经历 最大堆 → 最小堆 即可
总之保证 最大堆比最小堆个数相等或者多一个

别人的解释：
为了找到添加新数据以后，数据流的中位数，我们让这个新数据在大顶堆和小顶堆中都走了一遍。
而为了让大顶堆的元素多 1 个，我们让从小顶堆中又拿出一个元素“送回”给大顶堆；
"""

import heapq


class MedianFinder:
    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        # 最大堆 → 最小堆 → ..
        heapq.heappush(self.max_heap, -num)
        max_heap_top = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def findMedian(self) -> float:
        if self.count & 1: # 这个牛笔
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return -self.max_heap[0]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] - self.max_heap[0]) / 2


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