# https://leetcode.cn/problems/linked-list-components/
# 2022年10月12日 13:26:24

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s=set(nums)
        ret=0
        while head:
            if head.val in s and (head.next==None or head.next.val not in s):
                ret+=1
            head=head.next
        return ret

