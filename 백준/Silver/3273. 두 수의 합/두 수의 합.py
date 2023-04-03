# 3273 두 수의 합 (정렬, 투 포인터)

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr = sorted(arr)

left = 0
right = n-1
ans = 0

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == x: ans += 1
    if tmp < x:
        left += 1
    else:
        right -= 1

print(ans)