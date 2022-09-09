// https://leetcode.com/problems/binary-tree-inorder-traversal/
// 2022年09月08日 14:52:38

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// v1 recursive? code not consice
func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	ret := append(inorderTraversal(root.Left), root.Val)
	ret = append(ret, inorderTraversal(root.Right)...)
	return ret
}

// v2 iterative
func inorderTraversal(root *TreeNode) []int {
	stack := []*TreeNode{}
	ret := []int{}
	for len(stack) > 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ret = append(ret, root.Val)
		root = root.Right
	}
	return ret
}
