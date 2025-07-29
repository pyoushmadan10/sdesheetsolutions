from typing import List
class Solution:
    def compute_next_or_positions(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        next_or = [0] * 32 
        max_or_positions = [n - 1] * n 
        max_or = 0
        for i in range(n - 1, -1, -1):
            max_or |= nums[i]
            for b in range(32):
                if (nums[i] >> b) & 1:
                    next_or[b] = i
            furthest = i
            for b in range(32):
                if ((max_or >> b) & 1):
                    furthest = max(furthest, next_or[b])
            max_or_positions[i] = furthest
        return max_or_positions

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        max_or_positions = self.compute_next_or_positions(nums)
        return [max_or_positions[i] - i + 1 for i in range(len(nums))]