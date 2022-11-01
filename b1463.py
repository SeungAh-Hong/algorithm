n = int(input())

dp = [0]*(n+1)


# 10 : 10->5->4->2->1 (4)
# 10 : 10->9->3->1 (3)

for i in range(2, n+1): # Bottom-Up
    dp[i] = dp[i-1]+1
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1) # 비교
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1) # 비교

print(dp[n])
