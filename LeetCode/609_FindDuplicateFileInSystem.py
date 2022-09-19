# https://leetcode.com/problems/find-duplicate-file-in-system/
# 2022年09月19日 20:32:00

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={} # hash:pathlist
        ret=[]
        for pstr in paths:
            arr=pstr.split()
            path=arr[0]+'/'
            # print(arr)
            for i in range(1,len(arr)):
                name,content=arr[i].split('(')
                # print(name,content)
                ha=hash(content)
                if ha not in d:
                    d[ha]=[path+name]
                else:
                    d[ha].append(path+name)
        # print(d)
        for k in d:
            if len(d[k])>1:
                ret.append(d[k])
        return ret
            
            