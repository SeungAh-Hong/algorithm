# 백준 1697. 숨바꼭질
import math
from collections import deque

n, k = map(int, input().split())
INF = math.inf
time = [0]*(100001)
time[n] = 0

def BFS(idx):
    queue = deque()
    queue.append(idx)
    while queue:     
        if idx == k:
            return time[k]
        idx = queue.popleft()
        if 0 <= idx+1 < 100001 and time[idx+1] == 0:
            time[idx+1] = time[idx]+1
            queue.append(idx+1)
        if 0 <= idx-1 < 100001 and time[idx-1] == 0:
            time[idx-1] = time[idx]+1
            queue.append(idx-1)  
        if 0 <= 2*idx < 100001 and time[idx*2] == 0:
            time[2*idx] = time[idx]+1
            queue.append(2*idx)

    return time[k]

print(BFS(n))
