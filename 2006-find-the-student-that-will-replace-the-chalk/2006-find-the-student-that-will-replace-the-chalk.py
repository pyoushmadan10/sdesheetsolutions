class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        to=sum(chalk)
        remain=k%to
        for si,schk in enumerate(chalk):
            if remain<schk:
                return si
            remain-=schk
        return 0