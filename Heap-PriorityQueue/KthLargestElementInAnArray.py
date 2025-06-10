import heapq
class Solution:
    # Solution 1 - using max heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        return -heapq.heappop(maxHeap)

'''
💡 Main Idea
• Use a max-heap to efficiently retrieve the largest elements.

• Since heapq is a min-heap in Python, insert negative values of the numbers to simulate a max-heap.

• Heapify the array (as negatives).

• Pop the largest element (k-1 times) from the heap.

• The next element popped will be the kth largest element in the original array.

• Return its absolute value (negating the popped result).


⏳ Time : O(n + k log n)
🗂️ Space : O(n)
'''


class Solution:
    # Solution 2 - using min heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]


class Solution:
    # Solution 3 - Quick Select - getting time limit exceeded for k = 50000
    def partition(self, nums, l, r):
        pivot_index = random.randint(l, r)
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(low, high):
            pivot = self.partition(nums, low, high)
            if pivot == len(nums) - k:
                return nums[pivot]
            elif pivot > len(nums) - k:
                return quickSelect(low, pivot - 1)
            else:
                return quickSelect(pivot + 1, high)
        return quickSelect(0, len(nums) - 1)

'''
💡 Main Idea:
• Use the QuickSelect algorithm, an efficient selection algorithm based on the partitioning logic of QuickSort:

    • Randomly pick a pivot and partition the array such that:

    • Elements less than or equal to the pivot move to its left.

    • Elements greater move to its right.

• After partitioning, check the position of the pivot:

    • If it’s at len(nums) - k, that’s the kth largest element — return it.

    • If it's greater, recursively search in the left half.

    • If it's smaller, recursively search in the right half.

• This avoids fully sorting the array, achieving better average performance.


⏳ Time : Avg - O(n), Worst - O(n^2)
🗂️ Space : Avg - O(log n), Worst - O(n)
'''