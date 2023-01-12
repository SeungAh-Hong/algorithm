# 11053 가장 긴 증가하는 부분 수열 (DP)

## 00:13 시작 00:54 끝

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N # 자기 자신값 1

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
        elif A[i] == A[j]:
            dp[i] = max(dp[i], dp[j]) ### 중간에 값이 같은 경우도 max로 잡아야 함
             
       
#print(dp)
print(max(dp))

""" 반례
20
31 84 18 62 35 77 23 53 60 94 3 77 60 51 42 18 83 85 63 51

# 18 23 53 60 77 83 85
ans : 7
"""