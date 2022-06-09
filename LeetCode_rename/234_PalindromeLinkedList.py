# https://leetcode.com/problems/palindrome-linked-list/
# 2022 3.28

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # v1 iterative using two-pointer and stack
        if not head.next: return True
        fast=slow=head
        stack=[]
        while fast and fast.next:
            fast=fast.next.next
            stack.append(slow.val)
            slow=slow.next
            # print(stack)
            # print("fast",fast.val,"slow",slow.val)
        if fast: slow=slow.next # if total length is odd, then jump over the central node.
        # 如果整体长度是奇数，那经过第一个while之后，fast会停在最后一个节点，fast.next==None，
        # 如果整体长度是偶数，那经过第一个while之后，fast会停在末尾的空节点，fast==None
        while slow:
            if slow.val!=stack.pop():
                return False
            slow=slow.next
        return True