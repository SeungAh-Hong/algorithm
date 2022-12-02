# 2660 회장뽑기
import sys
input = sys.stdin.readline
from collections import deque

node = int(input())
graph = [[0]*(node+1) for _ in range(node+1)]

while 1:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break
    graph[a][b] = graph[b][a] = 1


friendship = [[0]*(node+1)for _ in range(node+1)] ## depth 담아줌

def BFS(start, end):
    queue = deque()
    queue.append(start)
    while queue:
        idx = queue.popleft()
        if idx==end:
            return depth[end]
        for i in range(1, node+1):
            if depth[i] == 0 and graph[idx][i] == 1:
                depth[i] = depth[idx]+1
                queue.append(i)
                
for i in range(1, node+1): ## 노드 하나에 대해
    for j in range(1, node+1): ## 모든 거리 구함
        depth = [0]*(node+1) ## depth 계산
        BFS(i, j)
        friendship[i][j] = depth[j]

# for i in range(node+1):
#     print(friendship[i])

score = sys.maxsize
for i in range(1, node+1):
    tmp = max(friendship[i])
    if score >= tmp:
        score = tmp

# print("score", score)
person_cnt = 0
person = []
for i in range(node+1):
    if score==max(friendship[i]):
        person_cnt+=1
        person.append(i)

print(score, person_cnt)
for i in person:
    print(i, end=' ')