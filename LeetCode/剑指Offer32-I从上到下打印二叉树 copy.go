// https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 2023年03月25日 16:59:59

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) []int {
	if root == nil {
		return make([]int, 0)
	}
	q := make([]*TreeNode, 0)
	q = append(q, root)
	res := make([]int, 0)
	for len(q) > 0 {
		curr := q[0]
		res = append(res, curr.Val)
		q = q[1:]
		if curr.Left != nil {
			q = append(q, curr.Left)
		}
		if curr.Right != nil {
			q = append(q, curr.Right)
		}

	}
	return res
}