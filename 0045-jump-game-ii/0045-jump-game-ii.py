class Solution:
    def jump(self, nums: List[int]) -> int:
    # set current maximum reachable index for every position, and update the jumps only when the previous farthest index is reached.
        if len(nums) == 0 or len(nums) == 1:
            return 0
        curr_max = 0
        farthest = 0
        jumps = 0
        for i in range(len(nums)):
            curr_max = max(curr_max, i + nums[i])
            if i == farthest:
                jumps += 1
                farthest = curr_max
                if curr_max >= len(nums) - 1:
                    return jumps
        return jumps
        