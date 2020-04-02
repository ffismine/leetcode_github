# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/2 23:59

"""
用两个栈实现一个队列。
队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
"""

'''
思考：这题和232是一样的，都可以从输入和输出两步进行变化。
以输入时变化为例，栈中为[1,2,3,4]栈顶为1，则输出为1234，新加入5，
要想要想输出变为12345，即将5加入栈尾，即可实现题目要求。

题目转换为将新加入元素加入栈尾

因此先将栈中原来元素依次放入临时栈，临时栈变为[4,3,2,1]，再将新元素加入栈[5]，再将临时栈依次入栈，原栈变为[1,2,3,4,5]
'''


class CQueue:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def appendTail(self, value: int) -> None:
        # 原 -> 临时
        while self.stack:
            self.temp_stack.append(self.stack.pop())
        # add value
        self.stack.append(value)
        # 原 <- 临时
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

    def deleteHead(self) -> int:
        if not self.stack: return -1
        return self.stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()