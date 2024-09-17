class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3=s1+" "+s2
        ss3=s3.split(" ")
        freq=Counter(ss3)
        res=[]
        for s,cnt in freq.items():
            if cnt==1:
                res.append(s)
        return res