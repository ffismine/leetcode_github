"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1
 
说明:
你可以认为每种硬币的数量是无限的。
"""
from typing import List

# 这题动归要用自下而上的方式
# 而转移方程是当前这个
# dp[i] = min(dp[i-x1],dp[i-x2],...) + 1
# x为coins的值


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # 这里双层循环不容易看出来
        # 不过可以理解为，从0到amount，全部只用1，需要多少。全部只用1和2，需要多少。这是有提升的了。
        # 到了最后一个coin，dp已经很小了，因为很多前面的coin做了优化，这时候在循环一次for x in range(coin, amount + 1):    就可以得到最终答案
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


Solution().coinChange([1, 2, 5], 34)


















