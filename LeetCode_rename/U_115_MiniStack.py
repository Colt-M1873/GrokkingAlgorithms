# https://leetcode.com/problems/min-stack/
# 2022年04月14日 16:09:13


# 用python来实现这样的数据结构没有意义，之后用c++尝试一下

class MinStack(object):

    def __init__(self):
        self.s=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.s:
            self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.s:
            return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.s)    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()