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
 

提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k or k < 1:
            return []

        res = []
        queue = []
        for i in range(len(nums)):
            # 在队列不为空的情况下，如果队列尾部的元素要比当前的元素小，或等于当前的元素
            # 那么为了维持从大到小的原则，我必须让尾部元素弹出
            while len(queue) != 0 and nums[queue[-1]] <= nums[i]:
                queue.pop()

            # 不走 while 的话，说明正常在队列尾部添加元素
            queue.append(i)

            # 如果滑动窗口已经略过了队列中头部的元素，则将头部元素弹出
            if queue[0] == i - k:
                queue.pop(0)

            # 看看窗口有没有形成，只有形成了大小为 k 的窗口，才能收集窗口内的最大值
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res


print(Solution().maxSlidingWindow([1, 3, -1, -3, 2, 3, 6, 7], 3))
