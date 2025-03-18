class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 1  # Minimum length is 1 (single element is always valid)

        leftIdx = 0  # Left boundary of the sliding window
        usedBits = 0  # Tracks the bits "used" (set to 1) in the current window

        for rightIdx in range(n):  # Right boundary of the sliding window
            # While the new number overlaps with usedBits AND window is non-empty
            while usedBits & nums[rightIdx] != 0 and rightIdx > leftIdx:
                usedBits ^= nums[leftIdx]  # Remove leftmost element's bits
                leftIdx += 1  # Shrink window from the left
            usedBits |= nums[rightIdx]  # Add the current number's bits
            maxLen = max(maxLen, rightIdx - leftIdx + 1)  # Update max length
        
        return maxLen
        