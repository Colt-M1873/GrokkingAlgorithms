// https://leetcode.com/problems/reverse-linked-list-ii/
// 2022年07月21日 19:17:09

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 import "fmt"
 func reverseBetween(head *ListNode, left int, right int) *ListNode {
	 curr:=head
	 i:=1
	 leftBreak,rightBreak,subHead,subEnd:=head,head,head,head
	 for curr!=nil {
		 if i==left-1{
			 leftBreak=curr
		 }
		 if i==right{
			 subEnd=curr
		 }
		 curr=curr.Next
		 i++
	 }
	 subHead=leftBreak.Next
	 curr=subHead
	 if left==1{
		 curr=head
	 }
	 rightBreak=subEnd.Next
	 fmt.Println(leftBreak)
	 fmt.Println(subHead)
	 fmt.Println(subEnd)
	 fmt.Println(rightBreak)    
	 prev:=rightBreak
	 tmpNext:=curr.Next
	 for curr!=rightBreak {
		 tmpNext=curr.Next
		 curr.Next=prev
		 prev=curr
		 curr=tmpNext
	 }
	 if left==1 {
		 return prev
	 }else{
		 leftBreak.Next=prev
		 return head        
	 }
 }