class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mir, mar = rows, 0
        mic, mac = cols, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    mir = min(mir, r)
                    mar = max(mar, r)
                    mic = min(mic, c)
                    mac = max(mac, c)
        width = mac - mic + 1
        height = mar - mir + 1
    
        return width * height