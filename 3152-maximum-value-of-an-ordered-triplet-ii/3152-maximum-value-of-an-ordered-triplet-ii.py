class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        if n==3:
            return max(0,(nums[0]-nums[1])*nums[2])
        pre=[0]*n
        su=[0]*n
        maxi=-1
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        su[n-1]=nums[n-1]
        for j in range(n-2,-1,-1):
            su[j]=max(su[j+1],nums[j])
        ans=0
        it=1
        while(it<n-1):
            temp=(pre[it-1]-nums[it])
            temp2=temp*su[it+1]
            ans=max(ans,temp2)
            it+=1
        return ans