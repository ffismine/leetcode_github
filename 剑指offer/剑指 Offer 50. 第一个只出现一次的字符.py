# -*- coding: utf-8 -*-
# Time   : 2020/8/10 10:02
# Author : Zhang Xie

"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：
0 <= s 的长度 <= 50000
"""


# 哈希

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return ' '
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = -1

        for x in d:
            if d[x] >= 0:
                return s[d[x]]

        return ' '


print(Solution().firstUniqChar("leetcode"))
