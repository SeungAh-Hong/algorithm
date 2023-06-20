# [5972] 택배 배송
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [ [] for _ in range(n+1)]
dis = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for dir, wei in graph[now]:
            cost = dist + wei
            if cost < dis[dir]:
                dis[dir] = cost
                heapq.heappush(q, (cost, dir))

for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

dijkstra(1)

print(dis[-1])

