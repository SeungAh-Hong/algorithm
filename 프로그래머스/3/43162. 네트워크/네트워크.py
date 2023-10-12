def solution(n, computers):
    answer = 0
    visited = [0] * (n+1)
    
    def DFS(start):
        visited[start] = 1
        for i in range(n):
            if computers[start][i] == 1 and not visited[i]:
                DFS(i)

    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    return answer