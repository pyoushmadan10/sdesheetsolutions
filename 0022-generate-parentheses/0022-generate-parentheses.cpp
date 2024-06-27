void back(vector<string>& result, string current,int left,int right,int n){
    if(current.size()==2*n){
        result.push_back(current);
        return;
    }
    if(left<n){
        back(result,current+'(',left+1,right,n);
    }
    if(right<left){
        back(result,current+")",left,right+1,n);
    }
}
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        back(result,"",0,0,n);
        return result;
    }
};