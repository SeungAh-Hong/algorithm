## 5014 스타트링크 (DFS/BFS)

import sys
input = sys.stdin.readline
from collections import deque

f, start, end, up, down = map(int, input().split())
## 백만층까지 ㄱㄴ

## start => end 까지의 최소값
visit = [0]*(f+1)
queue = deque()
isUp = 0
isDown = 0

if up:
    isUp = 1
if down:
    isDown = 1

def circle(start):
    global visit
    queue.append(start)
    while queue:
        idx = queue.popleft()
        if idx == end:
            break
        nup = idx+up
        ndown = idx-down
        if 0< nup <= f and visit[nup]==0 and isUp == 1: ## f층까지밖에 못올라감 !!!!!
            visit[nup]=visit[idx]+1
            #print("nup",nup,"visit[nup]",visit[nup])
            queue.append(nup)
        if f >= ndown > 0 and visit[ndown]==0 and isDown == 1: ## 0층은 못내려감!!
            visit[ndown]=visit[idx]+1
            #print("ndown",ndown,"visit[ndown]",visit[ndown])
            queue.append(ndown)

            
circle(start)

# print(visit)
if start == end:
    print(0)
elif visit[end] == 0:
    print("use the stairs")
else:
    print(visit[end])
