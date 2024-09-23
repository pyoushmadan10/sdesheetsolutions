class Node{
private:
    Node * links[26];
    bool wordEnd = false;
public:
    bool isNull(int ind){
        return links[ind] == NULL;
    }
    void put(int ind,Node * node){
        links[ind] = node;
    }
    Node* get(int ind){
        return links[ind];
    }
    void setEnd(){
        wordEnd = true;
    }
    void unSetEnd(){
        wordEnd = false;
    }
    bool isEnd(){
        return wordEnd;
    }
};

class Solution {
private:
    Node * root;
public:
    Solution(){
        root = new Node();
    }
    void insertInTrie(vector<string>& dictionary){
        for(string & str : dictionary){
            Node * temp = root;
            for(char ch : str){
                int ind = ch - 'a';
                if(temp -> isNull(ind)){
                    temp -> put(ind,new Node());
                }
                temp = temp->get(ind);
            }
            temp->setEnd();
        }
    }
    int minExtraChar(string s, vector<string>& dictionary) {
        insertInTrie(dictionary);
        int n = s.size();
        vector<int> dp(n+1,n);
        dp[0] = 0;
        for(int i = 0; i<s.size();i++){
            Node * temp = root;
            for(int j=i; j<n; j++){
                int ind=s[j]-'a';
                if(temp->isNull(ind)){
                    break;
                }

                temp = temp->get(ind);

                if(temp->isEnd()){
                    dp[j+1] = min(dp[j+1],dp[i]);
                }
            }
            dp[i+1] = min(dp[i+1],dp[i]+1);
        }
        return dp[n];
    }
};