class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive=0
        negative=0
        for i in range(len(nums)):
            if (nums[i])*(-1)>0:
                negative+=1
            elif (nums[i])*(-1)<0:
                positive+=1
            else:
                continue
        return (max(positive,negative))