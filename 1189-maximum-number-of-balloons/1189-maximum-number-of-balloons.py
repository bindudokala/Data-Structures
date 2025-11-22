class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        freq = [0] * 26
        for ch in text:
            if ch in s:
                freq[ord(ch) - ord('a')] += 1
        
        return min(freq[ord('b') - ord('a')], freq[ord('a') - ord('a')], freq[ord('l') - ord('a')] // 2, freq[ord('o') - ord('a')] // 2, freq[ord('n') - ord('a')])
