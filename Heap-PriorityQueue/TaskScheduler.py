import heapq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        maxHeap, q, time = [], [], 0
        for t in tasks:
            freq[t] += 1
        for task in freq:
            maxHeap.append(-freq[task])
        heapq.heapify(maxHeap)
        while(maxHeap or q):
            time += 1
            if maxHeap:
                rem = heapq.heappop(maxHeap) + 1
                if rem != 0:
                    q.append([rem, time + n])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.pop(0)[0])
        return time



'''
💡 Main Idea
• Count the frequency of each task using a dictionary.

• Use a max-heap (by storing negative frequencies) to always schedule the task with the highest remaining count.

• Use a queue q to keep track of tasks in their cooldown period:

    • Each queue entry stores the remaining count and the time when it becomes available again (time + n).

• In each CPU interval unit of time:

    • Increment time.

    • If the heap isn't empty, run the task with the highest count.

    • If that task still has remaining counts, add it to the cooldown queue with its available time.

    • If any task in the queue is ready (its cooldown is over), push it back into the heap.

    • Repeat until both the heap and queue are empty.

• Return the total time taken.


⏳ Time : O(n log n)
🗂️ Space : O(n)
'''