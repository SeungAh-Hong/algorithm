from collections import deque

def solution(n, edge):
    answer = 0
    graph = [ [] for _ in range(n+1) ]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n+1)
    distance[1] = 0
    
    queue = deque([1]) # 1번 노드부터 시작
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1: #방문전
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)
    
    max_dist = max(distance)
    answer = distance.count(max_dist)
    return answer