class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return '0'
        req=(1<<n)-1
        mid=req//2+1
        if k==mid:
            return '1'
        if k<mid:
            return self.findKthBit(n-1,k)
        return '1' if self.findKthBit(n-1,req-k+1)=='0' else '0'
        