# [2003] 수들의 합 2 (실버 4)
import sys
input=sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
# 이 수열의 i번째 수부터 j번째 수까지의 합 == M이 되는 경우의 수

ans, l, r, tmp = 0, 0, 0, 0

while l < N and r < N:
    tmp = sum(A[l:r+1])
    if tmp < M:
        r += 1
    elif tmp == M:
        ans += 1
        l += 1
    else:
        l += 1

print(ans)