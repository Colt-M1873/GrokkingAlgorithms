// https://leetcode.com/problems/reshape-the-matrix/
// 2022年07月21日 18:08:23

func matrixReshape(mat [][]int, r int, c int) [][]int {
    m,n:=len(mat),len(mat[0])
    if m*n != r*c { return mat }
    array:=[]int{}
    for i:=0;i<m;i++{
        array=append(array,mat[i]...) // need 3 dot to append slice to slice
    }
    ret:=[][]int{} // note: [][]int{} is different from [][]int{{}} 
    for j:=0;j<r;j++{
        ret=append(ret,array[j*c:(j+1)*c])
    }
    return ret
}