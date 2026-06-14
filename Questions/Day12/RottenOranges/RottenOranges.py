# Question 1: Rotting Oranges
# Pattern:
# BFS + Queue
#Input:
grid = [
[2,1,1],
[1,1,0],
[0,1,1]
]
Output= 4

from collections import deque

def orangesRotting(grid):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    fresh_count = 0
    minutes = 0

    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    # Step 1: Find rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 2:
                queue.append((r,c))

            elif grid[r][c] == 1:
                fresh_count += 1

    # Step 2: BFS
    while queue and fresh_count > 0:

        for _ in range(len(queue)):

            r,c = queue.popleft()

            for dr,dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 1
                ):

                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr,nc))

        minutes += 1

    return minutes if fresh_count == 0 else -1


grid = [
[2,1,1],
[1,1,0],
[0,1,1]
]

print(orangesRotting(grid))
