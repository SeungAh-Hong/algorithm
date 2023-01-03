## 1931 회의실 배정 (그리디)
n = int(input())
if n == 0:
    print(0)
    exit(0)

se = []
for i in range(n):
    start, end = map(int, input().split())
    se.append([start, end])

se = sorted(se, key=lambda x:(x[1], x[0]))
# print(se)

d = [0]*(n+1) ## n번째 회의 진행했을 때 해당 회의를 진행했을 경우 최대 회의의 수
end = se[0][1]
cnt=1
for i in range(1, n):
    ns = se[i][0]
    if ns >= end:
        cnt+=1
        end = se[i][1]

print(cnt)