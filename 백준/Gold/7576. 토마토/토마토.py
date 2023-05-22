# 7576 토마토
import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


queue = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            queue.append([i, j])

if cnt == m*n:
    print(0)
    exit(0)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx,ny])

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(arr[i]))

print(ans-1)