// https://leetcode.com/problems/implement-stack-using-queues/submissions/
// 2022年04月28日 19:07:23

// 参考以下两个重构，题目里要求的是用queue，go有自带的queue结构吗？好像有
// https://leetcode.com/problems/implement-stack-using-queues/discuss/570763/Golang-1-queue-pop-O(n)-push-O(1)
// https://leetcode.com/problems/implement-stack-using-queues/discuss/1746131/Golang-solution-or-pop-O(1)-push-O(n)

type MyStack struct {
    s []int 
}


func Constructor() MyStack {
    return MyStack{[]int{}}
}


func (this *MyStack) Push(x int)  {
    this.s=append(this.s,x)
}


func (this *MyStack) Pop() int {
    l:=len(this.s)
    ret:=this.s[l-1]
    this.s=this.s[:l-1]
    return ret
}


func (this *MyStack) Top() int {
    return this.s[len(this.s)-1]
}


func (this *MyStack) Empty() bool {
    return len(this.s)==0
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */