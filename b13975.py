# 13975 파일 합치기 3

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

tc = int(input())

for test in range(tc):
    n = int(input())
    heap = []
    doc = list(map(int, input().split()))
    for i in range(n): ## 입력 heapq에 정렬
        heappush(heap, doc[i])
    ans = 0
    if len(heap) == 0:
        print(0)
    else:
        while len(heap) > 1:
            a = heappop(heap)
            b = heappop(heap)
            next = a+b
            ans += next
            heappush(heap, next)
        print(ans)