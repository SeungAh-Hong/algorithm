# [15686] 치킨 배달
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dosii = []
chic = []
house = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chic.append([i, j])

ans = int(1e9) # 최소 치킨 거리 총합
def DFS(idx, arr):
    global ans, chic, house
    if len(arr) == M:
        tmp_ans = 0
        for h in house:
            len_h = int(1e9)
            for c in arr:
                len_h = min(len_h, abs(h[0]-c[0])+abs(h[1]-c[1]))
            tmp_ans += len_h
        ans = min(ans, tmp_ans)
        return

    if idx == len(chic):
        return
    
    DFS(idx+1, arr)
    DFS(idx+1, arr+[chic[idx]])


DFS(0, [])
print(ans)