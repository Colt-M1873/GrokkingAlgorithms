# https://leetcode.com/problems/plus-one/discuss/24091/Easy-Python-solution-O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # v1 dumb carry
        # digits[-1]+=1
        # carry=0
        # for i in range(len(digits)-1,-1,-1):
        #     if digits[i]+carry==10:
        #         digits[i]=0
        #         carry=1
        #     else:
        #         digits[i]+=carry
        #         carry=0
        #         break
        # if carry==1:
        #     digits.insert(0,carry)
        # return digits    
        
        # v2 copied  clean and brilliant
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

        # # v3 copied  oneliner map list element to str and join to one str convert 
        # # to int and plus one and convert to str and map back to int list
        # return list(map(int, str(int(''.join(map(str,digits)))+1)))