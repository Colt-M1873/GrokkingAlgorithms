// https://leetcode.com/problems/merge-two-sorted-lists/
// 2022年07月24日 21:48:47

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 import "fmt"
 func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
     if list1==nil{
         return list2
     }else if list2==nil {
         return list1
     } 
     if list1.Val<list2.Val {
         ret:=list1
         ret.Next=mergeTwoLists(list1.Next, list2)
         return ret
     }else if list1.Val>=list2.Val {
         ret:=list2
         ret.Next=mergeTwoLists(list1, list2.Next)
         return ret
     }
     return nil
     
     
     // // v1 recursive failed to handle void value
     // var ret *ListNode
     // if list1==nil && list2==nil{
     //     return ret
     // }else if list2==nil || list1.Val<list2.Val {
     //     ret:=list1
     //     fmt.Println("list1",ret)
     //     ret.Next=mergeTwoLists(list1.Next, list2)
     //     return ret
     // }else if list1==nil || list1.Val>=list2.Val {
     //     ret:=list2
     //     fmt.Println("list2",ret)
     //     ret.Next=mergeTwoLists(list1, list2.Next)
     //     return ret
     // }
     // fmt.Println("ret",ret)
     // return ret
     
     
     
     
 }