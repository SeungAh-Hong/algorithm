# [10819] 차이를 최대로
import sys
input=sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

arr = []
ans = 0
isused = [0]*N
def sum_arr(arr):
    ret = 0
    for i in range(len(arr)-1):
        ret += abs(arr[i]-arr[i+1])
    return ret

def backtracking():
    global ans, nums, N
    if len(arr) == N:
        ans = max(ans, sum_arr(arr))
        return

    for i in range(N):
        if isused[i] == 1:
            continue
        isused[i] = 1
        arr.append(nums[i])
        backtracking()
        arr.pop()
        isused[i] = 0

backtracking()
print(ans)