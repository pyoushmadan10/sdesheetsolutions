class Solution {
public:
    bool check(vector<int>& nums) {
        int si=nums.size();
        int check=0;
        for(int i=1;i<si;i++){
            if(nums[i-1]>nums[i]){
                check++;
            }
        }
        if(nums[si-1]>nums[0]){
            check++;
        }
        if(check<=1){
            return true;
        }
        else{
            return false;
        }
    }
};