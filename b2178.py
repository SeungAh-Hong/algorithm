## 2178 미로 탐색
from collections import deque


n, m = map(int, input().split()) 
maze = []
# sys 사용하면 append 안됨 (ValueError 뜸)
## sys 사용하려면 # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 rstrip()으로 제거해줘야 함
for i in range(n):
    maze.append(list(map(int, input())))

# print(maze)


# (1, 1) 에서 끝까지 갔을 때 최소 칸 수
## [0, 0] -> [3, 5] [n-1, m-1]
check = [[0]*(m) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]  

def BFS(xy):
    queue = deque()
    queue.append(xy)

    while queue:
        xy = queue.popleft()
        x = xy[0]
        y = xy[1]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                nxy = (nx, ny)
                queue.append(nxy)
    return maze[n-1][m-1]


# def BFS(x, y):
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx, ny))
#     return maze[n-1][m-1]

start = (0, 0)
print(BFS(start))