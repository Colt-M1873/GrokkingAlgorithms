# https://leetcode.com/problems/merge-k-sorted-lists/
# 2022 3.28

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # # v1 太慢，超时，但思路基本正确
        # if not lists: return None
        # # 删掉列表里的所有空链表（已经指到末尾的链表）
        # l=len(lists)
        # i=0
        # while i < l:
        #     if not lists[i]: 
        #         lists.pop(i)
        #         # i-=1
        #         l-=1
        #     else:
        #         i+=1
        # if not lists: return None
        # # 找到列表中所有链表头节点中最小的
        # m=lists[0]
        # mindex=0
        # for i in range(len(lists)):
        #     if lists[i].val<m.val:
        #         m=lists[i]
        #         mindex=i
        # # print(m)
        # ret=m # 返回最小的
        # lists[mindex]=lists[mindex].next # 最小链表的表头指向下一位
        # ret.next=self.mergeKLists(lists) #递归
        # return ret


        # v2 通过 
        # 处理初始的空链表，保证传入recursion的lists不包含空链表
        l=len(lists)
        i=0
        while i <  l:     
            if not lists[i]:
                lists.pop(i)
                l-=1
            else:
                i+=1

        def recursion(lists):
            if not lists: return None
            m=lists[0]
            mindex=0
            l=len(lists)
            for i in range(len(lists)):
                if not lists[i]:
                    popList.append(i)
                    continue
                if lists[i].val<m.val:
                    m=lists[i]
                    mindex=i

            ret=m # 返回最小的
            lists[mindex]=lists[mindex].next # 最小链表的表头指向下一位
            if not lists[mindex]: # 如果为空则删掉
                lists.pop(mindex)
            ret.next=recursion(lists) #递归
            return ret    
                
        return recursion(lists)