# 11055 가장 큰 증가 부분 수열

## 22:35 시작 23:12 끝
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0]*N
# 값이 증가인 경우 : 이전 + 자신
# 값이 증가가 아닌 경우 : 
# # 자신보다 작은 값이던 A의 dp 값을 가져와서 더함

dp[0] = A[0]
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])
    dp[i] = max(dp[i], A[i]) # 이전에 작은 값이 없으면 자기자신 값 넣어줌

#print(dp)
print(max(dp))

## 반례
"""
5
5 1 2 3 10
"""

"""
6
5 2 10 13 21 17
"""