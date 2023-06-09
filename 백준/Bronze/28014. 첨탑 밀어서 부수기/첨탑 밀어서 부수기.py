# [28014] 첨탑 밀어서 부수기
import sys
input=sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

ans = 1
for i in range(N-1):
    if  H[i] <= H[i+1]:
        ans += 1

print(ans)
