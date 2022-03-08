# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # v1 iterative 
        if not head:
            return None
        arr=[]
        while head:
            arr.append(head)
            head=head.next
        thisNode=None
        while arr:
            arr[0].next=thisNode
            thisNode=arr.pop(0)
            print(thisNode.val)
            
        return thisNode