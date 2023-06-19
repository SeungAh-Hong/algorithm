# [1446] 지름길
import sys
input = sys.stdin.readline
N, D = map(int, input().split())

dp = [0]*(D+1)
for i in range(D+1):
    dp[i] = i

shortcut = []
for i in range(N):
    shortcut.append(list(map(int, input().split())))

shortcut.sort(key=lambda x:(x[1], x[0]))

for start, end, dist in shortcut:
    if end <= D and dp[end] > dp[start]+dist: # 현재 지름길이 원래 길보다 짧으면 update
        dp[end] = dp[start]+dist
        cnt = 1
        for i in range(end+1, D+1): # 이후 길들도 지름길 사용하도록 update
            dp[i] = dp[end]+cnt
            cnt+=1


print(dp[D])