
## 구름 알고리즘 챌린지 7주차 3. 구름이의 여행 2

from collections import deque
# from collections import defaultdict
node, line, k = map(int, input().split())

graph = [ [] for _ in range(node+1)]

for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)

check = [0]*(node+1)

def BFS(idx):
    global check
    queue = deque()
    queue.append(idx)
    while queue:
        idx = queue.popleft()
        for i in graph[idx]:
            if check[i] == 0:
                check[i] = check[idx]+1
                if i == k:
                    return check[k]
                else:
                    queue.append(i)
    return -1

## 4 -> 5 -> 3 -> 1 -> 4
print(BFS(k))