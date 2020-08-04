# -*- coding: utf-8 -*-
# Time    : 2020/8/4 10:49
# Author  : Zhang Xie


"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""

# 思考：需要左右两个指针 同时作用
# i寻找到奇数就停下，j寻找到偶数停下  然后交换

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1:
                i += 1
            while i < j and nums[j] & 1 == 0:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        return nums
