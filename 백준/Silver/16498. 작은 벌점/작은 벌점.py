# [16498] 작은 벌점 (실버 1)
import sys
from bisect import bisect_left
input = sys.stdin.readline
A, B, C = map(int, input().split())
a_list = sorted(list(set(map(int, input().split()))))
b_list = sorted(list(set(map(int, input().split()))))
c_list = sorted(list(set(map(int, input().split()))))
answer = 1e9

def Nearest(mid, target, ret):
    if abs(mid-target) < abs(ret-target):
        return True
    return False

def BS(arr, target):
    s = 0
    e = len(arr)-1
    m = (s+e)//2
    ret = arr[m]
    while s <= e:
        m = (s+e)//2
        if arr[m] == target:
            return target
        if arr[m] < target:
            s = m+1
        elif arr[m] > target:
            e = m-1
        
        if Nearest(arr[m], target, ret):
            ret = arr[m]
    return ret

# a 선택 -> b는 a와 가까운 값 선택 -> c는 a, b 중 가장 가까운 값 선택
for a in a_list:
    b = BS(b_list, a)
    c1 = BS(c_list, a)
    c2 = BS(c_list, b)

    big1 = max(a, b, c1)
    small1 = min(a, b, c1)
    ans1 = big1-small1

    big2 = max(a, b, c2)
    small2 = min(a, b, c2)
    ans2 = big2-small2

    # print(a, b, c1, c2)
    # print("ans1", ans1)
    # print("ans2", ans2)
    answer = min(answer, ans1, ans2)

print(answer)