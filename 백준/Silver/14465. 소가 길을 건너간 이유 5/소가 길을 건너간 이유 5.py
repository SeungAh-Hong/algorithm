# [14465] 소가 길을 건너간 이유 5 (실버 2)
import sys
input = sys.stdin.readline
# 1이 연속 K개가 되기 위해 고쳐야 하는 최소 신호등의 수
N, K, B = map(int, input().split())
lights = [-1]+[1]*(N)
for b in range(B):
    err = int(input())
    lights[err] = 0

tmp=sum(lights[1:K+1])
ans = K-tmp
for r in range(K+1, N+1):
    tmp += lights[r]
    tmp -= lights[r-K]
    ans = min(ans, K-tmp)
    if ans <= 0:
        break


if ans <= 0:
    print(0)
else:
    print(ans)