import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = A-B
ans = sorted(ans)
print(len(ans))
for aa in ans:
    print(aa, end=' ')
