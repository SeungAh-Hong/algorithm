# 2579 계단 오르기
n = int(input())

arr = [0 for i in range(301)] ## 이렇게 안하면 IndexError 남
dp = [0 for i in range(301)]

for i in range(0, n): # 0~n-1
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2]) ## 조건 2

for i in range(3, n): #3~n-1
    # 조건 3
    ## 1. 마지막 계단 -1 밟은 경우
    a = dp[i-3] + arr[i-1] + arr[i]
    ## 2. 마지막 계단 -2 밟은 경우
    b = dp[i-2] + arr[i]
    dp[i] = max(a, b)

print(dp[n-1])