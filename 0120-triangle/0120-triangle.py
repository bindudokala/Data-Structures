class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Bottom up dynamic programming approach
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for j in range(len(row)):
                dp[j] = row[j] + min(dp[j], dp[j + 1])
        return dp[0]