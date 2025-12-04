class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    # Solution 1 - Sliding window dynamic size
        n1, n2 = len(s1), len(s2)
        freq1 = [0] * 26
        freq2 = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(n1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        if freq1 == freq2:
            return True
        
        for j in range(n1, n2):
            freq2[ord(s2[j]) - ord('a')] += 1
            freq2[ord(s2[j - n1]) - ord('a')] -= 1
            if freq1 == freq2:
                return True
        return False



    # Solution 2 - match variable
        # if len(s1) > len(s2):
        #     return False
        # s1Count = [0] * 26
        # s2Count = [0] * 26

        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord('a')] += 1
        #     s2Count[ord(s2[i]) - ord('a')] += 1
        
        # l, matches = 0, 0
        # for i in range(26):
        #     matches += (1 if s1Count[i] == s2Count[i] else 0)

        # for r in range(len(s1), len(s2)):
        #     if matches == 26:
        #         return True

        #     rIndx = ord(s2[r]) - ord('a')
        #     s2Count[rIndx] += 1
        #     if s1Count[rIndx] == s2Count[rIndx]:
        #         matches += 1
        #     elif s1Count[rIndx] + 1 == s2Count[rIndx]:
        #         matches -= 1
            
        #     lIndx = ord(s2[l]) - ord('a')
        #     s2Count[lIndx] -= 1
        #     if s1Count[lIndx] == s2Count[lIndx]:
        #         matches += 1
        #     elif s1Count[lIndx] - 1 == s2Count[lIndx]:
        #         matches -= 1
        #     l += 1
        # return True if matches ==26 else False

        


    # Solution 3 - Backtracking (Time limit exceeded)
        # def permutations(s1, indx, result):
        #     if indx == len(s1):
        #         result.add("".join(s1))
        #         return
        #     for i in range(indx, len(s1)):
        #         s1[indx], s1[i] = s1[i], s1[indx]
        #         permutations(s1, indx + 1, result)
        #         s1[indx], s1[i] = s1[i], s1[indx]
        
        # result = set()
        # permutations(list(s1), 0, result)
        # for p in result:
        #     if p in s2:
        #         return True
        # return False
        