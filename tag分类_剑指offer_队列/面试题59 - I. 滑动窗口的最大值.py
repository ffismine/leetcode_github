# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/3 0:20

"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""

'''
思考：

解法1:
首先按照len(nums)/k+1 将原数组分为这么多块，
left：从左至右实现一个保存每个块内部按照原索引检索的最大值数组
right：从右至左实现一个保存每个块内部按照原索引检索的最大值数组
以[1,3,-1,-3,5,3,6,7]为例
left = [1,3,3,-3,5,5,6,7]
right = [3,3,-1,5,5,3,7,7]
考虑从下标i到下标j的滑动窗口，那么:
right[i]是左侧块内的最大元素，left[j]是右侧块内的最大元素。因此滑动窗口中的最大元素为max(right[i], left[j])

解法2：

'''


class Solution:
    def maxSlidingWindow(self, nums, k: 'int'):
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        # 定义初始元素
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else: # 记录最后那个较小的block内的left数组值
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            # i+j == n-1
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


# 有点难
class Solution1:
    def maxSlidingWindow(self, nums, k: int):
        deque = []
        res = []

        for i in range(len(nums)):

            # 如果相距超过窗口k长度则弃掉
            while deque and deque[0] <= i - k:
                deque.pop(0)

            # 只存有可能成为最大值的数字的index进deque
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)

            # 这过程中始终保持deque[0]为最大值的index
            if i >= k-1:
                res.append(nums[deque[0]])

        return res


Solution().maxSlidingWindow([1,6,-1,-3,5,3,6,7],3)
Solution1().maxSlidingWindow([1,6,-1,-3,5,3,6,7],3)