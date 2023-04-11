# [13423] Three Dots (실버2)

import sys
input = sys.stdin.readline
import bisect

def BS(l, r, t):
    while l<=r:
        m = (l+r)//2
        if X[m] == t:
            return 1
        elif X[m] > t:
            r = m-1
        else:
            l = m+1
    return 0

T = int(input())
while T:
    N = int(input())
    X = list(map(int, input().split()))
    ans = 0
    X.sort()
    l, r = 0, N-1
    for i in range(N-1):
        for j in range(i+1, N):
            dist = abs(X[j]-X[i])
            if BS(l, r, X[j]+dist):
                ans+=1
    print(ans)
    T-=1