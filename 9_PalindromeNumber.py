# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # # v1 str compare
        # if x>=0:
        #     listx=list(str(x))
        #     for i in range(len(x)//2):
        #         if listx[i]!=listx[-i-1]:
        #             return False
        #     return True
        # return False
        
        # # v1.1 str compare enhanced, no need to convert str into list
        # if x>=0:
        #     strx=str(x)
        #     for i in range(len(strx)//2):
        #         if strx[i]!=strx[-i-1]:
        #             return False
        #     return True
        # return False

        # # v1.3 no need to check if x>0 while checking the string
        #     strx=str(x)
        #     for i in range(len(strx)//2):
        #         if strx[i]!=strx[-i-1]:
        #             return False
        #     return True

        # v2 copied
        # a str can be reversely indexed by [::-1]  
        return str(x) == str(x)[::-1] 

        # # v3 copied
        # if x<0 or (x>0 and x%10==0):
        #     return False
        # reversedNum=0
        # while x>reversedNum:
        #     reversedNum=reversedNum*10+x%10
        #     # print(reversedNum)
        #     x=x//10
        #     # print(x)
        # if x==reversedNum or x==reversedNum//10:
        #     return True
        # return False

