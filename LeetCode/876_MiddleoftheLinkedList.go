// https://leetcode.com/problems/middle-of-the-linked-list/
// 2022年07月07日 16:30:31

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func middleNode(head *ListNode) *ListNode {
    fast,slow:=head,head
    for fast!=nil && fast.Next !=nil {
        fast=fast.Next.Next
        slow=slow.Next
    }
    return slow
}