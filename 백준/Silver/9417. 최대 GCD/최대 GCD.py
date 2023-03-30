# [9417] 최대 GCD
import sys
input = sys.stdin.readline
def GCD(num1, num2):
    tmp = 0
    b = max(num1, num2)
    s = min(num1, num2)

    for i in range(1, s+1):
        if s%i==0 and b%i==0:
            tmp = i
    return tmp


N = int(input())
for n in range(N):
    ans = 0
    nums = list(map(int, input().split()))
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            ans = max(ans, GCD(nums[i], nums[j]))
    
    print(ans)