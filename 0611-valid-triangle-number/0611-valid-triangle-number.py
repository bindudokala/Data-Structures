class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        triplets = 0
        nums.sort()
        for k in range(len(nums) - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all the pairs i to j can make triangle
                    triplets += j - i
                    j -= 1
                else:
                    i += 1
        return triplets
                