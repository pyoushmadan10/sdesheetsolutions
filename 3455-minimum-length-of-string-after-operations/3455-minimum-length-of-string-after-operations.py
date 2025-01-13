class Solution:
    from collections import defaultdict
    def minimumLength(self, s: str) -> int:
        res=len(s)
        dict={}
        for i in s:
            dict[i]=dict.get(i,0)+1
            if dict[i]>2:
                dict[i]=1
                res-=2
        return res