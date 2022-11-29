## 11399 ATM
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()
time = 0
tmp = 0
for i in range(n):
    tmp += p[i]
    time += tmp
print(time)