# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # # v1  iterative
        # dummyhead=ListNode(0)
        # dummyhead.next=head
        # rethead=dummyhead
        # while dummyhead.next: 
        #     if dummyhead.next.val==val:
        #         dummyhead.next=dummyhead.next.next
        #     else:
        #         dummyhead=dummyhead.next
        # return rethead.next
        
        # v2 recursive
        if head==None:
            return None
        if head.val==val:
            return self.removeElements(head.next,val)
        head.next=self.removeElements(head.next,val)
        return head