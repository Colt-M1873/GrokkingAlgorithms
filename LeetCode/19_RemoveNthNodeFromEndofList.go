// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// 2022年07月07日 16:18:15

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func removeNthFromEnd(head *ListNode, n int) *ListNode {
    fast,slow:=head,head
    for n>0 {
        fast=fast.Next
        n--
    }
    if fast==nil{
        return head.Next
    }
    for fast.Next!=nil {
        fast=fast.Next
        slow=slow.Next
    }
    remove:=slow.Next
    slow.Next=remove.Next
    remove.Next=nil
    return head
}