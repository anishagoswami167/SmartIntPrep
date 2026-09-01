#Approach
# Store all request timestamps in a queue.
# Add the current request.
# Remove all timestamps older than:
# t - 3000
# Return the number of remaining requests.


from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t):

        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)


rc = RecentCounter()

print(rc.ping(1))      # 1
print(rc.ping(100))    # 2
print(rc.ping(3001))   # 3
print(rc.ping(3002))   # 3


# Time Complexity

# Each timestamp:

# Added once
# Removed once

# So overall:

# O(1) amortized per ping()

# Space Complexity
# O(n)

# where n is the number of requests currently inside the 3000 ms window.