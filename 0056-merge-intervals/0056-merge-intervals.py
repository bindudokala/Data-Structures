class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x : x[0])
        result = [intervals[0]]
        for item in intervals[1:]:
            if item[0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(item[1], result[-1][1])]
            else:
                result.append(item)
        return result
                   