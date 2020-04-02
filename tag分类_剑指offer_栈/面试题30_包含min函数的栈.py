# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/8 2:19


"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 
提示：各函数的调用总次数不超过 20000 次
"""

'''
思考：调用一个数据栈外的最小值栈，两个栈相当于状态一一对应的关系
每次只需要比较栈顶，最小值栈顶记录数据栈的最小值

例如：
数据栈：   [-2, 0, -5, 4]
最小值栈： [-2, -2, -5, -5]
这样哪怕数据栈有元素出栈，最小值栈仍然记录下了最小值。
'''

# 最终结果用时和内存分别打败93%和100%


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.dataStack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        else:
            self.minStack.append(x if x <= self.minStack[-1] else self.minStack[-1])

    def pop(self) -> None:
        if len(self.dataStack) > 0:
            self.dataStack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if len(self.dataStack) > 0:
            return self.dataStack[-1]

    def min(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()