class Solution {
public:
    void solve(vector<string>&res,string ip,string op){
        if(ip.length()==0){
            res.push_back(op);
            return;
        }
        if(isalpha(ip[0])){
            string op1=op;
            string op2=op;
            op1.push_back(tolower(ip[0]));
            op2.push_back(toupper(ip[0]));
            ip.erase(ip.begin()+0);
            solve(res,ip,op1);
            solve(res,ip,op2);
        }
        else{
            string op3=op;
            op3.push_back(ip[0]);
            ip.erase(ip.begin()+0);
            solve(res,ip,op3);
        }

    }
    vector<string> letterCasePermutation(string s) {
        vector<string> res;
        int n=s.length();
        string ip=s;
        string op="";
        solve(res,ip,op);
        return res;
    }
};