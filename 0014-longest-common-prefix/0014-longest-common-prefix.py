class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''Meth1 : Sort the array of strings. Compare the first and last strings for the result.     
        Meth2: Find the smallest string length in the strs array and run a loop of the smallest string length through the array and start comparing all the string at the index.'''
        commonPrefix = ""
        minLength = float('inf')
        for s in strs:
            minLength = min(minLength, len(s))
        
        for i in range(minLength):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
        return strs[0][:minLength]    