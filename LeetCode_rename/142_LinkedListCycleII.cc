// https://leetcode.com/problems/linked-list-cycle-ii/
// 2022 3.21

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        // v1 two pointer refer to 3.13 note discussion
        ListNode *slow=head, *fast=head;
        while(fast and fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast){
                slow=head;
                int count=0;
                while(slow!=fast){
                    slow=slow->next;
                    fast=fast->next;
                    count++;
                }
                return slow;
            }            
        }
        return NULL;
    }
        // 假设直线部分长s，也就是从第s个节点开始进入环，s是环的起点。
        // 环形周长r
        // 第一次相遇的点距离环起点s的距离设为d，距原点的距离为s+d
        // 假设第一次相遇时候慢已经走了n圈
        // 所以快慢第一次相遇的时候
        // 慢走了 s+nr+d 步
        // 块走了 s+(n+1)r+d 步

        // 假设快的速度是慢的2倍
        // s+(n+1)r+d＝2(s+nr+d)
        // r＝s+nr+d
        // (1-n)r＝s+d
        // n只能是0
        // r＝s+d
        // 所以二者第一次相遇的点s+d到原点的距离也就是r
        // 之后慢指针回原点，快指针从原地继续走
        // 二者同时走s步，也就是r-d步后相遇，
        // 因为慢指针从原点走s就是进环点，
        // 快指针从s+d处开始走，如走r步会回到s+d处，
        // 那么走s＝r-d步时，会走到s处，进环点。
        // 所以两个指针第二次相遇必定是在进环点

};