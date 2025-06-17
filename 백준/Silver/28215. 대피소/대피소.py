
# 28215 (실버4)
# 구현, 브루트포스알고리즘, 시뮬레이션
from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
x_arr = []
y_arr = []

for i in range(n):
    tmp_x, tmp_y = map(int, input().split())
    x_arr.append(tmp_x)
    y_arr.append(tmp_y)

comb = list(combinations(range(n), k))
answer = 1e9

for c in comb: # c: 대피소 후보들 idx
    case = 0 # 후보별 가장 먼 거리
    for home_idx in range(n): # 집별로 돌기
        distance = 1e9
        for h in c: # 대피소 후보까지 min 거리
            tmp = abs(x_arr[home_idx] - x_arr[h]) + abs(y_arr[home_idx] - y_arr[h])
            distance = min(distance, tmp)

        case = max(case, distance) # 집-후보 거리 최대값 저장

    answer = min(answer, case)

print(answer)

