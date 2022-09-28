// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// 2022年09月28日 22:47:11

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummyhead=new ListNode(-1);
        dummyhead.next=head;
        ListNode fast=dummyhead,slow=dummyhead;
        for (;n>=0;n--){
            fast=fast.next;
        }
        while(fast!=null){
            slow=slow.next;
            fast=fast.next;
        }
        ListNode tmpNext=slow.next.next;
        slow.next.next=null;
        slow.next=tmpNext;
        return dummyhead.next;
    }
}