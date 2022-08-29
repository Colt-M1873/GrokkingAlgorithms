// https://leetcode.com/problems/number-of-islands/
// 2022年08月29日 10:17:05

// v1  35min
import "fmt"
func numIslands(grid [][]byte) int {
    
    // 4 commected area, can be seen as a quad-tree
    // propogate using stack
    islandCount:=0
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            // fmt.Printf("%c ",grid[i][j])
            if grid[i][j]=='1' {
                quadtree(grid,[]int{i,j})
                islandCount++
            }
        }
        // fmt.Println()
    }
    // fmt.Println(grid)
    return islandCount
}

func quadtree(grid [][]byte, root []int) int{
    dir:=[][]int{{-1,0},{0,-1},{1,0},{0,1}}
    stack:=[][]int{root}
    for len(stack)>0 {
        curr:=stack[0]
        x:=curr[0]
        y:=curr[1]
        grid[x][y]='2'
        stack=stack[1:]
        for d:=0;d<4;d++{
            newx:=x+dir[d][0]
            newy:=y+dir[d][1]
            if newx<len(grid) && newx>=0 && newy<len(grid[0]) && newy>=0 && grid[newx][newy]=='1'{
                grid[newx][newy]='2'
                stack=append(stack,[]int{newx,newy})
            }
        }
    }
    return 0
}


// v1.1
import "fmt"
func numIslands(grid [][]byte) int {
    // 4 commected area, can be seen as a quad-tree
    // propogate using stack
    islandCount:=0
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            // fmt.Printf("%c ",grid[i][j])
            if grid[i][j]=='1' {
                grid[i][j]='2'
                quadtree_bfs(grid,[]int{i,j})
                islandCount++
            }
        }
    }
    return islandCount
}

func quadtree_bfs(grid [][]byte, root []int) {
    dir:=[][]int{{-1,0},{0,-1},{1,0},{0,1}} // using direction list to reduce code amount
    stack:=[][]int{root} // bfs traversal stack
    for len(stack)>0 {
        x,y:=stack[0][0],stack[0][1] // get current node
        stack=stack[1:] // pop current node
        for d:=0;d<4;d++{
            newx:=x+dir[d][0] // childnode
            newy:=y+dir[d][1] // 
            if newx<len(grid) && newx>=0 && newy<len(grid[0]) && newy>=0 && grid[newx][newy]=='1'{
                grid[newx][newy]='2' // set to different value in case of repeat counting
                stack=append(stack,[]int{newx,newy})
            }
        }
    }
}