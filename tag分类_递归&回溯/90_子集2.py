# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/19 3:06

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

'''
原始数组排序后去重，就等价于第一个子集问题了
但是需要注意，不能有重复的元素，所以要多一个集合来判断是否已经有了。
而python的set不可以存储unhashable元素，所以要多一个tuple用以每次判断
'''

class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        item =[]
        res_set = set()
        nums.sort()

        def helper(i, item, ans, res_set):
            if i == len(nums):
                return
            item.append(nums[i])
            # 浅拷贝实现append
            real = item.copy()
            real_ = tuple(real)
            if real_ not in res_set:
                res_set.add(real_)
                ans.append(real)
            helper(i + 1, item, ans, res_set)
            item.pop()
            helper(i + 1, item, ans, res_set)

        real = item.copy()
        ans.append(real)
        helper(0, item, ans, res_set)
        return ans

print(Solution().subsetsWithDup([4,4,4,1,2]))
