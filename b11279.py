## 11279. 최대 힙 (우선순위 큐)

# 배열에 자연수 x를 넣음
# 배열에서 가장 큰 값을 출력 후, 배열에서 제거

import sys
input = sys.stdin.readline
from heapq import  heappop, heappush

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-x, x))
