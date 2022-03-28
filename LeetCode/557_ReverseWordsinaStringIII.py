# https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
# 2021 11.25

class Solution:
    def reverseWords(self, s: str) -> str:
        # # v1 split and join
        # list1=s.split(' ')
        # for i in range(len(list1)):
        #     list1[i]=list1[i][::-1]
        # return ' '.join(list1)
        
        # v1.1 copied oneliner split and join
        return ' '.join(x[::-1] for x in s.split())
        
        # # v1.2 copied oneliner using lambda
        # return " ".join(map(lambda x: x[::-1], s.split()))