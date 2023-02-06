import sys
input = sys.stdin.readline

K, P, N = map(int, input().split())

ans = K
for _ in range(N):
    ans *= P
    ans %= 1000000007

print(ans)