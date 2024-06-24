def solve(arr):
    n = len(arr)
    prev = arr[0]
    prev2 = 0

    for i in range(1, n):
        pick = arr[i]
        if i > 1:
            pick += prev2
        nonPick = 0 + prev

        cur_i = max(pick, nonPick)
        prev2 = prev
        prev = cur_i

    return prev
class Solution:
    def rob(self, nums: List[int]) -> int:
        arr1=[]
        arr2=[]
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(n):
            if i!=0:
                arr1.append(nums[i])
            if i!=n-1:
                arr2.append(nums[i])
        res1=solve(arr1)
        res2=solve(arr2)
        return max(res1,res2)