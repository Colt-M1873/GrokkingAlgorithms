# https://leetcode.com/problems/implement-queue-using-stacks/
# 2022年07月14日 21:53:33
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x: int) -> None:
        l1=len(self.s1)
        l2=len(self.s2)
        if l1==0 and l2!=0 :
            for _ in range(l2):
                self.s1.append(self.s2.pop())        
        self.s1.append(x)
        
    def pop(self) -> int:
        l1=len(self.s1)
        l2=len(self.s2)
        if l1==0 and l2==0:
            return None
        if l2==0 and l1 !=0 :
            for _ in range(l1):
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        l1=len(self.s1)
        l2=len(self.s2)
        if l1==0 and l2==0:
            return None
        if l2==0 and l1 !=0 :
            for _ in range(l1):
                self.s2.append(self.s1.pop())
        return self.s2[-1]
                
    def empty(self) -> bool:
        return len(self.s1)==0 and len(self.s2)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()