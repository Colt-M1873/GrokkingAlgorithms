// https://leetcode.cn/problems/maximum-binary-tree-ii/
// 2022年08月30日 16:52:14

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 // v1 dumb, recover array from Tree, append, and cunstruct a new tree like Q.654
 import "fmt"
 func insertIntoMaxTree(root *TreeNode, val int) *TreeNode {
	 nums:=recoverArray(root)
	 // fmt.Println(nums)
	 nums=append(nums,val)
	 return constructMaximumBinaryTree(nums)
 }
 
 func recoverArray(root *TreeNode) []int {
	 if root==nil {return []int{}}
	 nums:=[]int{root.Val}
	 nums=append(recoverArray(root.Left),nums...)
	 nums=append(nums,recoverArray(root.Right)...)
	 return nums
 }
 
 func constructMaximumBinaryTree(nums []int) *TreeNode {
	 if len(nums)==0{
		 return nil
	 }
	 idx:=maxIdx(nums)
	 // fmt.Println(idx,nums[idx])
	 root:=TreeNode{Val:nums[idx],Left:constructMaximumBinaryTree(nums[:idx]),Right:constructMaximumBinaryTree(nums[idx+1:])}
	 // fmt.Println(root)
	 return &root
 }
 
 func maxIdx(nums []int) int {
	 idx:=0
	 max:=nums[0]
	 for i:=range nums{
		 if nums[i]>max{
			 max=nums[i]
			 idx=i
		 }
	 }
	 return idx
 }