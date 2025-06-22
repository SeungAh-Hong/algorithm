def solution(n, computers):
    answer = 0
    visited = set()
    
    def dfs(node):
        visited.add(node)
        print("node: ", node)
        print("visited: ", visited)
        for i in range(n):
            if i not in visited and computers[node][i] == 1:
                dfs(i)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1
    
    return answer