## 7562 나이트의 이동
import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())

dx = [1, 2, -1, -2, 1, 2, -1, -2]
dy = [2, 1, 2, 1, -2, -1, -2, -1]

def BFS(start, end):
    global cnt
    queue = deque()
    sx, sy = start
    ex, ey = end
    queue.append([sx, sy])
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            return chess[ex][ey]
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<L and 0<=ny<L:
                if chess[nx][ny] != 0:
                    continue
                chess[nx][ny] = chess[x][y] + 1
                if nx == ex and ny == ey:
                    return chess[ex][ey]
                queue.append([nx,ny])

for testcase in range(tc):
    L = int(input())
    chess = [[0]*L for _ in range(L)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    ## 최소 이동 거리 구하기
    print(BFS(start, end))