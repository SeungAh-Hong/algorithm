import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
want = deque()
for _ in range(n):
    want.append(int(input()))

stack = deque()
# 1 2 3 4 5 6 7 8
# 4 3 6 8 7 5 2 1
# + + + + -
idx = 0
answer = []
flag = True
while want:
    if idx > n:
        flag = False
        break
    if stack and want[0] == stack[-1]:
        answer.append("-")
        want.popleft()
        stack.pop()
    else:
        idx += 1
        answer.append("+")
        stack.append(idx)

if flag == False:
    print("NO")
else:
    for ans in answer:
        print(ans)