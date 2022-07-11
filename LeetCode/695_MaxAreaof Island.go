// https://leetcode.com/problems/max-area-of-island/
// 2022年07月09日 21:54:51

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