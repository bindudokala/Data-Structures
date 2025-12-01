class Solution:
    def search(self, nums: List[int], target: int) -> int:
    # Solution 1 - Binary Search
    # First find minimum of the Rotated Sorted Array
        l, r = 0, len(nums) - 1
        minIndex = 0
        while(l < r):
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        minIndex = l

    # Check where the target is at : left or right sorted part of minimum and set the binary search range to that part
        l, r = 0, len(nums) - 1
        if target >= nums[minIndex] and target <= nums[r]:
            l = minIndex
        else:
            r = minIndex - 1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1



    # Solution 2
        # l, r = 0, len(nums) - 1
        # while(l <= r):
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > nums[r]:
        #         if target < nums[mid] and target >= nums[l]:
        #             r = mid - 1
        #         else:
        #              l = mid + 1
        #     else:
        #         if target > nums[mid] and target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return -1
        