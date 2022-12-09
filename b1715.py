# 1715 카드 정렬하기 (우선순위 큐)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    heappush(heap, int(input()))

ans = 0

if len(heap)==1 or len(heap)==0:
    print(0)
    exit(0)

while 1: ## 앞 2개 더해서 heap에 넣어줌
    if len(heap) < 2:
        break
    one = heappop(heap)
    two = heappop(heap)
    next = one+two
    ans += next
    heappush(heap, next)

print(ans)