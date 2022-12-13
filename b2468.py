## 백준 2468 안전 영역 (BFS/DFS)

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

ans = []
max_rain = max(max(area))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(a, b, rain):
    x, y = a, b
    rain = rain
    queue = deque()
    queue.append([x, y])
    check[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and area[nx][ny] > rain and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append([nx, ny])
            else:
                continue

ans = 1
for rain in range(max_rain+1):
    ret = 0
    check = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > rain and check[i][j] == 0:
                BFS(i, j, rain)
                ret += 1
                # print("rain:", rain, "ret:", ret)
                # for i in range(n):
                #     print(check[i])
    ans = max(ans, ret)

print(ans)