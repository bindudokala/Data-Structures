class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()
        def backtrack(ind):
            res.append(subset[:])
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return res
  


'''
📌 Main Idea:
The code uses backtracking to generate all possible subsets of a given list of numbers that may contain duplicates, while ensuring no duplicate subsets are included in the result.

To handle duplicates:

The input list is sorted first so that duplicate numbers appear consecutively.

During iteration, the code skips over consecutive duplicate elements at the same recursion level by checking if i > ind and nums[i] == nums[i-1].

At each step:

The current subset is added to the result list.

It iterates through the remaining numbers, decides whether to include each number, and recursively explores further possibilities.

After recursion, it backtracks by removing the last added element to explore other combinations.

* Time Complexity: O(2^N)
* Space Complexity: O(N)
'''