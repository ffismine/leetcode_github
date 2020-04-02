# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/5 15:47

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:  输入: "()"  输出: true
示例 2:  输入: "()[]{}"  输出: true
示例 3:  输入: "(]"  输出: false
示例 4:  输入: "([)]"  输出: false
示例 5:  输入: "{[]}"  输出: true
"""

'''
思考：个人认为难点在于示例4，如果简单的进行三组匹配，那么这个实例就通过不了了。
因此要用栈进行实时更新。
简单来说，遇到左括号入栈，遇到右括号如果符合栈顶，则栈顶出栈。最终栈为空即true。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in dict1:
                stack.append(c)
            elif len(stack) > 0 and dict1[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return len(stack) == 0


print(Solution().isValid('{]}'))

