## 11501 주식
import sys
input = sys.stdin.readline


tc=int(input())
while tc:
    n=int(input())
    costs=list(map(int, input().split()))
    ans = 0
    max_c = 0
    for c in reversed(costs):
        if max_c <= c:
            max_c = c
        else:
            ans += max_c - c
    print(ans)
    tc-=1