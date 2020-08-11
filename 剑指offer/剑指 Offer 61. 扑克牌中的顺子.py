# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/11 12:31

"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0，可以看成任意数字。
A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True
 
示例 2:
输入: [0,0,1,2,5]
输出: True
 

限制：
数组长度为 5 
数组的数取值为 [0, 13] .
"""

# 思考：难点在于万能牌

# 首先，不能有重复，其次，如果没有重复的前提下，最大牌-最小牌 <= 4，就满足题目要求
# 万能牌直接跳过就行

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        temp = set()
        res = []
        for x in nums:
            if x in temp:
                return False
            else:
                if x != 0:
                   res.append(x)
                   temp.add(x)

        return max(res) - min(res) <= 4





