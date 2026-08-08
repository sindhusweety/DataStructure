"""
lfu cache
cache size = 2
put - retrive (cache)
put - 1, 7 (cache{1: 7})
put 2, 8 cache {1: 7, 2: 8}

get 1 -> 7  frequency  +1; otherwise -1 

put 3, 9 - > exceeded the limit of size ,
eliminate least frequently used 
in which 2 is lfu 

Here, the goal is to obtain O(1) 
"""
from collections import defaultdict
class Node:
    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        
        self.freq = 0
        
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0
        
    def add_node(self, node):
        
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node #here current node become head + tail's reference linked to the current node
        self.head.next = node # here current node become tail + head's reference linked to the current node
        self.size += 1 
    
    
    def remove_node(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.size -= 1
        
    def remove_last(self):
        
        if self.size == 0:
            return None
            
        node = self.tail.prev
        self.remove_node(node)
        
        return node
        
     
    def traversed(self):
        
        current = self.head.next
        while current.key >0:
            print(
            f"Key={current.key}, "
            f"Value={current.value}, "
            f"Freq={current.freq}"
        )
            current =current.next 
        

class LFUCache():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.size = 0
        self.key_map = {}
        self.freq_map = defaultdict(DoublyLinkedList)
    
    def update_frequency(self, node):
        
        old_freq = node.freq
        
        #remove node from old frequency list
        self.freq_map[old_freq].remove_node(node)
        
        if old_freq == self.min_freq and self.freq_map[old_freq].size == 0:
            self.min_freq += 1  
            
        node.freq += 1
        
        self.freq_map[node.freq].add_node(node)
        
        
        
        
        
    def get(self, key):
        
        if key not in self.key_map:
            return -1
            
        node = self.key_map[key]
        self.update_frequency(node)
        
        return node
        
        
    def put(self, key, value):
        
        if self.capacity == 0:
            return 
        
        # Update existing key
        if key in self.key_map:

            self.key_map[key].value = value
            return

        # Cache full -> remove LFU node
        if self.size == self.capacity:

            node_to_remove = self.freq_map[self.min_freq].remove_last()
            
            del self.key_map[node_to_remove.key]

            self.size -= 1
            
        
        
        new_node = Node(key, value)
        self.key_map[key] = new_node
        
        self.freq_map[0].add_node(new_node)
        
        #print(self.freq_map[self.min_freq].head.next.key, self.freq_map[self.min_freq].head.next.value)
        
        self.size += 1
        
        
    
    def traverse(self):
        
        for i in self.freq_map:
            print(f'Hash Map Node: {str(i)}')
            self.freq_map[i].traversed()
            print(" ")
        
        
cache = LFUCache(3)
cache.put(1, 7)
cache.put(2, 8)
cache.put(3, 9)
print("STAGE 1: Put Method & Traverse")
cache.traverse()
print("-------------------------")
print()
print("STAGE 2: GET Method & Traverse")
cache.get(1)

cache.traverse() #O(n)
print()
print("STAGE 3: Put Method & Traverse")
cache.put(4, 9)
cache.traverse() #O(n)


"""
STAGE 1: Put Method & Traverse
Hash Map Node: 0
Key=3, Value=9, Freq=0
Key=2, Value=8, Freq=0
Key=1, Value=7, Freq=0
 
-------------------------

STAGE 2: GET Method & Traverse
Hash Map Node: 0
Key=3, Value=9, Freq=0
Key=2, Value=8, Freq=0
 
Hash Map Node: 1
Key=1, Value=7, Freq=1
 

STAGE 3: Put Method & Traverse
Hash Map Node: 0
Key=4, Value=9, Freq=0
Key=3, Value=9, Freq=0
 
Hash Map Node: 1
Key=1, Value=7, Freq=1
 """
