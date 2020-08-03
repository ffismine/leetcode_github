"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0
"""



from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        len_ = len(numbers)
        if len_ == 0:
            return
        if len_ == 1:
            return numbers[0]

        temp = numbers[0]
        for i in range(1, len_):
            if numbers[i] >= temp:
                temp = numbers[i]

            else:
                return numbers[i]

        return numbers[0]


# 二分法牛笔
class Solution1:
    def minArray(self, numsber: List[int]) -> int:
        l, r = 0, len(numsber) - 1
        while l<r:
            m = (l+r)//2
            if numsber[m]>numsber[r]:
                l = m+1
            elif numsber[r]>numsber[m]:
                r = m
            else:
                r -= 1
        return numsber[l]


