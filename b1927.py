## 1927 최소 힙

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
heap = []
for i in range(n):
    x= int(input())
    if x!=0:
        heappush(heap, x)
    elif not heap:
        print(0)
    else:
        print(heappop(heap))
