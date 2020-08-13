# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/13 9:24

"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。


示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 
提示：
s.length <= 40000
"""
# 思考：这题我做失败了，但是不影响，看得懂就行。后续复习
# 不要动归理解
# 重点就是哈希表记录索引，tmp记录当前的最大的子串答案，然后和res进行比较

# 之所以默认是 -1 是因为最开始的时候j = 0 取 -1 可以使得tmp + 1



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], 0)  # 获取索引 i
            dic[s[j]] = j  # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res


Solution().lengthOfLongestSubstring("abcaecacab")