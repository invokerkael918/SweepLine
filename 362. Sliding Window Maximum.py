from collections import deque


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here

        if not nums or not k:
            return []
        dq = deque([])
        for i in range(k - 1):
            self.inQueue(dq, i, nums)

        result = []
        for i in range(k - 1, len(nums)):
            self.inQueue(dq, i, nums)
            result.append(nums[dq[0]])
            if dq[0] == i - k + 1:
                dq.popleft()
        return result

    def inQueue(self, queue, index, nums):
        # if the tail is smaller or equal to me, I kicked them out, I am in
        while (queue and nums[queue[-1]] <= nums[index]):
            queue.pop()
        queue.append(index)
