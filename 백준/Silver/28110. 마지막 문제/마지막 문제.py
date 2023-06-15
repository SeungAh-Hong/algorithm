import sys
input = sys.stdin.readline

n = int(input())
levels = list(map(int, input().rstrip().split()))
levels.sort()

flag = False
ans = 0
gap = -1

for i in range(n-1):
    target = (levels[i] + levels[i+1]) // 2
    if target != levels[i]:
        if min(target-levels[i], levels[i+1]-target) > gap :
            ans = target
            gap = min(target-levels[i], levels[i+1]-target)


if gap != -1:
    print(ans)
else:
    print(-1)