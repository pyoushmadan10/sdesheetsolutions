class Solution:
    def isValid(self, s: str) -> bool:
        pair={"(":")","{":"}","[":"]"}
        st=[]
        for ch in s:
            if ch in pair:
                st.append(ch)
            else:
                if not st:
                    return False
                previous=st.pop()
                if pair[previous]!=ch:
                    return False
        return not st