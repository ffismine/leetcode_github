# -*- coding:utf-8 -*-

"""
Created on '2021/11/26-15:42'
Author: Xie Zhang
"""

'''
一个严格递增数列是指每个数都严格比前一个数大的一列数。
一个严格递减数列是指每个数都严格比前一个数小的一列数。
一个严格单调数列是指严格递增数列或是严格递减数列。例如1, 5, 6, 10和9, 8, 7, 1  两个数列都是严格单调数列，
而1, 5, 2, 6和1, 2, 2, 3就不是严格单调数列。
给定你一个数列seq，请找到满足严格单调定义的最长连续子数列，并返回其长度

参数： seq
列表
返回值： l, n（l: 满足严格单调定义的最长连续子数列，n: 满足严格单调定义的最长连续子数列的长度）

# str1 str
# 返回值： True/False

# 理解：递归查找 记录临时答案和flag
'''


class Solution(object):
    def __init__(self):
        self.allLen = 0
        self.res = 0

    def conSeq(self, seq):
        self.allLen = len(seq)
        return self.findMaxAddSeq(seq)

    def findMaxAddSeq(self, seq):
        flag = 0
        tempRes = 0
        for i in range(len(seq)):
            if flag < seq[i]:
                flag = seq[i]
                tempRes += 1
                continue
            else:
                break

        if tempRes > self.res:
            self.res = tempRes

        if tempRes < len(seq):
            seq = seq[tempRes:]
            return self.findMaxAddSeq(seq)
        else:
            return self.res


if __name__ == '__main__':
    seq = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 8, 3, 4, 5, 6]
    result = Solution()
    answer = result.conSeq(seq)
    print(answer)
