# [11724] 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = True

visited = [False]*(N+1)
def DFS(idx):
    global visited
    if visited[idx]:
        return
    else:
        visited[idx] = True
        for i in range(1, N+1):
            if graph[idx][i]:
                DFS(i)


answer = 0
for i in range(1, N+1):
    if visited[i] == False:
        DFS(i)
        answer += 1


print(answer)
