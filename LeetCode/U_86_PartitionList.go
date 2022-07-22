// https://leetcode.com/problems/partition-list/submissions/
// 2022年07月22日 14:57:04

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 import "fmt"
 func partition(head *ListNode, x int) *ListNode {
	 if head==nil {return head}
	 var lHead,rHead,lCurr,rCurr *ListNode
	 curr:=head
	 for curr!=nil {
		 tmpNext:=curr.Next // while looping, cut off every Next connection in original linked list
		 curr.Next=nil  //  in case of mispointing, loop or multipointing in operations below
		 if curr.Val<x {
			 if lHead==nil{
				 lHead=curr
				 lCurr=curr
			 }else{
				 lCurr.Next=curr
				 lCurr=lCurr.Next
			 }
		 }
		 if curr.Val>=x {
			 if rHead==nil{
				 rHead=curr
				 rCurr=curr
			 }else{
				 rCurr.Next=curr
				 rCurr=rCurr.Next
			 }
 
		 }
		 curr=tmpNext // because connections are cut, neet a tmpNext to store next node
	 }
	 if lHead == nil{ // in case of x smaller than any value in linked list
		 return rHead
	 }else{
		 lCurr.Next=rHead
		 return lHead        
	 }
	 // fmt.Println(lHead)
	 // fmt.Println(rHead)
 }