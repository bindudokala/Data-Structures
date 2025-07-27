class Solution:
    # Technique : expand around centers for odd and even lengths of the string
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            # odd length
            sub = self.expandAroundCenter(s, i, i)
            if len(result) < len(sub):
                result = sub

            # even length
            sub = self.expandAroundCenter(s, i, i + 1)
            if len(result) < len(sub):
                result = sub
            
        return result

