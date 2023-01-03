## 백준 11000 강의실 배정

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
lec = []
for i in range(N):
    lec.append(list(map(int, input().split())))

lec = sorted(lec, key=lambda x:(x[0], x[1])) ## 종료 시간 먼저 정렬
heap = []
heappush(heap, lec[0][1]) ## 처음 값 넣어줌

for i in range(1, N):
    start = lec[i][0]
    end = lec[i][1]
    if start < heap[0]:
        heappush(heap, end)
    else: ## update
        heappop(heap)
        heappush(heap, end)

print(len(heap))