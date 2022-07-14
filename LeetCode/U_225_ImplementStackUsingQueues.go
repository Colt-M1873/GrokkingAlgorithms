// https://leetcode.com/problems/implement-stack-using-queues/submissions/
// 2022年04月28日 19:07:23 wrong
// 2022年07月14日 21:47:56

// 参考以下两个重构，题目里要求的是用queue，go有自带的queue结构吗？好像有
// https://leetcode.com/problems/implement-stack-using-queues/discuss/570763/Golang-1-queue-pop-O(n)-push-O(1)
// https://leetcode.com/problems/implement-stack-using-queues/discuss/1746131/Golang-solution-or-pop-O(1)-push-O(n)

type MyStack struct {
    q []int 
}


func Constructor() MyStack {
    return MyStack{[]int{}}
}


func (this *MyStack) Push(x int)  {
    this.q=append(this.q,x)
}


func (this *MyStack) Pop() int {
    for l:=len(this.q)-1;l>0;l-- {
        this.q=append(this.q[1:],this.q[0])
    }
    ret:=this.q[0]
    this.q=this.q[1:]
    return ret
}


func (this *MyStack) Top() int {
    for l:=len(this.q)-1;l>0;l-- {
        this.q=append(this.q[1:],this.q[0])
    }
    ret:=this.q[0]
    this.q=append(this.q[1:],this.q[0])
    return ret
}


func (this *MyStack) Empty() bool {
    return len(this.q)==0
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */