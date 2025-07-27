class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        j = 0
        n = len(nums)
        for i in range(1, n - 1):
            if (nums[j] < nums[i] > nums[i + 1]) or (nums[j] > nums[i] < nums[i + 1]):
                cnt += 1
                j = i
        return cnt