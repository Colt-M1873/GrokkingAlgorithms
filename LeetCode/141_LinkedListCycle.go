// https://leetcode.com/problems/linked-list-cycle/
// 2022年07月24日 22:29:01

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func hasCycle(head *ListNode) bool {
    // v1
    slow,fast:=head,head
    for fast!=nil && fast.Next!=nil{
        fast=fast.Next.Next
        slow=slow.Next
        if fast==slow{
            return true
        }
    }
    return false
}