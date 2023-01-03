# 백준 2170 선 긋기 (정렬, 스위핑 / 그리디)
import sys
input = sys.stdin.readline

n = int(input())
dot = []
for i in range(n):
    a, b = map(int, input().split())
    dot.append([a, b])

dot = sorted(dot, key=lambda x:(x[0], x[1]))

#print(dot)

start, end = dot[0]
result = 0
for i in range(1, n):
    nx, ny = dot[i]
    if end >= nx:
        end = max(end, ny) ## 더 큰 값을 end로 넣어줘야 함!
    else:
        result += (end-start)
        start, end = dot[i]
result += (end-start)
print(result)