"""
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。

一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""

"""思考：递归就完事了"""

class Solution:
    def __init__(self):
        self.count = 0
        self.cache = {}

    def translateNum(self, num: int) -> int:
        return self.add_(num)

    def add_(self, num):
        # 前两位小于26，可以继续递归，否则当前位数参与的就是1
        if len(str(num)) > 2:
            if int(str(num)[:2]) > 25:
                if num not in self.cache:
                    self.cache[num] = self.add_(int(str(num)[1:]))
                return self.cache[num]

            else:
                a = int(str(num)[1:])
                b = int(str(num)[2:])
                if a not in self.cache:
                    self.cache[a] = self.add_(a)
                if b not in self.cache:
                    self.cache[b] = self.add_(b)

                return self.cache[a] + self.cache[b]

        return 1 if (num > 25 or len(str(num)) == 1) else (1 if 0 <= num < 10 else 2)


print(Solution().translateNum(12258))
