# DFS/BFS
# 기출문제 1
# 특정 거리의 도시 찾기

from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [0] * (n+1) #거리
visited = [False] * (n+1) #방문여부

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    dist[start] = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                dist[next] = dist[now] + 1
                q.append(next)
                if dist[next] == k:
                    answer.append(next)
    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for ans in answer:
            print(ans)

bfs(x)
    
