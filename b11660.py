# 구간 합 구하기 5 (DP, 누적 합)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

dp = [[0]*(n+1) for _ in range(n+1)] ## 누적 합 저장해둘 배열

## dp 배열은 1부터 시작
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1] + nums[i-1][j-1]


for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)