

class ListNode:

    def __init__(self, key = 0, val: int = 0, next: 'ListNode' | None = None, prev: 'ListNode' | None = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class DList:

    def __init__(self):
        self.head = ListNode(key=-1, val=-1)
        self.tail = ListNode(key=-2, val=-2)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def append(self, node: ListNode):
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next= self.tail
        self.tail.prev = node
    
    def remove(self, node: ListNode):
        assert node is not self.head
        assert node is not self.tail
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
    
    def popfront(self) -> ListNode:
        node = self.head.next
        self.remove(node)
        return node




class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._size = 0
        self._store = {}
        self._dlist = DList()

    def get(self, key: int) -> int:
        node = self._store.get(key)
        if node is None:
            return -1
        self._dlist.remove(node)
        self._dlist.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._store:
            node = self._store[key]
            node.val = value
            self._dlist.remove(node)
            self._dlist.append(node)
        else:
            node = ListNode(key=key, val=value)
            self._store[key] = node
            self._dlist.append(node)
            self._size += 1
    
        if self._size > self.capacity:
            n = self._dlist.popfront()
            del self._store[n.key]
            self._size -= 1
        
        

def main():
    c = LRUCache(3)
    print('get 3', c.get(3))
    c.put(3, "a")
    print('get 3', c.get(3))

    c.put(4, 'b')
    c.put(5, 'c')
    print('get 3', c.get(3))
    print('get 4', c.get(4))
    print('get 5', c.get(5))
    c.put(6, 'cat')
    print('get 3', c.get(3))
    print('get 6', c.get(6))
    print('get 4', c.get(4))
    print('get 5', c.get(5))
    c.put(6, 'dog')
    print('get 6', c.get(6))
    print('get 4', c.get(4))
    print('get 5', c.get(5))

main()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
