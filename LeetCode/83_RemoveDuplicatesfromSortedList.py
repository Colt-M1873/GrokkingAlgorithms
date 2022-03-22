# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # # v1 
        # returnHead=head
        # while head:
        #     mid=head
        #     while mid.next and  mid.val==mid.next.val:
        #         mid=mid.next
        #     head.next=mid.next
        #     head=head.next        
        # return returnHead
        
        # # v2 Recursion
        # if head == None:
        #     return head
        # while head.next!=None and head.next.val==head.val:
        #     head=head.next
        # head.next=self.deleteDuplicates(head.next) 
        # return head
        
        # v2.1 copied Recursion
        if head == None or head.next==None:
            return head
        head.next=self.deleteDuplicates(head.next) 
        return head.next if head.val == head.next.val else head

l=[10,2,2,2,3,4,5,6,6,6,6,6,7]
Ln=ListNode(l[0])
lnhead=Ln
for i in range(1,len(l)):
    Ln.next=ListNode(l[i])
    Ln=Ln.next
# print(lnhead.val)

s=Solution()
ret=s.deleteDuplicates(lnhead)
while ret:
    print(ret.val)
    ret=ret.next
