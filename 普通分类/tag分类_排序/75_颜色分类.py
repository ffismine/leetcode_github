"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

# 把所有的2移动到后面。所有的0移到前面
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        荷兰三色旗问题解
        '''
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        f0 = cur = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        f2 = len(nums) - 1

        while cur <= f2:
            if nums[cur] == 0:
                nums[cur], nums[f0] = nums[f0], nums[cur]
                f0 += 1

            if nums[cur] == 2:
                nums[cur], nums[f2] = nums[f2], nums[cur]
                f2 -= 1

            else:
                cur += 1


Solution().sortColors([2, 0, 1])
