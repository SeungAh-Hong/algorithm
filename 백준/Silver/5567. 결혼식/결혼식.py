## 5567 결혼식 (BFS/DFS)
import sys
input = sys.stdin.readline

node = int(input())
line = int(input())
## 친구, 친구의 친구
### 처음 0은 제외
graph = [[0]*(node+1) for _ in range(node+1)]
for i in range(line):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def DFS(start, depth):
    global friend_list
    if depth >= 2:
        return
    for i in range(node+1):
        if graph[start][i] == 1:
            if i not in friend_list:
                friend_list.append(i)
                depth += 1
                DFS(i, depth)
                depth -= 1
            else:
                depth+=1
                DFS(i, depth)
                depth-=1

friend_list = [1,]
depth=0
DFS(1,0)

print(len(friend_list)-1) ## 자기 자신 제외