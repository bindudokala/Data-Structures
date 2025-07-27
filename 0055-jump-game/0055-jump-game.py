class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from the end of the array, for every index check whether we can reach the goal from the particular index. if yes change the goal to current index.
        goal = len(nums) - 1 
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return True if goal == 0 else False
 
 # Test case [2, 0, 0]