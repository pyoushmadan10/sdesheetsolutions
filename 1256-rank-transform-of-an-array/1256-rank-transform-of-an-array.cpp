class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int>temp=arr;
        sort(temp.begin(),temp.end());
        unordered_map<int,int>mp;
        int rank=1;
        int n=temp.size();
        for(int i=0;i<n;i++){
            if (mp.find(temp[i])==mp.end()){
                mp[temp[i]]=rank;
                rank++;
            }
        }
        vector<int>res(arr.size());
        for(int i=0;i<arr.size();i++){
            res[i]=mp[arr[i]];
        }
        return res;
    }
};