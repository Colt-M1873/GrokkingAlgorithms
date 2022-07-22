// https://leetcode.com/problems/search-a-2d-matrix/
// 2022年07月22日 15:15:11

import "fmt"
func searchMatrix(matrix [][]int, target int) bool {
    u,d:=0,len(matrix)-1
    for u<d{
        mid:=int((u+d)/2)
        if target<matrix[mid][0] {
            d=mid-1
        }else if target>matrix[mid][len(matrix[0])-1]{
            u=mid+1
        }else{
            u,d=mid,mid
        }
    }
    // fmt.Println(u)
    // fmt.Println(d)
    l,r:=0,len(matrix[0])-1
    if target<matrix[u][0] || target>matrix[u][r]{
        return false
    }else{
        for l<=r {
            mid:=int((l+r)/2)
            if target<matrix[u][mid]{
                r=mid-1
            }else if target>matrix[u][mid]{
                l=mid+1
            }else{
                return true
            }
        }
    }
    return false
}