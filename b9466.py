# 9466 텀 프로젝트 (그래프 탐색)

import sys
input = sys.stdin.readline

## 사이클에 포함되지 않는 인원 구하기

## DFS 돌면서 start == end 면 
# ==> 맨 처음 시작 학생과 만난다면 사이클에 해당하므로 cycle에 추가
def DFS(start, end):
    global cycle ## 사이클에 포함되는 인원 구함
    cycle.add(start)
    for i in range(1, n+1):
        if graph[start][i] == 1 and check[i] == 0:
            check[i] = 1
            if i==end:
                for c in cycle:
                    r_cycle.append(c)
                return
            elif 0 in check:
                DFS(i, end)
    return

def get_checklist(check): # 체크리스트 갱신
    for i in range(1, n+1):
        if i in r_cycle:
            check[i] = 1
        else:
            check[i] = 0

tc = int(input())
for test in range(tc):
    n = int(input())
    graph = [[0]*(n+1) for _ in range(n+1)]
    wants = list(map(int, input().split()))
    for i in range(n):
        a = i+1
        b = wants[i]
        graph[a][b] = 1

    check = [0]*(n+1)
    r_cycle = [] ## 사이클에 해당하는 학생들

    for start in range(1, n+1):
        get_checklist(check)
        cycle = set() ## 학생 한 번마다 cycle 초기화
        DFS(start, start) ## 시작번호부터 쭉 사이클 돌기

    ans = n - len(r_cycle)
    print(ans)
