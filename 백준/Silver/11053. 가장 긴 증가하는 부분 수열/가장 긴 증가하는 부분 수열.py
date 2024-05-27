# 백준 11053: https://www.acmicpc.net/problem/11053
# DP (LIS)

n = int(input())
array = list(map(int, input().split()))

dp = [1]*n

for now in range(1, n):
    for before in range(now):
        if array[now] > array[before]:
            dp[now] = max(dp[now], dp[before]+1)
        elif array[now] == array[before]:
            dp[now] = max(dp[now], dp[before])
        else: # n[now] < n[before]
            continue # 1로 그대로 둠

print(max(dp))