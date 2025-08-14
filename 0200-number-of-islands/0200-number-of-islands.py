class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        def bfs(row, col):
            que = deque()
            que.append((row, col))
            visited.add((row, col))
            while que:
                r, c = que.popleft()
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == "1" and (r + dr, c + dc) not in visited:
                        que.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands