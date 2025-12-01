class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding Window - fixed window size
        if k > len(nums):
            return
        i = 0
        curr_sum = sum(nums[i : k])
        max_sum = curr_sum
        for j in range(k, len(nums)):
            curr_sum += nums[j] - nums[i]
            max_sum = max(max_sum, curr_sum) 
            i += 1
        return max_sum / k