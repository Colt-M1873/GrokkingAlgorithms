// https://leetcode.com/problems/intersection-of-two-arrays/
// 2022年07月20日 12:29:55


import "fmt"
func intersection(nums1 []int, nums2 []int) []int {
    d:=make(map[int]int)
    ret:=[]int{}
    for i:=0;i<len(nums2);i++{
        if _,ok:=d[nums2[i]]; !ok{
            d[nums2[i]]=-1
        }
    }
    for j:=0;j<len(nums1);j++{
        if _,ok:=d[nums1[j]]; ok{
            d[nums1[j]]=1
        }
        
    }    
    for key,val := range d{
        if val==1{
            ret=append(ret,key)
        }
    }
    return ret
}