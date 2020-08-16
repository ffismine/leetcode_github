# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/16 11:09

"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：
0 <= 数组长度 <= 10^5
"""

# 动态规划：
# 当前的最大利润是前面最大利润 和 当前价格减去之前最低价格  之间的最大值

# dp[i] = max(dp[i-1], prices[i] - min[i-1])
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_ = len(prices)
        if len_ == 0:
            return 0
        min_price = prices[0]
        dp = len_ * [0]
        for i in range(len_):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            if prices[i] < min_price:
                min_price = prices[i]

        return dp[-1]


print(Solution().maxProfit([1]))
