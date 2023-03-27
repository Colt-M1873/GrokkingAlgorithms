// https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
// 2023年03月25日 17:18:56

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	ret := make([][]int, 0)
	layer := []*TreeNode{}
	nextLayer := []*TreeNode{}
	layer = append(layer, root)
	for len(layer) != 0 || len(nextLayer) != 0 {
		layerRet := []int{}
		for len(layer) != 0 {
			curr := layer[0]
			layer = layer[1:]
			layerRet = append(layerRet, curr.Val)
			if curr.Left != nil {
				nextLayer = append(nextLayer, curr.Left)
			}
			if curr.Right != nil {
				nextLayer = append(nextLayer, curr.Right)
			}
		}
		// fmt.Println(layerRet)
		ret = append(ret, layerRet)
		layer = nextLayer
		nextLayer = []*TreeNode{}
	}
	return ret
}