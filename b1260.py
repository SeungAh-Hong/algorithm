# 1260 DFS와 BFS
from collections import deque

node, line, start = map(int, input().split())
graph = [[0]*(node+1) for i in range(node+1)]
check = [0] * (node+1)

for i in range(0, line):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def DFS(idx): # 재귀
    check[idx] = 1
    print(idx, end=' ')
    for i in range(1, node+1): # 정점 번호 1~n까지 돌기
        if(check[i]==0 and graph[idx][i]==1):
            DFS(i)


def BFS(idx): # 큐
    queue = deque()
    queue.append(idx)
    while queue:
        idx = queue.popleft()
        print(idx, end=' ')
        check[idx] = 1
        for i in range(1, node+1):
            if(check[i]==0 and graph[idx][i]==1):
                queue.append(i)
                check[i] = 1

DFS(start)
print()
check = [0] * (node+1)
BFS(start)