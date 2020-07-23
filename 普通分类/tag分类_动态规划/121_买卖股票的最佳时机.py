"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

"""
思考过程：
方法1：只要我在当前最低价的时候卖出，就可以
因此一次遍历：
记录当前股票最低价，然后每次更新股票最低价以及股票利润

方法2：动态规划，
dp[i] = max(dp[i-1], (prices[i] - min_price))

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            profit = max(profit, prices[i] - min_price)

        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            dp[i] = max(dp[i - 1], (prices[i] - min_price))

        return dp[-1]


print(Solution().maxProfit2([7, 1, 5, 3, 6, 4]))
