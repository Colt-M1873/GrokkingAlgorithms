# https://leetcode.com/problems/design-hashmap/submissions/
# 2022年04月04日 16:33:31

# # v1 using list and tuple, too slow 
# class MyHashMap(object):
#     def __init__(self):
#         self.m=[]

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         elemtuple=(key,value)
#         for i in range(len(self.m)):
#             if self.m[i][0]==key:
#                 self.m[i]=elemtuple
#                 return None
#         self.m.append(elemtuple)
#         return None
        
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         for item in self.m:
#             if item[0]==key:
#                 return item[1]
#         return -1
        
#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         for i in range(len(self.m)):
#             if self.m[i][0]==key:
#                 self.m.pop(i)
#                 break
        
# # Your MyHashMap object will be instantiated and called as such:
# # obj = MyHashMap()
# # obj.put(key,value)
# # param_2 = obj.get(key)
# # obj.remove(key)

