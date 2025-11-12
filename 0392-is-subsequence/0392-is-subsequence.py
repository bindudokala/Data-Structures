class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if len(s) > len(t):
        #     return False
        # l1, l2 = 0, 0
        # while l2 < len(t):
        #     if l1 == len(s):
        #         return True
        #     if s[l1] == t[l2]:
        #         l1 += 1
        #     l2 += 1
        # return True if l1 == len(s) else False   

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
