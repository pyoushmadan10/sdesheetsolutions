class Solution:
    def punishmentNumber(self, n):
        return sum(i**2 for i in range(1, n + 1) if isPunishment(i * i, i))

@cache 
def isPunishment(split, target):
    if target < 0 or split < target:
        return False
    if split == target:
        return True  
        
    return (
        isPunishment(split // 10, target - split % 10)         
        or isPunishment(split // 100, target - split % 100)     
        or isPunishment(split // 1000, target - split % 1000)   
    )