// https://leetcode.com/problems/max-area-of-island/
// 2022年07月09日 21:08:51

import "fmt"
func DFSrecursion(grid [][]int, x int,y int) int {
    area:=1
    if grid[x][y]==1{    
        grid[x][y]=2
        if x-1>=0{
            area+=DFSrecursion(grid,x-1,y)
        }
        if y-1>=0{
            area+=DFSrecursion(grid,x,y-1)
        }
        if x+1<len(grid){
            area+=DFSrecursion(grid,x+1,y)
        }
        if y+1<len(grid[x]){
            area+=DFSrecursion(grid,x,y+1)
        }
        return area
    }else{
        return 0
    }
}

func maxAreaOfIsland(grid [][]int) int {
    maxArea:=0
    for x:=0; x<len(grid); x++{
        for y:=0; y<len(grid[x]);y++{
            if grid[x][y]==1{
                currArea:=DFSrecursion(grid,x,y)
                if currArea > maxArea {
                    maxArea=currArea
                }
            }
        }
    }
    // for x:=0; x<len(grid); x++{
    //     fmt.Println(grid[x])
    // }
    return maxArea
}



// 2022年07月15日 10:10:43
import "fmt"

func BFSqueue(grid [][]int, x int,y int) int {
    coord:=[]int{x,y}
    grid[x][y]=2
    area:=1
    stack:=[][]int{coord} //2d array
    // fmt.Println(stack)
    direction:=[][]int{{1,0},{-1,0},{0,1},{0,-1}} // create 2d array with value
    for len(stack)>0{
        curr:=stack[0]
        stack=stack[1:]
        for d:=0;d<len(direction);d++{
            newx:=curr[0]+direction[d][0]
            newy:=curr[1]+direction[d][1]
            if newx>=0 && newx<len(grid) && newy>=0 && newy<len(grid[0]) && grid[newx][newy]==1{
                stack=append(stack,[]int{newx,newy})
                grid[newx][newy]=2
                area++
            }
        }
    }
    return area
}


func maxAreaOfIsland(grid [][]int) int {
    maxArea:=0
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            if grid[i][j]==1{
                area:=BFSqueue(grid,i,j)
                if area>maxArea{
                    maxArea=area
                }
                // fmt.Println(area)
            }
        }
    }
    return maxArea
}