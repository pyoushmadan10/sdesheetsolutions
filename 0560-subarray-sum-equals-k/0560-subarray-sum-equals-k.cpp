class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int,int>m1;
        m1[0]=1;
        int curr=0,res=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            curr+=nums[i];
            int diff=curr-k;
            if(m1.find(diff)!=m1.end()){
                res+=m1[diff];
            }
            m1[curr]++;
        }
        return res;
    }
};