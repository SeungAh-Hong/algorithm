# 2932 표 회전
## 메모리초과 ㅜ

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

matrix = [[0]*N for _ in range(N)]
tmp = 0
for i in range(N):
    for j in range(N):
        tmp += 1
        matrix[i][j] = tmp

def row_move(x, cm): # 행 회전
    tmp = []
    for i in range(N):
        idx = (i-cm)%N 
        tmp.append(matrix[x][idx])
    matrix[x] = tmp
    return 0

def column_move(y, rm): # 열 회전
    tmp = []
    for i in range(N):
        idx = (i-rm)%N
        tmp.append(matrix[idx][y])
    
    for i in range(N):
        matrix[i][y] = tmp[i]
    return 0


while K != 0:
    X, R, C = map(int, input().split())
    R -= 1
    C -= 1 # index니까 -1 해줘야 함
    # 현재 x의 좌표값 구함
    idx = [[i, j] for i in range(N) for j in range(N) if matrix[i][j] == X]
    x, y = idx[0]
    #print(x, y)
    rm = R-x # 열 회전 수
    if rm < 0: # 만약 0보다 작으면 N만큼 더해줘야 함
        rm += N
    cm = C-y # 행 회전 수
    if cm < 0:
        cm += N

    ans = rm+cm
    
    row_move(x, cm) # C열이 될 때까지 X가 있는 행 회전
    # for a in range(N):
    #     print(matrix[a])
    column_move(C, rm) # R행이 될 때까지 X가 있는 열 회전
    # for a in range(N):
    #     print(matrix[a])

    print(ans)
    K-=1
