import sys

n, k = map(int, input().split())

value = [0]*n
for i in range(n):
    value[i] = int(sys.stdin.readline())


value.sort(reverse=True)
ans = 0
for i in value:
    ans += k//i
    k -= (k//i)*i

print(ans)