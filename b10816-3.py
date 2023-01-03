# 백준 10816 숫자 카드 2 (이분 탐색)
import sys
input = sys.stdin.readline

N = int(input()) ## 상근이가 갖고 있는 카드 전체 개수
nList = sorted(list(map(int, input().split()))) ## 숫자 카드 (정렬!!)


M = int(input()) ## 몇 개 갖고 있는지 구하려는 숫자 카드의 개수
mList = list(map(int, input().split())) ## 구하려는 숫자 카드의 값 리스트

def lowerbound(nums, target): ## 찾고자 하는 숫자 이상의 값이 처음으로 나온 인덱스 값 구함
# nums[k-1] < target 이고 nums[k] >= target인 k를 찾는다
    l = 0
    r = len(nums)
    while l < r:
        mid = (l+r)//2
        if nums[mid] < target: ## target이 오른쪽에 있음
            l = mid + 1
        else: ## 
            r = mid
    return r
            
def upperbound(nums, target): ## 찾고자 하는 숫자 초과하는 값이 처음으로 나온 인덱스 값 구함
# nums[k] > target 을 만족하는 최소 k를 찾는다
    l = 0
    r = len(nums)
    while l < r:
        mid = (l+r)//2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return r

for m in mList:
    print(upperbound(nList, m)-lowerbound(nList, m))
