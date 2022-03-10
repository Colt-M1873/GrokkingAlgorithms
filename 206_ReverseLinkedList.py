# https://leetcode.com/problems/reverse-linked-list/
# 2022 3.05 3.09

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 不论循环还是递归重点在于暂存原本的head.next
        
        # # v1 dumb, iterative using queue
        # if not head:
        #     return None
        # arr=[]
        # while head:
        #     arr.append(head)
        #     head=head.next
        # thisNode=None
        # while arr:
        #     arr[0].next=thisNode
        #     thisNode=arr.pop(0)
        # return thisNode

        # # v2 copied iteretive
        # prev=None
        # curr=head
        # while curr:
        #     tmp=curr.next
        #     curr.next=prev 
        #     prev=curr
        #     curr=tmp
        # return prev
        
        # v3 recursive
        
        def recursion(head,lastNode):
            if not head:
                return lastNode
            tmpNext=head.next
            head.next=lastNode
            return recursion(tmpNext,head)
        
        return recursion(head,None)