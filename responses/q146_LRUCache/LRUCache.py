class DoublyLinkedNode:
    # The linked list needs to be doubly linked, otherwise we cannot do O(1) deletions of the LRU node from the linked list
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

    def __str__(self):
        # For debugging purposes
        head = self

        rep = []
        while head:
            rep.append(head.key)
            head = head.next

        return str(rep)

class LRUCache:
    # Two data structures, hashmap, and doubly linked list linked list
    # We'll be using the hashmap for its O(1) time lookup and insertions
    # We'll be using the doubly linked list to store the order of recently used keys from most recent, to least recent
    # So we'll have a head pointer and a tail pointer as well.

    def __init__(self, capacity: int):
        self._maxSize = capacity
        self._cache = {}
        self._head = None
        self._tail = None

    def __insertNodeAtHead(self, listNode: DoublyLinkedNode):
        # Insert a node at the beginning of the linked list
        if not self._head:
            self._head = self._tail = listNode
        else:
            # insert node at beginning of linked list
            self._head.prev = listNode
            listNode.next = self._head
            self._head = listNode

    def __removeNodeAndMoveToHead(self, listNode: DoublyLinkedNode):
        # Remove the node from the linked list and append it to the front of the linekd list
        if listNode == self._head:
            return # linked list of size 1, not much else you can do

        prevNode = listNode.prev
        nextNode = listNode.next

        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
        else:
            # this is the tail, move it back to the previous node
            self._tail = prevNode

        self.__insertNodeAtHead(listNode)

    def get(self, key: int) -> int:
        if key in self._cache:
            # Remove this node from LL and insert at head
            # We'll doing this because we're interacting with the node, so it should be the most recently updated node
            # AKA at the head pointer
            listNode = self._cache[key][1]
            self.__removeNodeAndMoveToHead(listNode)

            return self._cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            listNode = self._cache[key][1]
            self._cache[key] = (value,listNode) # update the cache
            
            # Remove this node from LL and insert at head
            # We'll doing this because we're interacting with the node, so it should be the most recently updated node
            # AKA at the head pointer
            self.__removeNodeAndMoveToHead(listNode)
        else:
            listNode = DoublyLinkedNode(key)
            self._cache[key] = (value,listNode) # insert new entry into cache

            self.__insertNodeAtHead(listNode)
        
        #print(key, value, self._head, len(self._cache))

        if len(self._cache) > self._maxSize:
            # Remove the last node from the linked list and the cache
            del self._cache[self._tail.key]
            self._tail.prev.next = None
            self._tail = self._tail.prev

        #print(self._head)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)