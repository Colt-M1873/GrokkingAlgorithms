// https://leetcode.com/problems/flood-fill/
// 2022年07月08日 20:54:07


func DFSrecursion(grid [][]int, x int,y int, origColor int, dstColor int) int {
    if grid[x][y]==dstColor{
        return 0
    }
    if grid[x][y]==origColor{    
        grid[x][y]=dstColor
        if x-1>=0{
            DFSrecursion(grid,x-1,y,origColor,dstColor)
        }
        if y-1>=0{
            DFSrecursion(grid,x,y-1,origColor,dstColor)
        }
        if x+1<len(grid){
            DFSrecursion(grid,x+1,y,origColor,dstColor)
        }
        if y+1<len(grid[x]){
            DFSrecursion(grid,x,y+1,origColor,dstColor)
        }
    }
        return 0
}

func floodFill(image [][]int, x int, y int, color int) [][]int {
    // v1 DFS using recursion
    origColor:=image[x][y]
    DFSrecursion(image,x,y,origColor,color)
    return image
}