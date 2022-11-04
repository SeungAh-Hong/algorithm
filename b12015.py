# 12015  긴 증가하는 부분 수열 2
## 이분탐색 이용 -> 시간복잡도 O(nlogn)
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

def binarySearch(dp, target): ## target이 dp에 들어갈 idx 구함
    start = 0
    end = len(dp)
    if target < dp[0]:
        return 0
    while start <= end:
        mid = (start+end)//2
        if dp[mid] > target:
            end = mid-1
        elif dp[mid] < target:
            start = mid+1
        else: ## dp[mid] == target
            return mid
    return start
    


## 이렇게 풀면 정답 수열 도출은 불가능함 (수열 길이만 구할 수 있음)
### => 14002, 14003
for i in range(n):
    # 현재 위치 i의 값이 이전 위치의 값들보다 크면 dp에 추가
    if arr[i] > dp[-1]: 
        dp.append(arr[i])
    else: # 현재 위치 i의 값이 이전 값들보다 작거나 같으면
        ## dp에서 i 값보다 큰 원소 중 최소값과 대치 (이진탐색)
        # idx = bisect_left(dp, arr[i])
        idx = binarySearch(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))