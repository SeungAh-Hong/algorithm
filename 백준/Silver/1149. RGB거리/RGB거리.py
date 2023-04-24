## 1149 RGB 거리 (DP)
import sys
input = sys.stdin.readline

n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

# dp = [[0]*n for _ in range(n)]
# ## 모든 경우의 수 구함
# dp[0][0] = cost[0][0]
# dp[0][1] = cost[0][1]
# dp[0][2] = cost[0][2]

# for i in range(1, n):
#     dp[i][0] = min(dp[i-1][1]+cost[i][0], dp[i-1][2]+cost[i][0])
#     dp[i][1] = min(dp[i-1][0]+cost[i][1], dp[i-1][2]+cost[i][1])
#     dp[i][2] = min(dp[i-1][0]+cost[i][2], dp[i-1][1]+cost[i][2])
    
for i in range(1, n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

    
print(min(cost[n-1]))