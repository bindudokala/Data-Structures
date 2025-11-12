class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        minLength = float('inf')
        for s in strs:
            minLength = min(minLength, len(s))
        
        for i in range(minLength):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
        return strs[:i]    