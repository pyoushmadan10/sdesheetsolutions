class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isValidCap(cap):
            robbed, canRob = 0, True
            for house in nums:
                if not canRob:
                    canRob = True # can't rob house, need to skip and can now rob next
                elif house <= cap:
                    robbed += 1 # can rob house and house less than cap, so rob
                    canRob = False # can't rob next house
            return robbed >= k # if can rob at least k houses, then cap is valid

        posCaps = list(sorted(set(nums))) # sorted list of all possible capacities
        left, right = 0, len(posCaps) - 1 # indices of posCaps

        while left < right: # binary search for lowest posCap[i]
            mid = (left + right) // 2

            if isValidCap(posCaps[mid]):
                right = mid # valid capacity, move right down to look for smaller
            else:
                left = mid + 1 # current capacity can't make k groups, move left up

        # left = right, posCap[left or right] = min capacity that can make k groups
        # posCaps[left - 1] is first capacity that is too small
        return posCaps[left] 