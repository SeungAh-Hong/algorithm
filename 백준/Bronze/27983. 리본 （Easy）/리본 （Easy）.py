# [27893] 리본(Easy)
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
l = list(map(int, input().split()))
c = list(map(str, input().split()))
flag = False
answer = []
for i in range(n):
    for j in range(i+1, n):
        if abs(x[i] - x[j]) <= (l[i] + l[j]) and c[i] != c[j]:
            flag = True
            answer = (i+1, j+1)
            break

if not flag:
    print("NO")
else:
    print("YES")
    print(*answer)