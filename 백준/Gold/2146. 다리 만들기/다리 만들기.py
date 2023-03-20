# [2146] 다리 만들기 (골드 3)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
islands = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def indexing_island(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        islands[x][y] = idx
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and islands[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])

def find_island(z):
    global answer
    dist = [[-1]*N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if islands[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<N and 0<=ny<N and dist[nx][ny] == -1:
                # 다른 땅
                if islands[nx][ny] != z and islands[nx][ny] < 0:
                    answer = min(answer, dist[x][y])
                # 바다
                if islands[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])

idx = -1
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if islands[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            indexing_island(i, j)
            idx -= 1

answer = 1e9

for i in range(-1, idx, -1):
    find_island(i)


print(answer)

