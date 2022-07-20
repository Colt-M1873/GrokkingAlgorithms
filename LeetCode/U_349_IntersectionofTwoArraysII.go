// https://leetcode.com/problems/intersection-of-two-arrays-ii/
// 2022年07月20日 12:40:18

func intersect(nums1 []int, nums2 []int) []int {
    d:=make(map[int]int) //  count apperance in each element
    ret:=[]int{}
    for i:=0;i<len(nums2);i++{
        if _,ok:=d[nums2[i]];ok{
            d[nums2[i]]++
        }else{
            d[nums2[i]]=1
        }
    }
    for j:=0;j<len(nums1);j++{
        if _,ok := d[nums1[j]]; ok{
            if d[nums1[j]]>1 {
                d[nums1[j]]--
            }else{
                delete(d,nums1[j])
            }
            
            ret=append(ret,nums1[j])
        }
    }
    return ret
}