# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/3 2:56

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"
 
提示: 0 < nums.length <= 100
说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""

'''
例如数组test = [3, 30, 34, 5, 9]

例如'30' + '3' = '303'
从小到大排序：303 < 330, 确定30一定在3前面; 
3034 < 3430, 30一定在34前面; 334 < 343...
以此类推。。。30, 3, 34, 5, 9, 所以输出结果3033459
'''


class Solution:
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 0:
            return ""
        for i in range(n):
            nums[i] = str(nums[i])
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(nums)


Solution().minNumber([3, 30, 34, 5, 9])