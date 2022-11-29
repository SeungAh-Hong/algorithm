# 10971 외판원 순회 2 (브루트포스, 백트래킹, DFS)
## a에서 출발해 모든 도시를 거쳐 다시 a로 돌아오는 동안 드는 최소 비용 구하기

from sys import stdin
import sys
input = stdin.readline

n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

def finished(visit):
    for i in range(n):
        if visit[i] == 0:
            return 1
    return 0

def DFS(idx, end, tmp, visit):
    global ans
    if finished(visit)==0: ## 다 돌았으면
        if cost[idx][end]: ## 마지막으로 돌아가는 값이 있으면
            ans = min(ans, tmp+cost[idx][end])
        return
    
    if tmp > ans: ## 현재 최솟값보다 tmp가 크면 돌지말고 바로 종료
        return

    for i in range(n): ## 선택된 줄에서 나머지 줄로 가는 경우의 수 모두 탐색
        if visit[i] == 0 and cost[idx][i]: # 들리지 않고 값이 있다면
            visit[i] = 1
            tmp+=cost[idx][i] ## 비용 추가
            DFS(i, end, tmp, visit) # 해당 줄로 가서 안들린 곳 ㄱㄱ
            tmp-=cost[idx][i] ## 비용 다시 빼줌 (새로운 경우의 수 돌려야 하니까)
            visit[i] = 0 ## visit도 마찬가지로 다시 취소
                    ## 여기서 return 만날 때까지 각각 경우의 수에 대해 재귀 시작

ans = sys.maxsize

visit = [0]*n
for i in range(n): ## 첫 번째 줄부터 n줄까지 시작 줄 선택하여 반복
    visit[i] = 1
    tmp = 0
    DFS(i, i, tmp, visit)
    visit[i] = 0

print(ans)