## 11286 절댓값 힙
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
queue = []
for i in range(n):
    x = int(input())
    if x != 0:
        heappush(queue, (abs(x), x))
    else:
        if not queue:
            print(0)
        else:
            print(heappop(queue)[1])
        
