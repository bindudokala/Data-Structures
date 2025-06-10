import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            minHeap.append((dist,point))
        heapq.heapify(minHeap)
        kClosest = []
        print(minHeap, kClosest)
        while(len(kClosest) < k):
            dist, point = heapq.heappop(minHeap)
            kClosest.append(point)
        return kClosest



'''
💡 Main Idea
• Use a min-heap to keep track of points based on their distance from the origin.

• For each point:

    • Compute the squared Euclidean distance (since we only care about relative distances — no need to take the square root).

    • Push a tuple of (distance, point) into a list.

• Convert the list into a min-heap using heapq.heapify().

• Pop the top (smallest distance) k elements from the heap and collect their corresponding points into the result list.

• Return the result list.


⏳ Time : O(n + k log n)
🗂️ Space : O(n)
'''