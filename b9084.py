## 백준 9084. 동전
### DP, Knapsack
from sys import stdin 
tc= int(stdin.readline())

for t in range(tc):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    # print(coins)
    money = int(stdin.readline())
    dp = [0] * (money+1)
    dp[0] = 1 ## 0원을 만들 수 있는 경우의 수는 무조건 1

    for coin in coins:
        for m in range(1, money+1):
            if m >= coin:
                dp[m] += dp[m-coin]

    print(dp[money])