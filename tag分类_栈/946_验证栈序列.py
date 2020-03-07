# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/8 3:01

"""
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，
只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

"""

'''
思考：重点在于理解元素入栈后可以 停留 或者 立即出栈
所以说可以45321，但是43512不可能

拿测试序列和12456同步比较，模拟入栈过程

例如 32541 和 12345
过程如下：
测试序列第1个为3：1入栈 - 2入栈 - 3入栈 - 3出栈 
测试序列第2个为2: 2出栈
测试序列第3个为5: 4入栈 - 5入栈 - 5出栈
测试序列第4个为4: 4出栈
测试序列第5个为1: 1出栈
最终栈空
符合！

43512 和 12345
过程如下：
测试序列第1个为4：1入栈 - 2入栈 - 3入栈 - 4入栈 - 4出栈 
测试序列第2个为3: 3出栈
测试序列第3个为5: 5入栈 - 5出栈
测试序列第4个为1: 1无法出栈，还有2在栈头
最终栈不空
不符合！
'''


class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()
        return len(stack) == 0


a = Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])

print(a)

