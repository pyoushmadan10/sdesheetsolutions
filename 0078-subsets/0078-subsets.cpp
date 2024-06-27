class Solution {
public:
    void solve(int i,vector<int>&nums,vector<vector<int>> &result,vector<int> &path){
        if(i>=nums.size()){
            result.push_back({path});
            return;
        }
        path.push_back(nums[i]);
        solve(i+1,nums,result,path);
        path.pop_back();
        solve(i+1,nums,result,path);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        solve(0,nums,result,path);
        return result;
    }
};