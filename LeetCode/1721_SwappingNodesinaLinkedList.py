# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/
# 2022年04月04日 11:12:05

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # v1 read the problem description carefully, it says swap the value.
        # so no need to do the hard work swapping the real node.
        fast=slow=head
        while k>1:
            fast=fast.next
            k-=1
        leftnode=fast
        
        while fast.next:
            fast=fast.next
            slow=slow.next
        rightnode=slow
        leftnode.val, rightnode.val=rightnode.val,leftnode.val
        return head