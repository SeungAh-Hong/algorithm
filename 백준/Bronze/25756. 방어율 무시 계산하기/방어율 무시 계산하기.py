# [25756] 방어율 무시 계산하기
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

v = 1
for i in arr:
    v *= (1-i/100)
    print(round((1-v)*100, 6))