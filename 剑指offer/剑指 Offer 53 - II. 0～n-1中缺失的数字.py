# -*- coding: utf-8 -*-
# Time   : 2020/8/4 11:05
# Author : Zhang Xie

"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""

# 思考：排序数组中的搜索问题，首先想到 二分法 解决。
# 二分法的难点在于，最后的返回值，以及边界情况
# 可以记住套路：
# l, r = 0, len(nums) - 1
# m = (l + r) // 2

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == m:
                l = m + 1
            else:
                r = m - 1

        return l
