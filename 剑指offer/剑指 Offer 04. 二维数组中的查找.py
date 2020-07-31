"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。


限制：
0 <= n <= 1000
0 <= m <= 1000
"""

# 思考：如果比第一列最后一个小，说明最后一行可以去掉了
# 如果比第一行最后一个小，那么最后一列可以去掉了

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])
        if not n:
            return False
        if m == 1:
            return target in matrix[0]

        def findNum(m0, m1, n0, n1):
            if m0 == m1 and n0 == n1:
                return target == matrix[m0][n0]
            if m0 == m1:
                return target in matrix[m0][n0:n1 + 1]
            if n0 == n1:
                for i in range(m0, m1 + 1):
                    if target == matrix[i][n0]:
                        return True
                return False
            if target < matrix[m1][n0]:
                if target < matrix[m0][n1]:
                    m1 -= 1
                    n1 -= 1
                    return findNum(m0, m1, n0, n1)
                else:
                    m1 -= 1
                    return findNum(m0, m1, n0, n1)
            if target < matrix[m0][n1]:
                n1 -= 1
                return findNum(m0, m1, n0, n1)
            if target > matrix[m1][n0]:
                if target > matrix[m0][n1]:
                    m0 += 1
                    n0 += 1
                    return findNum(m0, m1, n0, n1)
                else:
                    n0 += 1
                    return findNum(m0, m1, n0, n1)
            if target > matrix[m0][n1]:
                m0 += 1
                return findNum(m0, m1, n0, n1)
            if target == matrix[m0][n1] or target == matrix[m1][n0]: return True

        return findNum(0, m - 1, 0, n - 1)


print(Solution().findNumberIn2DArray(
    [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]],
    20))

print(Solution().findNumberIn2DArray([[5, 6, 9], [9, 10, 11], [11, 14, 18]], 9))
