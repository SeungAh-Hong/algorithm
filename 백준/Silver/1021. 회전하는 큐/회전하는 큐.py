import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
want = list(map(int, input().split()))

q = deque()
for i in range(1, n+1):
    q.append(i)

cnt = 0

for num in want:
    while 1:
        if q[0] == num:
            q.popleft()
            break
        else:
            if q.index(num) <= len(q)//2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1

print(cnt)

