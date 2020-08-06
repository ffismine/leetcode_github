# -*- coding: utf-8 -*-
# Time   : 2020/8/6 10:41
# Author : Zhang Xie

"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""


# 思考：可以转换为找target的右边界以及 target-1的左边界

# 二分查找，第一反应是哈希，这样可不好

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(tar):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2

                # 这里一定要注意！！！！！！！！！！！！！！ <= 就是右边界   <就是左边界！！！！！！！！！！！！！！
                if nums[m] <= tar:
                    l = m + 1
                else:
                    r = m - 1

            return l

        return find(target) - find(target - 1)


