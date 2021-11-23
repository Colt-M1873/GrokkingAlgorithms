# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # v1  confusing iterative method
        # if l1==None or l2==None:
        #     return l1 or l2
        # if l1.val<l2.val:
        #     op=l1
        # else:
        #     op=l2
        # while l1!=None and l2!=None:
        #     if l1.val<l2.val:
        #         nl1=l1.next
        #         if l1.next==None or l1.next.val>=l2.val:      
        #             l1.next=l2
        #         l1=nl1
        #     else:
        #         nl2=l2.next
        #         if l2.next==None or l2.next.val>l1.val:
        #             l2.next=l1
        #         l2=nl2
        # return op

        # # v1.1 copied  better and cleaner iterative method
        # # no need to check void input and tail of listnode
        # # None is like False, can be bool operated with other types: 
        # # None and 's' == None   None or 's' == 's' 
        # dummy = cur = ListNode(0)
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # cur.next = l1 or l2
        # return dummy.next
    
    
        # # v2 copied   clean recursive method
        # if not l1 or not l2:
        #     return l1 or l2
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
    
    
        # # v2.1 copied  clean recursive method
        # # First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
        # a=l1
        # b=l2
        # if not a or b and a.val > b.val:
        #     a, b = b, a
        # if a:
        #     a.next = self.mergeTwoLists(a.next, b)
        # return a

        # v2.2 copied   elegant recursive method
        # If both lists are non-empty, I first make sure l1 starts smaller, use its head as result, and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


