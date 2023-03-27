# [1978] 소수 찾기 (실버 5)
import sys
import math
input = sys.stdin.readline
N=int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for i in range(N):
    isPrime = True
    num = nums[i]
    if num == 1:
        continue
    for j in range(2, int(math.sqrt(num)+1)):
        if num%j==0:
            isPrime=False
    
    if isPrime:
        cnt += 1

print(cnt)