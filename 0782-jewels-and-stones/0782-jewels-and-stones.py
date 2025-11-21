class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Using Dictionary
        jewels_dict = defaultdict(int)
        for ch in jewels:
            jewels_dict[ch] = 0
        
        for ch in stones:
            if ch in jewels_dict:
                jewels_dict[ch] += 1
        
        result = 0
        for k in jewels_dict:
            result += jewels_dict[k]
        return result

        # Using Hashset
        jewels_set = set(jewels)
        result = 0
        for ch in stones:
            if ch in jewels_set:
                result += 1
        return result