# 15903 카드 합체 놀이 (그리디, 우선순위 큐)

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n, m = map(int, input().split())

cards = list((map(int, input().split())))
heap = []
for card in cards:
    heappush(heap, card)

if m==0:
    print(sum(heap))
    exit(0)

for i in range(m):
    a = heappop(heap)
    b = heappop(heap)
    next = a+b
    heappush(heap, next)
    heappush(heap, next)

print(sum(heap))