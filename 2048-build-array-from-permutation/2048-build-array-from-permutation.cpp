class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            int p=n*(nums[nums[i]]%n);
            nums[i]+=p;
        }
        for(int i=0;i<n;i++){
            nums[i]/=n;
        }
        return nums;
    }
};