## 8980 택배 (그리디)

import sys
input = sys.stdin.readline


## N : 마을의 수
## C : 트럭의 용량
N, C = map(int, input().split())
## M : 보낼 박스 정보의 개수
M = int(input())

deliveries = []
for i in range(M):
    deliveries.append(list(map(int, input().split())))


## 택배를 받는 마을을 기준으로 오름차순 정렬을 하되, 받는 마을이 같을 경우
## 보내는 마을을 기준으로 오름차순 정렬을 한다.

deliveries = sorted(deliveries, key=lambda x:x[1])

## 각 마을당 보낼 수 있는 최대 용량 설정
weight = [C]*(N)

ans = 0
for i in range(M):
    start = deliveries[i][0]
    end = deliveries[i][1]
    box = deliveries[i][2]
    
    maxBoxNum = sys.maxsize
    ## 보내는 마을과 받는 마을 사이의 경로 마을 중에서 보낼 수 있는 최대 한도를 구한다.
    for j in range(start, end):
        maxBoxNum = min(maxBoxNum, weight[j])
    
    ## 위에서 구한 보낼 수 있는 최대 한도가 현재 보내려는 택배의 개수보다 크다면,
    ## 보내는 마을과 받는 마을 사이의 경로 마을 모두 용량에서 현재 보내려는 택배의 개수를 뺀다.
    if maxBoxNum >= box:
        for j in range(start, end):
            weight[j] -= box
        ans += box
    else:
        ## 보낼 수 있는 최대 한도보다 현재 보내려는 택배의 개수가 클 경우,
        ## 현재 보내려는 택배의 개수가 아닌 위에서 구한 최대 한도를 기준으로 한다.
        for j in range(start, end):
            weight[j] -= maxBoxNum
        ans += maxBoxNum

print(ans)