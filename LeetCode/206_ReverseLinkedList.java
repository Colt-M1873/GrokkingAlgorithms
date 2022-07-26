// https://leetcode.com/problems/reverse-linked-list/submissions/
// 2022年07月25日 12:31:39

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
    public ListNode reverseList(ListNode head) {
        ListNode prev,tmp;
        prev=null;
        while (head != null){
            tmp=head.next;
            head.next=prev;
            prev=head;
            head=tmp;
        }
        // System.out.println(prev);
        return prev;
    }
}