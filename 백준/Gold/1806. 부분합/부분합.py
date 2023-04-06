# [1806] 부분합 (골드4) / 누적 합, 두 포인터
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(0) #

l, r, ts = 0, 0, 0
ans = sys.maxsize

while r <= N: #
    if ts < S:
        ts += nums[r]
        r+=1
    else:
        ans = min(ans, r-l)
        ts -= nums[l]
        l+=1
        
print(ans if ans != sys.maxsize else 0)

"""
반례
10 10
1 1 1 1 1 1 1 1 1 1
"""