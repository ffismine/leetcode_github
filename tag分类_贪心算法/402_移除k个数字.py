# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/18 20:43

"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
"""
'''
思考：
数字可能特别大，肯定不能遍历
如果去除一个数字，
以1432219为例，肯定是去除4
原因是因为要优先最高位最小，其实再是后面位最小
即 对于最高位：如果去掉1，432219>1*****，应该保留1
对于次高位，如果去掉4，13****<14****，所以应该去掉4

如果是k
最暴力：对应数字大于下一位数字，则应该把去掉，重复遍历k次
用栈：遍历数字
大于等于栈顶元素，就push进入
小于栈顶元素，就pop栈顶，并且继续比较当前值与栈顶元素
直到栈空或者k==0或者栈顶小于当前元素
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        S = []
        ans = ''
        for i in range(len(num)):
            number = int(num[i])
            while len(S) != 0 and k > 0 and S[-1] > number:
                S.pop()
                k -= 1
            if number != 0 or len(S) != 0:
                S.append(number)
        while len(S) != 0 and k > 0:
            S.pop()
            k -= 1
        for i in range(len(S)):
            ans += str(S[i])

        if ans == '':
            ans = '0'
        return ans


Solution().removeKdigits("1432219", 3)