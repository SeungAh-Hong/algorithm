# [16283] Farm (브론즈 1)
import sys
input = sys.stdin.readline

A, B, N, W = map(int, input().split())

answer = []
for x in range(1, 1001):
    for y in range(1, 1001):
        if x+y == N and (A*x) + (B*y) == W:
            answer.append([x, y])

a, b = 0, 0
if len(answer) != 1:
    print(-1)
else:
    a, b = answer[0]
    print(a, b)