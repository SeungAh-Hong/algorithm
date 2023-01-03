## 11726 2xn 타일링 (DP)
### 배열로 풀면 index error로 안풀림
n = int(input())
dp = [0, 1, 2]

if n<=3:
    print(n)
    exit(0)

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n]%10007)