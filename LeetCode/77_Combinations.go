// https://leetcode.com/problems/combinations/
// 2023年03月27日 13:45:51

func combine(n int, k int) [][]int {
    nums:=[]int{}
    for i:=1;i<=n;i++{
        nums=append(nums,i)
    }
    ret:=[][]int{}
    bt(nums,k,[]int{},&ret)
    return ret
}

func bt(n []int, k int, path []int, ret *[][]int){
    if len(path)==k{
        newPath:=make([]int,len(path))
        copy(newPath,path) // 每次均开辟新地址，防止ret里的所有值都指向同一个path
        *ret=append(*ret,newPath)
    }
    for idx,val:=range n{
        fmt.Println(val)
        fmt.Println(n[idx+1:])
        path=append(path,val)
        bt(n[idx+1:],k,path,ret)
        path=path[:len(path)-1]
    }
}