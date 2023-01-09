# 7570 줄 세우기

import sys
input=sys.stdin.readline

c_num = int(input())
ch = list(map(int, input().split()))

## 연속된 증가수열을 제외한 모든 어린이들을 이동
### 1 3 5 2 4 인 경우
### 연속되는 증가 수열은 (1, 2) 와 (3, 4) 존재
### 결국 값은 5 - 2 = 3 임
dp = [0]*(c_num+1)

for i in range(c_num):
    dp[ch[i]] = dp[ch[i]-1] + 1 # 연속된 증가 수열 구함
## ch[i] 값에 대해 ch[i]-1 에 대한 수가 이미 나왔다면 longest length가 ++되는 것임

print(c_num - max(dp))