class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, combinations, visited = [], [], []
        def backtrack(ind):
            if sum(combinations) == target:
                res.append(combinations[:])
                return
            if sum(combinations) > target or ind == len(candidates):
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                combinations.append(candidates[i])
                backtrack(i + 1)
                combinations.pop()

        backtrack(0)
        return res



'''
📌 Main Idea:
The code uses backtracking to explore all unique combinations of numbers from the candidates list that sum up to the given target, where each number can be used at most once.

To handle duplicates and avoid repeated combinations:

The candidates are sorted first.

During iteration, the code skips over duplicate numbers at the same recursion level by checking if i > ind and candidates[i] == candidates[i-1].

It recursively builds combinations by adding numbers to the current list, and when the sum equals the target, it adds a copy of the combination to the result list. If the sum exceeds the target or all candidates are considered, it backtracks.
Ex : candidates = [1,1,2,5,6,7,10], target = 8

* Time Complexity: O(2^N)
* Space Complexity: O(N)
'''