class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 1 - using 2-pointer approach
        output = []
        i, j = 0, len( nums) - 1
        while i <= j:
            if abs(nums[j]) > abs(nums[i]):
                output.insert(0, nums[j] * nums[j])
                j -= 1
            else:
                output.insert(0, nums[i] * nums[i])
                i += 1
        return output

        # Solution 2 - using sort method
        # output = []
        # nums.sort(key = lambda n : abs(n))
        # for i in range(len(nums)):
        #     output.append(nums[i] * nums[i])
        # return output