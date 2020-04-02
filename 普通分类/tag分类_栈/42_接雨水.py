# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/5 16:33

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

"""
import inspect

'''
出于加解法考虑，这题貌似动态规划比较好。
出于简单考虑，可以分列求，暴力解法，见Solution
但是出于栈专题考虑，还是在Solution1里面使用栈解。
'''


# ------------------------------------------------------------------------------------
# 分列求
# 第一列和最后一列免去
# 找出遍历过程每次左边最大值和右边最大值，如果从1开始遍历，那么left_max = height[0]


class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        left_max = height[0]
        right_max = 0
        ans = 0
        for i in range(1, len(height) - 1):
            if height[i] > left_max:
                left_max = height[i]
            right_max = max(height[i + 1:])
            # 先判断左边最大和右边最大
            if height[i] < min(left_max, right_max):
                ans += min(left_max, right_max) - height[i]
        return ans


a = Solution().trap([4,1,0,5,1,4])
print(a)


# ------------------------------------------------------------------------------------

# 栈求   消耗空间少很多

# 栈顶入第一个索引。
# 如果当前height[i]小于或等于height[栈顶索引]，将当前索引入栈，意思是当前的i被栈中的前面的元素界定
# 如果发现当前长于栈顶，可以确定栈顶的索引被当前索引和栈的前面的索引界定，因此我们可以一个个弹出栈顶元素并且累加到ans，直到栈再为空。
# 重复第一步。


class Stack(object):
    """模拟栈"""
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return 0

    def isEmpty(self):
        return len(self.stack) == 0


class Solution1:
    def trap(self, height):
        ans = 0
        current = 0
        st = Stack()
        while current < len(height):
            while (st.isEmpty() is False) and height[current] > height[st.top()]:
                top = st.top()
                st.pop()
                if (st.isEmpty()): break
                distance = current - st.top() - 1
                bounded_height = min(height[current], height[st.top()]) - height[top]
                ans += distance * bounded_height
            st.push(current)
            current += 1
        return ans


aa = Solution1().trap([0,4,0,0,5,1,4])
print(aa)

# ------------------------------------------------------------------------------------
