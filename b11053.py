# 11053 가장 긴 증가하는 부분 수열

n = int(input())
list_ = list(map(int, input().split()))

## DP 이용한 경우 -> 시간복잡도 O(n^2)
dp = [0]*(n+2)

for i in range(n):
    dp[i] = 1 ## 증가하는 부분 수열 개수 (1은 자기 자신)
    for j in range(i):
        if list_[j] < list_[i]: ## 해당 자리까지의 리스트 원소중 i번째 자리값보다 작은 수가 있으면
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


