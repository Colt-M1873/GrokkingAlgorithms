# https://leetcode.com/problems/the-number-of-good-subsets/

from cmath import sqrt


class Solution:
    def isPrime(self,n:int) -> bool:
        # pro version, copied
        # 1. to check if n is prime, common method is to see if n%i==0 for every i<n
        # 2. sqrt(n): 
        #     non-prime number n can be seen as p1*p2 where p1<=sqrt(n) and p2>=sqrt(n)
        # so for a number n we can just calculate from 1 to sqrt(n) to check if n is prime
        # 3. 6x-1 and 6x+1:
        #     x is an interger, all prime number except 2 and 3 can be denoted by 6x-1 or 6x+1. 
        # because 6x+2 can be divided by 2, 6x+3 can be divided by 3, 6x+4 can be divided by 2,
        # only 6x+1 and 6x-1 (i.e. 6x+5) are possible to be a prime number. So we dont neet to 
        # check every i<n, just jump by 6 when i>5
        if n<4:
            return n!=1
        if n%6!=1 and n%6!=5:
            return False
        nroot=int(n**0.5)
        for i in range(5,nroot+1,6):
            if n%i==0 or n%(i+2)==0 :
                return False
        return True

    # def numberOfGoodSubsets(self, nums: List[int]) -> int:
        

s=Solution()
j=0
for i in range(1,100):
    if s.isPrime(i):
        print(i)
        j+=1

print("j",j)