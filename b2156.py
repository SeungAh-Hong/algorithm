
n = int(input())
grape = [0] * (n+2)
for i in range(n):
    grape[i] = int(input())

dp = [0] * (n+2)
dp[0] = grape[0]
dp[1] = grape[0] + grape[1]

## 현재 잔 마시는 경우 -> 이전 잔 O, 이전 잔 X
### dp[i-3]+grape[i-1]+grape[i]
### dp[i-2]+grape[i]
## 현재 잔 안마시는 경우
### dp[i-1]
dp[2] = max(grape[0]+grape[2], grape[1]+grape[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-3]+grape[i-1]+grape[i], dp[i-2]+grape[i], dp[i-1])

print(dp[n-1])