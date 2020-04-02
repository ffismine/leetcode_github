# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/4 23:51

"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


'''
思考：
在入过程做改进：
这题画图还是很快的，假设栈和队列的出栈是一模一样的，那么在入栈时进行处理（push），而出栈就是一样的操作就行了。
对于同样的pop顺序54321，加入6时，栈的pop顺序为654321，而队列为543216，因此这题本质上转换为了：在push过程中将543216转换为654321的过程，即除去最后一位（push进来的）,剩下的元素逆序。
用python语法可以写为：

        for i in range(0,q_length-1):
            self.q.append(self.q.pop(0))
            
当然，也可以增加临时队列实现
'''



class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        q_length = len(self.q)
        for i in range(0,q_length-1):
            self.q.append(self.q.pop(0))  # 除去最后一位（push进来的）,剩下的元素逆序

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.q)


# -----------------------------------------------------------------
# 临时队列实现


class MyStack1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []


    def push(self, x: int) -> None:
        temp_queue = []
        temp_queue.append(x)
        for i in range(len(self.q)):
            temp_queue.append(self.q[0])
            self.q.pop(0)
        for i in range(len(temp_queue)):
            self.q.append(temp_queue[0])
            temp_queue.pop(0)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.q)


# -----------------------------------------------------------------
a = MyStack()
a.q = [5,4,3,2,1]
b = MyStack1()
b.q = [5,4,3,2,1]

a.push(6)
a.push(7)
b.push(6)
b.push(7)

print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())

print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
