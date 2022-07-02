// https://leetcode.com/problems/reverse-linked-list/
// 2022年07月01日 17:59:33

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 import "fmt"
 func reverseList(head *ListNode) *ListNode {
     // fmt.Println(head.Val)
     var prev,next *ListNode
     for head!=nil {
         next=head.Next
         head.Next=prev
         prev=head
         head=next
     }
     return prev
 }