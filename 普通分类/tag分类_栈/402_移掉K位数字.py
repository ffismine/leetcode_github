"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
示例 1 :

输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :

输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :

输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
"""


# 这题可以利用栈或者队列，在入口处做文章，以栈为例
# 第一个进入4，第二个进入3，那么就丢弃第一个，即丢弃其左边的那个数字，以此下去，直到丢弃k个数字为止

# 不过也要考虑特殊情况，如果是一个递增的，那么最终没有丢弃，因此选择截取前（n-k）个留下
# 另一种特殊情况是相等，其实不用管就行
# 另一种特殊情况，开头是0，比如10200除去1，结果是200


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        temp = 0
        stack.append(num[0])
        for s in num[1:]:
            while stack and s < stack[-1] and temp < k:
                stack.pop()
                temp += 1
            stack.append(s)
        stack = stack[:len(num) - k]
        return ''.join(stack).lstrip('0') or '0'


print(Solution().removeKdigits("10", 1))
print(Solution().removeKdigits("10200", 1))
print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("1222219", 3))

