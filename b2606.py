node = int(input())
line = int(input())

# 배열 선언
graph = [[0]*(node+1) for i in range(node+1)]
check = [0]*(node+1)
cnt = 0

for i in range(1, line+1):# line 개수만큼 반복
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def DFS(idx):
    global cnt
    check[idx] = 1
    for i in range(1, node+1):
        if(check[i]==0 and graph[idx][i]==1):
            cnt+=1
            DFS(i)

DFS(1)
print(cnt)