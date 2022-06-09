# https://leetcode.com/problems/design-hashset/
# 2022 4.02

class MyHashSet(object):
    s=[]
    def __init__(self):
        self.s=[]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            self.s.append(key)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.s)):
            if self.s[i]==key:
                self.s.pop(i)
                break
        
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.s
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)