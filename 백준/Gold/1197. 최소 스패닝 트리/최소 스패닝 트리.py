import sys
input = sys.stdin.readline
# https://roytravel.tistory.com/348

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

graph = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph.append([a, b, cost])

graph.sort(key=lambda x:x[2])

costs, mst = 0, [] # mst: 최소 스패닝 트리
for i in range(e):
    a, b, cost = graph[i]
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 아닌 경우만 확인
        union_parent(parent, a, b)
        mst.append((a, b))
        costs += cost

#print(mst)
print(costs)