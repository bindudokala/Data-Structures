class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(ind):
            if ind == len(nums):
                res.append(nums[:])
                return
            for i in range(ind, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]
                backtrack(ind + 1)
                nums[ind], nums[i] = nums[i], nums[ind]
        backtrack(0)
        return res
    


    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     res, permutation, visited = [], [], [False] * len(nums)
    #     def backtrack(ind):
    #         if len(permutation) == len(nums):
    #             res.append(permutation[:])
    #             return
    #         for i in range(len(nums)):
    #             if visited[i]:
    #                 continue
    #             visited[i] = True
    #             permutation.append(nums[i])
    #             backtrack(i + 1)
    #             permutation.pop()
    #             visited[i] = False
    #     backtrack(0)
    #     return res



'''
📌 Main Idea:
The code uses backtracking with in-place swapping to generate all possible permutations of a given list of numbers.

At each step, it iterates through the available numbers starting from the current index, and:

Swaps the current element with each possible candidate.

Recursively generates permutations for the remaining elements.

Backtracks by swapping the elements back to their original positions after the recursive call.

When the current index reaches the end of the list (ind == len(nums)), a complete permutation is formed and added to the result list.

* Time Complexity: O(N!)
* Space Complexity: O(N)
'''