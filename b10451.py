## 10451 순열 사이클
# 사이클 개수 구하는 문제
### pypy3으로 제출해야 함

import sys
from collections import deque

input = sys.stdin.readline
tc = int(input())

def BFS(idx): ## 사이클 개수 출력
    global cnt
    queue = deque()
    if visited[idx] == 1:# 이미 이전 사이클에 해당되는 수면
        return
    queue.append(idx)

    while(queue):
        idx = queue.popleft()
        visited[idx] = 1
        for i in range(1, n+1):
            if visited[i] == 0 and graph[idx][i] == 1:
                queue.append(i)
    cnt+=1



while tc:
    n = int(input())
    inputs = list(map(int, input().split()))

    graph = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n):
        a = i+1
        b = inputs[i]
        graph[a][b] = graph[b][a] = 1

    visited = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        BFS(i)
    print(cnt) ## 사이클 개수 출력
    tc-=1


    
