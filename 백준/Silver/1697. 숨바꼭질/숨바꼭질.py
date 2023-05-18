# [1697] 숨바꼭질
from collections import deque

N, K = map(int, input().split())
INF = 1e9
time = [0]*(100001)
time[N] = 0

def BFS(idx):
    queue = deque()
    queue.append(idx)
    while queue:
        idx = queue.popleft()
        if idx == K:
            return time[K]
        if 0<= idx+1 < 100001 and time[idx+1] == 0:
            time[idx+1] = time[idx]+1
            queue.append(idx+1)
        if 0 <= idx-1 < 100001 and time[idx-1] == 0:
            time[idx-1] = time[idx]+1
            queue.append(idx-1)
        if 0<= idx*2 < 100001 and time[idx*2] == 0:
            time[idx*2] = time[idx]+1
            queue.append(idx*2)

    return time[K]

print(BFS(N))