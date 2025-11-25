class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        waterTrapped = 0
        # while(l < r):
        #     if maxLeft <= maxRight:
        #         l += 1
        #         waterTrapped += (maxLeft - height[l]) if (maxLeft - height[l]) > 0 else 0
        #         if height[l] > maxLeft:
        #             maxLeft = height[l]
                  
        #     else:
        #         r -= 1
        #         waterTrapped += (maxRight - height[r]) if (maxRight - height[r]) > 0 else 0
        #         if height[r] > maxRight:
        #             maxRight = height[r]
                       
        # return waterTrapped

        while(l < r):
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] <= height[r]:  # if maxLeft <= maxRight:
                waterTrapped += maxLeft - height[l]
                l += 1
            else:
                waterTrapped += maxRight - height[r]
                r -= 1
        return waterTrapped