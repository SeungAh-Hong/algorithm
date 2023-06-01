# [25630] 팰린드롬 소떡소떡
import sys
input = sys.stdin.readline

n = int(input())
st = input()
ans = 0
for i in range(n//2):
    if st[i] != st[n-i-1]:
        ans += 1

print(ans)