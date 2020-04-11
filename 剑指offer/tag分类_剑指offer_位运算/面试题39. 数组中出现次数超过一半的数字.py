# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/11 9:47

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 
限制：1 <= 数组长度 <= 50000
"""

'''
可以用哈希表记录，见解法1

也可以用投票，见解法2
'''


class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        temp = {}
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 1
            else:
                temp[nums[i]] += 1
                if temp[nums[i]] >= len(nums)/2:
                    return nums[i]


# [1, 2, 3, 2, 2, 2, 5, 4, 2]
class Solution1:
    def majorityElement(self, nums):
        vote = 0
        demo = 0
        for x in nums:
            if vote == 0:
                demo = x
            if demo == x:  # 是相同的
                vote += 1
            else:
                vote -= 1
        return demo

Solution1().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2])