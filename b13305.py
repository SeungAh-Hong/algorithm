## 13305 주유소 (그리디)

import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
val = list(map(int, input().split()))

ans = 0
v = sys.maxsize
for i in range(n-1):
    dis = dist[i]
    v = min(val[i], v)
    ans += (dis*v)

print(ans)