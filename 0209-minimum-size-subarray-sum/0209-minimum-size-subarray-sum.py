class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window - Dynamic window size
        i, currSum = 0, 0
        minSubarray = float('inf')
        for j in range(len(nums)):
            currSum += nums[j]            
            while currSum >= target:
                minSubarray = min(minSubarray, j - i + 1)
                currSum -= nums[i]
                i += 1
        return minSubarray if minSubarray != float('inf') else 0