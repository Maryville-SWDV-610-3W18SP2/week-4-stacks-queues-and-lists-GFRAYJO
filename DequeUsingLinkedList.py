class _Node:
    
    __slots__ = '_object', '_prev', '_next'
    
    def __init__(self,object,prev,next):
        self._object = object
        self._prev = prev
        self._next = next
        
class Deque:
         
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self.size = 0
        
    def len(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def insert_between(self,obj,predecessor,successor):
        newObj = self._Node(obj,predecessor, successor)
        predecessor._next = newObj
        successor._prev = newObj
        self.size +=1
        return newObj
    
    def delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self.size -= 1
        object = node.object
        node._prev = node._next = node.object = None
        return object
        
        

        
