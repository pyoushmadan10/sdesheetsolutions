class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(num):
            c = 0
            for i in range(31, -1, -1):
                temp=(num >> i)
                if (temp & 1) == 1:
                    c += 1
            return c

        def check(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        count = [count_set_bits(i) for i in nums]
        k = 0

        while k < len(nums):
            for i in range(1, len(nums)):
                if count[i] == count[i - 1] and nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

            if check(nums):
                return True

            k += 1

        return False
        