def sumi(n):
    sum1 = 0
    while(n > 0):
        sum1+=int(n % 10)
        n=int(n/10)
    return sum1 
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low,high+1):
            temp=i
            digi=math.floor(math.log10(temp)+1)
            if(digi%2!=0):
                continue
            temp2=digi//2
            divi=math.pow(10,temp2)
            half1=i//divi
            half2=i%(divi)
            if(sumi(half1)==sumi(half2)):
                res+=1
        return res
            