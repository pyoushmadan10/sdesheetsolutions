class Solution:
    def checkValidString(self, s: str) -> bool:
        open=[]
        star=[]
        for idx,ch in enumerate(s):
            if ch=="(":
                open.append(idx)
            elif ch=="*":
                star.append(idx)
            elif ch==")":
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while open and star:
            if open[-1]<star[-1]:
                open.pop()
                star.pop()
            else:
                return False
        return len(open)==0