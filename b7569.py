import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

#box = [[[0]*(m) for _ in range(n)] for _ in range(h)]
boxes = []
queue = deque()

for i in range(h):
    box = []
    for j in range(n):
        box.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if box[j][k] == 1:
                queue.append([i, j, k]) ## h, n, m
    boxes.append(box)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while(queue): ## BFS
    z, y, x = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nz<h and 0<=ny<n and 0<=nx<m:
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = boxes[z][y][x]+1
                queue.append((nz, ny, nx))

day = 0
for i in range(h): 
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                print(-1)
                exit(0)
        day = max(day, max(boxes[i][j]))

if day == 1:
    print(0)
else:
    print(day-1)