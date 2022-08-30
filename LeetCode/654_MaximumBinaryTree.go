// https://leetcode.cn/problems/maximum-binary-tree/
// 2022年08月30日 16:03:34


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 // v1 recurison
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