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
    int gcd(int a,int b){
        if(b==0){
            return a;
        }
        else{
            return gcd(b,a%b);
        }
    }
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
            ListNode* curr=head;
            while(curr->next!=NULL){
            ListNode* ncurr=curr->next;
            int pre=curr->val;
            int ne=ncurr->val;
            ListNode* newNode=new ListNode(gcd(pre,ne));
            curr->next=newNode;
            newNode->next=ncurr;
            curr=curr->next->next;
            
        
        }
        return head;
    }
};