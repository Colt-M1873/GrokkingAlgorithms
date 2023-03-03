// https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 2023年03月03日 11:46:06

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        ListNode last = new ListNode();
        if (head == null) {
            return new int[] {};
        }
        ListNode next = head.next;
        int count = 0;
        while (head != null) {
            count++;
            next = head.next;
            head.next = last;
            last = head;
            head = next;
        }
        // System.out.println(count);
        int[] ret = new int[count];
        int i = 0;
        while (last.next != null) {
            ret[i] = last.val;
            last = last.next;
            i++;
        }
        return ret;
    }
}