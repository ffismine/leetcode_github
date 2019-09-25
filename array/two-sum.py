# -*- coding:utf-8 -*-

"""
Created on '2019/9/25-15:25'
Author: Xzreal
"""
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''

class Solution:
    def __init__(self,nums, target: int):
        self.nums=nums
        self.target=target

    # 方法一：暴力法
    def twoSum1(self):
        size = len(self.nums)
        for i, m in enumerate(self.nums):
            j = i + 1
            while j < size:
                if self.target == (m + self.nums[j]):
                    return [i, j]
                else:
                    # print(i, j, m + _n, " didn't match!")
                    j += 1
        return "not exist"

    # 方法二：字典模拟Hash
    def twoSum2(self):
        _dict = {}
        for i, m in enumerate(self.nums):
            _dict[m] = i

        for i, m in enumerate(self.nums):
            j = _dict.get(self.target - m)
            if j is not None and i != j:
                return [i, j]
        return "not exist"

    # 方法三：一遍字典模拟Hash
    def twoSum3(self):
        _dict = {}
        for i, m in enumerate(self.nums):
            if _dict.get(self.target - m) is not None:
                return [_dict.get(self.target - m), i]
            _dict[m] = i
        return "not exist"


if __name__ == '__main__':
    a=Solution(nums=[2,7, 11, 15], target=9)
    print(a.twoSum1())
    print(a.twoSum2())
    print(a.twoSum3())




