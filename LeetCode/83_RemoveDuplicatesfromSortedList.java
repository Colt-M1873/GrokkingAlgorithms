// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
// 2022年07月25日 12:47:18

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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummyHead,curr;
        dummyHead=new ListNode(-101,head);
        // System.out.println(dummyHead.next.val);
        curr=dummyHead;
        while (curr!=null && curr.next!=null){
            while (curr.next!=null && curr.next.val==curr.val){
                curr.next=curr.next.next;
            }
            curr=curr.next;
        }
        return dummyHead.next;
    }
}