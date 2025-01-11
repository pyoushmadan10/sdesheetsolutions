class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        charCount = [0] * 26
        for c in s:
            charCount[ord(c) - ord('a')] += 1
        oddCount = 0
        for i in range(26):
            if charCount[i] % 2 == 1:
                oddCount += 1
        return oddCount <= k and k <= len(s)