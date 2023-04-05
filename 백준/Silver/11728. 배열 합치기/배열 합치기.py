# [11728] 배열 합치기
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

p1, p2 = 0, 0
ab_plus = deque()

while p1 < N and p2 < M:
    pv1 = A[p1]
    pv2 = B[p2]

    if pv1 <= pv2:
        ab_plus.append(pv1)
        p1 += 1
    else:
        ab_plus.append(pv2)
        p2 += 1

while p1 < N:
    ab_plus.append(A[p1])
    p1+=1

while p2 < M:
    ab_plus.append(B[p2])
    p2+=1

print(*ab_plus)

