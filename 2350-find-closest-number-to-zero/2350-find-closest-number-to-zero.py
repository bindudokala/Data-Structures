class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for n in nums:
            if n == 0:
                return 0
            if n < 0 and abs(n) < abs(result):
                result = n
            elif n > 0 and n <= abs(result):
                result = n

        return result