# [2606] 바이러스 (실버3)
import sys
input = sys.stdin.readline

node = int(input())
line = int(input())
cnt = 0
graph = [[0]*(node+1) for _ in range(node+1)]
check = [False]*(node+1)

for i in range(line):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def DFS(idx):
    global cnt
    check[idx] = 1
    for i in range(1, node+1):
        if (check[i] == 0 and graph[idx][i] == 1):
            cnt += 1
            DFS(i)

DFS(1)
print(cnt)