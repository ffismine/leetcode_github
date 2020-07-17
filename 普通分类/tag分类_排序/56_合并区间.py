"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


"""
思考：一定要栈的尾部数组的右端，大于等于新数组的左端，便可以考虑合并。
首先排序，排序之后有以下情况
1,3  2,4
1,2  1,4
1,3  5,6
明显是第二位和第三位进行比较
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for i in range(len(intervals)):
            if not stack:
                stack.append(intervals[i])

            else:
                a = stack[-1]
                if intervals[i][0] <= a[1]:
                    stack.pop()
                    stack.append([min(a[0], intervals[i][0]), max(a[1], intervals[i][1])])
                else:
                    a = intervals[i]
                    stack.append(a)
        return stack


print(Solution().merge([[3,3],[1,2],[1,10],[15,18]]))
