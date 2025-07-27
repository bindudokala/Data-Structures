class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for current in range(len(nums)):
            if current > max_reachable:
                return False
            max_reachable = max(max_reachable, current + nums[current])
            if max_reachable >= len(nums)-1:
                return True
        return True
            
            

        