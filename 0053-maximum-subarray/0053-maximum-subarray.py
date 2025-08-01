class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm - whenever the current sum becomes negative, reset it to 0.
        max_sum, curr_sum = nums[0], 0
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum