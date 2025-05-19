class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[2] + nums[0] <= nums[1]:
            return "none"
    
    # Check for equilateral triangle
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
    
    # Check for isosceles triangle
        if nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
            return "isosceles"
    
    # If none of the above conditions are met, it is a scalene triangle
        return "scalene"