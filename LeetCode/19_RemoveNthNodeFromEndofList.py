# https://leetcode.com/problems/remove-nth-node-from-end-of-list/\
# 2022年07月06日 11:17:09

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer
        # v1 fast pointer point to the last amd get length
        # slow pointer point to length-n 
        f,s=head,head
        length=0
        while f:
            f=f.next
            length+=1
        if length==n:
            return head.next
        for _ in range(length-n-1):
            s=s.next
        remove=s.next
        s.next=remove.next
        remove.next=None
        return head

        # v2 no need to calculate length
        # using the ralative position of fast and slow pointer
        # fast pointer move n, slow pointer stay still
        # then two pointers move together, 
        # when fast pointer reach the end
        # slow pointe pointing n th node
        fast,slow=head,head
        while n:
            fast=fast.next
            n-=1
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        remove=slow.next
        slow.next=remove.next
        remove.next=None
        return head
