class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Solution 1 - using Bucket Sort
        # eleCount = defaultdict(int)
        # eleFreq = [[] for bd in range(len(nums) + 1)]
        # output = []
        # for ele in nums:
        #     eleCount[ele] += 1
        # for key in eleCount:
        #     eleFreq[eleCount[key]].append(key)
        # for i in range(len(nums), -1, -1):
        #     for val in eleFreq[i]:
        #         if len(output) == k:
        #             return output
        #         output.append(val)
        # return output



        # Solution 2- using min heap - maintaining heap size k while iterating and pushing each value in nums onto heap
        freq = defaultdict(int)
        minHeap = []
        for n in nums:
            freq[n] += 1
        for n in freq:
            heapq.heappush(minHeap, (freq[n], n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [x[1] for x in minHeap]



        # Solution 3 - using min heap
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        minHeap = [(freq[n], n) for n in freq]
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return [x[1] for x in minHeap]
