# 18869 멀티버스 Ⅱ (좌표 압축)

import sys
input = sys.stdin.readline

from bisect import bisect_left

M, N = map(int, input().split())

uni = []
for _ in range(M):
    uni.append(list(map(int, input().split())))

set_uni = []
for m in range(M):
    set_uni.append(sorted(list(set(uni[m]))))

## 값 크기 순으로 변환 ( == 좌표압축)
real_uni = [[0]*N for _ in range(M)]
for m in range(M):
    for n in range(N):
        # idx = set_uni[m].index(uni[m][n])
        idx = bisect_left(set_uni[m], uni[m][n])
        real_uni[m][n] = idx

# for m in range(M):
#     print(uni[m])
#     print(set_uni[m])
#     print(real_uni[m])

ans = 0
for i in range(M-1):
    for j in range(i+1, M):
        if real_uni[i] == real_uni[j]:
            ans += 1

print(ans)
