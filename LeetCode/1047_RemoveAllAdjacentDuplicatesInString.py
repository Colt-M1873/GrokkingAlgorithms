# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# 2022年05月06日 17:33:14

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # # v1 iterative using stack 98ms faster than 64.32%
        # stack=[]
        # for i in range(len(s)):
        #     if not stack or stack[-1]!=s[i]:
        #         stack.append(s[i])
        #     else:
        #         stack.pop()
        # return ''.join(stack)
        
        # v2 copied, iterative two pointer
        # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294893/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
        # 这里双指针是在模拟栈的操作，原理和栈的操作一模一样，唯一的不同在于不需要额外空间
        # 快指针相当于栈方法中遍历range(len(s))的那个变量i，慢指针相当于栈顶
        # 用s[slow]=s[fast]这样的操作来入栈，模拟stack.append
        # 慢指针-2+1的操作相当于栈的pop
        # 在C或者go这种数组本身可变的语言里，该方法的优势在于不需要额外空间，一切全在原数组中操作
        # python数组不可变，所以还是需要转成list
        # fast快指针每次都稳定加一，慢指针遇到重复之后就-2+1即退缩一步，退缩之后slow所指的实际上是出现重复的第一个位置，
        # 此时fast和slow之间的内容全为重复，因此没有意义，可以直接用新的fast来替代，
        slow=fast=0
        s=list(s)
        while fast<len(s):
            s[slow]=s[fast]
            if s[slow]==s[slow-1] and slow>0: # 大于0是为了保证slow在-2并+1之后不出现负数
                slow-=2
            slow+=1
            fast+=1
        return ''.join(s[:slow])