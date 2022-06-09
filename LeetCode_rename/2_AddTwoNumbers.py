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


# 2022年05月20日 15:09:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # # v1 passed but ugly and chaos
        # rethead=l1
        # c=0
        # while l1 or l2 or c:
        #     if l1 and l2:
        #         curr=l1.val+l2.val+c
        #         l1.val=curr%10
        #         c=curr//10
        #         if not l1.next and l2.next:
        #             l1.next=l2.next
        #             l2.next=None
        #         if not l2.next and not l1.next:
        #             if c:
        #                 l1.next=ListNode(c,None)
        #                 break
        #         l1=l1.next
        #         l2=l2.next
        #     elif (not l2) and l1:
        #         curr=l1.val+c
        #         l1.val=curr%10
        #         c=curr//10
        #         if not l1.next and c:
        #             l1.next=ListNode(c,None)
        #             break
        #         else:
        #             l1=l1.next
        #     else:
        #         return rethead
        # return rethead
    
        # v2 copied clear
        c1 = l1
        c2 = l2
        sentinel = ListNode(0)
        d = sentinel
        sum = 0
        while c1 != None or c2 != None :
            sum //= 10
            if c1 != None:
                sum += c1.val
                c1 = c1.next
            if c2 != None:
                sum += c2.val
                c2 = c2.next
            d.next = ListNode(sum % 10)
            d = d.next
        if sum // 10 == 1:
            d.next = ListNode(1)
        return sentinel.next
    
        # v3 copied clear
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next