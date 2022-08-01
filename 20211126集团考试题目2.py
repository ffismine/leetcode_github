# -*- coding:utf-8 -*-

"""
Created on '2021/11/26-15:26'
Author: Xie Zhang
"""

'''
# 给定一个字符串，请编写程序判断，
是否能通过在原字符串任意位置添加一个字母将其变为回文串
（一个正读和反读都一样的字符串，如“level”或者“noon”等等就是回文串）。


# str1 str
# 返回值： True/False


# 理解：等同于去掉一个位置仍然为回文串
'''


class Solution(object):
    def palindrome(self, n1):
        # 如果有一个去掉是回文串则返回True
        for i in range(len(n1)):
            newStr = n1[:i] + n1[i + 1:]
            if self.ispalindrome(newStr):
                return True
        return False

    # 判断回文
    def ispalindrome(self, n1):
        for i in range(len(n1)):
            if n1[i] != n1[len(n1) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    str1 = 'como'
    result = Solution()
    answer = result.palindrome(str1)
    print(answer)
