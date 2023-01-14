# 플로이드 워셜 알고리즘 : 모든 정점 사이의 최단 경로를 찾는 탐색 알고리즘
# 최단 경로는 길이 순으로 구해짐
"""
과정
1. 하나의 정점에서 다른 정점으로 바로 갈 수 있으면 최소 비용, 갈 수 없다면 INF로 배열에 값 저장
2. 3중 for문 통해 거쳐가는 정점을 설정한 후, 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값 변경
3. 위 과정 반복해 모든 정점 사이의 최단 경로 탐색

시간 복잡도 = O(N^3)
"""

INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

# 노드 개수 및 간석 개수 입력받은
n = int(input())
m = int(input())

# 2차원 리스트(그래프) 만든 후, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신끼리의 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0

# 각 간선에 대한 정보를 입력 받은 후, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용 : C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 INF 출력
        if graph[a][b] == INF:
            print("INF", end=' ')
        else: # 도달할 수 있는 경우 거리 출력
            print(graph[a][b], end=' ')
    print()