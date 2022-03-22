// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// 2022 3.22

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        // v1 two pointer count length
        ListNode* tmp,*fast=head,*slow=head;
        int length=0;
        while(fast){
            fast=fast->next;
            length++;
        }
        int l2=length-n;
        if(l2==0) {return head->next;}
        while(l2-1>0){
            slow=slow->next;
            l2--;
        }
        tmp=slow->next->next;
        slow->next->next=NULL;
        slow->next=tmp;
        return head;
    }
};