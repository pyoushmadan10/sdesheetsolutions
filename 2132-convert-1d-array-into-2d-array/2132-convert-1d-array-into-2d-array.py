class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        prod=m*n
        si=len(original)
        if prod!=si:
            return []
        for ii in range(0,si,n):
            ans.append(original[ii:ii+n])
        return ans