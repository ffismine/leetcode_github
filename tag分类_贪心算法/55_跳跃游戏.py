# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/18 0:11

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4] 输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4] 输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""

'''
思考：重点在于 最多可跳跃nums[i]
例如[2 3 1 1 4]
第0位置可以跳跃到第1或者第2
第1位置可以2 3 4
第2位置可以3
无法选择


因为可以跳的最远的位置之前的所有位置都可以到达
所以只需要当前位置能够达到，并且当前位置+跳数>最远位置，就可以更新最远位置

最后只需要比较最远位置和数组长度就可以了
'''


class Solution:
    def canJump(self, nums) -> bool:
        len_nums = len(nums)
        index = []
        for i in range(len(nums)):
            index.append(i + nums[i])

        jump_index = 0
        max_jump = index[0]
        # 只需要当前位置能够达到
        while jump_index < len_nums and jump_index <= max_jump:
            # 当前位置+跳数>最远位置，更新最远位置
            if index[jump_index] > max_jump:
                max_jump = index[jump_index]
            jump_index += 1
        if jump_index == len_nums:
            return True
        return False


a = Solution().canJump([3,2,1,0,4])
print(a)

