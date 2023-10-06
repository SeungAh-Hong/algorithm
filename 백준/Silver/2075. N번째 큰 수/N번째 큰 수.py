## 2075 N번째 큰 수
import sys
input = sys.stdin.readline
n = int(input())

from heapq import heappop, heappush
heap = []

list1 = list(map(int, input().split()))
for i in list1:
    heappush(heap, i)

for i in range(1,n): ## 입력값 받자마자 최소값 계속 비교
    list2 = list(map(int, input().split()))
    for j in range(n):
        if list2[j] > heap[0]:
            heappop(heap)
            heappush(heap, list2[j])

print(heap[0])