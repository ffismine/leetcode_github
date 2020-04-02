# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/3 1:15

"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 
限制：
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""

'''
思考：个人感觉可以和栈的最大值一样，实现一个辅助队列
区别在于，栈是先入后出，出栈的时候不影响前面的记录
但是队列不同，先入先出，不进行操作会导致很难记录当前的最大值
根据队列的特点，如果在辅助队列中，入队时检查前面的小元素，如果比现在这个小，那么将其从双向队列去除掉，那么辅助队列也可以记录队列的最大值了。
不过还需要一个出队的时候，比较辅助队列首和当前出队元素，如果一样，辅助队列也出队。

'''


class MaxQueue:

    def __init__(self):
        self.data_queue = []
        self.max_stack = []

    def max_value(self) -> int:
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.data_queue.append(value)
        while self.max_stack and self.max_stack[-1] < value:  # 必须是小于，不能等于！！
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.data_queue:
            return -1
        ans = self.data_queue.pop(0)
        if ans == self.max_stack[0]:
            self.max_stack.pop(0)
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()