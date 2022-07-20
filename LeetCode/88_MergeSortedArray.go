// https://leetcode.com/problems/merge-sorted-array/
// 2022年07月19日 17:57:00

import "fmt"
func merge(nums1 []int, m int, nums2 []int, n int)  {
    m--
    n--
    for n>=0||m>=0 {
        if  (n>=0 && m<0) || (n>=0 && nums2[n]>=nums1[m]){
            nums1[m+n+1]=nums2[n]
            n--
            // fmt.Println(nums1)
        }else if (m>=0 && n<0) || (m>=0 && nums2[n]<nums1[m]) {
            nums1[m+n+1], nums1[m]=nums1[m],nums1[m+n+1]            
            m--
            // fmt.Println(nums1)
        }
    }
}