import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [(-stone) for stone in stones]
        heapq.heapify(maxHeap)
        while(len(maxHeap) > 1):
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, -(y-x))
        return -maxHeap[0] if len(maxHeap) > 0 else 0



'''
💡 Main Idea
• Use a max-heap to efficiently track and retrieve the two heaviest stones in each iteration.

• Since heapq module only supports min-heaps in Python, store the negatives of the stone weights to simulate a max-heap.

• In each iteration:

    • Pop the two largest stones.

    • If their weights differ, push the difference back into the heap (as a negative).

• Continue until one or no stones remain.

• Return the final stone's weight if one exists, otherwise 0.


⏳ Time : O(n log n)
🗂️ Space : O(n)
'''