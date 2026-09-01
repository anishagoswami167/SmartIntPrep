# Clone Graph
# Pattern:
# BFS + HashMap
# Learn:
# 	• Graph traversal
# 	• Visited dictionary
# 	• Queue
node = [[2,4],[1,3],[2,4],[1,3]]
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []
def cloneGraph(node):
    if not node:
        return None
    queue=deque([node])
    visited={}
    visited[node]=Node(node.val)
    
    while queue:
        current=queue.popleft()
    for n in current.neighbors:
        if n not in visited:
            visited[n]=Node(n.val)
            queue.append(n)
        visited[current].neighbors.append(visited[n])
    return visited[node]
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone graph
cloned = cloneGraph(node1)

# Check output
print(cloned.val)
for neighbor in cloned.neighbors:
    print(neighbor.val)    
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        