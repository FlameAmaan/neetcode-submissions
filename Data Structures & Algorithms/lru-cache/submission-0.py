class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None
class LRUCache:
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next=nxt
        node.prev=prev
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} #map key to node
        #left is LRu and right is MRU
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]   
            self.remove(node)
            self.insert(node)             
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            #remove from left
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
