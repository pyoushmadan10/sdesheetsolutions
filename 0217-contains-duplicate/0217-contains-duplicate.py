class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=list(set(nums))
        if(len(s)<len(nums)):
            return True
        else:
            return False