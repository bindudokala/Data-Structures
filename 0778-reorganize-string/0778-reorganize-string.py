class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        maxHeap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(maxHeap)
        res = ""
        prev = [0, ""]
        while maxHeap:
            x, y = heapq.heappop(maxHeap)
            res += y
            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)
            prev = (x + 1, y)
        return res if len(res) == len(s) else ""

