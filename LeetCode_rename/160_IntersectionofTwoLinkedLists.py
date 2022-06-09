# https://leetcode.com/problems/intersection-of-two-linked-lists/
# 2022 3.11

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # A B may not the same length but with the same end.
        
        # # v1 iterative. align and pass twice. the feature of this question is 
        # # if there are any intersection ListNode A and B must end at the same point.
        # # So the last part of A and B are the same.
        # # to let A and B reach the intersection at the same time
        # # we pass thuough A and B with the same pace, then if there are not of the same length
        # # we will cut the difference at the second pass through.
        # if not headA or not headB:
        #     return None
        # Atmp=headA # pointers for the second pass
        # Btmp=headB # 
        # # the first pass
        # while headA and headB:
        #     if headA == headB:
        #         return headA
        #     headA=headA.next
        #     headB=headB.next
        # # make up for the length difference between A and B
        # # if B is longer than A
        # if headB and not headA:
        #     while headB:
        #         Btmp=Btmp.next
        #         headB=headB.next
        # # if A is longer than B
        # if headA and not headB:
        #     while headA:
        #         Atmp=Atmp.next
        #         headA=headA.next
        # # the second pass
        # while Atmp and Btmp:
        #     if Atmp == Btmp:
        #         return Atmp
        #     Atmp=Atmp.next
        #     Btmp=Btmp.next
        # return None


        # v2 copied, brilliant the same idea but in a more concise way
        if not headA or not headB:
            return None
        pa=headA
        pb=headB
        while pa is not pb:
            # if walk to the end the just back to headA
            # after at most two pass through, pa and pb will be the same
            # either be the intersection or be None
            pa=headA if pa is None else pa.next
            pb=headB if pb is None else pb.next
        return pa