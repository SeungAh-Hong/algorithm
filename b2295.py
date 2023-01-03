## 백준 2295 세 수의 합

import sys
input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

## 3중 for문으로 하면... 시간초과

## 2중 for문 -> a+b = d-c

# a,b,c가 모두 같아도 됨
## 중복없이 받기
ab = set() ## set
for a in nums:
    for b in nums:
        ab.add(a+b)


## 가장 큰 k번째 수를 출력 (== d)
# -> a+b = d-c 만족하는 경우가 있으면 d를 ans에 넣어줌
# 마지막에 ans에서 제일 큰 값 print
ans = set() ## 중복 제거
# a+b = d-c
for d in nums:
    for c in nums:
        if (d-c) in ab: ## 있으면 dict에 추가!
            ans.add(d)

ans = sorted(ans, reverse=True)
print(ans[0])