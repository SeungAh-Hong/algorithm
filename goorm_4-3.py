n = int(input())
dp = [[0]*5 for i in range(n+1)]

for i in range(5):
    dp[1][i] = 1 ## 처음 경우의 수는 언제나 1

for i in range(2, n+1):
    ## 0: XXX
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4])%100000007
    ## 1: OXX
    dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3])%100000007
    ## 2: XOX
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4])%100000007
    ## 3: XXO
    dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%100000007
    ## 4: OXO
    dp[i][4] = (dp[i-1][0] + dp[i-1][2])%100000007

answer = 0
for i in range(5):
    answer += dp[n][i]
## 마지막 answer 도 100000007 나머지 구해야 함
print(answer%100000007)

