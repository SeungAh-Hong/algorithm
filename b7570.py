# 7570 줄 세우기

import sys
input=sys.stdin.readline

c_num = int(input())
ch = list(map(int, input().split()))

## 연속된 증가수열을 제외한 모든 어린이들을 이동
dp = [0]*(c_num+1)

for i in range(c_num):
    dp[ch[i]] = dp[ch[i]-1] + 1 # 연속된 증가 수열 구함

dp = sorted(dp)
print(c_num - max(dp))