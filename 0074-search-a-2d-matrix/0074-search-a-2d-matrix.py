class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    # Solution 1
        # rows, cols = len(matrix), len(matrix[0])
        # l, r = 0, (rows * cols) - 1
        # if not rows or not cols:
        #     return False
        # while( l <= r):
        #     mid = (l + r) // 2
        #     if matrix[mid // cols][mid % cols] == target:
        #         return True
        #     elif matrix[mid // cols][mid % cols] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return False



        # Solution 2 - Performing binary search on 2D matrix
    
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                return self.search(matrix[mid], target)
        return False
 
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return False