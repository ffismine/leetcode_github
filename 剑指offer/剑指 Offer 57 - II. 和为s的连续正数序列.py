"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：
1 <= target <= 10^5
"""

# 这题采用滑动窗口解决


from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1
        j = 2
        res = []
        while i <= target / 2:
            if (i + j) * (j - i + 1) / 2 < target:
                j += 1
                continue
            if (i + j) * (j - i + 1) / 2 > target:
                i += 1
                continue
            else:
                res.append([x for x in range(i, j + 1)])
                i += 1

        return res


Solution().findContinuousSequence(3)