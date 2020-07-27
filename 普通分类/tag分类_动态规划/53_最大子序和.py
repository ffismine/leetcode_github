"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

# 第一次自己手动尝试动归
# dp[i] = max(dp[i-1] + nums[i], dp[i-1], nums[i])


# 第二种解法，其实这题的动归很简单，就是最大值要么是本身，要么是本身和前者加本身
# nums[i] = max(nums[i-1] + nums[i], nums[i])

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_ = len(nums)
        if len_ == 1:
            return nums[0]
        dp = [0] * len_
        dp[0] = max_ = nums[0]
        for i in range(1, len_):
            if dp[i - 1] <= 0:
                # 1 -2 4
                if nums[i] > 0:
                    dp[i] = nums[i]
                # 1 -2 -1
                else:
                    max_ = max(max_, nums[i])
                    continue
            else:
                # 2 -1 3
                if nums[i] > 0:
                    dp[i] = dp[i - 1] + nums[i]
                # 2 -1 -2
                # 3 -1 -1
                else:
                    dp[i] = max(dp[i - 1] + nums[i], 0)

            max_ = max(max_, nums[i], dp[i])

        return max_

    def maxSubArray2(self, nums: List[int]) -> int:
        # 第二种解法，其实这题的动归很简单，就是最大值要么是本身，要么是本身和前者加本身
        # nums[i] = max(nums[i-1] + nums[i], nums[i])

        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])

        return max(nums)


Solution().maxSubArray([-2, -3, -1])
