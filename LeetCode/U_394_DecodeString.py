class Solution:
    def decodeString(self, s: str) -> str:
        # recursive first get all non-parentesised letters done
        # then strip the patenthesis to get letters inside,
        # then send those inside letters through regression
        ls=list(s)
        ret=''
        i=0
        repeatstr=''
        while i < len(ls):
            if ls[i]>='a' and ls[i]<='z':
                ret=ret+ls[i]
            else:
                repeatnumstr=''
                while ls[i]>='0' and ls[i]<='9':
                    repeatnumstr+=ls[i]
                    i+=1
                repeatnum=int(repeatnumstr)
                print('repeatnum')
                print(repeatnum)
                substr=''
                stack=[]
                stack.append(ls[i])
                i+=1
                while stack:
                    if ls[i]=='[':
                        stack.append(ls[i])
                    elif ls[i]==']':
                        stack.pop()
                    substr+=ls[i]
                    i+=1
                ret=ret+repeatnum*self.decodeString(substr。strip)
            i+=1
        return ret