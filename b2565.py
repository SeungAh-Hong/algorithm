n = int(input())

line = []
for i in range(n):
    a, b = map(int, input().split())
    line.append([a, b])

line.sort(key=lambda x:x[0]) ## 첫 번째 값 기준 정렬

lis = [0]*(n+2)
for i in range(n):
    lis[i+1] = line[i][1]

dp = [0]*(n+2)
for i in range(1, n+1):
    dp[i] = 1
    for j in range(1, i):
        if lis[j] <= lis[i]:
            dp[i] = max(dp[j]+1, dp[i])


print(n-max(dp))