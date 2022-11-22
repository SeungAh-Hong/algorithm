import sys
from collections import deque
input = sys.stdin.readline

node = int(input())
start, end = map(int, input().split())
graph = [[0]*(node+1) for _ in range(node+1)]

line = int(input())
for i in range(line):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

## start 0촌, 멀어질 수록 +1촌
chonsu = [0]*(node+1)
def BFS(idx):
    queue = deque()
    queue.append(idx)
    while queue:
        idx = queue.popleft()
        if idx == end:
            return chonsu[end]
        for i in range(1, node+1):
            if chonsu[i] == 0 and graph[idx][i] == 1:
                chonsu[i] = chonsu[idx]+1
                queue.append(i)
    return -1

print(BFS(start))