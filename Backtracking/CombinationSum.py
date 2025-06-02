class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combinations = [], []
        def backtrack(ind):
            if sum(combinations) == target:
                res.append(combinations[:])
                return
            if sum(combinations) - target > 0 or ind == len(candidates):
                return
            combinations.append(candidates[ind])
            backtrack(ind)
            combinations.pop()
            backtrack(ind + 1)
            
        backtrack(0)
        return res



'''
📌 Main Idea:
The code uses backtracking to explore all possible combinations of numbers from the candidates list that sum up to the given target. At each step, it iterates through the available candidates starting from the current index, deciding whether to include a candidate number in the current combination.

It recursively builds combinations by adding numbers to the current list, and whenever the sum matches the target, it adds a copy of the current combination to the result list. If the sum exceeds the target, it stops exploring that path (prunes the branch).

By recursively making these decisions and allowing the same number to be reused (by passing the same index again), it systematically generates all unique combinations that sum up to the target.

* Time Complexity: O(2^N)
* Space Complexity: O(N)
'''