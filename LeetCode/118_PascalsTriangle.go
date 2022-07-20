// https://leetcode.com/problems/pascals-triangle/
// 2022年07月19日 18:12:08

import "fmt"
func generate(numRows int) [][]int {
    pas:=[][]int{{1},{1,1}}
    
    if numRows<3 {return pas[:numRows]}
    for n:=numRows;n>2;n--{
        currLine:=[]int{1}
        last:=len(pas)-1
        for i:=0;i<len(pas[last])-1;i++{
            currLine=append(currLine,pas[last][i]+pas[last][i+1])
        }
        currLine=append(currLine,1)
        pas=append(pas,currLine)
    }
    return pas
}