class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nesw = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(row, col):
            visiting = deque()
            visited.add((row, col))
            visiting.append((row, col))

            while visiting:
                r, c = visiting.popleft()
                for dr, dc in nesw:
                    row = r + dr
                    col = c + dc
                    if (
                        row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == "1"
                        and (row, col) not in visited
                    ):
                        visiting.append((row, col))
                        visited.add((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands