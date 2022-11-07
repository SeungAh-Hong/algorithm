## 10844 쉬운 계단 수

n = int(input())
dp = [[0]*(10) for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1): # 2~n
    for j in range(10): # 0~9
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

answer = sum(dp[n]) % 1000000000

print(answer)
## 0 1 2 3 4 5 6 7 8 9 (끝자리 수 기준)
#n=1,
## 1 1 1 1 1 1 1 1 1 1
#n=2,
## 1 1 2 2 2 2 2 2 2 1
#n=3,
## 1 3
#n=4,
## 3