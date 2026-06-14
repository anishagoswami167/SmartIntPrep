# Level Order
# Level by Level
# Minimum Steps
# Shortest Path
# Nearest

#Think of BFS+Queue

#Binary Tree Level Order Traversal
#Input:
root = [3,9,20,None,None,15,7]
Output=[[3],[9,20],[15,7]]

from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    
def levelOrder(root):
        if not root:
            return []
        queue=deque([root])
        result=[]
        
        while queue:
            level_size=len(queue)
            level=[]
            for _ in range(level_size):
                node=queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
        
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

print(levelOrder(root))

#Time Complexity: O(n)
#Space Complexity: O(n)