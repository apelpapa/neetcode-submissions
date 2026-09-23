class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        rotten_queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten_queue.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        rot_directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while len(rotten_queue) > 0 and fresh > 0:
            for rotten in range(len(rotten_queue)):
                crr, crc = rotten_queue.popleft()
                for tbr, tbc in rot_directions:
                    temp_r = crr + tbr
                    temp_c = crc + tbc
                    if (
                        temp_r < 0
                        or temp_c < 0
                        or temp_r >= len(grid)
                        or temp_c >= len(grid[0])
                        or grid[temp_r][temp_c] != 1
                    ):
                        continue
                    else:
                        rotten_queue.append([crr + tbr, crc + tbc])
                        grid[temp_r][temp_c] = 2
                        fresh -= 1
            time += 1

        if fresh > 0:
            return -1
        return time
