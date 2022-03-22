# https://leetcode.com/problems/simplify-path/
# 2022 3.15

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # # v1 using str.split
        # a=[]
        # folders=path.split('/')
        # print(folders)
        # for i in range(len(folders)):
        #     if folders[i]=='.' or folders[i]==''  :
        #         continue
        #     elif folders[i]=='..':
        #         if a :
        #             a.pop()
        #         else:
        #             continue
        #     else:
        #         a.append(folders[i])
        # a.insert(0,'')
        # a.append('')
        # ret='/'.join(a);
        # if len(ret)<2:
        #     return '/'
        # else:
        #     return ret[:-1]
        

        # v1.1 copied more clean 
        stack=[]
        for item in path.split('/'):
            if stack and item=='..':
                stack.pop()
            elif item not in ['','.','..']:
                stack.append(item)
        return '/'+'/'.join(stack)