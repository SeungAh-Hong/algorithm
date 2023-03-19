# [7795] 먹을 것인가 먹힐 것인가 (실버 3)
import sys
import bisect
input =sys.stdin.readline
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    idx = 0
    answer = 0
    for a in A:
        idx = bisect.bisect_left(B, a)
        #print(idx)
        answer += idx
    print(answer)
