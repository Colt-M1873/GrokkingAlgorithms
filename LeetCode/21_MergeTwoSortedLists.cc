// https://leetcode.com/problems/merge-two-sorted-lists/
//  2021 11.23 2022 3.10 3.27


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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(not list1) return list2;
        if(not list2) return list1;
        
        ListNode* a, *b, *ret, *tmp;
        if (list1->val<=list2->val){
            a=list1;
            b=list2;
        }else{
            a=list2;
            b=list1;
        }
        ret=a;
        while (a->next){
            if(a->next->val <= b->val){
                a=a->next;
            }else{
                tmp=a->next;
                a->next=b;
                b=tmp;
            }
        }
        a->next=b;
        return ret;

        // // v2 recursive
        // if(not list1)return list2;
        // if(not list2)return list1;
        // ListNode *small=list1,*big=list2;
        // if(list1->val>list2->val){
        //     small=list2;
        //     big=list1;
        // }
        // small->next=mergeTwoLists(small->next,big);
        
        // return small;
        




    }
};