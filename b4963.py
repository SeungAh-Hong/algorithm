## 4963. 섬의 개수
from collections import deque
import sys
read = sys.stdin.readline

def BFS(x, y): ## 사이클 수 세기
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [-1, 1, 0, 0, 1, -1, 1, -1]

    test[x][y] = 0
    queue = deque()
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < h and 0 <= ny < w and test[nx][ny] == 1:
                queue.append([nx, ny])
                test[nx][ny] = 0

while 1:
    w, h = map(int, read().split())
    if w==0 and h==0:
        break
    test = []
    cnt = 0
    for i in range(h):
        test.append(list(map(int, read().split())))
    for i in range(h):
        for j in range(w):
            if(test[i][j] == 1): ## 땅이 있을 때
                BFS(i, j) ## BFS 돌림
                cnt+=1
    
    print(cnt)