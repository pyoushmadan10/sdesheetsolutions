class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int maxi=0;
        for(int i=0;i<nums.size();i++){
            maxi=max(maxi,nums[i]);
        }
        int ini=0;
        int end=0;
        int cnt=0;
        long long int ans=0;
        while(end<nums.size()){
            if(nums[end]==maxi ){
                cnt++;
            }
            while(cnt==k){
                ans+=nums.size()-end;
                if(nums[ini]==maxi){
                    cnt--;
                }
                ini++;
            }
           
            end++;

        }
        return ans;
        
    }
};