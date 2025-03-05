class Solution:
    def coloredCells(self, n: int) -> int:
        res=1 + 4 * n * (n-1) // 2
        return res