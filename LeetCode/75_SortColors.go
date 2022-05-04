// https://leetcode.com/problems/sort-colors/submissions/
// 2022年05月02日 17:17:40

func sortColors(nums []int)  {
    // // v1 bubble sort
    // for i:=0;i<len(nums);i++{
    //     for j:=i+1;j<len(nums);j++{
    //         if nums[i]>nums[j]{
    //             nums[i],nums[j]=nums[j],nums[i]
    //         }
    //     }
    // }
    
    // v2 three pointer
    p0:=0
    p1:=0
    p2:=len(nums)-1
    for p1<=p2{
        if nums[p1]==0{
            nums[p1],nums[p0]=nums[p0],nums[p1]
            p1++
            p0++
        } else if nums[p1]==2{
            nums[p1],nums[p2]=nums[p2],nums[p1]
            p2--            
        }else{
            p1++
        }
    }
    
}