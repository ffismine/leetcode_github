# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/3 1:30

"""
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
 
限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""

'''
思考：用一个最大堆实时维护数组的前k小值。最大堆堆顶储存最大值，取出来说明至少有k个比它小。
首先将前k个数插入最大堆中，随后从第k+1数开始遍历，如果当前遍历到的数比最大堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。
最后将大根堆里的数存入数组返回即可。
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
    def getLeastNumbers(self, arr, k: int):
        if k == 0:
            return list()

        # python默认最小堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])

        ans = [-x for x in hp]
        return ans
