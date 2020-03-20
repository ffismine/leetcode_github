# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/18 22:48

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

'''
对于每个元素都可以放入或者不放入
对于第一个元素1，最后的结果就两种：放1或者不放1
因此就是一种回溯思想
'''


# 结果以列表的列表返回
class Solution:
    def subsets(self, nums):
        ans = []
        item =[]

        def helper(i, item, ans):
            if i == len(nums):
                return
            item.append(nums[i])
            # 浅拷贝实现append
            real = item.copy()
            ans.append(real)
            helper(i + 1, item, ans)
            item.pop()
            helper(i + 1, item, ans)

        real = item.copy()
        ans.append(real)
        helper(0, item, ans)
        return ans


print(Solution().subsets([1,2,3]))


