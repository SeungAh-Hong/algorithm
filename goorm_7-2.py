# 구름 알고리즘 챌린지 7주차 2. 퍼져나가는 소문
from collections import deque

node = int(input())
line = int(input())
graph = [[0]*(node+1) for _ in range(node+1)]

for i in range(line):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

"""
## DFS
check = [0]*(node+1)
cnt = 0
def DFS(idx):
    check[idx] = 1
    global cnt
    cnt+=1
    for i in range(1, node+1):
        if check[i] == 0 and graph[idx][i] == 1:
            DFS(i)

DFS(1)
print(cnt)
"""


## BFS
check = [0]*(node+1)
cnt = 0

def BFS(idx):
    global cnt
    queue = deque()
    queue.append(idx)
    while queue:
        idx = queue.popleft()
        check[idx] = 1
        cnt+=1
        for i in range(1, node+1):
            if check[i] == 0 and graph[idx][i] == 1:
                queue.append(i)
                check[i] = 1

BFS(1)
print(cnt)