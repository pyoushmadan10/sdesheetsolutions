from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0

        # Check each bit position up to 32 bits
        for bit in range(32):
            count = 0

            # Count how many numbers have the current bit set
            for num in candidates:
                if (num & (1 << bit)) != 0:
                    count += 1

            # Update max_count to store the maximum count of numbers with the same bit set
            max_count = max(max_count, count)

        return max_count