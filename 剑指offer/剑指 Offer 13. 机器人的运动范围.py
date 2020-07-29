"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1
提示：
1 <= n,m <= 100
0 <= k <= 20

"""

"""
思考：
如果[i-1, j]或者[i, j-1]可以，并且i和j满足条件，那么便可以加入该坐标
"""


def sum_(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = {(0, 0)}
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in res or (i, j - 1) in res) and (sum_(i) + sum_(j) <= k):
                    res.add((i, j))
        return len(res)


