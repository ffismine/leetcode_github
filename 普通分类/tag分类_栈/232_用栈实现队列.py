# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/7 2:00

"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明:
你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""

'''
思考：和225题基本一样。如果入栈时为12345，队列也是12345。
添加新元素6，出栈为654321，队列却为123456。
因此这题可以转换为在出栈时将654321转换为123456的过程。
很简单，出栈之前，添加一个新栈，654321进新栈，再由新栈出栈，便成为了654321

'''

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):    # 进栈
        self.stack.append(value)

    def pop(self):  #出栈
        if self.stack:
            self.stack.pop()

    def is_empty(self): # 如果栈为空
        return len(self.stack) == 0

    def top(self):
        #取出目前stack中最新的元素
        return self.stack[-1]


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sk1 = Stack()
        self.sk2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.sk1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #if len(self.sk2.stack) == 0:
        if self.sk2.is_empty():
            for i in range(len(self.sk1.stack)):
                self.sk2.push(self.sk1.top())
                self.sk1.pop()
        a = self.sk2.top()
        self.sk2.pop()
        return a


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.sk1.stack) == 0:
            if len(self.sk2.stack) > 0:
                return self.sk2.stack[-1]
        else:return self.sk1.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.sk2.stack) <= 0 if len(self.sk1.stack) == 0 else False




a = MyQueue()

a.push(2)
a.push(3)
print(a.pop())
a.push(4)
a.push(5)


print(a.pop())
print(a.peek())
print(a.empty())

