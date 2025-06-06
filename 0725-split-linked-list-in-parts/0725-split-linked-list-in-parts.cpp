/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
ListNode* curr=head;
        int n=0;
        while(curr){
            curr=curr->next;
            n++;
        }
        auto [q, r]=div(n, k);
        vector<int> iLen(k, q);
        for (int i=0; i<r; i++)
            iLen[i]++;
        vector<ListNode*> ans(k);
        curr=head;
        for(int i=0; i<k; i++){
            ans[i]=curr;
            int j=0;
            ListNode* prev=NULL;//extra pointer is needed
            while(j<iLen[i]){
                prev=curr;
                curr=curr->next;
                j++;
            }
            if (prev)
                prev->next=NULL;//Remove the link
        }
        return ans;
    }
};