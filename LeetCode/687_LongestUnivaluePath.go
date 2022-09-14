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
// no idea, copied

func longestUnivaluePath(root *TreeNode) int {
    currMax:=0
    mixedType:=[]interface{} {0,root,nil}
    postorder := []interface{}
    d := make(map[*TreeNode]int)
    for len(postorder)>0{
        seen,node,parent := postorder[len(postorder)-1]
        postorder=postorder[:len(postorder)-1]
        if node==nil{
            continue
        }
        if seen==0{
            postorder=append(postorder,[]int{1,node,parent})
            postorder=append(postorder,[]int{0,node.Left,node.Val})
            postorder=append(postorder,[]int{0,node.Right,node.Val})
        }else{
            if node.Val==parent{
                d[node]:=max(d[node.Left],d[node.Right])+1
            }else{
                d[node]:=0
            }
            currMax=max(currMax,d[node.Left]+d[node.Right])
        }
    }
    return currMax
}
func max(a,b int)int{
    if a>b {return a}
    return b
}
