class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Solution 1 - using a max heap - maintaining the heap size as k as we perform heappush and heappop
        def distance(x, y):
            return (x * x) + (y * y)

        maxHeap = []
        for p in points:
            heapq.heappush(maxHeap, (-distance(p[0], p[1]), p))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [p[1] for p in maxHeap]



        # Solution 2 - using a min heap
        minHeap = []
        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            minHeap.append((dist,point))
        heapq.heapify(minHeap)
        kClosest = []
        while(len(kClosest) < k):
            dist, point = heapq.heappop(minHeap)
            kClosest.append(point)
        return kClosest
      