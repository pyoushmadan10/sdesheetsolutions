class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix)==1:
            return matrix[0][0]
        n=len(matrix)
        # dp=[[0]*n for i in range(n)]
        # dp=matrix.copy()
        for i in range(n-2,-1,-1):
            for j in range(n):
                mini=matrix[i+1][j]
                if j>0:
                    mini=min(mini,matrix[i+1][j-1])
                if j<n-1:
                    mini=min(mini,matrix[i+1][j+1])
                matrix[i][j]+=mini
        result=float('inf')
        for num in matrix[0]:
            result=min(result,num)
        return result
