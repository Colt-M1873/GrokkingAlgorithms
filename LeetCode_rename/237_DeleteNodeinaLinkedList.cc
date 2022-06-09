// https://leetcode.com/problems/delete-node-in-a-linked-list/
// 2022 3.22

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        // v1 cheat by changing the value of rest of the node
        // flaw in this question, though value are changed,
        // the memory address of the to-be-deleted-node is not changed
        while(node->next->next){
            node->val=node->next->val;
            node=node->next;
        }
        node->val=node->next->val;
        node->next=NULL; 
    }
};