# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/11 12:45


"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 
示例 1:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12

解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 


提示：
0 < grid.length <= 200
0 < grid[0].length <= 200
"""

# 思考：这题算是比较简单的动态规划
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


print(Solution().maxValue([[1, 2, 5], [3, 2, 1]]))
