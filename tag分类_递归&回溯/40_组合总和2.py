# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/20 19:58

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""

'''
与78和90相比，简单的思路是将所以子集求出来，然后看有没有相加和等于8的，这是暴力法
但是在尝试过程中，浪费了很多时间，比如10+1和7+6明显大于8
由于复杂度为2^n，长度大的数组，肯定是不行的
而且对于10这种选择，浪费了2^n次无效筛选
因此在过程中进行剪枝操作，
第一个剪纸是剪去所有值大于target的值
第二剪枝是如果当前sum>target，直接返回，不进行更深的回溯
并且在对应的item里面进行pop
'''


class Solution:
    def combinationSum2(self, candidates, target: int):
        ans = []
        item =[]
        res_set = set()
        candidates.sort()
        for i in range(len(candidates)-1, -1, -1):
            if candidates[i] > target:
                candidates = candidates[:i]
            else:
                break

        def helper(i, item, ans, sum_, res_set):
            if i == len(candidates) or sum_ > target:
                return
            item.append(candidates[i])
            # 浅拷贝实现append
            real = item.copy()
            real_ = tuple(real)
            sum_ = sum(real)
            if sum_ == target and real_ not in res_set:
                res_set.add(real_)
                ans.append(real)
            helper(i + 1, item, ans, sum_, res_set)
            sum_ -= candidates[i]
            item.pop()
            helper(i + 1, item, ans, sum_, res_set)

        helper(0, item, ans, 0, res_set)
        return ans
print(Solution().combinationSum2([6,6,4,1,2,3],5))