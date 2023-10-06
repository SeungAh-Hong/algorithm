import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque()
ans = []
for _ in range(n):
    cmd = input()
    if "push" in cmd:
        cmd, num = cmd.split()
        q.append(num)
    else:
        if "pop" in cmd:
            if q:
                ans.append(q.popleft())
            else:
                ans.append(-1)
        if "size" in cmd:
            ans.append(len(q))
        if "empty" in cmd:
            if q:
                ans.append(0)
            else:
                ans.append(1)
        if "front" in cmd:
            if q:
                ans.append(q[0])
            else:
                ans.append(-1)
        if "back" in cmd:
            if q:
                ans.append(q[-1])
            else:
                ans.append(-1)

for a in ans:
    print(a)