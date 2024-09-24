from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = defaultdict(int)
        for num in arr1:
            sn1 = str(num)
            for i in range(1, len(sn1)+1):
                prefixes[sn1[:i]] += 1

        res = 0
        for num in arr2:
            sn2 = str(num)
            for i in range(1, len(sn2)+1):
                if sn2[:i] in prefixes:
                    res = max(res, i)
                else:
                    break
        return res