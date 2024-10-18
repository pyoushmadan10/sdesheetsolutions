class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int maxOr=0; 
        for(int n:nums) maxOr|=n;
        int numberOfBadSubsets = 0;
        for(int mask=maxOr;mask; mask=(mask-1)&maxOr){
            int cnt = 0; 
            for(int n:nums) if(!(n&mask)) cnt++;
            numberOfBadSubsets += (__builtin_popcount(mask)%2 ? 1 : -1)*((1<<cnt)-1); 
        }
        return (1<<nums.size())-1- numberOfBadSubsets;
    }
};