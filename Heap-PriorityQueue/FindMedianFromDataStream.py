import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if(self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0])):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap)) 

    def findMedian(self) -> float:
        if (len(self.minHeap) - len(self.maxHeap)) == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2    
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]        



'''
💡 Main Idea
• Use two heaps to dynamically maintain the lower and upper halves of the data:

• maxHeap (as a min-heap with negated values) for the lower half

• minHeap for the upper half

Steps:

• When a number is added:

    • Push it to maxHeap (as negative).

    • Move the maximum from maxHeap to minHeap if necessary to maintain order i.e., for max of maxHeap is greater than min of minHeap.

    • Balance the sizes so that the difference in their lengths is at most 1.

• Median retrieval:

    • If heaps are balanced: median is the average of the two middle values (tops of both heaps).

    • If one heap is bigger: median is the top of the larger heap.


⏳ Time : O(log n)
🗂️ Space : O(n)
'''