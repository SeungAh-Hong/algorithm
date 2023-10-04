# [1926] 그림 (실버1)

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(paper, a, b):
    queue = deque()
    queue.append((a, b))
    paper[a][b] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx and nx < n and 0 <= ny and ny < m and paper[nx][ny] == 1:
                count += 1
                paper[nx][ny] = 0
                queue.append((nx, ny))
    return count

paint = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            pic = bfs(paper, i, j)
            paint.append(pic)
            

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))