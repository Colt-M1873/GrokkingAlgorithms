# https://leetcode.com/problems/rotate-list/
# 2022 3.29 
# 18 min 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # v1 two-pass
        if not head :return head 
        fast=tmphead=head
        l=0
        # calculate total length
        while fast.next: # stop at the last non-void node. 
            fast=fast.next
            l+=1
        l+=1
        # print(l)
        # print(k%l)
        cutl=k%l # cut off length
        if cutl == 0: # if k is a multiple of length l, then no need to move
            return head
        while l>cutl+1: # locate the cut off node
            tmphead=tmphead.next
            l-=1
        ret=tmphead.next # remember new head
        tmphead.next=None # cut through middle
        fast.next=head # link the last node to the tmphead
        return ret