## 백준 18870 좌표 압축 (이분 탐색)

import sys
input = sys.stdin.readline
import bisect

N = int(input())

X = list(map(int, input().split()))

## set으로 받아서 중복 삭제 후 정렬
Xlist = sorted(list(set(X)))
# print(Xlist)

## X를 정렬했을 때, X보다 앞에 있는 수의 개수를 출력하면 됨
for x in X: ## lowerbound 값(idx 값)을 출력
    ans = bisect.bisect_left(Xlist, x)
    if ans <= 0:
        print(0, end=' ')
    else:
        print(ans, end=' ')
