## 1012 유기농배추
import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def BFS(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if field[x][y] != 1:
            continue
        field[x][y] = 0
        for i in range(4):
            nx = dx[i]+x # 세로
            ny = dy[i]+y # 가로
            if 0<=nx<N and 0<=ny<M and field[nx][ny] == 1:
                queue.append([nx, ny])

for t in range(tc):
    M, N, K = map(int, input().split()) ## M 가로 N 세로
    field = [[0]*(M) for _ in range(N)]
    ans = 0
    for k in range(K): ## 입력 넣어줌
        a, b = map(int, input().split())
        field[b][a] = 1
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                BFS(i, j)
                ans+=1

    print(ans)