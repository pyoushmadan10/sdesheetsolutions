class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        val=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    val=(nums[i]-nums[j])*nums[k]
                    ans=max(val,ans)
        return ans