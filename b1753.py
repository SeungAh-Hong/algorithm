# 1753 최단경로 (다익스트라)
# 하나의 정점에서 나머지 모든 정점까지의 최단 거리를 찾는 알고리즘
# 플로이드-워셜과는 다른 알고리즘임 !!!

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

# 최단 거리 테이블 (K에서부터 모든 경로까지의 최단경로)
distance = [INF]*(V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    # a -> b 비용 : c
    # (목적지 노드, 가중치)
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작노드로 가기 위한 최단 경로는 0으로 설정 후 큐에 삽입
    heapq.heappush(q, (0, start)) # (가중치, 노드)
    distance[start] = 0

    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼냄
        wei, now = heapq.heappop(q)
        
        # 현재 테이블과 비교해 불필요한 (더 가중치가 큰) 튜플이면 무시
        if distance[now] < wei:
            continue
    
        for next_node, w in graph[now]:
            # 현재 정점까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 w
            # == 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei

            # 다음 노드까지의 가중치(next_wei)가 현재 기록된 값보다 작으면 업데이트
            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                # 다음 정점까지의 가중치와 다음 정점에 대한 정보를 튜플로 묶어 최소 힙에 넣어줌
                heapq.heappush(q,(next_wei, next_node))


dijkstra(K)
for i in range(1, V+1):
    print("INF"if distance[i] == INF else distance[i])

