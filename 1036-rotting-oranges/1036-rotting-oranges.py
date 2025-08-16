class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        fresh, time = 0, 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    que.append([r, c])
        
        while que and fresh > 0:
            for i in range(len(que)): # One-minute worth of rotting
                r, c = que.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == 1:
                        que.append([r + dr, c + dc])
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
            time += 1 # one minute finishes after current level rotting is done
        
        return time if fresh == 0 else -1
