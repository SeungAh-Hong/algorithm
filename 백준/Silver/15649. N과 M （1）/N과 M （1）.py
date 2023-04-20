# 1564 N과 M(1) # 백트래킹
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
# 1~n까지 자연수 중에서 중복 없이 m개를 고른 수열

# 방법 2. 백트래킹 구현
arr = [] # 각 조합 하나씩 구해서 바로바로 출력
isused = [0]*(n+1)
def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if isused[i] == 1:
            continue
        isused[i] = 1
        arr.append(i)
        backtracking()
        arr.pop()
        isused[i] = 0

backtracking()