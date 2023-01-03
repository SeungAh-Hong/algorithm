## 백준 1920 수 찾기 (이분 탐색)

import sys
input = sys.stdin.readline

N = int(input())
nList = list(map(int, input().split()))
nList.sort()

M = int(input())
mList = list(map(int, input().split()))

def BS(m, fList): ## 이분탐색
    idx = len(fList)//2 # 중간지점
    l = 0
    r = len(fList)-1
    while l <= r:
        if fList[idx] < m: ## idx 기준 오른쪽에 m 존재
            l = idx+1
            idx = (l+r)//2
        elif fList[idx] > m: ## idx 기준 왼쪽에 m 존재
            r = idx-1
            idx = (l+r)//2
        else:
            return 1

    return 0 ## 리스트에 없으면 0 반환


for m in mList:
    fList = nList
    print(BS(m, fList))

