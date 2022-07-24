// https://leetcode.com/problems/remove-linked-list-elements/
// 2022年07月24日 22:22:21

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func removeElements(head *ListNode, val int) *ListNode {
    // v1 ugly
    for head!=nil && head.Val==val{
        head=head.Next
    }
    if head==nil || ( head.Next==nil && head.Val!=val) {
        return head
    }else if head.Next==nil && head.Val==val{
        return nil
    }
    curr:=head
    var ret *ListNode
    ret=head
    for curr!=nil && curr.Next!=nil{
        if curr.Next.Val == val{
            curr.Next=curr.Next.Next
        }else{  
            curr=curr.Next
        }
    }
     
    return ret
}