class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        cnt=0
        flag=True
        for i in words:
            flag=True
            for ch in i:
                if ch not in s:
                    flag=False
                    break
            if flag:
                cnt+=1
        return cnt
            
