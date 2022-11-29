from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

## b의 가장 큰수 <-> a의 가장 작은 수
a.sort(reverse=True)
b.sort()

ans = 0
for i in range(n):
    ans += (a[i]*b[i])

print(ans)