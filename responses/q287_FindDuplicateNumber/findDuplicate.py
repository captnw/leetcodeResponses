class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N) complexity, O(1) space
        # We can use Floyd's cycle detection to detect the duplicate number in O(N) time
        # You can see this array of intengers [1, n] as pointers, so given a number in one cell
        # We can hop to another element. Also note that since the range begins with 1, no cell points
        # to cell 0, so the starting point of this linked list would be cell 0.

        # The first part is having a fast and slow pointer, this two pointer approach is 
        # to detect a cycle in a linked list, but in our case we'll be using it to set up for our second part.

        fast = slow = 0 # we start at index 0

        slow = nums[slow] # move once
        fast = nums[nums[fast]] # move twice (twice as fast as slow)
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # At this point fast and slow are at the same index, within the cycle. If we consider this array of numbers/indices
        # as a linked list, the entry node into the cycle would be the duplicate number, because there are two nodes that
        # are pointing to it. 

        # Now we'll work with our old slow pointer at the current location, and a new slow pointer at the 0th node. 
        # There is an equation that proves that this works (look it up), but essentially if we march our old slow pointer 
        # and new slow pointer at the same speed of one node per iteration, they'll eventually meet up at the entry cycle node.
        # The old slow pointer may make it rounds around the cycle (depending how long the path up to the cycle is), but it'll
        # eventually meet the new slow pointer. We'll then return the value of the entry node, the duplicate number.

        newSlow = 0
        while newSlow != slow:
            newSlow = nums[newSlow]
            slow = nums[slow]

        return newSlow