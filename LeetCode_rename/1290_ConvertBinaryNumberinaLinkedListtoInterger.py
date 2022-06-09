# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/
# 2021 12.07

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        # v1 read sum and multiply
        ret=0
        while head:
            ret=ret*2+head.val
            head=head.next
        return ret

        # # v2 convert binary to int
        # outstr=''
        # while head:
        #     outstr+=str(head.val)
        #     head=head.next
        # return int(outstr,2)