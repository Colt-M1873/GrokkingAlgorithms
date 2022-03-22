# https://leetcode.com/problems/linked-list-cycle/
# 2022 3.11

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # # v1 cheating but succeed, using the length limit 10e4
        # if not head or not head.next:
        #     return False
        # for i in range(10001):
        #     if not head.next:
        #         return False
        #     head=head.next
        # return True

        # v2 copied two pointer  fast and slow pointer
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
