## 2667 단지번호붙이기
import sys
input = sys.stdin.readline
n = int(input())
apt = []

for i in range(n):
    apt.append(list(map(int, input().rstrip())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def DFS(i, j):
    global cnt
    global apt_code
    x, y = i, j
    apt[x][y] = apt_code
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<n and 0<=ny<n and apt[nx][ny]==1:
            cnt+=1
            apt[nx][ny] = apt_code
            DFS(nx, ny)

ans_cnt=[]
apt_code = 2 ## 2부터 넣어주기
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            cnt=1
            DFS(i, j)
            apt_code+=1
            ans_cnt.append(cnt)


print(apt_code-2)
ans_cnt.sort()
for a_cnt in ans_cnt:
    print(a_cnt)