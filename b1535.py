from sys import stdin

n = int(stdin.readline())

L = []
L.extend(list(map(int, stdin.readline().split())))
L.insert(0, 0)
J = []
J.extend(list(map(int, stdin.readline().split())))
J.insert(0, 0)

dp = [[0]*(101) for _ in range(n+1)]
# 인사 횟수 당 최대 체력까지의 dp 배열에 기쁨 최대값을 넣음
dp[0][0] = 0

for i in range(1, n+1): ## 인사 한번~인사 전부 까지의 모든 경우의 수
    hp = L[i]
    happy = J[i]
    for j in range(1, 101): ## 인사 n번일 때 최대 허용 체력까지의 기쁨 최대값 구함
        if j >= hp:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp] + happy)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])