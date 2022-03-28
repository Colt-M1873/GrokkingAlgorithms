# https://leetcode.com/problems/add-two-numbers/submissions/
# 2021 11.23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def generate_node(self,nums):
        p_head = ListNode(-1)
        temp_head = p_head
        for num in nums:
            temp = ListNode(num)
            temp_head.next = temp
            temp_head = temp_head.next
        return p_head.next


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        outputlist = []
        carry=0
        adder1 = l1
        adder2 = l2
        # outputlist.append(0)
        while (adder1 is not None) or (adder2 is not None):
            outputlist.append(0)
            if adder1 is None:
                adder1val=0
            else:
                adder1val=adder1.val
            if adder2 is None:
                adder2val=0
            else:
                adder2val=adder2.val

            sumval = adder1val + adder2val + carry
            outputlist[-1] += sumval % 10
            if sumval >= 10:
                carry=1
            else:
                carry=0
            if adder1 is not None:
                adder1 = adder1.next
            if adder2 is not None:
                adder2 = adder2.next
        if carry==1:
            outputlist.append(1)
        # if outputlist[-1]==0:
        #     outputlist.pop(-1)
        node=ListNode()
        len1=len(outputlist)
        headA=self.generate_node(outputlist)
        head=headA
        while headA is not None:
            # print(headA.val)
            headA=headA.next
        return head