class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        checker={i:i for i in "abcdefghijklmnopqrstuvwxyz"}
        def previous(i):
            check=checker[i]
            while check!=i:
                check,i=checker[check],check
            return check
        for i,j in zip(s1,s2):
            i1,j1=previous(i),previous(j)
            checker[max(i1,j1)]=min(i1,j1)
        return "".join(previous(i) for i in baseStr)