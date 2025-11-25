class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        waterTrapped = 0
        # Solution 1
        # while l < r:
        #     if height[l] <= height[r]:
        #         if height[l] >= maxLeft:
        #             maxLeft = height[l]
        #         else:
        #             water += maxLeft - height[l]
        #         l += 1
        #     else:
        #         if height[r] >= maxRight:
        #             maxRight = height[r]
        #         else:
        #             water += height[r]
        #         r -= 1           
        # return waterTrapped

        # Solution 2
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] <= height[r]:  # if maxLeft <= maxRight:
                waterTrapped += maxLeft - height[l]
                l += 1
            else:
                waterTrapped += maxRight - height[r]
                r -= 1
        return waterTrapped