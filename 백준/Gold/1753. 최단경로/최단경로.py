# 1753 최단경로 (다익스트라)
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        wei, now = heapq.heappop(q)
        if distance[now] < wei:
            continue
    
        for next_node, w in graph[now]:
            next_wei = w + wei
            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                heapq.heappush(q,(next_wei, next_node))
                
dijkstra(K)
for i in range(1, V+1):
    print("INF"if distance[i] == INF else distance[i])

