# 백준 9663 N-Queen (브루트포스, 백트래킹)

import sys
input = sys.stdin.readline
N = int(input())

isused1 = [False]*(2*N+1) # 위아래
isused2 = [False]*(2*N+1) # 왼쪽 대각선
isused3 = [False]*(2*N+1) # 오른쪽 대각선

ans = 0
def n_queen(x):
    global ans
    if x == N:
        ans += 1
        return
    
    for i in range(N):
        if isused1[i] or isused2[x+i] or isused3[x-i+N-1]:
            continue
        isused1[i] = True
        isused2[x+i] = True
        isused3[x-i+N-1] = True
        n_queen(x+1)
        isused1[i] = False
        isused2[x+i] = False
        isused3[x-i+N-1] = False

n_queen(0)
print(ans)
"""
row = [0] * N # 열 하나당 무조건 퀸 하나만 둘 수 있음
def isOk(x): # 퀸 둘 수 있는지 확인
    for i in range(x):# 현재까지 두어진 퀸들이 지나가는 길 확인
        # 대각선끼리 겹치면 안됨 -> row[x]-row[i] != x-i
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    
    return True

ans = 0
def n_queen(x):
    global ans
    if x == N:
        ans += 1
        return

    for i in range(N):
        row[x] = i # 만약 [x, i] 에 퀸을 놓는다면?
        if isOk(x): # 확인
            n_queen(x+1) # 되면 그 다음줄로 넘어감

n_queen(0)

print(ans)
"""