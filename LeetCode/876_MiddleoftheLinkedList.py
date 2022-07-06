# https://leetcode.com/problems/middle-of-the-linked-list/
# 2022 3.25
# 2022年07月06日 12:15:23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow

        # 2022年07月06日 12:15:17
        # # v1 calculate length
        # f,s=head,head
        # l=0
        # while f:
        #     f=f.next
        #     l+=1
        # l//=2
        # while l:
        #     s=s.next
        #     l-=1
        # return s
    
        # v2
        # fast and slow pointer with different speed
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
        