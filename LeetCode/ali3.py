
def func3(s:str):
    if not s: return True
    l=len(s)
    if s[:l//2]==s[l//2:] and l%2==0 and s[0]==s[l//2]=='c':
        print('Yes')
        return True
    if  s[1:l//2]==s[l//2+1:l-1] and l%2==1 and s[0]==s[-1]=='b' and s[l//2]=='a':
        print('Yes')
        return True
    print('No')
    return False

# print(func3('caca'))
# print(func3('bsadaasadab'))
print(func3('cbabcbab'))
print(func3('bcba'))
print(func3('ss'))