class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        pres=0
        preind=0
        res=0
        for i in range(len(arr)):
            preind+=i
            pres+=arr[i]
            if preind==pres:
                res+=1
        return res