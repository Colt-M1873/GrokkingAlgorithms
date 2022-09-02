// https://leetcode.cn/problems/longest-univalue-path/
// 2022年09月02日 07:46:02

// v1 recursive DFS
func longestUnivaluePath(root *TreeNode) int {
    currMax:=0
    var recDFS func(node *TreeNode) int
    recDFS = func(node *TreeNode) int {
        if node==nil {return 0}
        leftPath:=recDFS(node.Left)
        rightPath:=recDFS(node.Right)
        if node.Left!=nil && node.Val==node.Left.Val{
            leftPath++
        }else{
            leftPath=0
        }        
        if node.Right!=nil && node.Val==node.Right.Val{
            rightPath++
        }else{
            rightPath=0
        }
        if leftPath+rightPath>currMax{
            currMax=leftPath+rightPath
        }
        if leftPath>rightPath{
            return leftPath
        }
        return rightPath
    }
    recDFS(root)
    return currMax
}

// v1.1 recursive without local variable
func longestUnivaluePath(root *TreeNode) int {
    var recDFS func(node *TreeNode) (int,int)
    recDFS = func(node *TreeNode) (int,int) {
        if node==nil {return 0,0}
        maxL,pathL:=recDFS(node.Left)
        maxR,pathR:=recDFS(node.Right)
        currMax:=max(maxL,maxR)
        if node.Left!=nil && node.Val==node.Left.Val{
            pathL++
        }else{
            pathL=0
        }        
        if node.Right!=nil && node.Val==node.Right.Val{
            pathR++
        }else{
            pathR=0
        }
        currMax=max(currMax,pathL+pathR)
        return currMax, max(pathL,pathR)
    }
    ret,_:=recDFS(root)
    return ret
}
func max(a,b int) int{
    if a>b {return a}
    return b
}



// v2 iterative post-order DFS
// no idea


