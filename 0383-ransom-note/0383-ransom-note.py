class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        for ch in ransomNote:
            count[ch] += 1
        
        for ch in magazine:
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    del count[ch]
        
        for k in count:
            if count[k] != 0:
                return False
        return True