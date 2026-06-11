# DSA Pattern Cheat Sheet

| Pattern                    | Questions                                                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| HashMap / Frequency Count  | Character Frequency, Valid Anagram, First Non-Repeating Character, Two Sum, Top K Frequent Elements, Top K Frequent Words |
| Set Pattern                | Contains Duplicate, Remove Duplicates, Common Elements in Arrays, Longest Substring Without Repeating Characters          |
| Two Pointers               | Move Zeroes, Remove Duplicates from Sorted Array, Valid Palindrome                                                        |
| Fixed Sliding Window       | Maximum Sum Subarray of Size K, Maximum Average Subarray                                                                  |
| Variable Sliding Window    | Longest Substring Without Repeating Characters, Longest Subarray Sum = K                                                  |
| String Traversal           | Longest Common Prefix, Prefix Check, Suffix Check                                                                         |
| Reverse Traversal          | Reverse String, Reverse Words                                                                                             |
| Running Max / Running Min  | Largest Element, Smallest Element, Second Largest Element, Best Time to Buy and Sell Stock                                |
| Prefix / Suffix Pattern    | Product of Array Except Self                                                                                              |
| Sorting Pattern            | Group Anagrams, Valid Anagram using Sort, Second Largest using Sort                                                       |
| Binary Search              | Binary Search, Search Insert Position, First Occurrence, Last Occurrence                                                  |
| Heap (Priority Queue)      | Kth Largest Element, Top K Frequent Elements                                                                              |
| Queue                      | Implement Queue, Queue using Two Stacks, Number of Recent Calls                                                           |
| BFS (Queue Based)          | Level Order Traversal, Number of Islands, Rotting Oranges                                                                 |
| Graph Traversal            | Number of Islands, Clone Graph                                                                                            |
| Brute Force → Optimization | Two Sum, Product of Array Except Self, Longest Substring Without Repeating Characters, Buy & Sell Stock                   |

---

# Pattern Recognition Cheat Sheet

```text
Count / Frequency / Occurrence     → HashMap

Duplicate Detection                → Set

Need Unique Elements               → Set

Need Faster Lookup                 → HashMap / Set

Move Elements in Array             → Two Pointers

Sorted Array Problems              → Two Pointers / Binary Search

Search in Sorted Array             → Binary Search

Find First / Last Occurrence       → Binary Search

Kth Largest / Top K                → Heap

Contiguous Subarray                → Sliding Window

Contiguous Substring               → Sliding Window

Longest / Shortest Window          → Variable Sliding Window

Window Size = K                    → Fixed Sliding Window

Largest / Maximum Profit           → Running Max

Smallest / Minimum                 → Running Min

Prefix / Suffix Product            → Prefix-Suffix Pattern

Anagrams                           → Sorting / HashMap

Need Processing in Arrival Order   → Queue

FIFO Requirement                   → Queue

Level-by-Level Traversal           → BFS + Queue

Graph/Matrix Traversal             → BFS / DFS

Need Highest Priority Element      → Heap

Need Ordered Comparison            → Sorting
```

---

# Time Complexity Cheat Sheet

```text
Dictionary Lookup     → O(1)

Set Lookup            → O(1)

Heap Push             → O(log n)

Heap Pop              → O(log n)

Queue Append          → O(1)

Queue Popleft         → O(1)

List Append           → O(1)

String Concatenation  → O(n)

Sorting               → O(n log n)

Binary Search         → O(log n)

Array Traversal       → O(n)

Sliding Window        → O(n)

Two Pointers          → O(n)

BFS                   → O(V + E)

DFS                   → O(V + E)

Nested Loops          → O(n²)
```

---

