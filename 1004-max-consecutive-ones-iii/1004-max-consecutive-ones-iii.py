class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window - dynamic size window
        i, j = 0, 0
        longest, flipped = 0, k
        while j < len(nums):
            if nums[j] == 0:
                flipped -= 1
            while flipped < 0:
                if nums[i] == 0:
                    flipped += 1
                i += 1
            longest = max(longest, j - i + 1)     
            j += 1

        return longest