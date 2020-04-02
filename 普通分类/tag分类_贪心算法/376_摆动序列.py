# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/17 22:40

"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。
第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。
相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
给定一个整数序列，返回作为摆动序列的最长子序列的长度。
通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:
输入: [1,7,4,9,2,5]  输出: 6
解释: 整个序列均为摆动序列。

示例 2:
输入: [1,17,5,10,13,15,10,5,16,8]  输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

示例 3:
输入: [1,2,3,4,5,6,7,8,9]  输出: 2
"""

'''
思考：这题之所以用贪心，就是看示例2：
1 17 5后面的第4个数字，即10 13 15三个选择一个，构成摇摆序列
其实选择的肯定越大越好，那么后续选择更多一点，因此选择15

所以保留连续递增或者递减的首尾元素，剩下的去除，这样就保留了最大的子序列
'''


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        len_nums = len(nums)
        if len(nums) <= 1:
            return len_nums
        if len(set(nums)) == 1:
            return 1
        else:
            # 1 2 3 2 1 4 3
            # 初始状态为0 上升为1 下降为-1
            status = 0
            ans = 2
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    continue
                else:
                    temp_status = 1 if nums[i] > nums[i-1] else -1
                    if status == 0:
                        status = temp_status
                    elif status != temp_status:
                        status = temp_status
                        ans += 1
        return ans

print(Solution().wiggleMaxLength([1,2,1]))