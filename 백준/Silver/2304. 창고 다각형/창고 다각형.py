# [2304] 창고 다각형

import sys
input = sys.stdin.readline

N = int(input())

rec = [list(map(int, input().split())) for _ in range(N)]
rec = sorted(rec, key=lambda x:(x[0], x[1]))

max_idx, max_hei = rec[-1][0], rec[-1][1]
mid_idx, mid_hei = sorted(rec, key=lambda x:x[1])[-1]
min_idx, min_hei = rec[0][0], rec[0][1]

answer = 0
# 왼쪽 계산

tmp = min_hei
for i in range(min_idx, mid_idx):
    for r in rec:
        if r[0] == i:
            tmp = max(tmp, r[1])
    answer += tmp

answer += mid_hei

# 오른쪽 계산
tmp = max_hei
for i in range(max_idx, mid_idx, -1):
    for r in rec:
        if r[0] == i:
            tmp = max(tmp, r[1])
    answer += tmp

print(answer)