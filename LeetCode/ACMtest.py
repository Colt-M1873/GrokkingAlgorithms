# 2022年04月24日 14:40:15
# ACM 模式 判断素数，通过


import math
def isprime(n:int):
    if n<2: return 'no'
    for i in range(2,int(math.sqrt(n))+1):
        # print('n%i',n,i,n%i)
        if n%i==0:
            return 'no'
    return 'yes'


a=input()
numlist=map(lambda x:int(x),a.split())
retlist=[]
for item in numlist:
    retlist.append(isprime(item))

print(' '.join(retlist))