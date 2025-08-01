class Solution {
public:
    vector<int> grow(int row){
         vector<int> v;       //function for storing each row elements
        int n=row;   
        v.push_back(1);
        for(long i=1;i<n;i++){
            v.push_back((v[i-1]*(n-i))/i);        
        }
        return v;   
    }
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> a;         // function to store each row
        for(int i=1;i<=numRows;i++){
            a.push_back(grow(i));
        }
        return a;
    }
};