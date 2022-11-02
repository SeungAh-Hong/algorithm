## 구름 알고리즘 챌린지 4주차 - 2. 단풍나무
n = int(input())
park = []

for i in range(n):
    park.append(list(map(int, input().split()))) ## 2차원 배열 입력

# for i in range(n):
#     print(park[i])

## 상하좌우 탐색
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def search(x, y, cnt):
    for a in range(4):
        pcount=0 ## 상하좌우 0 몇 개 있는지 확인할 변수
        nx = i + dx[a]
        ny = j + dy[a]
        if(nx < n and ny < n and nx >=0 and ny >= 0):
            if park[nx][ny] == 0:
                cnt[x][y] += 1

def update(cnt):
    for i in range(n):
        for j in range(n):
            if(park[i][j] <= cnt[i][j]):
                park[i][j] = 0
            else:
                park[i][j] -= cnt[i][j]


def zero():
    for i in range(n):
        for j in range(n):
            if(park[i][j] != 0):
                return False
    return True

ans = 0
## 완전 탐색
while 1:
    if zero() == True: ## 전부 0일 경우 stop
        break
    ## 하루에 얼마나 줄어드는지 저장
    cnt = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(park[i][j] != 0): ## 0이 아닌 구역이 있을 경우
                search(i, j, cnt)
    ## 하루 지난 후 값 갱신
    update(cnt)
    ans+=1

print(ans)

            
