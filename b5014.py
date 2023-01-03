## 5014 스타트링크 (DFS/BFS)

import sys
input = sys.stdin.readline
from collections import deque

f, start, end, up, down = map(int, input().split())
## 백만층까지 ㄱㄴ

## start => end 까지의 최소값
visit = [0]*(f+1)
queue = deque()
ud = [up, (-down)]

def circle(start):
    global visit
    queue.append(start)
    while queue:
        idx = queue.popleft()
        if idx == end:
            break
        
        for i in range(2):
            next = idx + ud[i]
            if i==0 and up==0:
                continue
            if i==1 and down==0:
                continue
            if 0 < next <= f and visit[next] == 0:
                visit[next] = visit[idx]+1
                queue.append(next)

            
circle(start)

if start == end:
    print(0)
elif visit[end] == 0:
    print("use the stairs")
else:
    print(visit[end])
