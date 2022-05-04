// https://leetcode.com/problems/invert-binary-tree/
// 2022年04月29日 15:08:51


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func invertTree(root *TreeNode) *TreeNode {
    
    // // v1 recursive
    // if root==nil {
    //     return nil
    // }
    // root.Left,root.Right=invertTree(root.Right),invertTree(root.Left)
    // return root

    // v2 iterative BFS using queue
    if root==nil {
        return nil
    }
    q := []*TreeNode {root}
    for len(q)>0 {
        curr:=q[0]
        q=q[1:]
        curr.Left,curr.Right=curr.Right,curr.Left
        if curr.Left!=nil {
            q=append(q,curr.Left)
        }
        if curr.Right!=nil {
            q=append(q,curr.Right)
        }
    }
    return root

    // v3 copied iterative DFS using stack
    // if root==nil {
    //     return nil
    // }
    // s := []*TreeNode {root}
    // for len(s)>0 {
    //     curr:=s[len(s)-1]
    //     s=s[:len(s)-1]
    //     if curr !=nil{
    //         curr.Left,curr.Right=curr.Right,curr.Left
    //         s=append(s,curr.Left,curr.Right)
    //     }
    // }
    // return root
}