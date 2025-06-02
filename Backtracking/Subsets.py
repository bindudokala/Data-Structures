class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, res = [], []

        def backtrack(ind):
            res.append(subset[:])
            
            for i in range(ind, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        # def backtrack(ind):
        #     if ind == len(nums):
        #         res.append(subset[:])
        #         return
            
        #     subset.append(nums[ind])
        #     backtrack(ind + 1)
        #     subset.pop()
        #     backtrack(ind + 1)
        
        
        backtrack(0)
        return res         
        


'''
📌 Main Idea:
The code uses backtracking to explore all possible combinations (subsets) of a given list of numbers. At each step, it iterates through the remaining elements starting from the current index, deciding whether to include each element in the current subset. It recursively builds up all possible subsets by adding the current subset to the final result at every recursion level.

By recursively making these include/exclude decisions for each element and backtracking after each choice (removing the last added element), it systematically generates the power set (all subsets) of the input list.

* Time Complexity: O(2^N)
* Space Complexity: O(N)
'''