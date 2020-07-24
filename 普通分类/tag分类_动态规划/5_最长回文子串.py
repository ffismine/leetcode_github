"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""

"""
动态规划： dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
考虑边界条件： j-1 <= i+1 即 
i < j <= i+2
在此边界条件下，相当于i和j之间的数为1个或者0个
因此只需要验证dp[i][j] = s[i] == s[j]

否则 dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_ = len(s)
        if len_ <= 1:
            return s

        dp = [[False for _ in range(len_)] for _ in range(len_)]

        index = 0
        max_len = 1

        # 可以省略，后面蕴含了这一步
        for i in range(len_):
            dp[i][i] = True

        for j in range(1, len_):
            for i in range(j):
                if s[i] == s[j]:
                    if j <= i + 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        index = i

        return s[index:index + max_len]


Solution().longestPalindrome("cbbd")
