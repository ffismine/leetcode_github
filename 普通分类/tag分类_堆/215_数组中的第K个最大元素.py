# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/9 18:32

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""

'''
思考：
创建一个k长度的最小堆。然后先放进去k个，然后大于于堆顶就替换
'''

import heapq
# 在这里顺便复习python堆的用法
# heappush(heap, x) 将x压入堆中
# heappop(heap) 从堆中弹出最小的元素
# heapify(heap) 让列表具备堆特征
# heapreplace(heap, x) 弹出最小的元素，并将x压入堆中，返回弹出的元素
# nlargest(n, iter) 返回iter中n个最大的元素
# nsmallest(n, iter) 返回iter中n个最小的元素


class Solution:
    def findKthLargest(self, nums, k: int):
        nums_len = len(nums)
        H = []
        for index in range(k):
            heapq.heappush(H, nums[index])

        for index in range(k, nums_len):
            top = H[0]
            if nums[index] > top:
                heapq.heapreplace(H, nums[index])
        return H[0]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
