Step-by-Step Explanation

Input:

2 1 1
1 1 0
0 1 1

Legend:

2 = Rotten
1 = Fresh
0 = Empty
Step 1

Create variables

queue = deque()
fresh_count = 0
minutes = 0

Think:

queue       -> Rotten oranges waiting to spread

fresh_count -> Fresh oranges remaining

minutes     -> Time taken
Step 2

Scan entire grid

for r in range(rows):
    for c in range(cols):

Cell:

(0,0) = 2

Add to queue

queue.append((0,0))

Queue:

[(0,0)]

Count fresh oranges

Fresh positions:

(0,1)
(0,2)
(1,0)
(1,1)
(2,1)
(2,2)

Count:

fresh_count = 6

State after traversal

queue = [(0,0)]
fresh_count = 6
minutes = 0
Why BFS?

Because rotting spreads like:

Virus
Fire
Infection

These are BFS problems.

Minute 1

Queue:

[(0,0)]

Length:

1

Process only these oranges.

for _ in range(len(queue)):

Means:

Process current minute only

Take out:

r,c = queue.popleft()

(0,0)

Check directions

Down:

(1,0)

Fresh?

Yes

Rot it:

grid[1][0] = 2
fresh_count -= 1
queue.append((1,0))

Right:

(0,1)

Fresh?

Yes

Rot it.

Queue becomes:

[(1,0),(0,1)]

Fresh:

4

Minute complete

minutes += 1

Now:

minutes = 1

Grid

2 2 1
2 1 0
0 1 1
Minute 2

Queue:

[(1,0),(0,1)]

Length:

2

Process BOTH.

From:

(1,0)

Rot:

(1,1)

From:

(0,1)

Rot:

(0,2)

Queue becomes:

[(1,1),(0,2)]

Fresh:

2

Minutes:

2

Grid

2 2 2
2 2 0
0 1 1
Minute 3

Process:

[(1,1),(0,2)]

Rot:

(2,1)

Queue:

[(2,1)]

Fresh:

1

Minutes:

3
Minute 4

Process:

[(2,1)]

Rot:

(2,2)

Queue:

[(2,2)]

Fresh:

0

Minutes:

4

Loop stops because:

fresh_count == 0

Return:

4
Most Important Interview Concept

Why do we use:

for _ in range(len(queue))

instead of:

while queue

Because:

Each BFS Level = 1 Minute

If we process newly rotten oranges immediately:

Minute 1
↓
Minute 2 oranges also processed
↓
Wrong answer

We need:

Current Level
↓
Finish
↓
minutes += 1
↓
Next Level

Rotting Oranges

Pattern:
Multi-Source BFS

Queue:
All rotten oranges

Target:
Fresh oranges

Level:
1 minute

When fresh orange found:
1. Make rotten
2. Reduce fresh count
3. Add to queue

Time:
O(m*n)

Space:
O(m*n)