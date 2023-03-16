# [2851] 슈퍼마리오 (브론즈 1)

import sys
input = sys.stdin.readline

mushroom = [int(input()) for _ in range(10)]

hap, hapup = 0, 0
for m in mushroom:
    if hap+m >= 100:
        hapup = hap + m
        break
    else:
        hap += m

if abs(hapup-100) <= abs(hap-100):
    print(hapup)
else:
    print(hap)
