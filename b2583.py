# 2583 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())

## M : x, N : y
arr = [[0]*(N) for _ in range(M)]

for i in range(K):
    y1, x1, y2, x2 = map(int, input().split())

    ## 정사각형 값 arr에 채우기
    # 원래 파이썬 배열 : 0,0 <-> 입력 배열 : m-1, n-1
    ## 아래대로 입력해서 출력해보면 문제 배열이랑 같게 나옴
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1
    

# for i in range(M):
#     print(arr[i])
# print("--------------")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(i, j):
    global cnt
    global tmp
    queue = deque()
    queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        arr[x][y] = cnt  # 맨 처음 값도 변경해줘야 함
        tmp += 1
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = cnt
                    queue.append([nx, ny])
    
    return tmp

# 영역 개수 구함
cnt = 2
# while any(0 in l for l in arr):
answer = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            tmp = 0
            answer.append(BFS(i, j))
            cnt += 1

# for i in range(M):
#     print(arr[i])

print(cnt-2)
# 오름차순 정렬 출력
answer = sorted(answer)
for a in answer:
    print(a, end=' ')

