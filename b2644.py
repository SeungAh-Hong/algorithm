from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())


## a에서 b까지 line 개수 계산, 없으면 -1
def BFS(start, end):
    cnt = 0
    queue = deque()
    queue.append(start)
    depth[start]=0
    while queue:
        idx = queue.popleft()
        if idx == end:
            return depth[end]
        for i in range(1, n+1):
            if graph[idx][i]==1 and depth[i]==0:
                cnt+=1
                depth[i] = depth[idx]+1
                queue.append(i)
        


graph = [[0]*(n+2) for _ in range(n+2)]
depth = [0]*(n+2)
for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

answer = BFS(a, b)
if answer==None:
    print(-1)
else:
    print(answer)
