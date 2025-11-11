class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(min(len(word1), len(word2))):
            merged.append(word1[i])
            merged.append(word2[i])
        if len(word1) > len(word2):
            merged.append(word1[len(word2):])
        if len(word2) > len(word1):
            merged.append(word2[len(word1):])
        return "".join(merged)