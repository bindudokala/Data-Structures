import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while(len(self.minHeap) > k):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]



'''
💡 Main Idea
The core idea is to maintain a min-heap of size k to track the k largest elements seen so far:

• On initialization, we heapify the given list and reduce its size to k by popping the smallest elements.

• Each time a new number is added:

    • Push it into the heap.

    • If the heap size exceeds k, remove the smallest element.

    • The top of the heap (index 0) will always hold the kth largest element.

By maintaining a heap of only k elements, we avoid sorting or storing the entire stream, optimizing for both time and space.


⏳ Time : O(n log n + m log k)
🗂️ Space : O(k)
'''
