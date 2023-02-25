# 백준 15686 치킨 배달

import sys
import itertools
input = sys.stdin.readline

# 집(1)에서 가장 가까운 치킨집(2) 거리 
# 최대 치킨집은 M개, 나머지는 모두 폐업시켰을 때,
# 도시의 치킨 거리의 최솟값은?

N, M = map(int, input().split())
lists = []
## 치킨집 모든 조합에 대해 거리 최솟값 구함
home, chicken = [], []

for i in range(N):
    lists.append(list(map(int, input().split())))
    for j in range(N):
        if lists[i][j] == 1:
            home.append([i,j])
        elif lists[i][j] == 2:
            chicken.append([i,j])


ans = int(1e9)
for x in itertools.combinations(chicken, M):
    #print(x)
    tmp_ans = 0
    for h in home:
        tmp_h = int(1e9)
        for i in x: # 가장 가까운 치킨집 거리 찾기
            tmp_h = min(tmp_h, abs(h[0]-i[0])+abs(h[1]-i[1]))
        tmp_ans += tmp_h # 도시 치킨 거리에 더해줌 (모든 집에 대해)
    
    ans = min(tmp_ans, ans)

print(ans)