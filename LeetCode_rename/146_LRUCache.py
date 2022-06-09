# https://leetcode.com/problems/lru-cache/
# 2022年05月23日 14:07:54

# v1 slow, 1519ms, 80.5Mb

class Node:
    def __init__(self,k,x):
        # 双向链表的一端没有prev，一端没有next
        self.prev=None
        self.key=k
        self.val=x
        self.next=None

class LRUCache:
    # hashmap + double linked list
    def __init__(self, capacity: int):
        self.cap=capacity
        self.dict={} # hashmap
        self.head=None # most recent, pointing the head of double linked list
        self.tail=None # least recent, pointing the tail of double linked list
        pass
    
    def move_to_top(self,node):
        self.head.next=node
        node.prev=self.head
        self.head=node
        pass
    
    def get(self, key: int) -> int:
        # print(self.dict)
        # self.printfrombottom()
        # ret value & promote the priority in tehe double linked list
        if key in self.dict:
            # if dict[key] isnot head
            if key == self.head.key:
                pass     
            elif key == self.tail.key:
                # detatch tail
                newtail=self.tail.next
                self.tail.next=None
                # move to head
                self.move_to_top(self.tail)
                # new tail
                self.tail=newtail
            else:
                # detatch node from linked list
                pNode=self.dict[key].prev
                nNode=self.dict[key].next
                self.dict[key].next=None
                self.dict[key].prev=None
                pNode.next=nNode
                nNode.prev=pNode
                # link back to head
                self.move_to_top(self.dict[key])
            return self.head.val
        # if key not exist
        return -1
        pass
        
    def put(self, key: int, value: int) -> None:
        # if key already exist, update the value and promote it to head
        if key in self.dict:
            # update its value
            self.dict[key].val=value
            # promote to head
            self.get(key)
        else: # if new key
            # check if capacity limit reached, if so, delete tail
            if len(self.dict)>=self.cap:
                # del the least recent one, i.e, the tail
                # print("over capacity, old tail deleted {}, maybe".format(self.tail.val))

                newtail=self.tail.next
                del self.dict[self.tail.key]
                self.tail = newtail
            # put new node into head
            self.dict[key]=Node(key,value)
            if not self.tail:
                self.tail=self.dict[key]
            if not self.head:
                self.head=self.dict[key]
            else:
                self.move_to_top(self.dict[key])
            # print("a new item put")        
            
            
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# can also use OderedDict in Collection package instead of finishe it by yourself




# v2 copied using builtin OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
