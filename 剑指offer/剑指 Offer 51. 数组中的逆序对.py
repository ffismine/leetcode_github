# -*- coding: utf-8 -*-
# Time   : 2020/8/7 16:53
# Author : Zhang Xie

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5

限制：
0 <= 数组长度 <= 50000
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
