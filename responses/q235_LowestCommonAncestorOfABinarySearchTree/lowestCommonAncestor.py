# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The idea is to keep track of the "path" as we iterate to find p and q, and store them in stacks
        # The first element of the stack is always the root, and the stack can grow as large as log n (height of BST tree)
        
        # If the lengths of the stacks are unequal, we pop from the larger height until they're both equal
        # Consider the following:

        # Given root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 7
        # The paths to reach p and q are: [6,2], and [6,8,7]
        # 7 can't be an ancestor to 2, because 7's height exceeds 2's height.

        # Once the heights of both stacks are the sample, we compare the last elements for both stacks
        # 1) If they're the same, return the last element as the answer (lowest common ancestor)
        # 2) If they're NOT the same, pop both elements from the stacks and continue comparing

        # Time complexity: O(log N), because searching for p and q are both O(log N), and comparing the stacks
        # (which can only be at most log N length) is also O(log N)
        # Space complexity: O(log N), the stacks that stores the path to p and q can only be at most O(log N)

        # Iterative approach below:
        pPath = [root]
        qPath = [root]

        temp = root # Find p and store the path to get to there O(log N)
        while temp != p:
            if temp.val < p.val:
                temp = temp.right
            else:
                temp = temp.left
            pPath.append(temp)

        temp = root # Find q and store the path to get to there O(log N)
        while temp != q:
            if temp.val < q.val:
                temp = temp.right
            else:
                temp = temp.left
            qPath.append(temp)

        if len(pPath) != len(qPath):
            # Pop from the larger stack until the larger stack's length is equivalent to that of the smaller stack
            # O(log N) because either stack can only be as large as the height of the BST tree O(log N)
            for _ in range(len(pPath),len(qPath),-1):
                pPath.pop()
            
            for _ in range(len(qPath),len(pPath),-1):
                qPath.pop()

        # Iterate until the last nodes of both stacks are equivalent O(log N)
        while pPath[-1] != qPath[-1]:
            pPath.pop()
            qPath.pop()
        return pPath[-1] # They're equivalent, and we're guarenteed to have an LCA according to constraint