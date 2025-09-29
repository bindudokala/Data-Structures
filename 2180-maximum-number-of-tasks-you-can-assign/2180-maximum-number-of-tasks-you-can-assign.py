class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        print(tasks, workers)

        # Binary search
        def can_assign(k):
            available = workers[-k:]
            used = [False] * k
            p = pills
            for t in reversed(tasks[:k]):
                idx = bisect.bisect_left(available, t)
                if idx < k:
                    available.pop(idx)
                    k -= 1
                    continue
                if p == 0:
                    return False
                idx = bisect.bisect_left(available, t - strength)
                if idx == len(available):
                    return False
                available.pop(idx)
                p -= 1
                k -= 1
            return True
            
        low, high = 0, min(len(tasks), len(workers))
        best = 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best