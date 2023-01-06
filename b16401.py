# 과자 나눠주기

import sys
input=sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

start = 0
end = max(snacks)

while(start <= end):
    mid = (start + end) // 2
    target = 0 # 과자 최대 길이

    if mid == 0:
        ans = 0
        break

    for snack in snacks:
        if snack >= mid:
            target += (snack//mid)
    
    if target >= m:
        start = mid + 1
        ans = mid
    else:
        end  = mid - 1

print(ans)