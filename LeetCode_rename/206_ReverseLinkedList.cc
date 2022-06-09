// https://leetcode.com/problems/reverse-linked-list/
// 2022 3.12

// Definition for singly-linked list.
# include <iostream>
# include <stdlib.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // // v1 iterative
        // if(head==NULL){
        //     return NULL;
        // }
        // ListNode* curr=head;
        // ListNode* prev=NULL;
        // ListNode* tmpNext;
        // while(curr!=NULL){
        //     tmpNext=curr->next;
        //     curr->next=prev;
        //     prev=curr;
        //     curr=tmpNext;
        // }
        // return prev;

        //v2 recursive 
        return this->recursion(head,NULL);
    }

    // v2 recursive function
    ListNode* recursion(ListNode* curr,ListNode* prev){
        if(curr==NULL){
            return prev;
        }
        ListNode* tmpNext=curr->next;
        curr->next=prev;
        prev=curr;
        curr=tmpNext;
        return recursion(curr,prev);        
    }

};