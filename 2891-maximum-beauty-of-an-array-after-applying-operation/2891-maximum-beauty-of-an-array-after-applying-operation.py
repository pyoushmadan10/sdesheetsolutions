class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_value = max(nums)
        range_array = [0] * (max_value + 10)
        for num in nums:
            left = max(0, num - k)
            right = min(max_value, num + k) + 1
            range_array[left] += 1
            range_array[right] -= 1
        result = range_array[0]
        for i in range(1, len(range_array)):
            range_array[i] += range_array[i - 1]
            if range_array[i] > result:
                result = range_array[i]
        return result