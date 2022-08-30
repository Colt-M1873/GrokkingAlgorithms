// https://leetcode.com/problems/rotate-image/submissions/
// 2022年08月30日 15:08:16

import "fmt"
func rotate(matrix [][]int)  {
    // // v1 cheating, not in-place, building a new matrix
    // // but useful to understand 2d array deep copy in golang (like in c++)
    // mat2 := make([][]int, len(matrix))
    // for i := range matrix {
    //     mat2[i]=make([]int,len(matrix[i]))
    //     copy(mat2[i],matrix[i])
    // }
    // // fmt.Println(mat2)
    // for i:=0;i<len(matrix);i++{
    //     for j:=0;j<len(matrix);j++{
    //         matrix[i][j]=mat2[len(matrix)-1-j][i] // x=n-y2, y=x2
    //     }
    // }
    // // fmt.Println(mat2)
    
    // v2 brilliant, in-place, rotate = two step swap 
	// because we can't directly rotate 90 degree without
    // introducing middle variables. we swap matrix twice
    // rotate 90 degree = horizontal swap + diagnoal swap
	// come up by myself, same thought in 
	// https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
    // 1. horizontal swap
    n:=len(matrix)
    for i:=range matrix{
        for j:=0;j<n/2;j++{
            matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
        }
    }
    // fmt.Println(matrix)
    // 2. diagonal swap
    for i:=0;i<n;i++{
        for j:=0;j<n-i;j++{
            matrix[i][j],matrix[n-1-j][n-1-i]=matrix[n-1-j][n-1-i],matrix[i][j]
        }
    }
    // fmt.Println(matrix)
}