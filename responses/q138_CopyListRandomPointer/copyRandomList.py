"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(N) complexity, O(N) space
        # We'll be doing this with a cache (dict) and a previous pointer to hold the previous new node, in one pass
        # We'll be using the original nodes as keys, since their values are not guarenteed to be unique

        # Hash the old node with the corresponding new node
        # During every iteration, do the following:
        # 1) Check if the current original node has a corresponding new node
        # 2) If step 1 is false, create a new node (without copying the next and random pointers), and store in cache
        # 3) Assign the previous new node's next properter to this new node
        # 4) Access the random pointer of the current original node, check if that node has a corresponding new node
        # 5) If step 4 is false, create a new node (for the node at the random pointer), and store in cache

        cache = dict()
        previousNewNode = None
        ptr = head # don't change head, we need it if we want to return the head of the new list

        while ptr:
            # declaring these variables here so they'll be accessible outside the if statements
            newNode = randomNewNode = None 
            if ptr in cache:
                newNode = cache[ptr]
            else:
                newNode = Node(ptr.val)
                cache[ptr] = newNode # associate the original node with the new node

            # update the previousNewNode's next value as long as it's not nullish
            if previousNewNode:
                previousNewNode.next = newNode
            previousNewNode = newNode

            # Fetch the random new node or create it as long it's not nullish
            if ptr.random in cache:
                randomNewNode = cache[ptr.random]
            elif ptr.random: # null check
                randomNewNode = Node(ptr.random.val)
                cache[ptr.random] = randomNewNode

            newNode.random = randomNewNode # update the current newNode's random property            
            ptr = ptr.next

        return cache[head] if head else None