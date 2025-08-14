class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        islands = 0
        maxArea = 0
        def bfs(row, col):
            que = deque()
            que.append((row, col))
            visited.add((row, col))
            area = 0
            print(area)
            while que:
                r, c = que.popleft()
                area += 1
                dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dir:
                    if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and grid[r + dr][c + dc] == 1 and (r + dr, c + dc) not in visited:
                        que.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            print(area)
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, bfs(row, col))
        
        return maxArea