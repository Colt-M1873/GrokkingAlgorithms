# # int process(string str, int k) {
# # 	set<char>visited;
# # 	int count = 0;
# # 	string res = "";
# # 	for (int i = 0; i < str.size(); ++i) {
# # 		if (visited.find(str[i]) == visited.end()) {//如果没有访问过，直接加入set中
# # 			visited.insert(str[i]);
# # 		}
# # 		string temp = "";
# # 		temp += str[i];
# # 		for (int j = i + 1; j < str.size(); ++j) {
# # 			if (visited.find(str[j]) == visited.end()) {
# # 				visited.insert(str[j]);
# # 			}
# # 			if (visited.size() <= k) {//如果里面存放的元素个数小于等于k，继续
# # 				temp += str[j];
# # 				res = res.size() > temp.size() ? res : temp;
# # 			}
# # 			else {//否则清空之
# # 				visited.clear();
# # 				break;
# # 			}
# # 		}
# # 	}
# # 	return res.size();



# def func(s:str):
#     cost1=0 # 101010
#     cost2=0 # 010101
#     for i in range(len(s)):
#         if i%2==0: # even
#             if s[i]=='0':
#                 cost1+=i+1
#             else: 
#                 cost2+=i+1
#         else: # odd
#             if s[i]=='0':
#                 cost2+=i+1
#             else:
#                 cost1+=i+1
#     return min(cost1,cost2)

# # print(func('11101'))




# def func3(n: int ,k :int, s:str):
#     d1={}
#     count=0
#     result=0
#     left=0
#     right=0
#     while right<len(s):
#         high=s[right]
#         if high not in d1:
#             d1[high]=0
#             count+=1
#         d1[high]+=1
#         right+=1 # 改回这里
#         if  count> k:
#             low=s[left]
#             '''
#             if d1[low]>1:
#                 d1[low]-=1
#             else:
#                 d1[low]-=1  # 新增这一行             
#                 count-=1
#             '''
#             d1[low]-=1
#             if(d1[low] == 0):
#                 count-=1

#             left+=1
#         result=max(result,right-left)
        
#     return result


# print(func3(12,2,'aabcdaaaaaaa'))
# print(func3(8,4,'aabcdbca'))
# print(func3(5,3,'aabcd'))




# # def fun4():
# #     #输入部分
# #     n,m,q=2,3,2
# #     mat1=['aBc','AaD']
# #     mat2=[[1,1,1,2],[1,2,2,3]]
# #     print(mat1,mat2)
# #     # 算法
# #     for row in mat2:
# #         x1=row[0]-1
# #         y1=row[1]-1
# #         x2=row[2]-1
# #         y2=row[3]-1
# #         print(mat1[x1][y1],mat1[x2][y2])
        


# def fun1(t:int):
#     d={}
#     for i in range(t):
#         name=input()
#         if len(name)>12 or len(name)<6:
#             print('illegal length')
#             return False
#         for item in list(name):
#             if not('a'<=item<='z' or 'A'<=item<='Z'):
#                 print('illegal character')
#                 return False
#         if name not in d:
#             d[name]=1
#         else:
#             print('account existed')
#             return False

# print(fun1(3))



def func3(s:str):
    if not s: return True
    l=len(s)
    # print(s[1:l//2])
    # print(s[l//2+1:l-1])
    
    if s[:l//2]==s[l//2:] and l%2==0 and s[0]==s[l//2]=='c':
        # print(s[:l//2])
        # print(s[l//2:])
        return True
    if  s[1:l//2]==s[l//2+1:l-1] and l%2==1 and s[0]==s[-1]=='b' and s[l//2]=='a':
        # print(s[l//2])
        return True
    return False



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